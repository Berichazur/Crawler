import pandas as pd
import requests
for x in["1","2","3"]:
    # dfs = pd.read_html('http://www.contextures.com/xlSampleData01.html')

    url ="https://www.contextures.com/xlSampleData01.html"
    # 地址 http://data.eastmoney.com/money/Default.aspx?p=3
    response = requests.get(url)
    data = pd.read_html(response.text)[0]
    data.to_csv('SampleData_Mac.csv')
    print(data)


