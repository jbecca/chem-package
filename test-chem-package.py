import unittest
from collect import collect

class TestNWChemInputFiles(unittest.TestCase):
    #a user wants to manipulate information in a file, so first the file is supplied
    def setUp(self):
       self.file = collect('./testfiles/test.nw') 

    def test_inputProperties(self):
        self.assertEqual(self.file.name, './testfiles/test.nw')
        self.assertEqual(self.file.jobtype, 'NWChem')
        self.assertEqual(self.file.title, 'dplot_dft')
        self.assertEqual(self.file.calctype, set(['dplot', 'dft']))

    #def test_inputCoords(self):


class TestNWChemOutputFiles(unittest.TestCase):
    def setUp(self):
        self.file = collect('./testfiles/nwchem.out')

    def test_outputProperties(self):
        self.assertEqual(self.file.name, './testfiles/nwchem.out')
        self.assertEqual(self.file.jobtype, 'NWChem')
        self.assertEqual(self.file.title, 'dplot_dft')
        self.assertEqual(self.file.calctype, set(['dplot', 'dft']))
        self.assertEqual(self.file.walltime, '1.0')
        self.assertEqual(self.file.jobfinish, True)

    def test_dipole(self):
        self.assertEqual(self.file.dipole[0], 0.1) 
        self.assertEqual(self.file.dipole[1], 0.2) 
        self.assertEqual(self.file.dipole[2], 0.3) 

if __name__ == '__main__':
    unittest.main()
