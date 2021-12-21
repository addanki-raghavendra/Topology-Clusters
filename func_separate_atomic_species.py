#def read_xyz(filename):
#   """Read filename in XYZ format and return lists of atoms and coordinates.
#   If number of coordinates do not agree with the statd number in
#   the file it will raise a ValueError.
#   """



#---------------------------
#opening the xyz file
#----------------------------
def separate_atomic_species(n_atoms, atoms,coordinates):
#function to separate coordinates and get the arrays of indices of different atoatomic species
 import collections
 
 elements=[]
 for x in atoms:
   if x not in elements:
    elements.append(x)
 print(elements)

# """
# atoms11=[]
# atoms22=[]
#
# coordinates11=[]
# coordinates22=[]
#
# for i in range(0,len(elements)):
#         if atoms[i]==elements[0] then:
#                atoms11.append(i)
#                coordinates11.append(coordinates[i])
#         if atoms[i]==elements[1] then:
#                atoms22.append(i)
#                coordinates11.append(coordinates[i])#
#
#                print(atoms11)
#                print(atoms22)
#                print(coordinates11)
#                print(coordinates22)
#
# """
#return atoms, coordinates print coordinates[1]

#
#
#------------------------------
# METHOD 2: USING A COUNTER
#------------------------------
#convert list of atom symbols to a collection the first coordinates1 is S and coordinates 2 is Au.

 c=collections.Counter(atoms)
 print(c)
 d=c.keys()
 e=c.values()
 list_keys=[k for k in d]
 list_values=[v for v in e]

 n_atoms1=list_values[0]
 n_atoms2=list_values[1]
 #these are ordered by the alphabetically, or by value, order is different from elements. #sulfur is first. 
 print(d)
 print(e)
 print(list_keys)
 print(len(list_keys))
 print(list_values[0])
 print(list_values[1])
 #COUNTING THE DIFFERENT ATOM TYPES
 #record the index of atoms of different types
 print('list of keys 0',list_keys[0])
 print('list of keys 1',list_keys[1])
 print('first atom type',atoms[0])
 print('first coordinates type',coordinates[0])

 atoms1=[]  #or use a 2D array for storing the different atoms types. 
 coordinates1=[] 
 atoms2=[]  #or use a 2D array for storing the different atoms types. 
 coordinates2=[] 

 #use one dimensional arrays for each atom types ... fill up the arrays.#separate the coordinats. 


 for i in range(0,n_atoms):
  print(i)
  print(list_keys[1])
  #for j in range(1,len(list_keys)+1):
  
  if atoms[i]==list_keys[0]:
         atoms1.append(i)
         coordinates1.append(coordinates[i])
         print(atoms[i])
  if atoms[i]==list_keys[1]:
         atoms2.append(i)
         coordinates2.append(coordinates[i])
         print(atoms[i])

# 
#

 return n_atoms1, n_atoms2,elements, atoms1, atoms2, coordinates1,coordinates2

 #coordinates11,
 #coordinates22, 

#print(coordinates1)
#print(coordinates2)
#print(atoms1)
#print(atoms2)
#OUTPUT:

#atoms, n_atoms,natomtypes, elements, list_values, list_key_values, no_atom_types

#iatoms1 indices
#iatoms2 indices 
#coordinates 
#coordinates1
#coordinates2

#convert the arrays to numpy. 
#print('Au coordinates')
#for i in range(1,list_values[0]):
# print(coordinates1[1][i])
#for i in range(1,list_values[0]):
# print('Au atom indices')
# print(atoms1[1][i])

#convert to numpy arrays. 
#Separate the values
#for x in range(1,8):
#     print(atoms[x])
#     print(coordinates[x])
#    total number of different elements size(elements)
#

#for line in file:
#convert the list of vectors to numpy matrix with atom type (
#separate the vectors into different.
