def collect(file):
    '''
    Function to intialize collecting file of interest
    '''
    import sys, os

    nwchem_in = os.path.splitext(file)[1] == '.nw'
    with open(file) as f:
        if 'Northwest Computational Chemistry Package' in f.read():
            nwchem_out = True
    if nwchem_in or nwchem_out:
        from NWChemClass import NWChem
        d = NWChem(file)
    return d