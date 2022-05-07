import argparse
import sys
import os
new_wd = os.getcwd()

def mainParsArgs(arg):
    parser = argparse.ArgumentParser(description="testing...")
    parser.add_argument('--data_source', help='data source', default=new_wd + '/src/donald_besong_banking_package/data/data.xlsx')
    parser.add_argument('--cutoff_date', help='date assessed', default='01/01/2020')
    parser.add_argument('--risk_rating', help='risk rating', default='High')
    parser.add_argument('--test_number', help='test number', default=1)
    parser.add_argument('--dob_filter', help='date of birth', default='01/09/2003')
    parser.add_argument('--fee_str', help='fee type', default='overdraft')

    return parser.parse_args(arg)

my_args = mainParsArgs(sys.argv[1:])
#*****************begin reading arguments
data_source = my_args.data_source
cutoff_date = my_args.cutoff_date
risk_rating = my_args.risk_rating
dob_filter = my_args.dob_filter
fee_str = my_args.fee_str
testNumber = int(my_args.test_number)  
#*****************end reading arguments
