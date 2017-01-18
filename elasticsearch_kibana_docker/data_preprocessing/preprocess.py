#!/usr/bin/env python

''' Preprocess sample data to be used.
	Data was collected from http://ourairports.com/data/airports.csv.
'''

import pandas as pd
import json
import sys 

reload(sys)  
sys.setdefaultencoding('utf8')

def main():

	columns_to_keep = ['name','type','latitude_deg','longitude_deg','elevation_ft','wikipedia_link',]
	df = pd.read_csv('airports.csv',usecols = columns_to_keep,encoding='utf-8')

	# keep only the large airports
	df_summarized = df[ df['type'] == 'large_airport'].drop_duplicates('name').reset_index(drop=True).fillna(' ').rename({"type":"airport_type"})

	# convert latitude and longitude columns to format a string format that elasticsearch can parse
	df_summarized['lat_lon'] = df_summarized[['latitude_deg','longitude_deg']].apply(lambda x: str(x[0]) + ',' + str(x[1]),axis=1)

	#filter rows with values that are 0.0 and drop the columns we don't need
	df_summarized.drop(df_summarized[df_summarized['latitude_deg'] == 0.0].index,inplace=True)
	df_summarized.drop(df_summarized[df_summarized['longitude_deg'] == 0.0].index,inplace=True)
	df_summarized.drop(['latitude_deg','longitude_deg'],inplace=True,axis=1)

	# tuple containing column names
	columns = tuple(df_summarized.columns.tolist())
	# elasticsearch format for bulk insertion
	action_and_meta_data = { "index": { "_index" : "airports"}}
	print df.shape
	print df_summarized.shape
	return 
	# create a json file in the corresponding elasticsearch bulk format
	with open('data.json', 'w') as output:

		for row in df_summarized.itertuples(index=False,name=None):
			# map column_name to their correspondin value 
			data = { col_name:val for col_name,val in zip(columns,row) if val != ' '}
			# insert lines to new file
			json.dump(action_and_meta_data,output, ensure_ascii=False)
			output.write('\n')
			json.dump(data,output, ensure_ascii=False)
			output.write('\n')
	 

if __name__ == '__main__':
	main()