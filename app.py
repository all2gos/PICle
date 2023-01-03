import pandas as pd
import numpy as np
import streamlit as st
from joblib import load
from sklearn.preprocessing import MinMaxScaler


"""
## Welcome to the site in which Procedure to Indicate CLusters Energy (pickle for short) has been deployed!

#### You can put topological values of a cluster that you are interested in and then the machine learning model will return energy value for that cluster
"""

model = load('final_ada_m.joblib')

main_menu = st.radio('You can choose the specific topological value or you can just write down topology of clusters',('Specific value','Topology'))

if main_menu == 'Specific value':
    number_of_nickel = st.slider('Choose number of nickel',0,13,0)
    centre_atom = st.radio('Choose central atom of cluster', ('Ni','Cu'))
    mass_center = st.number_input('Write down the lenght beetwen mass and geometry centre of cluster')
    ni_ncentre = st.slider('Choose lenght of the shortest path throught nickel without centre atom',0,12,0)
    ni_centre = st.slider('Choose lenght of the shortest path throught nickel with centre atom',0,12,0)
    cu_ncentre = st.slider('Choose lenght of the shortest path throught copper without centre atom',0,12,0)
    cu_centre = st.slider('Choose lenght of the shortest path throught copper with centre atom',0,12,0)
    ni_0 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 0 nickel atoms', 0,12,0)
    ni_8 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 1 nickel atoms', 0,12,0)
    ni_17 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 2 nickel atoms', 0,12,0)
    ni_25 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 3 nickel atoms', 0,12,0)
    ni_33 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 4 nickel atoms', 0,12,0)
    ni_42 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 5 nickel atoms', 0,12,0)
    ni_50 = st.slider('Choose numbers of atom in cluster which first coordinate sphere consist of 6 nickel atoms', 0,12,0)
    nini = st.slider('Pick the number of ni-ni bonds in cluster'0,84,0)
    cucu = st.slider('Pick the number of cu-cu bonds in cluster'0,84,0)
    nicu = st.slider('Pick the number of ni-cu bonds in cluster'0,84,0)
    hydrogen = st.radio('Is cluster includes hydrogen?',('Yes','No'))
    first_atom = st.radio('What is the first atom of the cluster to which the molecule attaches?',('Cu','Ni'))
    second_atom = st.radio('What is the second atom of the cluster to which the molecule attaches?',('Cu','Ni'))

data = pd.DataFrame(data=[[
    5,  #number of nickel in cluster 0-13
    1,  #c_atom, Ni = 1
    0.04651,  #mass_center 0-0.05071
    7,  #ni_ncentre
    8,    #ni_centre
    5,  #cu_ncentre
    5,  #cu_centre
    0,  #0ni
    0,  #8ni
    1,    #17ni
    3,  #25ni
    5,  #33ni
    2,  #42ni
    1,  #50ni
    38,  #nini
    14,  #cucu
    32,  #nicu
    0,  #if particle has a hydrogen then it is equall to 1
    1,  #type_of_first_atom_ni
    1   #type_of_second_atom_ni
]])
minmax = pd.DataFrame(data=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[13,1,0.05071,12,13,12,13,12,12,10,10,10,12,12,84,84,52,1,1]])
scaler = MinMaxScaler()
scaler.fit(minmax)
X = scaler.transform(data)

model.predict(X)[0]