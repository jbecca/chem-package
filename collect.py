def collect(file):
    '''
    Function to intialize collecting file of interest
    '''
    import sys, os

    nwchem_in = os.path.splitext(file)[1] == '.nw'
    if nwchem_in:
        from NWChemClass import NWChem
        d = NWChem(file)
    return d