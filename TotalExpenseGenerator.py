###################################################################### 
### Description:
### 
### This program will create an expense csv from a 
### directory with appropriately named invoices
###
### Prerequisites:
###
### Python 2
###
### How to run:
###
### Run the command "python expense_generator name_of_csv path"
### where path contains all your invoices named in the following
### format mmddyy-description-vendor-dollars_cents, 
### where mm=month (01-12), dd=day(01-31), yy=(00-99), description 
### is a description of the invoice, dollars=dollars associated with 
### invoice, cens=cents associated with invoice. name_of_csv is the 
### name of the csv file you wish to generate.
###
### Optional arg1 - name of output file
### Optional arg2 - path of recipts
###
### Example Usage - python TotalExpenseGenerator.py result 
### ElectroneumMinerDocuments/Receipts/home/douglas/Documents/
########################################################################

import sys
import string
from os import listdir
from os.path import isfile, join

if(len(sys.argv) > 2):
    mypath = sys.argv[2]
    receipts = [f for f in listdir(mypath) if isfile(join(mypath, f))]
else:
    receipts = [f for f in listdir('.') if isfile(f)]

#open the output file to write
if(len(sys.argv) > 1):
    output_file = sys.argv[1]
else:
    output_file = "result"
output_file = output_file + '.csv'
f = open(output_file, 'w')

for r in receipts:
    #strip the file extension from the name
    strip_extension = r.split(".")[0]
    #replace dashes with commas
    comma_separated = string.replace(strip_extension, ':', ',')
    #replace _ with .
    result = string.replace(comma_separated, '_', '.')
    f.write(result)
    f.write('\n')
    #print result

summation = len(receipts)
f.write(',,,=SUM(D1:D%d)' % (summation))
#close the file
f.close()
    


