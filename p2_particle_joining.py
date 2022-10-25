#simple function that returns all neighbour location of given atom (with or without centre atom)
def neighbour(atom, centre = False):
    #atoms are returns in correct order - that mean that 
    #for example atom number 1 has 5 neighbours: 2,3,4,5,6 AND for example atom 4 is neighbour of atom 5 and 3
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

#function that analyse neughbourhood of all atom in cluster, function returned information in a list for example [1,2.1,3,Cu] means
#that atom number 1 is cooper with 2 nickel (.1 inform that beetween these nickels one another cooper are present) 
#neghbour and 3 other cooper neighbour
def neighbour_list(cluster):  
    
    variant_point_one = [[0,2],[1,3],[2,4],[0,3],[1,4],[1,3,4],[0,2,4],[0,1,3],[1,2,4],[0,2,3]]
    #final list
    neighbours = []
    
    for atom_in_cluster in range(12):        
        
        intra_neighbour_list = []
        ni = 0
        cu = 0 
        for neight_atom in range(5):
            
            #scanning all neighbour atoms and categorizing them into ni or cu variable
            if cluster[neighbour(atom_in_cluster + 1)[neight_atom]] == 'Ni':
                ni += 1
            else:
                cu += 1 

        if ni == 2 or ni ==3:
            
            #list where I put position of nickel atom
            ni_coordinates = []
            for k in range(5):
                if cluster[neighbour(atom_in_cluster + 1)[k]] == 'Ni':                    
                    ni_coordinates.append(k)  
        
        #convention is that I need to add information about number of atom just now
        intra_neighbour_list.append(atom_in_cluster + 1) 

        #checking if analyzing situation is 2.1         
        try:
            if sorted(ni_coordinates) in variant_point_one and (ni ==2 or ni ==3):
                intra_neighbour_list.append(ni+0.1)
            else:
                intra_neighbour_list.append(ni) 
        except:
            intra_neighbour_list.append(ni)            
        intra_neighbour_list.append(cu)
        
        if cluster[atom_in_cluster + 1] == 'Ni':
            intra_neighbour_list.append('Ni')
        else:
            intra_neighbour_list.append('Cu')   
        neighbours.append(intra_neighbour_list)
    return neighbours

