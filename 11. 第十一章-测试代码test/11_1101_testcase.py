import unittest
from class_model.name_joint import NameJoint
class NameJointTest(unittest.TestCase):
    def test_jointName(self):
        format_name = NameJoint().jointName("hr" , "yuan")
        print(format_name)
        self.assertEqual(format_name , "Hr Yuan")

test = NameJointTest()
test.test_jointName()

