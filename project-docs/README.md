# Digital Attendance and Productivity Tracker for Students
### Venture Ideation: Planning and Design Phase

A mobile-friendly app (PWA) where faculty show a QR code that **changes every 10 seconds**, and students scan it to mark attendance. Proxies are blocked with **time-limited codes, campus geofencing and device binding**. Students below **75%** get alerts and can track study time with a **Pomodoro timer, tasks and daily goals**. Faculty and admins get dashboards and report exports.
**Business model:** free for students; colleges pay an annual per-student subscription.

**Team:** Venuprasadd M.K · Kris Jefford I · Sujith S · Vignesh K · Ajin S.S

> This folder contains **planning and design only**. There is no app code yet.

---

## What's in this folder

| Path | What it contains |
|---|---|
| `01-problem-and-idea.md` | Problem statement, who is affected and their pain points, root causes, our solution, unique value proposition, target customers, and the **assumptions we must test** with the survey |
| `02-existing-solutions-study.md` | Comparison of manual roll call, RFID, fingerprint, face recognition, QR apps and productivity apps; references; **"Gap we fill"**. Items to check are marked **[VERIFY]** |
| `03-survey/survey-questions.md` | Student survey (12 questions), ready to copy into Google Forms, with question types. We survey **students only** |
| `03-survey/create_google_forms.gs` | Google Apps Script that **creates the student Google Form automatically** (paste into script.google.com and run `createStudentForm`) |
| `03-survey/responses-template.csv` | Empty CSV with the student-form column headers (same as the Google Forms export) |
| `03-survey/sample-test.csv` | **5 rows of TEST DATA, not real responses.** Only for checking that the script runs |
| `03-survey/analyze_survey.py` | Reads the exported CSV and creates charts (PNG) plus `survey-summary.md` |
| `04-features-and-system-flow.md` | Features by role with MoSCoW priority, user stories with acceptance criteria, Mermaid diagrams (use case, QR sequence, architecture, user flows, ER), data entities, business model canvas, and pilot cost estimate (INR) |
| `05-wireframes/` | Clickable greyscale wireframes: `index.html` plus 14 screens (8 student mobile, 3 faculty desktop, 3 admin desktop) and a shared `wireframe.css` |

---

## How to view the wireframes

1. Open `05-wireframes/index.html` in any browser (Chrome, Edge, Firefox). Just double-click it.
2. Click any screen. Buttons, tabs and the bottom / side menus are clickable. **← All screens** returns to the index.
3. Each screen has a **Wireframe notes** panel that explains its purpose, elements and links to features.
4. Try the interactive bits:
   - **Scan QR:** switch between the Scanning / Success / Failure states.
   - **Faculty Live QR:** the demo QR pattern redraws every 10 seconds.
   - **Focus Timer:** press Start to see the countdown.

> The pages load Tailwind CSS from the internet (`cdn.tailwindcss.com`), so **you need an internet connection**. Without it the pages still open but look unstyled.

## How to view the diagrams

The Mermaid diagrams in `04-features-and-system-flow.md` render automatically on **GitHub**. You can also paste any diagram into <https://mermaid.live> to view it or download it as an image for your report.

---

## How to run the survey analysis

**One-time setup** (needs Python 3.8 or newer):

```bash
pip install matplotlib
```

**Test the script first with the sample file:**

```bash
cd project-docs/03-survey
python analyze_survey.py sample-test.csv
```

You will see a **WARNING** that sample data is being used. Output goes to `output-student-SAMPLE/` and every chart is stamped "SAMPLE TEST DATA". **Do not use these in the report.**

**With your real responses:**

1. In Google Forms, open **Responses → ⋮ → Download responses (.csv)**.
2. Save the file in `03-survey/` (for example `student-responses.csv`).
3. Run:

```bash
python analyze_survey.py student-responses.csv
```

4. Open `output-student/survey-summary.md`. It contains counts, percentages, averages for 1–5 scales, and a PNG chart for each question (teal `#0F4C5C`, with the most common answer highlighted in orange `#E36414`).

**If the script says a question was "not found":** the question wording in your Google Form is different from `survey-questions.md`. Either fix the form, or edit the `QUESTIONS` list at the top of `analyze_survey.py` to match.

---

## ✅ Team checklist: things we must do ourselves

**Survey**
- [ ] Create the student Google Form by running `03-survey/create_google_forms.gs` at script.google.com (or build it by hand from `survey-questions.md`, copying the wording exactly).
- [ ] Get our guide's OK on the form before sending.
- [ ] Send the form link (class WhatsApp groups, department email, in person).
- [ ] Collect **at least 25–30 student responses** (more is better; try to cover different years and departments).
- [ ] Download the CSV export and run `analyze_survey.py` on it.
- [ ] Read `survey-summary.md` and write our **real findings** against assumptions A1–A9 in `01-problem-and-idea.md`. If an assumption is **not** supported, say so honestly and adjust the features. A7 and A8 (faculty) are not covered by the student survey, so list them as "not yet validated".

**Fact-checking**
- [ ] Review every **[VERIFY]** item in `02-existing-solutions-study.md` and `04-features-and-system-flow.md`.
- [ ] Confirm our university's minimum attendance rule (we assumed 75%).
- [ ] Check current prices for the domain, hosting and database in the cost estimate.
- [ ] Check what the DPDP Act 2023 means for storing student location and attendance data.
- [ ] Test phone GPS accuracy inside a few classrooms (for the geofence radius).

**Before submission**
- [ ] Walk through all wireframe screens together and note changes.
- [ ] Export the Mermaid diagrams as images (via mermaid.live) for the report or slides.
- [ ] Get feedback from our guide and from 2–3 faculty on the wireframes.
- [ ] Remove or clearly label any sample data in the final report.

---

## A note on honesty

- **No survey results are included.** `sample-test.csv` contains 5 made-up rows only for testing the script, and the script warns when it is used.
- Names and numbers in the wireframes are **sample data** (using our team's names).
- The comparison study uses no invented product names, prices or statistics. Uncertain points are marked **[VERIFY]**.
- Costs are **estimates**, not quotations.
