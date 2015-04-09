# A function that return one record for multiple input lines.
# Current version reads from standard input.
# It can be modified to handle input from file.

import sys

def get_record (input=sys.stdin):
    
    record = ''
    for line in input:
        if record and line.startswith ('lease'):
            yield record
            record = ''
        record += line
    if record:
            yield record


print ('Hello World')

for num, record in enumerate (get_record (sys.stdin), 1):
    print ('Record ' + str(num))
    print (record)

