DROPBOX_PATH = '/Users/tejav/Dropbox/Data_Int_Fin_Class/rawdata/fx/'

import csv
import xlrd

spot = DROPBOX_PATH + 'DataRequests_Barclays_SP_D.xlsm'
workbook = xlrd.open_workbook(spot)

# save 
sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_spot_83'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[1].row_values(row) for row in range(sheets[1].nrows))

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_spot_93'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[4].row_values(row) for row in range(sheets[4].nrows))

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_spot_03'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[7].row_values(row) for row in range(sheets[7].nrows))

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_spot_09'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[10].row_values(row) for row in range(sheets[10].nrows))


forward = DROPBOX_PATH + 'DataRequests_Barclays_FW1F_D.xlsm'
workbook = xlrd.open_workbook(forward)

# save 
sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_forward_83'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[1].row_values(row) for row in range(sheets[1].nrows))

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_forward_93'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[4].row_values(row) for row in range(sheets[4].nrows))

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_forward_03'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[7].row_values(row) for row in range(sheets[7].nrows))

sheets = workbook.sheets()
with open('{}.csv'.format(DROPBOX_PATH + 'barclays_forward_09'), 'w') as f:
    writer = csv.writer(f)
    writer.writerows(sheets[10].row_values(row) for row in range(sheets[10].nrows))