"""
Survey analysis for "Digital Attendance and Productivity Tracker for Students".

Reads the student survey CSV exported from Google Forms
(Responses -> Download responses (.csv))
and saves:
  * one chart (PNG) per question
  * survey-summary.md with counts and percentages

Usage:
    python analyze_survey.py <exported.csv>
    python analyze_survey.py <exported.csv> --out my-results     # custom output folder

Needs:  pip install matplotlib
"""

import argparse
import csv
import os
import sys
from collections import Counter, OrderedDict

import matplotlib

matplotlib.use("Agg")  # save images without opening a window
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

TEAL = "#0F4C5C"
ORANGE = "#E36414"
GREY = "#9AA5A8"
INK = "#1F2933"
MUTED = "#6B7780"
GRID = "#E3E7E8"
PIE_COLOURS = [TEAL, ORANGE, GREY, "#C9D1D3"]

# ---------------------------------------------------------------------------
# Question definitions. These must match the wording in survey-questions.md.
# type: "choice" (multiple choice), "checkbox", "scale" (1-5), "text"
# ---------------------------------------------------------------------------
QUESTIONS = [
    {"id": "S1", "type": "choice",
     "text": "Do you have a smartphone that you can use during class?",
     "options": ["Yes, my own smartphone", "Yes, but it is shared with family", "No"]},
    {"id": "S2", "type": "choice",
     "text": "How is attendance usually taken in your classes?",
     "options": ["Faculty calls out names (roll call)", "A paper sheet is passed around",
                 "Biometric or ID card machine", "An app or QR code", "Other"]},
    {"id": "S3", "type": "choice",
     "text": "About how much class time is spent on taking attendance in one lecture?",
     "options": ["Less than 2 minutes", "2 to 5 minutes", "5 to 10 minutes", "More than 10 minutes"]},
    {"id": "S4", "type": "scale", "low": "Never", "high": "Very often",
     "text": "How often do you notice proxy attendance (someone marking attendance for an absent student) in your classes?"},
    {"id": "S5", "type": "choice",
     "text": "Do you know your current attendance percentage in each subject?",
     "options": ["Yes, exactly", "Only roughly", "No"]},
    {"id": "S6", "type": "choice",
     "text": "Have you ever been below or close to the 75% attendance requirement?",
     "options": ["Yes, I was below 75%", "Yes, I was close (75% to 80%)", "No", "I don't know"]},
    {"id": "S7", "type": "choice",
     "text": "On a normal day, how many hours do you study outside class?",
     "options": ["Less than 1 hour", "1 to 2 hours", "2 to 4 hours", "More than 4 hours"]},
    {"id": "S8", "type": "checkbox",
     "text": "How do you currently plan or track your study time?",
     "options": ["I don't plan or track it", "Paper notes or a diary", "A to-do list app",
                 "A Pomodoro or focus timer app", "A calendar or planner app", "Other"]},
    {"id": "S9", "type": "scale", "low": "Very easy", "high": "Very hard",
     "text": "How hard is it for you to stay focused while studying (for example, because of phone distractions)?"},
    {"id": "S10", "type": "scale", "low": "Not comfortable at all", "high": "Very comfortable",
     "text": "How comfortable would you be if the app checked your location only at the moment you scan the attendance QR code?"},
    {"id": "S11", "type": "scale", "low": "Not interested", "high": "Very interested",
     "text": "How interested would you be in one free app that marks attendance by scanning a QR code AND helps you track your study time?"},
    {"id": "S12", "type": "checkbox",
     "text": "Which features would matter most to you? (Choose up to 3)",
     "options": ["Quick QR attendance", "Live attendance % for each subject", "Alert when I go below 75%",
                 "Pomodoro focus timer", "To-do tasks and daily goals", "Study time analytics", "Other"]},
]

SAMPLE_FILE_NAME = "sample-test.csv"
SAMPLE_MARKER = "TEST DATA"


def normalise(text):
    """Lower-case and squash spaces so small header differences still match."""
    return " ".join(str(text).replace("’", "'").lower().split())


def read_csv(path):
    # utf-8-sig removes the hidden BOM character that Excel / Google sometimes add
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        rows = [row for row in reader if any(cell.strip() for cell in row)]
    if not rows:
        sys.exit(f"ERROR: {path} is empty.")
    return rows[0], rows[1:]


def match_columns(header, questions):
    """Return {question id: column index}. Match by text first, then by '[S1]' style ids."""
    mapping = {}
    norm_header = [normalise(h) for h in header]
    for q in questions:
        target = normalise(q["text"])
        for i, h in enumerate(norm_header):
            if h == target or h.startswith(normalise(q["id"]) + ".") or h.startswith(target):
                mapping[q["id"]] = i
                break
    return mapping


