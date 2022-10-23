from ast import arg
from sys import argv
import os

catalog = '/home/rstottko/all_pos/'
os.chdir(catalog)

print(argv)
 
lista = [os.listdir(catalog)]


for no_cluster in range(int(argv[2]), int(argv[3])+1):
    
    for connection in argv[4:]:
        for f_atom in range(1,14):
            for s_atom in range(1,14):
                for letter in ['c','e']:
                    name_of_dir = (str(no_cluster) + '_' + str(connection) + '_' + str(f_atom) +'_' + str(s_atom) + letter)
                    
                    if name_of_dir in lista:
                        print(name_of_dir)

                
                        



#a = przechodze przez wszystkie foldery

#vasp = odpalam vaspa
#p = printuje wszystkie nazwy folderow
#info = pozyskuje informacje 

#python stav.py vasp 16 31 
#python stav.py dir 16 31
#python stav.py info 16 31