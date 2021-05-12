import json
import time
import datetime
eth = open('res.json')
ether=json.load(eth)
# print(ether['prices']
prices = []
for elements in ether['prices']:
    prices.append(elements[1])

dater=[]
timer=[]

for elements in ether['prices']:
    epoch_time=elements[0]/1000
    time_formatted = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch_time))
    new = time_formatted.split(' ')
    dater.append(new[0])
    timer.append(new[1])

# print(dater)
# print(timer)

import pandas as pd
dict = {'Date': dater, 'Time': timer, 'Price': prices} 
df = pd.DataFrame(dict)
df.to_csv('file1.csv')