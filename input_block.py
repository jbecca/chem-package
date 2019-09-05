def collect_input(self, name):
    '''
    Collect input section of file
    '''
    self.title = None
    with open(name) as f:
        line = f.readlines()
        if 'start' in line[2]:
            self.title = line[2].split(' ')[1].rstrip()


