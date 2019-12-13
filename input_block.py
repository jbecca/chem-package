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
        elif 'task dplot' in line:
            self.calctype.add('dplot')
        elif 'task dft' in line:
            self.calctype.add('dft')
        # stop reading line by line once end of echoed input block is found
        elif 'Northwest Computational Chemistry Package' in line:
            break

    l.close()


