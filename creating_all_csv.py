import pandas as pd
from p1_creating_clusters_db import compute
from p3_cuni_class import *

def creating_df():
    topology_of_clusters = compute()
    clusters = []
    for cluster in topology_of_clusters:
        clusters.append(CuNi_cluster(cluster).creating_db_row(cluster))
        print(cluster)
    clusters_df = pd.DataFrame(data = clusters, columns = ['no_nickel','topology','no_corners_comb','no_edges_comb','all_comb','all_corners_comb','all_edges_comb','c_atom','mass_center','shortest_paths','conformation','bonds'])
    clusters_df.to_csv('all.csv')
    print(clusters_df.info())    
    print('.csv file were created successfully!')
    return clusters_df

if __name__ == '__main__':
    creating_df()