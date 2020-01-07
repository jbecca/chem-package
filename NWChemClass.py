class NWChem:
    '''
    read and interpret data from NWChem files
    '''
    def __init__(self, name):

        import os
        self.name = name
        self.jobtype = 'NWChem'
        self.calctype = set()
        nwchem_in = os.path.splitext(name)[1] == '.nw'
        with open(name) as f:
            if 'Northwest Computational Chemistry Package' in f.read():
                nwchem_out = True
            else:
                nwchem_out = False

        if nwchem_in:
            from input_block import collect_input
            collect_input(self, name)
        if nwchem_out:
            from input_block import collect_input
            collect_input(self, name)
            from nwchem_functions import collect_dipole
            collect_dipole(self, name)
            from nwchem_functions import collect_output_prop
            collect_output_prop(self, name)
            from nwchem_functions import collect_energy
            collect_energy(self, name)