#list of all possible rotations in numerical notations (calculated by hand)
rotations = [
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
[0, 1, 3, 4, 5, 6, 2, 8, 9, 10, 11, 7, 12], 
[0, 1, 4, 5, 6, 2, 3, 9, 10, 11, 7, 8, 12], 
[0, 1, 5, 6, 2, 3, 4, 10, 11, 7, 8, 9, 12], 
[0, 1, 6, 2, 3, 4, 5, 11, 7, 8, 9, 10, 12],

[0, 2, 7, 8, 3, 1, 6, 11, 12, 9, 4, 5, 10],
[0, 2, 6, 7, 8, 3, 1, 5, 11, 12, 9, 4, 10], 
[0, 2, 1, 6, 7, 8, 3, 4, 5, 11, 12, 9, 10],
[0, 2, 3, 1, 6, 7, 8, 9, 4, 5, 11, 12, 10],
[0, 2, 8, 3, 1, 6, 7, 12, 9, 4, 5, 11, 10],
    
[0, 3, 1, 2, 8, 9, 4, 5, 6, 7, 12, 10, 11],
[0, 3, 2, 8, 9, 4, 1, 6, 7, 12, 10, 5, 11], 
[0, 3, 4, 1, 2, 8, 9, 10, 5, 6, 7, 12, 11], 
[0, 3, 8, 9, 4, 1, 2, 7, 12, 10, 5, 6, 11], 
[0, 3, 9, 4, 1, 2, 8, 12, 10, 5, 6, 7, 11],
    
[0, 4, 1, 3, 9, 10, 5, 6, 2, 8, 12, 11, 7],
[0, 4, 3, 9, 10, 5, 1, 2, 8, 12, 11, 6, 7], 
[0, 4, 5, 1, 3, 9, 10, 11, 6, 2, 8, 12, 7],
[0, 4, 9, 10, 5, 1, 3, 8, 12, 11, 6, 2, 7],
[0, 4, 10, 5, 1, 3, 9, 12, 11, 6, 2, 8, 7],

[0, 5, 1, 4, 10, 11, 6, 2, 3, 9, 12, 7, 8],
[0, 5, 4, 10, 11, 6, 1, 3, 9, 12, 7, 2, 8],
[0, 5, 6, 1, 4, 10, 11, 7, 2, 3, 9, 12, 8], 
[0, 5, 10, 11, 6, 1, 4, 9, 12, 7, 2, 3, 8], 
[0, 5, 11, 6, 1, 4, 10, 12, 7, 2, 3, 9, 8],

[0, 6, 1, 5, 11, 7, 2, 3, 4, 10, 12, 8, 9],
[0, 6, 2, 1, 5, 11, 7, 8, 3, 4, 10, 12, 9], 
[0, 6, 5, 11, 7, 2, 1, 4, 10, 12, 8, 3, 9],
[0, 6, 7, 2, 1, 5, 11, 12, 8, 3, 4, 10, 9], 
[0, 6, 11, 7, 2, 1, 5, 10, 12, 8, 3, 4, 9],
    
[0, 7, 2, 6, 11, 12, 8, 3, 1, 5, 10, 9, 4],
[0, 7, 6, 11, 12, 8, 2, 1, 5, 10, 9, 3, 4], 
[0, 7, 8, 2, 6, 11, 12, 9, 3, 1, 5, 10, 4], 
[0, 7, 11, 12, 8, 2, 6, 5, 10, 9, 3, 1, 4], 
[0, 7, 12, 8, 2, 6, 11, 10, 9, 3, 1, 5, 4],
    
[0, 8, 2, 7, 12, 9, 3, 1, 6, 11, 10, 4, 5],
[0, 8, 3, 2, 7, 12, 9, 4, 1, 6, 11, 10, 5], 
[0, 8, 7, 12, 9, 3, 2, 6, 11, 10, 4, 1, 5], 
[0, 8, 9, 3, 2, 7, 12, 10, 4, 1, 6, 11, 5], 
[0, 8, 12, 9, 3, 2, 7, 11, 10, 4, 1, 6, 5],

[0, 9, 3, 8, 12, 10, 4, 1, 2, 7, 11, 5, 6],
[0, 9, 4, 3, 8, 12, 10, 5, 1, 2, 7, 11, 6], 
[0, 9, 8, 12, 10, 4, 3, 2, 7, 11, 5, 1, 6], 
[0, 9, 10, 4, 3, 8, 12, 11, 5, 1, 2, 7, 6], 
[0, 9, 12, 10, 4, 3, 8, 7, 11, 5, 1, 2, 6],

[0, 10, 4, 9, 12, 11, 5, 1, 3, 8, 7, 6, 2],
[0, 10, 5, 4, 9, 12, 11, 6, 1, 3, 8, 7, 2], 
[0, 10, 9, 12, 11, 5, 4, 3, 8, 7, 6, 1, 2], 
[0, 10, 11, 5, 4, 9, 12, 7, 6, 1, 3, 8, 2], 
[0, 10, 12, 11, 5, 4, 9, 8, 7, 6, 1, 3, 2],

[0, 11, 5, 10, 12, 7, 6, 1, 4, 9, 8, 2, 3],
[0, 11, 6, 5, 10, 12, 7, 2, 1, 4, 9, 8, 3], 
[0, 11, 7, 6, 5, 10, 12, 8, 2, 1, 4, 9, 3], 
[0, 11, 10, 12, 7, 6, 5, 4, 9, 8, 2, 1, 3], 
[0, 11, 12, 7, 6, 5, 10, 9, 8, 2, 1, 4, 3],

[0, 12, 10, 9, 8, 7, 11, 5, 4, 3, 2, 6, 1],
[0, 12, 9, 8, 7, 11, 10, 4, 3, 2, 6, 5, 1], 
[0, 12, 7, 11, 10, 9, 8, 2, 6, 5, 4, 3, 1], 
[0, 12, 8, 7, 11, 10, 9, 3, 2, 6, 5, 4, 1],
[0, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

#list of all possible edge combination in numerical notation (calculated by hand)
edges = [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [2, 7], [2, 6], [2, 3], [2, 8], [3, 4], [3, 8], [3, 9], [4, 5], [4, 9], 

         [4, 10],[5, 6], [5, 10], [5, 11], [6, 7], [6, 11], [7, 8], [7, 11], [7, 12], [8, 9], [8, 12], [9, 10], 
         [9, 12], [10, 11], [10, 12],[11,12] ]

#list of clusters that I created a long time ago, unfortunalety I have to compare the new list
#with this otherwise I create chaos
old_list_of_clusters = [  
    ['Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],    
    
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
        
    ['Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],

    ['Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],

    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni'],

    ['Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni'],
        
    ['Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu'],
    ['Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu'],
        
    ['Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Cu', 'Ni'],
        
    ['Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu'],
        
    ['Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu'],
        
    ['Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
    ['Ni', 'Cu', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni'],
        
    ['Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Cu'],
        
    ['Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
    ['Ni', 'Cu', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni'],
        
    ['Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni', 'Ni']
    ]


#coordinates of optimized Cu13 clusters - I use that cords to approximate every cluster
cluster_cor = [
[-6.632957,6.037575,-2.050718],
[-9.241954,2.060907,-0.976492],
[-2.640703,4.539228,-4.420866],
[-6.855627,-1.813741,-2.622112],
[-2.759545,-0.255579,-4.71534],
[-0.01822,1.841885,-1.301971],
[-2.381029,5.705427,0.346483],
[-6.508221,4.192226,2.431102],
[-6.631873,-0.643828,2.133855],
[-2.629153,-2.128603,-0.209281],
[-2.411965,1.616422,2.934027],
#under this comment coordinates of center atom are
[-4.631614,1.94986,-1.127662],
[-6.855157,2.307289,-5.204222]]

paths = [(0, 0, 12, 13), (0, 1, 12, 12), (1, 1, 11, 12), (1, 2, 11, 11), (2, 2, 10, 11), (3, 3, 10, 11), (4, 3, 10, 11), (2, 3, 10, 10), (3, 3, 10, 10), (4, 3, 10, 10), (3, 3, 9, 10), (3, 3, 9, 10), (4, 4, 9, 10), (4, 4, 9, 10), (5, 5, 9, 10), (3, 4, 9, 9), (3, 4, 9, 9), (4, 4, 9, 9), (4, 4, 9, 9), (5, 5, 9, 9), (4, 4, 8, 9), (4, 4, 8, 9), (5, 5, 8, 9), (4, 4, 8, 9), (4, 4, 8, 9), (4, 4, 8, 9), (5, 5, 8, 9), (5, 5, 8, 9), (5, 5, 8, 9), (6, 6, 8, 9), (5, 5, 8, 9), (5, 5, 8, 9), (4, 5, 8, 8), (4, 5, 8, 8), (5, 5, 8, 8), (4, 5, 8, 8), (4, 5, 8, 8), (4, 5, 8, 8), (5, 5, 8, 8), (5, 5, 8, 8), (5, 5, 8, 8), (6, 6, 8, 8), (5, 5, 8, 8), (5, 5, 8, 8), (5, 5, 7, 8), (5, 5, 7, 8), (6, 6, 7, 8), (5, 6, 7, 8), (5, 5, 7, 8), (5, 5, 7, 8), (6, 6, 7, 8), (6, 7, 7, 8), (5, 5, 7, 8), (5, 5, 7, 8), (5, 6, 8, 8), (5, 5, 7, 8), (6, 6, 7, 8), (6, 6, 7, 8), (5, 6, 7, 7), (5, 6, 7, 7), (6, 6, 7, 7), (5, 6, 7, 8), (5, 6, 7, 7), (5, 6, 7, 7), (6, 6, 7, 8), (6, 7, 7, 7), (5, 6, 7, 7), (5, 6, 7, 7), (5, 7, 8, 8), (5, 6, 7, 7), (6, 7, 7, 7), (6, 6, 7, 7), (6, 6, 6, 7), (6, 6, 6, 8), (6, 6, 6, 7), (6, 6, 6, 7), (6, 6, 6, 7), (6, 6, 6, 7), (7, 7, 6, 8), (6, 6, 6, 8), (6, 6, 6, 7), (6, 6, 6, 8), (7, 7, 6, 7), (7, 7, 7, 7), (6, 7, 6, 8), (6, 6, 7, 7), (6, 7, 6, 8), (6, 7, 6, 7), (6, 6, 6, 8), (6, 6, 6, 7), (7, 7, 6, 7), (6, 6, 6, 7), (6, 6, 7, 7), (6, 6, 7, 8), (7, 8, 7, 7), (6, 7, 6, 7), (7, 7, 5, 6), (7, 7, 5, 6), (7, 7, 6, 6), (7, 8, 5, 6), (7, 7, 5, 6), (7, 7, 5, 6), (7, 8, 6, 6), (7, 7, 6, 7), (7, 7, 5, 6), (7, 7, 5, 6), (8, 8, 5, 7), (7, 7, 5, 6), (7, 7, 6, 7), (7, 7, 6, 6), (6, 7, 6, 6), (6, 8, 6, 6), (6, 7, 6, 6), (6, 7, 6, 6), (6, 7, 6, 6), (6, 7, 6, 6), (6, 8, 7, 7), (6, 8, 6, 6), (6, 7, 6, 6), (6, 8, 6, 6), (6, 7, 7, 7), (7, 7, 7, 7), (6, 8, 6, 7), (7, 7, 6, 6), (6, 8, 6, 7), (6, 7, 6, 7), (6, 8, 6, 6), (6, 7, 6, 6), (6, 7, 7, 7), (6, 7, 6, 6), (7, 7, 6, 6), (7, 8, 6, 6), (7, 7, 7, 8), (6, 7, 6, 7), (8, 8, 4, 5), (8, 8, 4, 5), (8, 8, 5, 5), (8, 8, 4, 5), (8, 8, 4, 5), (8, 8, 4, 5), (8, 8, 5, 5), (8, 8, 5, 5), (8, 8, 5, 5), (8, 8, 6, 6), (8, 8, 5, 5), (8, 8, 5, 5), (7, 8, 5, 5), (7, 8, 5, 5), (7, 8, 6, 6), (7, 8, 5, 6), (7, 8, 5, 5), (7, 8, 5, 5), (7, 8, 6, 6), (7, 8, 6, 7), (7, 8, 5, 5), (7, 8, 5, 5), (8, 8, 5, 6), (7, 8, 5, 5), (7, 8, 6, 6), (7, 8, 6, 6), (9, 9, 3, 4), (9, 9, 3, 4), (9, 9, 4, 4), (9, 9, 4, 4), (9, 9, 5, 5), (8, 9, 4, 4), (8, 9, 4, 4), (8, 9, 5, 5), (8, 9, 4, 4), (8, 9, 4, 4), (8, 9, 4, 4), (8, 9, 5, 5), (8, 9, 5, 5), (8, 9, 5, 5), (8, 9, 6, 6), (8, 9, 5, 5), (8, 9, 5, 5), (10, 10, 2, 3), (10, 10, 3, 3), (10, 10, 4, 3), (9, 10, 3, 3), (9, 10, 3, 3), (9, 10, 4, 4), (9, 10, 4, 4), (9, 10, 5, 5), (11, 11, 1, 2), (10, 11, 2, 2), (10, 11, 3, 3), (10, 11, 4, 3), (12, 12, 0, 1), (11, 12, 1, 1), (12, 13, 0, 0)]