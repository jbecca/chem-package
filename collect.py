def collect(file):
    '''
    Function to intialize collecting file of interest
    '''
    import sys, os

    f = open(file).read()
    nwchem_in = os.path.splitext(file)[1] == '.nw'
    nwchem_out = 'Northwest Computational Chemistry Package' in f
    if nwchem_in or nwchem_out:
        from NWChemClass import NWChem
        d = NWChem(file)
    return d