##############################################################
# Name: Evan Chow
# Email: echow@princeton.edu
# This script uses Pandas dataframes to find the metrics.
##############################################################

import pandas as pd

# Read data into a Pandas dataframe.
data = pd.read_csv(open('Metropolitan_Populations__2010-2012_.csv', 'rb'))

# Deliverable #1.
p50k = data.ix[data['2010 Population'] >= 50000].reset_index(drop=True)
del p50k['2011 Population']
city, p10, p12 = [p50k[p50k.columns[n]] for n in xrange(3)]
pChange = [(100. * (p12[i] - p10[i])/p10[i], city[i]) for i in p50k.index]
pChange.sort(reverse=True)
print "Top five cities to target based on highest population growth: "
for i in pChange[0:5]:
    print i[1]

# Deliverable #2.
pChange.sort()
print "\nTop 5 cities to avoid based on most shrinking population: "
for i in pChange[0:5]:
    print i[1]

# Deliverable #3.
data['Growth'] = data['2012 Population'] - data['2010 Population']
growth = [(data['Growth'][i], data['Geography'][i]) for i in data.index]
growth.sort(reverse=True)
print "\nTop five states with highest cumulative growth: "
for i in growth[0:5]:
    print i[1]