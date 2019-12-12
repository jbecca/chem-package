def collect_input(self, name):
    '''
    Collect input section of file
    '''
    self.title = None
    l = open(name)
    for line in l:
        line = line.rstrip()
        if 'start ' in line and self.title == None:
            self.title = line.split(' ')[1]
        if 'task dplot' in line:
            self.calctype.add('dplot')
        if 'task dft' in line:
            self.calctype.add('dft')


