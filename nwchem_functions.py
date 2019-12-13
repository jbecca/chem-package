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
            print(dipstring[4])
            dipoles.append(dipstring[4])
            dipstring = list(filter(None, next(l).rstrip().split(' '))) 
            print(dipstring[4])
            dipoles.append(dipstring[4])
            dipstring = list(filter(None, next(l).rstrip().split(' '))) 
            print(dipstring[4])
            dipoles.append(dipstring[4])
        self.dipole = array(dipoles[0:3], dtype=float)
