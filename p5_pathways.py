from p2_particle_joining import neighbor
#funtion that creates all_possible pathways of lenght n
def all_pathway(n):

    set_containing_all_paths = set()
    #this list contains all paths of length 1, this is a initial list
    set_of_path = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]]

    for _ in range(n-1):        
        final_paths =[]

        for no_path in range(len(set_of_path)):   
            for k in range(5): 

                path = list(set_of_path[no_path])

                #this is an atom that neighbors with last atom of current path
                el = neighbor(set_of_path[no_path][-1])[k]

                #if this atom isn't in that path before, program just adds new, longer path to the final list
                if el in set_of_path[no_path]:
                    continue
                else:                    
                    path.append(el)
                    final_paths.append(path)
        
        #the final iteration of the inner loop creates a new initial list containing a path that is one longer

        set_of_path = list(final_paths)

    #now program will be reduce duplicates pathways 
    for i in range(len(final_paths)):
        final_paths[i] = tuple(sorted(final_paths[i]))

    final_paths = set(final_paths)

    return list(final_paths)

#function that returns lenght of shortes pathway of given cluster by given atom (including or not center metal)
def scanning_cluster(cluster, metal, center = False):

    #need to create special generator

    def generator(center):        
        if center == True:
            i = 0            
        else:
            i = 1
        while i < 13:
            yield i
            i+=1

    #checking how much interested metals are in cluster
    no_metal = 0
    
    for atom in generator(center):        
        if cluster[atom] == metal:                        
            no_metal+=1

    for path_lenght in range(no_metal,13):
        scanning_pathways = all_pathway(path_lenght)        
        for path in range(len(scanning_pathways)):
            metal_counter = 0
            for no_atom in range(path_lenght):    
                if cluster[scanning_pathways[path][no_atom]] == metal:
                    metal_counter+=1            
            if metal_counter == no_metal:
                #print(cluster, scanning_pathways[path], len(scanning_pathways[path]))              
                break  
        if metal_counter == no_metal:
            break         
    return len(scanning_pathways[path])

if __name__ == '__main__':    
    print(len(all_pathway(3)))
    print(scanning_cluster(['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'], 'Ni'))
    
