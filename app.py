import pandas as pd
import numpy as np
import streamlit as st
from joblib import load
from sklearn.preprocessing import MinMaxScaler


"""
### Welcome to the site in which Procedure to Indicate CLusters Energy (pickle for short) has been deployed!

##### You can put topological values of a cluster that you are interested in and then the machine learning model will return energy value for that cluster
"""

model = load('final_ada_m.joblib')

#data preprocessing

def data_preprocessing():
    if first_atom == 'Cu':
            first_atom = 0
    else:
        first_atom = 1
    
    if second_atom == 'Cu':
        second_atom = 0
    else:
        second_atom = 1
    
    if hydrogen == 'Yes':
        hydrogen = 1
    else:
        hydrogen = 0
    
    if centre_atom == 'Ni':
        centre_atom = 1
    else:
        centre_atom = 0

main_menu = st.radio('You can choose the specific topological value or you can just write down topology of clusters',('Specific value','Topology'))

if main_menu == 'Specific value':
    number_of_nickel = st.slider('Choose number of nickel',0,13,6)
    centre_atom = st.radio('Choose central atom of cluster', ('Ni','Cu'))
    mass_center = st.number_input('Write down the lenght beetwen mass and geometry centre of cluster')
    ni_ncentre = st.slider('Choose lenght of the shortest path throught nickel without centre atom',0,12,6)
    ni_centre = st.slider('Choose lenght of the shortest path throught nickel with centre atom',0,12,6)
    cu_ncentre = st.slider('Choose lenght of the shortest path throught copper without centre atom',0,12,6)
    cu_centre = st.slider('Choose lenght of the shortest path throught copper with centre atom',0,12,6)
    ni_0 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 0 nickel atoms', 0,12,6)
    ni_8 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 1 nickel atoms', 0,12,6)
    ni_17 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 2 nickel atoms', 0,12,6)
    ni_25 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 3 nickel atoms', 0,12,6)
    ni_33 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 4 nickel atoms', 0,12,6)
    ni_42 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 5 nickel atoms', 0,12,6)
    ni_50 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 6 nickel atoms', 0,12,6)
    nini = st.slider('Pick the number of ni-ni bonds in cluster',0,84,42)
    cucu = st.slider('Pick the number of cu-cu bonds in cluster',0,84,42)
    nicu = st.slider('Pick the number of ni-cu bonds in cluster',0,84,42)
    hydrogen = st.radio('Is cluster includes hydrogen?',('Yes','No'))
    first_atom = st.radio('What is the first atom of the cluster to which the molecule attaches?',('Cu','Ni'))
    second_atom = st.radio('What is the second atom of the cluster to which the molecule attaches?',('Cu','Ni'))

    

if st.button('Compute'):  
    data_preprocessing() 
    data = pd.DataFrame(data=[[
        number_of_nickel,  #number of nickel in cluster 0-13
        centre_atom,  #c_atom, Ni = 1
        mass_center,  #mass_center 0-0.05071
        ni_ncentre,  #ni_ncentre
        ni_centre,    #ni_centre
        cu_ncentre,  #cu_ncentre
        cu_centre,  #cu_centre
        ni_0,  #0ni
        ni_8,  #8ni
        ni_17,    #17ni
        ni_25,  #25ni
        ni_33,  #33ni
        ni_42,  #42ni
        ni_50,  #50ni
        nini,  #nini
        cucu,  #cucu
        nicu,  #nicu
        hydrogen,  #if particle has a hydrogen then it is equall to 1
        first_atom,  #type_of_first_atom_ni
        second_atom   #type_of_second_atom_ni
    ]])
    minmax = pd.DataFrame(data=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[13,1,0.05071,12,13,12,13,12,12,10,10,10,12,12,84,84,52,1,1]])
    scaler = MinMaxScaler()
    scaler.fit(minmax)
    X = scaler.transform(data)

    st.write('Energy of given cluster is:',model.predict(X)[0])