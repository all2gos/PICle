from p2_particle_joining import neighbor
from p0_usable_data import cluster_cor
import numpy as np

#function that returns the number of atoms in which neighborhood are n (0,1,2,3,4,5,6) atoms of nickel

def conformation_number(topology):

    results = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for atom in range(1,len(topology)):
        neighbours = neighbor(atom, center = True)        
        ni = 0       

        for n in neighbours:
            if topology[n] == 'Ni':
                ni +=1            
        
        results[ni] +=1    
    
    return list(results.values())

#funtion that calculates the number of me-me bonds
def bonds(topology, metal):

    results = 0

    for atom in range(len(topology)):
        if topology[atom] == metal:
            neighbours = neighbor(atom, center = True)
            for n in range(len(neighbours)):
                
                if topology[neighbours[n]] == metal:
                    results +=1

    #because in neighbor function atom == 0 consist a 0 position as well I need to substract one atom
    if metal == topology[0]:
        results -=1

    return results

#function that returns ni-ni, cu-cu and cu-ni numbers of bond of a given cluster
def fully_description_of_bonds(topology):

    ni_ni = bonds(topology, 'Ni')
    cu_cu = bonds(topology, 'Cu')
    ni_cu = 84 - ni_ni - cu_cu

    return ni_ni, cu_cu, ni_cu

#simple geometric distance funtion
def distance(a,b, cluster_cor = cluster_cor):   
    
    x_a, y_a, z_a = cluster_cor[a][0], cluster_cor[a][1], cluster_cor[a][2]
    x_b, y_b, z_b = cluster_cor[b][0], cluster_cor[b][1], cluster_cor[b][2]
    
    return np.sqrt((x_a - x_b)**2 + (y_a - y_b)**2 + (z_a - z_b)**2)

#funtion that returns the average distance from all atoms of given metal for atoms in which CO2 are connected

def average_dist(topology, metal, nb_of_atom):

    metals = []
    avg_dist = 0

    for i in range(len(topology)):
        if topology[i] == metal:
            metals.append(i)
    
    for m in metals:
        if m != metals:
            avg_dist += distance(nb_of_atom,m)
    
    return avg_dist/len(metal)

    


    print(ni)
if __name__ == '__main__':
    #print(conformation_number(['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu']))
    #print(fully_description_of_bonds(['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu']))
    print(average_dist(['Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'], 'Ni', 1))
   
        
        
