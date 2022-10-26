from p0_usable_data import *
from itertools import combinations

#function that translate some rotation in numerical notation into one-dimensional Cu-Ni notation in correct order
def transcription(nickel,r):
    lista = [0,1,2,3,4,5,6,7,8,9,10,11,12]
    for j in range(len(nickel)):
        for i in range(len(r)):
            if nickel[j]==r[i]:
                lista[i]='Ni'
    for k in range(len(r)):
        if lista[k]!='Ni':
            lista[k]='Cu'
    return lista

#funtion that generate all independence combination with given number of nickel with cluster
def generating_clusters(number_of_nickel):
    possibilities = []

    #creating all combinations of position of nickel
    nickel = list(combinations(rotations[0],number_of_nickel))

    for i in range(len(nickel)):
        counter = 0
        for rotation in range(len(rotations)):

            #if rotations give topology that are in list of possibilities, leave it
            rotation_test = transcription(nickel[i],rotations[rotation])
            if rotation_test in possibilities:
                break
            else:
                counter +=1
        #only if all rotations are give cluster that isn't in list of possibilties program add new cluster to the list
        if counter == len(rotations):
            possibilities.append(transcription(nickel[i],rotations[0]))
    #print(len(possibilities))
    #for i in range(len(possibilities)):
        #print(possibilities[i])
    return possibilities

#function that create all possible clusters from a to b number of nickel
def creating_list_of_all_clusters(a=0,b=7):
    clusters = []
    for number_of_nickel in range(a,b):
        possibilities = generating_clusters(number_of_nickel)
        for topology in range(len(possibilities)):
            clusters.append(possibilities[topology])
    return clusters

#function that replace all Ni into Cu and all Cu into Ni in list of clusters (I use this for generate clusters that include 8-13 no. Nickel)
def reverse_atoms_in_cluster(possibilities):
    for rot in range(len(possibilities)):
        for atom in range(len(possibilities[rot])):
            if possibilities[rot][atom] == 'Cu':
                possibilities[rot][atom] = 'Ni'
            else:
                possibilities[rot][atom] = 'Cu'
    return possibilities

#unfortunalety at this place I need to restructurized data set that i just create because in old scripts procedure was slightly different
#I don't want to change the order of clusters in list because it will be too much effort so need to rearanged data set right now
def normalize_db(clusters):
    #I just imported old list of clusters, compare old one with new one and creating final list with old, correct order
    #I printed lenght of that list and bool value to be sure that replacement procedure went correct
    
    list_of_correct_spot = []
    for old_spot in range(len(old_list_of_clusters)):
        for new_spot in range(len(clusters)):
            if clusters[new_spot] == old_list_of_clusters[old_spot]:
                list_of_correct_spot.append(new_spot)
    correct_clusters = []
    for old_spot in range(len(clusters)):
        correct_clusters.append(clusters[list_of_correct_spot[old_spot]])
    print('number of clusters:', len(correct_clusters))
    print('new db is identical as old db:',correct_clusters == old_list_of_clusters)
    return correct_clusters

def compute(a=0,b=7):
    r_clusters = reverse_atoms_in_cluster(creating_list_of_all_clusters(a,b))
    clusters = creating_list_of_all_clusters(a,b)
    clusters += r_clusters
    clusters = normalize_db(clusters)
    return clusters




