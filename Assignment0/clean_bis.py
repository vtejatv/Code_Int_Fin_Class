import pandas as pd 
import os
import CONSTANTS


bis_file = CONSTANTS.DROPBOX_PATH + 'rawdata/bis/WEBSTATS_DEBTSEC_DATAFLOW_csv_col.csv'


def clean_file():

	bis_df = pd.read_csv(bis_file)

	# TO DO: not sure how to clean, as not sure how we will be using this file

	os.makedirs(CONSTANTS.DROPBOX_PATH+ 'output/bis')
	os.makedirs(CONSTANTS.DROPBOX_PATH + 'tmp/bis')
	bis_df.to_csv(CONSTANTS.DROPBOX_PATH + 'tmp/bis/WEBSTATS_DEBTSEC_DATAFLOW_csv_col.csv')
	bis_df.to_csv(CONSTANTS.DROPBOX_PATH + 'output/bis/WEBSTATS_DEBTSEC_DATAFLOW_csv_col.csv')


if __name__ == "__main__":
	clean_file()