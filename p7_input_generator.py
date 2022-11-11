import os, shutil
import pandas as pd
from p6_rotations import all_non_repetitive_rotations, topology_to_list, rotation, numerical_rotation_to_cuni
from p0_usable_data import cluster_cor, particle_cor_opt
from p8_data_to_make_spe_input import *

df = pd.read_csv('all.csv')

#funtion that calculates the weighted average of particle based on clear Cu and Ni clusters
def cord_of_particle(no_cluster, type_of_connection):
           
    ni = df['no_nickel'][no_cluster]
    cu = 13 - ni
    
    if type_of_connection == 'MO':        
        
        ni_cord = clear_Ni_MO_opt[-3:]
        cu_cord = clear_Cu_MO_opt[-3:]   
        
    elif type_of_connection == 'MOCOM':
        
        ni_cord = clear_Ni_MOCOM_opt[-4:]
        cu_cord = clear_Cu_MOCOM_opt[-4:]
            
    final_cord = []

        
    for particle in range(len(ni_cord)):
        particle_final_cord = []
        for coordinate in range(3):            
            particle_final_cord.append((ni*ni_cord[particle][coordinate]+cu*cu_cord[particle][coordinate])/13)
        final_cord.append(particle_final_cord)

    return final_cord

#MC, MO. MOC --> corners 
#MOC_, MOCM, MOCM_H_bond, MOCM_H_n_bond, MOCOM, MCMH, MCMH_p, MCM_p --> edges

generating_cluster = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133]
generating_particle =['MOCOM','MO']
sp_or_opt = 'sp'
rot_input = 'y'
pwd = os.getcwd() 
try:
    os.chdir(pwd+ '\\clusters')
except FileNotFoundError:
    os.system('mkdir clusters')
    os.chdir(pwd+ '\\clusters')

for particle in generating_particle:
    for cluster in generating_cluster:
        passed_rotations = []
        if particle in ['MC','MO','MOC']:
            possible_rotations = rotation(cluster)[2]
        else:
            possible_rotations = rotation(cluster)[0]
        
        for rot in range(len(possible_rotations)):   
            passed_rotations.append(numerical_rotation_to_cuni(cluster, possible_rotations[rot]))                     
            #to delete duplicates
            if possible_rotations[rot] not in passed_rotations:
                passed_rotations.append(possible_rotations[rot])   

        if sp_or_opt == 'sp':
            added_particle = cord_of_particle(cluster,particle)
                        
        elif sp_or_opt == 'opt':
            for type_of_particle in particle_cor_opt:
                if type_of_particle[0] == particle:
                    added_particle = type_of_particle[1]
        if len(added_particle) == 4:
            hydrogen = 1
        else:
            hydrogen = 0
        
        if rot_input == 'y':
            range_of_for = len(possible_rotations)
        elif rot_input == 'n':
            range_of_for = 1

        for case in range(range_of_for):
            name_of_dir = str(cluster) + '_' + particle + '_' + str(possible_rotations[case][1]) + '_' + str(possible_rotations[case][2])     
            os.mkdir(name_of_dir)  

            #first input file - INCAR
            shutil.copyfile(r''+pwd+'\INCAR', r''+pwd+ '\clusters\\' +name_of_dir+'\INCAR')

            #second input file - POTCAR

            os.chdir(pwd + '\\PSEUDO\\Cu')
            with open('POTCAR','r') as file:
                lines_Cu = file.readlines()
            os.chdir(pwd + '\\PSEUDO\\Ni')
            with open('POTCAR','r') as file:
                lines_Ni = file.readlines()
            os.chdir(pwd + '\\PSEUDO\\C')
            with open('POTCAR','r') as file:
                lines_C = file.readlines()
            os.chdir(pwd + '\\PSEUDO\\O')
            with open('POTCAR','r') as file:
                lines_O = file.readlines()

            if hydrogen ==1:
                os.chdir(pwd + '\\PSEUDO\\H')
                with open('POTCAR','r') as file:
                    lines_H = file.readlines()                   
                lines_potcar = lines_Cu + lines_Ni+lines_C+lines_O+lines_H
            else:
                lines_potcar = lines_Cu + lines_Ni+lines_C+lines_O

            os.chdir(pwd + '\\clusters\\' + name_of_dir)    
            with open('POTCAR','w') as file:
                for line in lines_potcar:
                    print(line.rstrip('\n'), file = file)

            
            #third file - POSCAR
            ni_list = []
            cu_list = []        
                        
            with open('POSCAR','w+') as file: 
                
                print(str(cluster),str(particle), file=file)
                print('   1.00000000000000', file=file)        
                print('    24    0.0000000000000000    0.0000000000000000', file = file)        
                print('    0.0000000000000000   24    0.0000000000000000', file = file)
                print('    0.0000000000000000    0.0000000000000000   24', file = file)

                if hydrogen == 1:                
                    print('Cu Ni C O H',file = file)
                else:
                    print('Cu Ni C O',file = file)

                if hydrogen == 1:
                    print(' ' + str((13-df['no_nickel'][cluster]))+' ' +str(df['no_nickel'][cluster]) + ' 1 2 1', file= file)
                else:
                    print(' ' + str((13-df['no_nickel'][cluster]))+' ' +str(df['no_nickel'][cluster]) + ' 1 2', file= file)
                print('Cartesian',file=file)        

                topology = topology_to_list(df['topology'][cluster])
                for j in range(13):            
                    atom = (topology[j] +'     ' + str(cluster_cor[j][0])+'    ' + str(cluster_cor[j][1])+'    ' + str(cluster_cor[j][2]))             
                    
                    if atom[0:2] == 'Cu':
                        cu_list.append(atom)
                    else:
                        ni_list.append(atom)

                    #all Cu atoms first
                for k in range(len(cu_list)):
                    print(cu_list[k][6:],file=file)

                    #then nickels
                for k in range(len(ni_list)):
                    print(ni_list[k][6:],file=file) 

                for k in range(3+hydrogen):                    
                        print(' ' + str(added_particle[k][0])+ ' ' + str(added_particle[k][1]) + ' '+ str(added_particle[k][2]), file = file)
            #wracam do folderu klastry
            os.chdir(pwd + '\\clusters')



