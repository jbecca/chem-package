import unittest
from collect import collect

class TestNWChemInputFiles(unittest.TestCase):

    #a user wants to manipulate information in a file, so first the file is supplied
    def setUp(self):
       self.file = collect('./testfiles/test.nw') 

    def test_inputName(self):
        self.assertEqual(self.file.name, './testfiles/test.nw')

    def test_inputJobtype(self):
        self.assertEqual(self.file.jobtype, 'NWChem')

if __name__ == '__main__':
    unittest.main()
