import csv

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])


'''
, delimiter=' ',
quotechar='|', quoting=csv.QUOTE_MINIMAL)
'''