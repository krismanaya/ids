# Insight-Data-Science-Challenge #
Solution to Insight Data Science coding challenge 

## Detailed Challenge Summary  
* Use Venmo payments that stream in to build a graph of users and their relationship with one another. 
* Calculate the median degree of a vertex in a graph and update this each time a new Venmo payment appears. I calculated the median degree across a 60-second sliding window. 

## Required python packages ##
Currently the python scripts in `code` require packages pandas, numpy, json and networkx. To install these packages system-wide, invoke 
* `sudo pip install pandas`
* `sudo pip install numpy` 
* `sudo pip install networkx` 
If local installation is sufficient or preffered, invoke `pip` with the `--user` flag. 

## Running the file ##
In python `import median_degree` located in the `src` file. 
* Assign a variable `d` so: `d = median_degree.parse('../venmo_input/venmo-trans.txt')` 
* To check IntersectDataFrame please enter: `median_degree.IntersectDataFrame(d,t)` for any `t` that is a timestamp in `d['created_time']`. 
* To find the MedianDegree please enter: `median_degree.MedianDegree(d)`.
* Finally, to find the RollingMedianDegree enter: `median_degree.RollingMedianDegree(d)`

## Running my-own-test ## 
In terminal `cd ids/insight_testsuite/tests/my-own-test`. The please enter `python test.py`. This will show the number of tests that were performed for each function. 






