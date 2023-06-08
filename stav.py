catalog = '/home/rstottko/all_pos/'
grad2_path = 'python ~/bin/2grad2.py'


import os
os.chdir(catalog)
counter = 0
primary_list = os.listdir(catalog) 
list_of_all_currently_clusters = []
for i in range(len(primary_list)):
	if ((primary_list[i][0])) in ['1','2','3']:
		list_of_all_currently_clusters.append(primary_list[i])

#print((primary_list))
print(len(list_of_all_currently_clusters))
list_of_MO = []
list_of_MOCOM = []

for i in range(len(list_of_all_currently_clusters)):
	if 'MOCOM' in list_of_all_currently_clusters[i]:
		list_of_MOCOM.append(list_of_all_currently_clusters[i])
	elif 'MO_' in list_of_all_currently_clusters[i]:
		list_of_MO.append(list_of_all_currently_clusters[i]) 
for klaster in range(0,len(list_of_all_currently_clusters)):
	name_of_dir = list_of_all_currently_clusters[klaster]
	try:
		counter +=1
		os.chdir(name_of_dir)
		#os.system('rm -r ' + name_of_dir)

# printing all name of directories
#		print(counter, name_of_dir)
#		list_of_all_currently_clusters.append(name_of_dir)

#starting the calculations
#		os.system('sub-vasp')

#checking results after calculations
		os.system(grad2_path)
		os.chdir(catalog)
	except:
		continue
print(counter)
