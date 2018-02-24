import unittest

from mailtest.api import Api


class MailTestTest(unittest.TestCase):
    active = "active.mailtest.in"
    disposable = "disposable.mailtest.in"
    robot = "robot.mailtest.in"
    invalid = "invalid.mailtest.in"
    unknown = "unknown.mailtest.in"
    error = "error.mailtest.in"

    def setUp(self):
        self.api = Api()

    def test_active(self):
        result = self.api.check(self.active)
        code = result.get("code")
        status = result.get("status")
        self.assertIsInstance(result, dict)
        self.assertIn(code, self.api.codes[self.api._active])
        self.assertEqual(status, self.api.statuses[self.api._active])

    def test_disposable(self):
        result = self.api.check(self.disposable)
        code = result.get("code")
        status = result.get("status")
        self.assertIsInstance(result, dict)
        self.assertIn(code, self.api.codes[self.api._disposable])
        self.assertEqual(status, self.api.statuses[self.api._disposable])

    def test_robot(self):
        result = self.api.check(self.robot)
        code = result.get("code")
        status = result.get("status")
        self.assertIsInstance(result, dict)
        self.assertIn(code, self.api.codes[self.api._robot])
        self.assertEqual(status, self.api.statuses[self.api._robot])

    def test_invalid(self):
        result = self.api.check(self.invalid)
        code = result.get("code")
        status = result.get("status")
        self.assertIsInstance(result, dict)
        self.assertIn(code, self.api.codes[self.api._invalid])
        self.assertEqual(status, self.api.statuses[self.api._invalid])

    def test_unknown(self):
        result = self.api.check(self.unknown)
        code = result.get("code")
        status = result.get("status")
        self.assertIsInstance(result, dict)
        self.assertIn(code, self.api.codes[self.api._unknown])
        self.assertEqual(status, self.api.statuses[self.api._unknown])

    def test_error(self):
        result = self.api.check(self.error)
        code = result.get("code")
        status = result.get("status")
        self.assertIsInstance(result, dict)
        self.assertIn(code, self.api.codes[self.api._error])
        self.assertEqual(status, self.api.statuses[self.api._error])


if __name__ == "__main__":
    unittest.main()
