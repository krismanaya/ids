import json 
import os.path
import pandas as pd 
import networkx as nx 
import numpy as np
import sys

#Parse Data
def parse(filename):
    filename = os.path.abspath(filename)
    f = open(filename)
    m = []
    for line in f: 
        m.append(json.loads(line))
    d = pd.DataFrame(m)
    d['created_time'] = pd.to_datetime(d['created_time'])
    current_max = d['created_time'].min()
    stale = []
    for k in range(len(d['created_time'])):
        current_max = max(current_max, d['created_time'][k])
        if current_max - d['created_time'][k] > pd.Timedelta(minutes = 1): 
            stale.append(k)
    return d.drop(stale)

#Intersect DataFrame
def IntersectDataFrame(d,t): 
    Bool_Vec_UpperBound = d['created_time'] <= t
    Bool_Vec_LowerBound = d['created_time'] > t-pd.Timedelta(minutes =1)
    return d[Bool_Vec_LowerBound][Bool_Vec_UpperBound]
    

#Find the median degree of an undirected graph. 
def MedianDegree(d): 
    G = nx.from_pandas_dataframe(d, 'actor', 'target', ['created_time'])
    G = sorted(list(G.degree().values()))
    return np.median(G)

#Find the rolling median degree within the 60 second intersected data frame 
def RollingMedianDegree(d):
    md = [] 
    for time in d['created_time']:
        Intersect = IntersectDataFrame(d,time)
        m = MedianDegree(Intersect)
        md.append(m)
    return md  

#write an output 
def main():
    source = sys.argv[1]
    output = sys.argv[2]
    f = open(output, 'w')
    for item in RollingMedianDegree(parse(source)):
        item = format(item, '.2f')
        f.write(str(item) + '\n') 
    f.close()
if __name__ == "__main__":
    main()