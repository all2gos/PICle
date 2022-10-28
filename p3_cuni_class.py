from p1_creating_clusters_db import compute
from p2_particle_joining import edge, corners, neighbor_list
from p4_mass_center import mass_center
from p5_pathways import *

class CuNi_cluster():
    def __init__(self, topology):
        self.topology = topology
    
    def no_nickel(self, topology):
        no_nickel = 0
        for atom in topology:
            if atom == 'Ni':
                no_nickel += 1
        return no_nickel

    def centre_atom(self, topology):
        if topology[0] == 'Ni':
            return 1
        else:
            return 0
    def name(self, topology):
        return topology

    def corners(self,topology):
        return corners(neighbor_list(topology))
    
    def edges(self,topology):
        return edge(neighbor_list(topology))

    def mass_center(self, topology):
        return mass_center(topology)

    def pathways(self, topology):
        return (scanning_cluster(topology,'Ni'), scanning_cluster(topology,'Ni',True),scanning_cluster(topology,'Cu'), scanning_cluster(topology,'Cu',True))

    def creating_db_row(self,topology):
        db_row = [] 
        db_row.append(CuNi_cluster(topology).no_nickel(topology))
        db_row.append(CuNi_cluster(topology).name(topology))
        db_row.append(len(CuNi_cluster(topology).corners(topology)))
        db_row.append(len(CuNi_cluster(topology).edges(topology)))
        db_row.append(2*db_row[-1]+9*db_row[-2])
        db_row.append(CuNi_cluster(topology).corners(topology))
        db_row.append(CuNi_cluster(topology).edges(topology))
        db_row.append(CuNi_cluster(topology).centre_atom(topology))
        db_row.append(f"{CuNi_cluster(topology).mass_center(topology):.4}")
        db_row.append(CuNi_cluster(topology).pathways(topology))

        return db_row


if __name__ == '__main__': 
    topology_of_clusters = compute()
    clusters = []
    for cluster in topology_of_clusters[52:55]:
        clusters.append(CuNi_cluster(cluster).creating_db_row(cluster))
print(clusters)
