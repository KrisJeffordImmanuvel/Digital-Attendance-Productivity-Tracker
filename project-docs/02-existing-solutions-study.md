# 02 · Existing Solutions Study

**Venture:** Digital Attendance and Productivity Tracker for Students

---

## 1. Purpose and method

Before building anything, we studied how colleges take attendance today and how students track their study time. We wanted to know what each approach does well and where it falls short.

**Rules we followed so that this document stays honest:**

- We describe **approaches** in general terms rather than reviewing specific commercial products.
- We do **not** quote prices, market sizes or accuracy percentages that we cannot prove. Costs are given only as **relative levels** (Low / Medium / High).
- Anything we still need to check is marked **[VERIFY]**. The team will confirm these items with our guide, vendors or official sources before the final submission.
- We cite only well-known, real references (listed at the end).

---

## 2. Comparison table

Cost levels are relative to each other and include setup plus yearly running cost for one college. They are our judgement, not measured figures.

| Approach | How it works | Cost (relative) | Accuracy | Proxy risk | Main limitations |
|---|---|---|---|---|---|
| **Manual roll call / paper sheet** | Faculty call names or pass a sheet; students answer or sign | **Low** (paper, but costs faculty time) | Depends on the faculty member; errors happen when copying into registers | **High:** a friend can answer or sign | Uses class time every lecture; registers must be typed in again; no real-time view; easy to change later |
| **RFID / smart ID cards** | Student taps an ID card on a reader at the classroom or gate | **Medium–High** (cards + a reader per room + software) | High for "card was present" | **Medium–High:** a friend can tap someone else's card | Proves the card was there, not the person; readers need power, network and maintenance; queues at the reader; lost cards |
| **Fingerprint biometrics** | Student places a finger on a scanner; the print is matched against stored templates | **High** (scanner per room, maintenance) | Generally high, but drops with wet, dirty or worn fingers [VERIFY] | **Low:** hard to fake casually | Queues in large classes; hygiene concerns from shared contact; sensitive biometric data must be protected under data-protection law [VERIFY: DPDP Act 2023 obligations]; device downtime |
| **Face recognition** | A camera captures faces; software detects them (e.g. Viola–Jones style detectors) and matches them (e.g. deep embeddings such as FaceNet) | **High** (good cameras, compute, setup) | Varies with lighting, camera angle, crowd size and dataset quality [VERIFY] | **Low–Medium:** photo/video spoofing is possible without liveness checks | Privacy concerns about continuous video of students; needs strong lighting and placement; possible bias across groups; heavy setup; biometric data rules [VERIFY] |
| **Existing QR attendance apps** | Faculty display a QR code; students scan it with a phone app | **Low–Medium** (software only) | High for "this account scanned" | **Medium–High if the code is static:** a photo of the QR can be shared on WhatsApp; a friend can log in on another phone | Many use one static code per class [VERIFY: check how common rotating codes are]; often no location or device check; usually attendance only, with no student-facing insights |
| **General productivity apps** (Pomodoro timers, to-do lists) | Students use separate apps for focus timers, task lists and habit tracking | **Low / Free** for the student | Not applicable to attendance | Not applicable | Not linked to the academic timetable or attendance; colleges cannot see it; students must install and juggle several apps; easy to abandon |

---

## 3. Notes on each approach

### 3.1 Manual roll call / paper sheet
The most common method and the default fallback. It needs no technology, but it costs lecture time in every class, and copying the data into spreadsheets adds a second chance for errors. Proxies are hard to catch in large classes because faculty cannot recognise every voice or signature.

### 3.2 RFID / smart ID cards
Contactless cards (commonly based on the ISO/IEC 14443 proximity-card standard) are fast to tap. However, the system verifies the **card**, not the **student**, so card sharing remains a weakness. Every room or entry point needs a reader, which brings installation and maintenance costs.

### 3.3 Fingerprint biometrics
Fingerprint matching is a mature field (see Maltoni et al., *Handbook of Fingerprint Recognition*). It strongly reduces proxies, but shared contact scanners create queues and hygiene concerns. Storing biometric templates also brings privacy and legal responsibilities. **[VERIFY]** which obligations apply to colleges under India's Digital Personal Data Protection Act, 2023.

