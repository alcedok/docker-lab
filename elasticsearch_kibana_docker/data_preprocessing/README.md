To download the raw .csv data go to: ourairports.com/data/airports.csv

or using curl:

 curl "http://wget ourairports.com/data/airports.csv" -o "airports.csv"


## preprocess.py 
loads the data and performs preprocessing, filtering and json file preparation for elasticsearch bulk consumption