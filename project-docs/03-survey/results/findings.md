# Survey Findings

**Venture:** Digital Attendance and Productivity Tracker for Students
**Survey:** Student Survey: Attendance and Study Habits (Google Forms)
**Responses:** **31 students**, collected 22–24 Oct 2026
**Full numbers and charts:** [`survey-summary.md`](survey-summary.md) (one chart per question: `S1.png` … `S12.png`)

> All figures below come from the **real** responses, produced with `analyze_survey.py`. The raw response file is **not** stored in this repository, because the form promised that answers would not be shared. Only these aggregated counts are kept.

---

## 1. Key numbers at a glance

| What we asked | Result |
|---|---|
| Have their own smartphone (S1) | **80.6%** (25), plus 12.9% shared with family; **6.5% (2) have none** |
| Attendance taken by roll call or paper sheet (S2) | **90.3%** (28) |
| Attendance takes 2 minutes or more per lecture (S3) | **71.0%** (22) |
| How often proxies are noticed (S4, 1–5) | Average **2.87**; 25.8% rate 4–5 |
| Know their attendance % only roughly or not at all (S5) | **54.8%** (17) |
| Have been below or close to 75% (S6) | **35.5%** (11) |
| Don't plan or track study time at all (S8) | **41.9%** (13); only 29.0% (9) use any app |
| Difficulty staying focused (S9, 1–5) | Average **3.32**; 41.9% rate 4–5 |
| Comfortable with a location check at scan time (S10, 1–5) | Average **3.16**; 35.5% comfortable (4–5), 25.8% not (1–2) |
| Interest in the app (S11, 1–5) | Average **3.26**; 25.8% rate 4–5; **54.8% chose the neutral 3** |
| Top features (S12, up to 3) | Quick QR attendance **45.2%**, Below-75% alert **41.9%**, To-do tasks and goals **35.5%**, Live attendance % 25.8%, Study analytics 22.6%, **Pomodoro timer 3.2%** |

---

## 2. Assumptions check

Assumptions and targets are from `01-problem-and-idea.md`, section 7.

| # | Assumption | Target | Result | Verdict |
|---|---|---|---|---|
| A1 | Most students have their own smartphone | Large majority "Yes, my own" | 80.6% own one; 6.5% have none | ✅ **Supported** |
| A2 | Taking attendance wastes noticeable class time | Most answer "2 to 5 minutes" or more | 71.0% say 2+ minutes | ✅ **Supported** |
| A3 | Proxy attendance is a real problem | Average ≥ 3 | Average 2.87; 41.9% chose 3 | ⚠️ **Not supported (just below target)** |
| A4 | Students don't know their attendance % | Many answer "No" / "Only roughly" | 54.8% roughly or not at all | ✅ **Supported** |
| A5 | Students struggle to focus and track study time | Focus average ≥ 3; few use tracking tools | Average 3.32; 41.9% don't track; 29.0% use an app | ✅ **Supported** |
| A6 | Students are interested in a combined app | Average ≥ 4; productivity features picked as well as attendance ones | Average 3.26; attendance features picked by 80.6%, productivity by 48.4% | ❌ **Not supported** |
| A7 | Faculty spend effort on reports | n/a | Not asked (student-only survey) | ➖ **Not tested** |
| A8 | Faculty willing to adopt | n/a | Not asked (student-only survey) | ➖ **Not tested** |
| A9 | Students accept a location check at scan time | Most comfortable (4–5) | 35.5% comfortable; 38.7% neutral; 25.8% not | ⚠️ **Not supported (mixed)** |

**Summary:** 4 supported, 3 not supported, 2 not tested.

---

## 3. What this means for our idea

1. **The attendance problem is real.** Most classes still use roll call or paper (90.3%), it costs 2+ minutes per lecture for most students (71.0%), and more than half don't know their exact attendance %. A third have been at or below the 75% line. This supports **QR attendance, live %, and the below-75% alert**, which were also the top-chosen features.
2. **Proxies are noticed "sometimes", not "very often".** At 2.87 the average is just below our target. Students might also under-report proxies because they don't want to admit it happens in their class; we can't tell from this data. In our pitch, **lead with time saved and live attendance %**, and present proxy prevention as a supporting benefit rather than the main one.
3. **Interest is lukewarm, and most students are neutral.** 54.8% chose "3". Students may need to see the app before deciding, so a **clickable demo or pilot** is the right next step, not a bigger build.
4. **Students want the attendance side most.** Within productivity, **to-do tasks and goals** (35.5%) and **study analytics** (22.6%) got some support, but the **Pomodoro timer got only 1 vote (3.2%)**, even though 41.9% find focusing hard.
5. **Location checks need a clear explanation.** One in four students is uncomfortable. The app should explain on first use that location is checked **only at the moment of scanning**, and that no tracking happens in the background.
6. **A few students have no phone (6.5%) or share one (12.9%).** The faculty **manual-mark** feature (FA-4) is necessary, not optional.

### Suggested changes (for the team to decide)

| Area | Current plan (doc 04) | Suggestion based on the survey |
|---|---|---|
| Pomodoro focus timer (ST-7) | Must | Consider moving to **Should**; keep **to-do tasks and goals** as the main productivity feature |
| Location permission screen | Mentioned in ST-3 | Make the privacy explanation a clear, separate first-use screen |
| Pitch / problem statement | Proxies are a headline problem | Lead with **time lost** and **not knowing attendance %**; proxies come second |
| Next validation step | n/a | Show the wireframes to 5–10 students and re-ask the interest question; talk to 2–3 faculty for A7 and A8 |

---

## 4. Limitations

- **Small sample:** 31 responses is enough for a student micro project, but not for strong conclusions. One response changes a percentage by about 3 points.
- **Convenience sample:** the link was shared through our own class groups, so most respondents are probably from our college and department. The survey didn't ask year or department, so we can't check this.
- **Self-reported answers:** for example, proxy frequency and study hours may be under- or over-reported.
- **No faculty voice:** A7 and A8 remain untested.
