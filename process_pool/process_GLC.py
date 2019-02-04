#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--poll', action="store", default=None)
args = parser.parse_args()

print args

if args.poll == None:
    print "Provide a --poll csv file"
    exit()

freq_vals = {'Once per month':'1/m','twice per month':'2/m','Once per week':'1/w'}
csv_reader = csv.reader(open(args.poll, "r+"), delimiter=',')

def vote_to_value(vote):
    return ["No", "Ifneedbe", "Yes"].index(vote)

linecount=0
for entry in csv_reader:
    for f in entry[1:len(entry)-1]:
        if linecount == 0:
            updated_str = f.replace('&colon;',':').replace('&plus;','+').replace('&lpar;','(').replace('&rpar;',')').replace('&quest;','?')
            #print "Columns:", updated_str,
            freq = updated_str.find("Freq")
            avail = updated_str.find("available at ? ")
            field_label = updated_str[:3]
            if freq >= 0:
                field_label = freq_vals[updated_str[6:]]
            elif avail >=0:
                field_label = updated_str[-5:]
            print field_label
        else:
            #print f, float(vote_to_value(f)) / 2.,'|',
            pass
    #print
    linecount +=1
