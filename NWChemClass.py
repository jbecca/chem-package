class NWChem:
    '''
    read and interpret data from NWChem files
    '''

    def __init__(self, name):
        self.name = name
        self.jobtype = 'NWChem'