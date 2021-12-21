#def read_xyz(filename):
#   """Read filename in XYZ format and return lists of atoms and coordinates.
#   If number of coordinates do not agree with the statd number in
#   the file it will raise a ValueError.
#   """
def read_xyz(filename):

 atoms = [] #array of atom type of each atom
 coordinates = [] #list of coordinates row vectors of each atom
#---------------------------
#opening the xyz file
#----------------------------
 xyz = open(filename)
 n_atoms = int(xyz.readline())
 title = xyz.readline()

 for line in xyz:
          spl = line.strip().split()
          if len(spl) == 4:  # this will take care of both empty lines and 
                            # lines containing greater than or less than four items
           atom,x,y,z=spl     # separate the string into different variables
           atoms.append(atom) # append the atom symbols to list of atoms. 
           coordinates.append([float(x), float(y), float(z)]) #convert x,y,z to flot and append
 xyz.close() #close the xyz file

 print('Number of Atoms:',n_atoms)
 if n_atoms != len(coordinates):
        raise ValueError("File says %d atoms but read %d points." % (n_atoms, len(coordinates)))
 return n_atoms, atoms, coordinates

