# Survey Questions

**Venture:** Digital Attendance and Productivity Tracker for Students
**Purpose:** To check the assumptions listed in `01-problem-and-idea.md` (section 7) using **real** responses from students.

We are surveying **students only** (no faculty survey).

| Form | Questions | Time to answer | Target responses |
|---|---|---|---|
| Student survey | 12 (S1–S12) | about 3 minutes | **25–30 or more** |

---

## How to set this up in Google Forms

> **Fastest way:** run `create_google_forms.gs`. It builds the student form automatically in your Google account, with the exact wording, question types, "Other" options, 1–5 scales and the "up to 3" limit on S12, plus a thank-you message shown after submitting. Open <https://script.google.com>, click **New project**, paste the whole file, click **Save**, choose `createStudentForm` and click **Run**. Allow the permission prompt, then copy the share and edit links from the **Execution log**.
>
> To do it by hand instead, follow the steps below.

1. Create a new Google Form.
2. Copy each question **exactly as written** (without the "S1." label). The analysis script matches the column headers in the export to this wording. If you change the wording, also update `QUESTIONS` at the top of `analyze_survey.py`.
3. Choose the question type shown in the **Type** line of each question.
4. For linear scales, set the range to **1 to 5** and type the two end labels shown.
5. **Do not use commas inside checkbox options.** Google Forms joins several ticked answers with commas, so a comma inside an option would break the count. (All options below already avoid commas.)
6. Mark every question as **Required**.
7. Turn **off** "Collect email addresses" so that responses stay anonymous.
8. Add this line to the form description:
   > *This is an anonymous survey for a college entrepreneurship project. Your answers are used only to study this problem and will not be shared.*
9. Add a thank-you message: **Settings → Presentation → Confirmation message**, then paste:
   > *Thank you for filling in our survey! 🙏 Your response has been recorded.*
10. To export later: **Responses → three-dot menu → Download responses (.csv)**.

---

## Student survey

**Form title:** Student Survey: Attendance and Study Habits

**S1. Do you have a smartphone that you can use during class?**
Type: Multiple choice
- Yes, my own smartphone
- Yes, but it is shared with family
- No

**S2. How is attendance usually taken in your classes?**
Type: Multiple choice
- Faculty calls out names (roll call)
- A paper sheet is passed around
- Biometric or ID card machine
- An app or QR code
- Other

**S3. About how much class time is spent on taking attendance in one lecture?**
Type: Multiple choice
- Less than 2 minutes
- 2 to 5 minutes
- 5 to 10 minutes
- More than 10 minutes

**S4. How often do you notice proxy attendance (someone marking attendance for an absent student) in your classes?**
Type: Linear scale 1–5 (1 = Never, 5 = Very often)

**S5. Do you know your current attendance percentage in each subject?**
Type: Multiple choice
- Yes, exactly
- Only roughly
- No

**S6. Have you ever been below or close to the 75% attendance requirement?**
Type: Multiple choice
- Yes, I was below 75%
- Yes, I was close (75% to 80%)
- No
- I don't know

**S7. On a normal day, how many hours do you study outside class?**
Type: Multiple choice
- Less than 1 hour
- 1 to 2 hours
- 2 to 4 hours
- More than 4 hours

**S8. How do you currently plan or track your study time?**
Type: Checkboxes (tick all that apply)
- I don't plan or track it
- Paper notes or a diary
- A to-do list app
- A Pomodoro or focus timer app
- A calendar or planner app
- Other

**S9. How hard is it for you to stay focused while studying (for example, because of phone distractions)?**
Type: Linear scale 1–5 (1 = Very easy, 5 = Very hard)

**S10. How comfortable would you be if the app checked your location only at the moment you scan the attendance QR code?**
Type: Linear scale 1–5 (1 = Not comfortable at all, 5 = Very comfortable)

**S11. How interested would you be in one free app that marks attendance by scanning a QR code AND helps you track your study time?**
Type: Linear scale 1–5 (1 = Not interested, 5 = Very interested)

**S12. Which features would matter most to you? (Choose up to 3)**
Type: Checkboxes (in Google Forms: Response validation → "Select at most" → 3)
- Quick QR attendance
- Live attendance % for each subject
- Alert when I go below 75%
- Pomodoro focus timer
- To-do tasks and daily goals
- Study time analytics
- Other

---

## Question-to-assumption map

| Assumption (from 01) | Student questions |
|---|---|
| A1 Smartphone access | S1 |
| A2 Class time lost | S3 |
| A3 Proxy problem | S4 |
| A4 Low awareness of attendance % | S5, S6 |
| A5 Focus and study-tracking problems | S8, S9 |
| A6 Interest in a combined app | S11, S12 |
| A7 Faculty reporting effort | Not covered (no faculty survey) |
| A8 Faculty willingness to adopt | Not covered (no faculty survey) |
| A9 Acceptance of location check | S10 |
| (Context) Current method and study hours | S2, S7 |

> A7 and A8 are about faculty, so this student survey cannot test them. In the report, list them as **not yet validated**. If there is time, a short chat with our guide or 2–3 faculty members can give an early signal.
