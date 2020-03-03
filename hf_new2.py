#This a program to calculate the Hatree-Fock energy of a closed shell molecule
from no_of_electron import no_of_e
from distance.py import dist
#Read the geometry
input_file=open('geom.dat')   #open the file

file_content=input_file.readlines()# read the content

input_file.close()            # close the file

#print(file_content)


# store the input in list
temp_geom=[]
for line in file_content:
      v_line=line.rstrip()
      if len(v_line)>0:
        temp_geom.append(v_line.split())

print(temp_geom)


#no of atoms
NATOM=int(temp_geom[0][0])

print('Total no of atom '+str(NATOM))

ATOM_SYMBOL=[] # this list contains the atom symbols

GEOM=[] # carteian coordinate

for i in range(1,NATOM+1): 
   ATOM_SYMBOL.append(temp_geom[i][0])
   GEOM.append(temp_geom[i][1:4])
                      
                       
print('Atom Symbol')
print(ATOM_SYMBOL)

print('Cartesian Coordinate in a.u.')
print(GEOM)

# count the total no of electrons

NE=0  #this is the total no of electron

for i in range(len(ATOM_SYMBOL)):
   k=no_of_e(ATOM_SYMBOL[i])
   NE+=k 

print('Total no of electron is '+str(NE))

#calculate the nuclear repulsion energy
E_nuc=0.0
for i in range(NATOM):
    for j in range(0,i):
        z_a=no_of_e(ATOM_SYMBOL[i])
        z_b=no_of_e(ATOM_SYMBOL[i])
        R_ab=find_distance(GEOM[i],GEOM[j])
        print(R_ab)
        E_nuc+=0.5*(z_a*z_b)/R_ab

#nbasis set dimension
nbasis=7
#Read s
S=read_file("s.dat",nbasis)