### 3.4 Face recognition
Modern systems combine two steps:
1. **Face detection:** finding faces in an image. The classic real-time method is the boosted cascade by **Viola and Jones (2001)**.
2. **Face recognition:** deciding whose face it is. Early methods include **Eigenfaces (Turk & Pentland, 1991)**; modern systems use deep-learning embeddings such as **FaceNet (Schroff, Kalenichenko & Philbin, 2015)**.

Recognition can be accurate in controlled conditions, but classroom conditions (lighting, angles, many faces at once, people partly hidden) make it harder. It also raises privacy questions because it captures images of every student. Without a liveness check, a photo or video of the student may be able to fool it.

### 3.5 Existing QR attendance apps
QR codes (ISO/IEC 18004) are free to generate and every smartphone camera can read them. The weakness is that a **static** QR code is just an image, so it can be photographed and forwarded to absent friends. Better designs regenerate the code every few seconds (an idea similar to time-based one-time passwords, RFC 6238) and add extra checks. **[VERIFY]** through hands-on trials which of these checks are common in apps used by colleges in our region.

### 3.6 General productivity apps
The **Pomodoro Technique**, created by **Francesco Cirillo**, splits work into focused intervals (traditionally 25 minutes) followed by short breaks. Many free timer and to-do apps follow this idea. They are useful but separate from academic life: they do not know the student's timetable, subjects or attendance, so they cannot say, for example, "You are at 72% in Maths. Plan a revision session today."

---

## 4. Key observations

1. **Hardware-based methods** (RFID, fingerprint, face) cost more and need devices in every room, but they are the only ones that link attendance to the physical person or card.
2. **Software-only methods** (QR) are cheap and fast, but simple versions are easy to cheat.
3. Almost every approach gives the data to **faculty and admin**, while students rarely see their own live attendance.
4. **No approach we studied joins attendance with study productivity** in one place for the student.
5. Privacy matters: biometric and video methods collect much more personal data than is needed just to mark attendance.

---

## 5. Gap we fill

> Colleges need a **low-cost, hardware-free** attendance system that is **hard to cheat**. Students need **live visibility of their attendance** together with **tools to study better**. No single common approach provides both.

Our app fills this gap by combining:

| Gap | How we fill it |
|---|---|
| Static QR codes are easy to share | The QR **changes every 10 seconds**, and each code works only for a short window |
| Remote scanning from home or the hostel | A **campus geofence** check at the moment of scanning, with no continuous tracking |
| A friend logs in on their own phone | **Device binding:** one registered device per student; any change needs admin approval |
| Hardware cost and maintenance | Uses phones students already own and the existing classroom projector; no readers or scanners |
| Students learn about shortages too late | **Live attendance %** per subject and an **alert below 75%** |
| Productivity apps are disconnected from studies | A built-in **Pomodoro timer, tasks and daily goals**, linked to the student's subjects |
| Manual reporting effort | **Dashboards and one-click export** for faculty and admin |
| Privacy concerns with biometrics | **No biometric data stored**; location is checked only during a scan |

---

## 6. References

1. Viola, P., & Jones, M. (2001). *Rapid object detection using a boosted cascade of simple features.* Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
2. Turk, M., & Pentland, A. (1991). *Eigenfaces for recognition.* Journal of Cognitive Neuroscience, 3(1), 71–86.
3. Schroff, F., Kalenichenko, D., & Philbin, J. (2015). *FaceNet: A unified embedding for face recognition and clustering.* Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR).
4. Cirillo, F. *The Pomodoro Technique.* (Method developed in the late 1980s; published as a book. [VERIFY] edition and publisher of the copy we cite.)
5. Maltoni, D., Maio, D., Jain, A. K., & Prabhakar, S. *Handbook of Fingerprint Recognition.* Springer. ([VERIFY] edition we cite.)
6. ISO/IEC 18004. *Information technology: Automatic identification and data capture techniques: QR Code bar code symbology specification.*
7. ISO/IEC 14443. *Identification cards: Contactless integrated circuit cards: Proximity cards.*
8. M'Raihi, D., Machani, S., Pei, M., & Rydell, J. (2011). *TOTP: Time-Based One-Time Password Algorithm.* IETF RFC 6238.
9. W3C. *Geolocation API.* https://www.w3.org/TR/geolocation/
10. Government of India. *The Digital Personal Data Protection Act, 2023.* ([VERIFY] how it applies to student attendance data.)
11. Our university's attendance regulations. ([VERIFY] the exact minimum % and condonation rules. We assume 75% in this project.)
