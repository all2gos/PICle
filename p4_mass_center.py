from p0_usable_data import cluster_cor
import math

def mass_center(cluster):
    vector_x, vector_y, vector_z, mass_sum = 0,0,0,0
    vector = []

    for atom in range(len(cluster)):
        if cluster[atom] == 'Ni':
            atom_mass = 58
        else:
            atom_mass = 63

        vector_x += atom_mass*(cluster_cor[atom][0])
        vector_y += atom_mass*(cluster_cor[atom][1])
        vector_z += atom_mass*(cluster_cor[atom][2])
        mass_sum += atom_mass
    vector.append(vector_x/mass_sum)
    vector.append(vector_y/mass_sum)
    vector.append(vector_z/mass_sum)
    
    return math.sqrt((vector[0]-cluster_cor[11][0])**2+(vector[1]-cluster_cor[11][1])**2+(vector[2]-cluster_cor[11][2])**2)


if __name__ == '__main__':
    print(mass_center(['Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni']))