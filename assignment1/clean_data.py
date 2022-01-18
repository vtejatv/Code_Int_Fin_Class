DROPBOX_PATH = '/Users/tejav/Dropbox/Data_Int_Fin_Class/rawdata/fx/'

import csv
import xlrd

spot_pre_2008 = DROPBOX_PATH + 'DataRequests_Reuters_SP_D_until_12_31_2008.xlsm'
workbook = xlrd.open_workbook(spot_pre_2008)

# save 
sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'reuters_spot_pre_2008'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[1].row_values(row) for row in range(sheets[1].nrows))

spot_post_2008 = DROPBOX_PATH + 'DataRequests_Reuters_SP_D_since_12_31_2008.xlsm'
workbook = xlrd.open_workbook(spot_post_2008)

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'reuters_spot_post_2008'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[1].row_values(row) for row in range(sheets[1].nrows))


forward_pre_2008 = DROPBOX_PATH + 'DataRequests_Reuters_FR_D_until_31_12_2008.xlsm'
workbook = xlrd.open_workbook(forward_pre_2008)

# save 
sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'reuters_forward_pre_2008'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[1].row_values(row) for row in range(sheets[1].nrows))

forward_post_2008 = DROPBOX_PATH + 'DataRequests_Reuters_FR_D_since_31_12_2008.xlsm'
workbook = xlrd.open_workbook(forward_post_2008)

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'reuters_forward_post_2008'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[1].row_values(row) for row in range(sheets[1].nrows))