class NWChem:
    '''
    read and interpret data from NWChem files
    '''
    def __init__(self, name):

        import os
        self.name = name
        self.jobtype = 'NWChem'
        self.calctype = set()
        f = open(name).read()
        nwchem_in = os.path.splitext(name)[1] == '.nw'
        nwchem_out = 'Northwest Computational Chemistry Package' in f
        if nwchem_in:
            from input_block import collect_input
            collect_input(self, name)
        if nwchem_out:
            from input_block import collect_input
            collect_input(self, name)
            from nwchem_functions import collect_dipole
            collect_dipole(self, name)