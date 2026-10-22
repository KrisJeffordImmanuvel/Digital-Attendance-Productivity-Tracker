/**
 * Creates the two survey Google Forms for
 * "Digital Attendance and Productivity Tracker for Students".
 *
 * HOW TO USE (takes about 2 minutes):
 *   1. Go to https://script.google.com and click "New project".
 *   2. Delete the sample code, paste this whole file, and click Save.
 *   3. In the toolbar, choose the function "createBothForms" and click Run.
 *   4. The first time, Google asks for permission ("Review permissions" ->
 *      choose your account -> Advanced -> Go to project -> Allow).
 *      This lets the script create forms in YOUR Google Drive only.
 *   5. Open "Execution log" at the bottom: it prints the link to share
 *      and the link to edit each form. Both forms also appear in Google Drive.
 *
 * The question wording here is generated from analyze_survey.py, so the CSV
 * you download later will match the analysis script. If you edit a question
 * in Google Forms, also edit QUESTIONS in analyze_survey.py.
 *
 * Before sharing: change the F1 department list to match our college.
 */

var STUDENT_QUESTIONS = [
    {"id": "S1", "type": "choice", "title": "Do you have a smartphone that you can use during class?", "choices": ["Yes, my own smartphone", "Yes, but it is shared with family", "No"], "other": false},
    {"id": "S2", "type": "choice", "title": "How is attendance usually taken in your classes?", "choices": ["Faculty calls out names (roll call)", "A paper sheet is passed around", "Biometric or ID card machine", "An app or QR code"], "other": true},
    {"id": "S3", "type": "choice", "title": "About how much class time is spent on taking attendance in one lecture?", "choices": ["Less than 2 minutes", "2 to 5 minutes", "5 to 10 minutes", "More than 10 minutes"], "other": false},
    {"id": "S4", "type": "scale", "title": "How often do you notice proxy attendance (someone marking attendance for an absent student) in your classes?", "low": "Never", "high": "Very often"},
    {"id": "S5", "type": "choice", "title": "Do you know your current attendance percentage in each subject?", "choices": ["Yes, exactly", "Only roughly", "No"], "other": false},
    {"id": "S6", "type": "choice", "title": "Have you ever been below or close to the 75% attendance requirement?", "choices": ["Yes, I was below 75%", "Yes, I was close (75% to 80%)", "No", "I don't know"], "other": false},
    {"id": "S7", "type": "choice", "title": "On a normal day, how many hours do you study outside class?", "choices": ["Less than 1 hour", "1 to 2 hours", "2 to 4 hours", "More than 4 hours"], "other": false},
    {"id": "S8", "type": "checkbox", "title": "How do you currently plan or track your study time?", "choices": ["I don't plan or track it", "Paper notes or a diary", "A to-do list app", "A Pomodoro or focus timer app", "A calendar or planner app"], "other": true},
    {"id": "S9", "type": "scale", "title": "How hard is it for you to stay focused while studying (for example, because of phone distractions)?", "low": "Very easy", "high": "Very hard"},
    {"id": "S10", "type": "scale", "title": "How comfortable would you be if the app checked your location only at the moment you scan the attendance QR code?", "low": "Not comfortable at all", "high": "Very comfortable"},
    {"id": "S11", "type": "scale", "title": "How interested would you be in one free app that marks attendance by scanning a QR code AND helps you track your study time?", "low": "Not interested", "high": "Very interested"},
    {"id": "S12", "type": "checkbox", "title": "Which features would matter most to you? (Choose up to 3)", "choices": ["Quick QR attendance", "Live attendance % for each subject", "Alert when I go below 75%", "Pomodoro focus timer", "To-do tasks and daily goals", "Study time analytics"], "other": true, "maxChecked": 3}
  ];

var FACULTY_QUESTIONS = [
    {"id": "F1", "type": "choice", "title": "Which department do you teach in?", "choices": ["CSE", "IT", "ECE", "EEE", "Mechanical", "Civil", "Science and Humanities"], "other": true},
    {"id": "F2", "type": "choice", "title": "How do you currently take attendance?", "choices": ["Roll call", "Paper sheet", "Biometric or ID card machine", "An app or software"], "other": true},
    {"id": "F3", "type": "choice", "title": "On average, how many minutes of each lecture do you spend on attendance?", "choices": ["Less than 2 minutes", "2 to 5 minutes", "5 to 10 minutes", "More than 10 minutes"], "other": false},
    {"id": "F4", "type": "scale", "title": "How often do you face proxy attendance problems?", "low": "Never", "high": "Very often"},
    {"id": "F5", "type": "choice", "title": "How much time do you spend each month on attendance registers and reports?", "choices": ["Less than 1 hour", "1 to 3 hours", "3 to 6 hours", "More than 6 hours"], "other": false},
    {"id": "F6", "type": "scale", "title": "How willing would you be to use a QR-based attendance app that blocks proxies (changing QR code + campus location check + one device per student)?", "low": "Not willing", "high": "Very willing"},
    {"id": "F7", "type": "checkbox", "title": "What concerns would you have about using such an app? (Tick all that apply)", "choices": ["Some students do not have smartphones", "Poor mobile network in classrooms", "Student privacy", "Time needed to learn a new system", "No projector or screen in some rooms", "Technical problems during class", "No concerns"], "other": true},
    {"id": "F8", "type": "text", "title": "Any suggestions or features you would like to see?"}
  ];

var DESCRIPTION =
  'This is an anonymous survey for a college entrepreneurship project. ' +
  'Your answers are used only to study this problem and will not be shared.';

function createBothForms() {
  var student = buildForm_('Student Survey: Attendance and Study Habits', STUDENT_QUESTIONS);
  var faculty = buildForm_('Faculty Survey: Attendance Process', FACULTY_QUESTIONS);
  report_('STUDENT form', student);
  report_('FACULTY form', faculty);
}

function buildForm_(title, questions) {
  var form = FormApp.create(title);
  form.setDescription(DESCRIPTION);
  form.setCollectEmail(false);       // keep responses anonymous
  form.setProgressBar(false);
  form.setShowLinkToRespondAgain(false);

  questions.forEach(function (q) {
    var item;
    if (q.type === 'choice') {
      item = form.addMultipleChoiceItem().setTitle(q.title).setChoiceValues(q.choices);
      if (q.other) item.showOtherOption(true);
      item.setRequired(true);
    } else if (q.type === 'checkbox') {
      item = form.addCheckboxItem().setTitle(q.title).setChoiceValues(q.choices);
      if (q.other) item.showOtherOption(true);
      if (q.maxChecked) {
        item.setValidation(FormApp.createCheckboxValidation()
          .setHelpText('Please choose up to ' + q.maxChecked + ' options.')
          .requireSelectAtMost(q.maxChecked)
          .build());
      }
      item.setRequired(true);
    } else if (q.type === 'scale') {
      item = form.addScaleItem().setTitle(q.title).setBounds(1, 5).setLabels(q.low, q.high);
      item.setRequired(true);
    } else if (q.type === 'text') {
      item = form.addTextItem().setTitle(q.title);
      item.setRequired(false);         // optional suggestions question
    }
  });
  return form;
}

function report_(label, form) {
  Logger.log('==== ' + label + ' ====');
  Logger.log('Share this link:  ' + form.getPublishedUrl());
  Logger.log('Edit the form:    ' + form.getEditUrl());
}
