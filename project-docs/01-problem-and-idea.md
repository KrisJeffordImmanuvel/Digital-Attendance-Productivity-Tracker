# 01 · Problem and Idea

**Venture:** Digital Attendance and Productivity Tracker for Students
**Team:** Venuprasadd M.K · Kris Jefford I · Sujith S · Vignesh K · Ajin S.S
**Phase:** Venture Ideation: planning and design

---

## 1. Problem statement

In most colleges, attendance is still taken by calling out names or passing a paper sheet around the class.
This takes several minutes of every lecture, and it is easy for one student to answer or sign for an absent friend (a "proxy").
Students usually do not know their exact attendance percentage until a shortage list is published, and by then it is often too late to recover to the required 75%.
Faculty spend extra time typing registers into spreadsheets and preparing monthly reports for the department.
At the same time, students have no simple way to plan and measure their own study time, so poor attendance and poor study habits go unnoticed until exam results arrive.

## 2. Who is affected

| Group | Pain points |
|---|---|
| **Students** | • Do not know their real-time attendance % for each subject<br>• Find out about a shortage only when the list is published<br>• Lose lecture time while attendance is taken<br>• Honest students are treated the same as those who use proxies<br>• No single place to plan study time, track tasks and stay focused<br>• Get distracted by their phone while studying |
| **Faculty** | • Spend lecture minutes on roll call every class<br>• Find it hard to catch proxies in large classes<br>• Copy paper registers into spreadsheets by hand<br>• Spend extra effort on monthly and semester reports<br>• Cannot easily see which students are at risk early enough to help |
| **College admin** | • Attendance data is spread across many registers and files<br>• Hard to check compliance with the 75% rule across departments<br>• Slow to produce reports for audits, parents and management<br>• No reliable proof that attendance records were not changed later<br>• Costly hardware options (biometric/RFID) need installation and maintenance |

## 3. Root causes

1. **Manual, paper-based process:** attendance is recorded by hand, so it is slow and must be typed in again later.
2. **No identity check at marking time:** a voice or a signature does not prove the student is physically present.
3. **No live feedback loop:** data reaches students weeks later, so they cannot act in time.
4. **Scattered records:** each faculty member keeps a separate register in their own format, so combining them is extra work.
5. **Hardware solutions are costly:** biometric and RFID systems need devices in every room, plus maintenance, and can form queues.
6. **Attendance and study habits are treated separately:** nothing connects "Am I attending?" with "Am I actually studying?"

## 4. Our solution idea

We will build a mobile-friendly web app (a Progressive Web App, or PWA) that works on any smartphone browser, with no app-store install needed. In class, the faculty member opens a live QR code on the projector that **changes every 10 seconds**. Students scan it with their phone to mark attendance in a couple of seconds. To stop proxies, the system checks that the code has not expired, that the phone is **inside the campus geofence**, and that the scan comes from the **student's own registered device**. Students see their attendance % for each subject in real time and get an **alert when they drop below 75%**. The same app also helps them study better with a **Pomodoro focus timer, a to-do task list and daily goals**. Faculty and admins get **dashboards and one-click report exports**. The app is **free for students**, and colleges pay an **annual subscription per student**.

## 5. Unique value proposition

> **Proxy-resistant attendance in seconds, plus a built-in study coach, on the phone every student already has, with no extra hardware.**

## 6. Target customers and users

| Role | Who | Why they care |
|---|---|---|
| **Paying customer** | Private engineering and arts & science colleges, then autonomous colleges and universities | Lower admin workload, reliable records for audits and compliance, better student outcomes |
| **Decision makers** | Principal, HODs, IQAC / academic coordinator, management | Approve the budget and policy |
| **Primary users** | Students (UG/PG) with a smartphone | Quick attendance, live %, early alerts, study tools (free) |
| **Primary users** | Faculty | Saves class time, fewer proxies, automatic reports |
| **Secondary users** | College admin / office staff | Central dashboard, user management, geofence setup |

**First target segment (beachhead):** our own college and similar private engineering colleges in our region, starting with one department as a pilot.

## 7. Assumptions we must validate with the survey

Question IDs (S1–S12, student survey) refer to `03-survey/survey-questions.md`.

| # | Assumption | Tested by | What would support it |
|---|---|---|---|
| A1 | Most students have their own smartphone with a working camera and internet on campus | S1 | A large majority answer "Yes, my own phone" |
| A2 | Taking attendance wastes noticeable class time | S3 | Most answers are "2 to 5 minutes" or more per class |
| A3 | Proxy attendance happens often enough to be a real problem | S4 | Average score of 3 or higher on the 1–5 scale |
| A4 | Students do not know their current attendance % | S5, S6 | Many answer "No" or "Only roughly" |
| A5 | Students struggle to stay focused and track study time | S8, S9 | Average focus difficulty of 3 or higher; few use any tracking tool |
| A6 | Students are interested in a combined attendance + productivity app | S11, S12 | Average interest of 4 or higher; productivity features are picked as well as attendance ones |
| A7 | Faculty spend significant effort on attendance reports | Not covered: student-only survey | Not tested by the survey. List as "not yet validated" (optional: ask our guide or 2–3 faculty informally) |
| A8 | Faculty are willing to switch to a QR-based system | Not covered: student-only survey | Not tested by the survey. List as "not yet validated" (optional: ask our guide or 2–3 faculty informally) |
| A9 | Students accept a location check only at the moment of scanning | S10 | Most students are comfortable (4–5) |

> If the survey does **not** support an assumption, we will write that honestly in our report and change the idea (for example, drop or reprioritise a feature).
