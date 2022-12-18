import pandas as pd
import numpy as np
import streamlit as st
from joblib import dump, load
from sklearn.preprocessing import MinMaxScaler


model = load('final_ada_m.joblib')


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