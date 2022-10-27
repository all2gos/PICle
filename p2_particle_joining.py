from p0_usable_data import edges
#simple function that returns all neighbor locations of a given atom (with or without center atom)
def neighbor(atom, centre = False):
    #atoms are returned in the correct order - that means that 
    #for example atom number 1 has 5 neighbors: 2,3,4,5,6 AND for example atom 4 is a neighbor of atoms 5 and 3
    if atom==1:
        neight_list = [0, 2, 3, 4, 5, 6]
    elif atom==2:
        neight_list = [0, 3, 1, 6, 7, 8]
    elif atom==3:
        neight_list = [0, 2, 8, 9, 4, 1]
    elif atom==4:
        neight_list = [0, 10, 5, 1, 3, 9]
    elif atom==5:
        neight_list = [0, 4, 10, 11, 6, 1]
    elif atom==6:
        neight_list = [0, 7, 2, 1, 5, 11]
    elif atom==7:
        neight_list = [0, 11, 12, 8, 2, 6]
    elif atom==8:
        neight_list = [0, 3, 2, 7, 12, 9]
    elif atom==9:
        neight_list = [0, 12, 10, 4, 3, 8]
    elif atom==10:
        neight_list = [0, 5, 4, 9, 12, 11]
    elif atom==11:
        neight_list = [0, 12, 7, 6, 5, 10]
    elif atom==12:
        neight_list = [0, 10, 9, 8, 7, 11]
    if centre == False:
        neight_list = neight_list[1:]
        return neight_list
    else:
        return neight_list

#function that analyses the neighborhood of all atoms in cluster, the function returned information in a list for example [1,2.1,3,Cu] means
#that atom number 1 is cooper with 2 nickel (.1 inform that between these nickels one another cooper are present) 
#neghbour and 3 other cooper neighbor

def neighbor_list(cluster):  
    
    variant_point_one = [[0,2],[1,3],[2,4],[0,3],[1,4],[1,3,4],[0,2,4],[0,1,3],[1,2,4],[0,2,3]]

    #final list
    neighbors = []
    
    for atom_in_cluster in range(12):        
        
        intra_neighbor_list = []
        ni = 0
        cu = 0 
        for neight_atom in range(5):
            
            #scanning all neighbor atoms and categorizing them into ni or cu variable
            if cluster[neighbor(atom_in_cluster + 1)[neight_atom]] == 'Ni':
                ni += 1
            else:
                cu += 1 

        if ni == 2 or ni ==3:
            
            #list where I put the position of the nickel atom
            ni_coordinates = []
            for k in range(5):
                if cluster[neighbor(atom_in_cluster + 1)[k]] == 'Ni':                    
                    ni_coordinates.append(k)  
        
        #convention is that I need to add information about the number of the atom just now
        intra_neighbor_list.append(atom_in_cluster + 1) 

        #checking if the analyzing situation is 2.1         
        try:
            if sorted(ni_coordinates) in variant_point_one and (ni ==2 or ni ==3):
                intra_neighbor_list.append(ni+0.1)
            else:
                intra_neighbor_list.append(ni) 
        except:
            intra_neighbor_list.append(ni)            
        intra_neighbor_list.append(cu)
        
        if cluster[atom_in_cluster + 1] == 'Ni':
            intra_neighbor_list.append('Ni')
        else:
            intra_neighbor_list.append('Cu')   
        neighbors.append(intra_neighbor_list)
    return neighbors

#function that returns all possible, independent ways of the spot to the corners particle joining
def corners(neighbor_list):
    
    #I made a returning list, I put it into them first element because I use the lenght of that list later
    combinations_c = [[1, 1, 1]]
    
    for i in range(len(neighbor_list)):        
             
        counter = 0
        
        #[10, 1, 4, 'Cu'] and [11, 1, 4, 'Cu'] are different atoms but particles will be joining in the same way
        for j in range(len(combinations_c)):
            if neighbor_list[i][1:] == combinations_c[j][1:]:
                counter+=1
                break
            
        if counter == 0:
            combinations_c.append(neighbor_list[i])
   
    return combinations_c[1:]

#function that returns all possible, independent ways of the spot to the edges particle joining
def edge(neighbor_list):

    #I made here pairs of edges with neighbor information
    pairs = [] 
    for pairs_of_edges in edges:
        pair = []
        pair.append(neighbor_list[pairs_of_edges[0]-1])
        pair.append(neighbor_list[pairs_of_edges[1]-1]) 
        pairs.append(pair)

    #I made a returning list, I put it into them first element because I use the length of that list later 
    combinations_e = [[[1, 1, 1, 1],[1,1,1,1]]]
           
    #I need to check either [1,4,Ni,0,5,Cu] or [0,5,Cu,1,4,Ni] are in list of results
    for i in range(len(pairs)):
        counter = 0
        for j in range(len(combinations_e)):
            if pairs[i][0][1:]+pairs[i][1][1:] == combinations_e[j][0][1:] + combinations_e[j][1][1:]:
                counter += 1                
            elif pairs[i][1][1:] + pairs[i][0][1:] == combinations_e[j][0][1:] + combinations_e[j][1][1:]:
                counter += 1
        if counter == 0:
            combinations_e.append(pairs[i])
    return combinations_e[1:]