def is_sample(path, header, rows):
    if os.path.basename(path).lower() == SAMPLE_FILE_NAME:
        return True
    return any(SAMPLE_MARKER in " ".join(row) for row in rows[:5])


def count_choice(values, options):
    counts = OrderedDict((opt, 0) for opt in options)
    for v in values:
        match = next((opt for opt in options if normalise(opt) == normalise(v)), None)
        if match is None:
            # Google Forms "Other" answers arrive as free text
            match = "Other"
            counts.setdefault("Other", 0)
        counts[match] += 1
    return counts


def count_checkbox(values, options):
    """Checkbox answers look like 'A, B, Other text'. Count each known option once per person."""
    counts = OrderedDict((opt, 0) for opt in options)
    for v in values:
        remaining = normalise(v)
        for opt in sorted(options, key=len, reverse=True):  # longest first avoids partial matches
            if opt == "Other":
                continue
            if normalise(opt) in remaining:
                counts[opt] += 1
                remaining = remaining.replace(normalise(opt), "", 1)
        leftover = remaining.replace(",", " ").strip()
        if leftover:
            counts.setdefault("Other", 0)
            counts["Other"] += 1
    return counts


def count_scale(values):
    counts = OrderedDict((str(n), 0) for n in range(1, 6))
    for v in values:
        v = v.strip()
        if v in counts:
            counts[v] += 1
    return counts


def pct(part, whole):
    return 0.0 if whole == 0 else 100.0 * part / whole


def style_axes(ax):
    for side in ("top", "right", "left"):
        ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color(GRID)
    ax.tick_params(colors=MUTED, length=0)
    ax.xaxis.grid(True, color=GRID, linewidth=0.8)
    ax.set_axisbelow(True)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))  # counts are whole people


def wrap(text, width=38):
    words, lines, line = text.split(), [], ""
    for w in words:
        if len(line) + len(w) + 1 > width:
            lines.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    lines.append(line)
    return "\n".join(lines)


def add_sample_stamp(fig):
    fig.text(0.5, 0.5, "SAMPLE TEST DATA - NOT REAL", fontsize=26, color=ORANGE, alpha=0.25,
             ha="center", va="center", rotation=20, weight="bold")


def bar_chart(q, counts, base, path, sample, x_label):
    """Horizontal bars, all teal; the most common answer is highlighted in orange."""
    labels = list(counts.keys())
    values = list(counts.values())
    top = max(values) if values else 0
    colours = [ORANGE if v == top and top > 0 else TEAL for v in values]

    fig, ax = plt.subplots(figsize=(8, 0.55 * len(labels) + 1.8), dpi=150)
    y = list(range(len(labels)))[::-1]
    ax.barh(y, values, color=colours, height=0.6, edgecolor="white", linewidth=2)
    ax.set_yticks(y)
    ax.set_yticklabels([wrap(l, 34) for l in labels], color=INK, fontsize=9)
    for yi, v in zip(y, values):
        ax.text(v + max(top, 1) * 0.02, yi, f"{v}  ({pct(v, base):.0f}%)",
                va="center", color=INK, fontsize=9)
    ax.set_xlim(0, max(top, 1) * 1.25)
    ax.set_xlabel(x_label, color=MUTED, fontsize=9)
    style_axes(ax)
    ax.set_title(f"{q['id']}. {wrap(q['text'], 70)}", loc="left", color=INK, fontsize=10.5, pad=12)
    if sample:
        add_sample_stamp(fig)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)


def pie_chart(q, counts, base, path, sample):
    """Used only for questions with 4 or fewer answer options. Every slice is labelled."""
    items = [(k, v) for k, v in counts.items() if v > 0]
    labels = [f"{wrap(k, 22)}\n{v} ({pct(v, base):.0f}%)" for k, v in items]
    fig, ax = plt.subplots(figsize=(7, 5), dpi=150)
    ax.pie([v for _, v in items], labels=labels, colors=PIE_COLOURS[:len(items)], startangle=90,
           counterclock=False, wedgeprops={"edgecolor": "white", "linewidth": 2},
           textprops={"color": INK, "fontsize": 9})
    ax.axis("equal")
    ax.set_title(f"{q['id']}. {wrap(q['text'], 70)}", loc="left", color=INK, fontsize=10.5)
    if sample:
        add_sample_stamp(fig)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", pad_inches=0.3)
    plt.close(fig)


