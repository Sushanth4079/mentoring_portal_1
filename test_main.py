import unittest


class TestMentoringPortal(unittest.TestCase):

    def test_online_slot(self):
        self.assertEqual(
            "Online Mentoring Slot",
            "Online Mentoring Slot"
        )

    def test_campus_slot(self):
        self.assertEqual(
            "On-Campus Mentoring Slot",
            "On-Campus Mentoring Slot"
        )


if __name__ == "__main__":
    unittest.main()
