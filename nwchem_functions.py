def collect_dipole(self, name):
    from numpy import array, append
    dipoles = []
    l = open(name)
    for line in l:
        line = line.rstrip()
        if 'Multipole analysis of the density' in line:
            blank = next(l)
            blank = next(l)
            blank = next(l)
            blank = next(l)
            blank = next(l)
            blank = next(l)
            dipstring = list(filter(None, next(l).rstrip().split(' '))) 
            dipoles.append(dipstring[4])
            dipstring = list(filter(None, next(l).rstrip().split(' '))) 
            dipoles.append(dipstring[4])
            dipstring = list(filter(None, next(l).rstrip().split(' '))) 
            dipoles.append(dipstring[4])
        self.dipole = array(dipoles[0:3], dtype=float)
    l.close()

def collect_output_prop(self, name):
    with open(name) as f:
        lastline = list(f)[-1]
        templist = list(filter(None, lastline.split(' ')))
        self.jobfinish = False
        if templist[0] == 'Total':
            self.jobfinish = True
            self.walltime = templist[5].rstrip()
            self.walltime = self.walltime[:-1]