def table(counts, base, label="Answer"):
    lines = [f"| {label} | Count | % |", "|---|---:|---:|"]
    for k, v in counts.items():
        lines.append(f"| {k} | {v} | {pct(v, base):.1f}% |")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyse the exported student survey CSV.")
    parser.add_argument("csv_file", help="CSV downloaded from Google Forms")
    parser.add_argument("--out", default=None,
                        help="output folder (default: output-student next to this script)")
    args = parser.parse_args()

    if not os.path.exists(args.csv_file):
        sys.exit(f"ERROR: file not found: {args.csv_file}")

    questions = QUESTIONS
    header, rows = read_csv(args.csv_file)
    sample = is_sample(args.csv_file, header, rows)

    if sample:
        print("=" * 70)
        print("WARNING: You are using SAMPLE TEST DATA (sample-test.csv or rows marked 'TEST DATA').")
        print("These rows are NOT real survey responses. Use them only to check")
        print("that the script works. Do NOT put these charts in your report.")
        print("=" * 70)

    out_dir = args.out or os.path.join(os.path.dirname(os.path.abspath(__file__)), "output-student")
    if sample and args.out is None:
        out_dir += "-SAMPLE"
    os.makedirs(out_dir, exist_ok=True)

    mapping = match_columns(header, questions)
    missing = [q["id"] for q in questions if q["id"] not in mapping]
    if missing:
        print(f"WARNING: could not find these questions in the CSV header: {', '.join(missing)}")
        print("         Check that the Google Form wording matches survey-questions.md.")

    n = len(rows)
    md = ["# Student Survey Summary", ""]
    if sample:
        md += ["> **WARNING: SAMPLE TEST DATA. These are NOT real responses. Do not use these results in the report.**", ""]
    md += [f"- Source file: `{os.path.basename(args.csv_file)}`",
           f"- Total responses: **{n}**",
           "- Percentages are out of the people who answered each question. For checkbox questions,",
           "  people can tick more than one option, so percentages can add up to more than 100%.",
           ""]

    for q in questions:
        md.append(f"## {q['id']}. {q['text']}")
        md.append("")
        if q["id"] not in mapping:
            md += ["_Question not found in the CSV._", ""]
            continue
        col = mapping[q["id"]]
        values = [r[col].strip() for r in rows if col < len(r) and r[col].strip()]
        answered = len(values)
        md.append(f"Answered by **{answered}** of {n}.")
        md.append("")
        img = f"{q['id']}.png"
        img_path = os.path.join(out_dir, img)

        if q["type"] == "choice":
            counts = count_choice(values, q["options"])
            if len(q["options"]) <= 4:
                pie_chart(q, counts, answered, img_path, sample)
            else:
                bar_chart(q, counts, answered, img_path, sample, "Number of responses")
            md += [table(counts, answered), "", f"![{q['id']}]({img})", ""]

        elif q["type"] == "checkbox":
            counts = count_checkbox(values, q["options"])
            bar_chart(q, counts, answered, img_path, sample, "Number of people who ticked this option")
            md += [table(counts, answered, "Option"), "", f"![{q['id']}]({img})", ""]

        elif q["type"] == "scale":
            counts = count_scale(values)
            labelled = OrderedDict()
            for k, v in counts.items():
                name = k
                if k == "1":
                    name = f"1 ({q['low']})"
                elif k == "5":
                    name = f"5 ({q['high']})"
                labelled[name] = v
            scored = sum(int(k) * v for k, v in counts.items())
            valid = sum(counts.values())
            mean = scored / valid if valid else 0.0
            agree = counts["4"] + counts["5"]
            bar_chart(q, labelled, valid, img_path, sample, "Number of responses")
            md += [table(labelled, valid, "Rating"), "",
                   f"- Average rating: **{mean:.2f} / 5**",
                   f"- Rated 4 or 5: **{agree}** ({pct(agree, valid):.1f}%)", "",
                   f"![{q['id']}]({img})", ""]

        else:  # free text: list answers, no chart
            md += ["Answers (copied as written):", ""]
            md += [f"- {v}" for v in values] or ["- (none)"]
            md.append("")

    summary_path = os.path.join(out_dir, "survey-summary.md")
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    print(f"Read {n} responses from {args.csv_file}")
    print(f"Saved charts and summary to: {out_dir}")
    print(f"Open {summary_path} to see the results.")
    if sample:
        print("REMINDER: sample data only - collect real responses before writing conclusions.")


if __name__ == "__main__":
    main()
