import unittest
from unittest.mock import MagicMock

class LoginSchedule:
    def user_login(self, email, password):
        if not email or not password:  # Handling empty input
            return "Email or password cannot be empty", False
        if email == "old_user@gmail.com" and password == "Password123":
            return "Login Successful", True
        return "Login Failed", False

class UserLogin(unittest.TestCase):
    def setUp(self):
        self.portal_system = LoginSchedule()
        self.email = "old_user@gmail.com"
        self.password = "Password123"

    def test_user_login_success(self):
        message, status = self.portal_system.user_login(self.email, self.password)
        self.assertTrue(status)
        self.assertEqual(message, "Login Successful")

    def test_user_login_failure(self):
        message, status = self.portal_system.user_login("user@example.com", "incorrect")
        self.assertFalse(status)
        self.assertEqual(message, "Login Failed")

    def test_user_login_empty_input(self):
        message, status = self.portal_system.user_login("", "")
        self.assertFalse(status)
        self.assertEqual(message, "Email or password cannot be empty")

class StudySchedule:
    def create_schedule(self, subject, date, time, duration):
        if any(not val for val in [subject, date, time, duration]):
            return "All fields must be filled", False
        return "Study Schedule Created", True

class TestStudySchedule(unittest.TestCase):
    def setUp(self):
        self.portal_system = StudySchedule()
        self.study_session_details = {
            "subject": "Software Engineering",
            "date": "03-15-2024",
            "time": "10:00 AM",
            "duration": "2 hours"
        }

    def test_create_schedule(self):
        message, status = self.portal_system.create_schedule(**self.study_session_details)
        self.assertTrue(status)
        self.assertEqual(message, "Study Schedule Created")

    def test_create_schedule_missing_fields(self):
        study_session_details = {
            "subject": "Software Engineering",
            "date": "",
            "time": "10:00 AM",
            "duration": "2 hours"
        }
        message, status = self.portal_system.create_schedule(**study_session_details)
        self.assertFalse(status)
        self.assertEqual(message, "All fields must be filled")

class Reminders:
    def user_reminder(self, alerts):
        if not alerts:
            return "No alerts specified", False
        return "Alert Reminders Set", True

class Notification(unittest.TestCase):
    def setUp(self):
        self.portal_system = Reminders()
        self.alerts = ["Upcoming Due Dates", "Software Engineering 03-15-2024; Due at 10:00 AM"]

    def test_user_reminder(self):
        message, status = self.portal_system.user_reminder(self.alerts)
        self.assertTrue(status)
        self.assertEqual(message, "Alert Reminders Set")

    def test_user_reminder_no_alerts(self):
        message, status = self.portal_system.user_reminder([])
        self.assertFalse(status)
        self.assertEqual(message, "No alerts specified")

class PersonalCustomization:
    def personal_schedule(self, dates, times):
        if len(dates) != len(times):  # Check for mismatch in dates and times
            return "Dates and times count mismatch", False
        return "Personal Schedule Completed", True

class UserTime(unittest.TestCase):
    def setUp(self):
        self.portal_system = PersonalCustomization()
        self.dates = ["March 5", "March 21", "April 1"]
        self.times = ["Club Meeting: 5:00 PM-5:30 PM", "Soccer Practice: 4:30 PM-7:00 PM", "Community Service: 11:00 AM-3:00 PM"]

    def test_personal_schedule(self):
        message, status = self.portal_system.personal_schedule(self.dates, self.times)
        self.assertTrue(status)
        self.assertEqual(message, "Personal Schedule Completed")

    def test_personal_schedule_mismatch(self):
        dates = ["March 5", "March 21"]
        message, status = self.portal_system.personal_schedule(dates, self.times)
        self.assertFalse(status)
        self.assertEqual(message, "Dates and times count mismatch")

class UpdateAccountInformation:
    def update_account_info(self, email, new_email, new_password):
        if not all([email, new_email, new_password]):
            return "Missing information", False
        return "Account Information Updated", True

class TestUpdateAccountInformation(unittest.TestCase):
    def setUp(self):
        self.portal_system = UpdateAccountInformation()
        self.email = "old_users@gmail.com"
        self.new_email = "new_email@gmail.com"
        self.new_password = "NewPassword123"

    def test_update_account_information(self):
        message, status = self.portal_system.update_account_info(self.email, self.new_email, self.new_password)
        self.assertTrue(status)
        self.assertEqual(message, "Account Information Updated")

    def test_update_account_missing_info(self):
        message, status = self.portal_system.update_account_info("", self.new_email, self.new_password)
        self.assertFalse(status)
        self.assertEqual(message, "Missing information")

if __name__ == '__main__':
    unittest.main()
