# ids #
Solution to Insight Data Science coding challenge 

## Detailed Challenge Summary ## 
* Use Venmo payments that stream in to build a graph of users and their relationship with one another. 
* Calculate the median degree of a vertex in a graph and update this each time a new Venmo payment appears. I calculated the median degree across a 60-second sliding window. 

## Required python packages ##
Currently the python scripts in `code` require packages pandas, numpy, json and networkx. To install these packages system-wide, invoke 
* `sudo pip install pandas`
* `sudo pip install numpy` 
* `sudo pip install networkx` 
If local installation is sufficient or preffered, invoke `pip` with the `--user` flag. 

## Running the file ##
In terminal `import median_degree` located in the `src` file. 
* Assign a varible `d` as so: `d = median_degree.parse('../data-gen/venmo-trans.txt')` 
* To check TimeStamp please enter: `median_degree.TimeStamp(d,i)` for any `i` that is a natural number. 
* To check IntersectDataFrame please enter: `median_degree.IntersectDataFram(d,i)` for any `i` that is a natural number. 
* To check EdgeList please enter: `median_degree.EdgeList(d,i)` for any `i` that is a natural number. 
* Finally, to find the MedianDegree please enter: `median_degree.MedianDegree(d,i)` for any `i` that is a natural number






