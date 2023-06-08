import pandas as pd
from p0_usable_data import rotations

df = pd.read_csv('all.csv')

#function which replaces topology back to python list format
def topology_to_list(imported_topology):
    topology = []
    for i in range(2,80,6):
        topology.append(imported_topology[i:i+2])        
    return topology

def corners_to_list(connection_info):
    final_list = []    
    for i in range(1,len(connection_info)):
        
        #I check if there is a character in front of the checked character 
        #suggesting that the list has just opened, which eliminates all 
        #numerical information about neighbors
        
        #then I check to see if there is a comma after that number to know if it is a
        #a one-digit number or a two-digit number
        #this last condition eliminates the addition of the first parenthesis to the list
        #and generally it's supposed to be here because it's a bit jarring if it's not there
        
        if connection_info[i-1] == '[' and connection_info[i+1] == ',' and connection_info[i] in  ['1','2','3','4','5','6','7','8','9']:
            final_list.append(int(connection_info[i]))  
        elif connection_info[i-1] == '[' and connection_info[i] in  ['1']:
            final_list.append(int((connection_info[i]) + (connection_info[i+1])))
    return final_list

#for edges there it will be a little bit more complicated

def edges_to_list(connection_info):
    
    final_list = []    
    single_connection = []
    for i in range(len(connection_info)):       
    
    #first atom in the connection (it's the same as corners_to_list_function)
        if connection_info[i-1] == '[' and connection_info[i+1] == ',' and connection_info[i] in  ['1','2','3','4','5','6','7','8','9']:
            single_connection.append(connection_info[i])  
        elif connection_info[i-1] == '[' and connection_info[i] in  ['1']:
            single_connection.append(connection_info[i] + connection_info[i+1])

    for position in range(0,len(single_connection)-1,2):
        double_connection = []
        double_connection.append(int(single_connection[position]))
        double_connection.append(int(single_connection[position+1]))
        final_list.append(double_connection)
    return final_list

def rotation(no_cluster):

    edges = edges_to_list(df['all_edges_comb'][no_cluster])
    corners = corners_to_list(df['all_corners_comb'][no_cluster])
    
    combinations = edges + corners
    
    r_corners = []
    r_edges = []
    r_mirror_edges = []

    for configuration in combinations:
              
        if isinstance(configuration,list):
            
            #program needs to detect two situations: when atom 1 and atom 2 in rotations are atom 1 and atom 2 in combinations and
            #when atom 1 and atom 2 in rotations are atom 2 and atom 1 in combinations (due to unsymetriccally cases)
            for rotation in rotations:
                if rotation[1] == int(configuration[0]) and rotation[2] == int(configuration[1]):
                    r_edges.append(rotation)                    
                elif rotation[1] == int(configuration[1]) and rotation[2] == int(configuration[0]):
                    r_mirror_edges.append(rotation)
        else:

            #in corners joining case there is much simpler           
            
            for rotation in rotations:
                if rotation[1] == int(configuration):
                    r_corners.append(rotation)
                    #program do not have a break at this place because I want to check all five possible rotation along single atom

    return r_edges, r_mirror_edges, r_corners, #combinations

#function which translate numerical rotations into CuNi notations
def numerical_rotation_to_cuni(no_cluster, rotation):
    
    topology = topology_to_list(df['topology'][no_cluster])
    nickel_position = []
    result = []
    for no_ni in range(len(topology)):
        if topology[no_ni] == 'Ni':
            nickel_position.append(no_ni)
    for pos in rotation:        
        if pos in nickel_position:
            result.append('Ni') 
        else:
            result.append('Cu') 
    return result

def all_non_repetitive_rotations(no_cluster, corners = True,  edges = True, mirrors = True):
    all_possible_rotations = []

    if corners == True:

        corners_rotations = rotation(no_cluster)[2]
        all_non_repetitive_corners_rot = []
        for rot in range(len(corners_rotations)):

            cluster = numerical_rotation_to_cuni(no_cluster,corners_rotations[rot])
            if cluster not in all_non_repetitive_corners_rot:
                all_non_repetitive_corners_rot.append(cluster)
        all_possible_rotations.append(all_non_repetitive_corners_rot)

    if edges == True:
        edges_rotations = rotation(no_cluster)[0]
        all_non_repetitive_edges_rot = []
        for rot in range(len(edges_rotations)):

            cluster = numerical_rotation_to_cuni(no_cluster,edges_rotations[rot])
            if cluster not in all_non_repetitive_edges_rot:
                all_non_repetitive_edges_rot.append(cluster)
        all_possible_rotations.append(all_non_repetitive_edges_rot)

    if mirrors == True:
        mirrors_rotations = rotation(no_cluster)[1]
        all_non_repetitive_mirrors_rot = []
        for rot in range(len(mirrors_rotations)):

            cluster = numerical_rotation_to_cuni(no_cluster,mirrors_rotations[rot])
            if cluster not in all_non_repetitive_mirrors_rot:
                all_non_repetitive_mirrors_rot.append(cluster)
        all_possible_rotations.append(all_non_repetitive_mirrors_rot)
    return all_possible_rotations

if __name__ == '__main__':    
    counter = 0
    for no_cluster in range(len(df)):
        lista = (all_non_repetitive_rotations(no_cluster))    
        lenght = len(lista[0])+len(lista[1])+len(lista[2])
        counter += lenght
        original_lenght = df['no_corners_comb'][no_cluster]+2*df['no_edges_comb'][no_cluster]    
        
        if original_lenght>lenght+3:
            print(str(no_cluster), 'is identical to other cluster which already is in the df')
        
    