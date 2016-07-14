import json 
import pandas as pd 
import networkx as nx 
import numpy as np

#Parse Data
def parse(filename): 
	f = open(filename)
	m = []
	for line in f: 
		m.append(json.loads(line))
	d = pd.DataFrame(m)
	d['created_time'] = pd.to_datetime(d['created_time'])
	return d

#Create a 60 second TimeStamp 
def TimeStamp(d,i):
    return d['created_time'][0] + pd.Timedelta(minutes = i)

#Intersect DataFrame
def IntersectDataFrame(d,i): 
    Bool_Vec_UpperBound = d['created_time'] < TimeStamp(d,i+1)
    Bool_Vec_LowerBound = d['created_time'] >= TimeStamp(d,i)
    return d[Bool_Vec_LowerBound][Bool_Vec_UpperBound]
    
#Make EdgeList
def EdgeList(d,i): 
    G = nx.from_pandas_dataframe(IntersectDataFrame(d,i), 'actor', 'target', ['created_time'])
    return G.edges()

#Find the Median Degree of an undirected graph. 
def MedianDegree(d,i): 
    G = nx.from_pandas_dataframe(IntersectDataFrame(d,i), 'actor', 'target', ['created_time'])
    G = sorted(list(G.degree().values()))
    return np.median(G)
