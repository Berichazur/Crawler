# Crawler
import pandas
import csv
# import requests


for i in range(1, 178):
    url = 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=' + str(i) # + '#QueryCondition'
    print(url)
    # response = requests.get(url)
    tb = pandas.read_html(url)[3]
    tb.to_csv(r'1.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
    print('第'+str(i)+'页抓取完成')

'''
with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])
'''