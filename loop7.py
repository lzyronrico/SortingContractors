import pandas as pd
from pandas import DataFrame

def dss():
    for p in range(1,9):
        path = r'C:\Users\刘之源\PycharmProjects\Selflearning\2019年-京东\福临门联营' + str(p) + '.xlsx'
        data = pd.read_excel(path, sheet_name='Sheet0')
        z = data.columns
        joined = pd.DataFrame(columns=z)
        records = {
            '广东': data[data.一级地址 == '广东']

        }

        for province in records:
            joined = joined.append(records[province])
            out = joined.loc[:, [ '商家ID', '店铺名称', '一级地址','二级地址','三级地址','四级地址', '店主']]

        out = out.drop_duplicates(['店铺名称'])


        if p == 1:
            out.to_csv('GD.csv', encoding='utf_8_sig')
        else:
            out.to_csv('GD.csv',  mode='a', header=False, encoding='utf_8_sig')

    for q in range(9,13):

        path = r'C:\Users\刘之源\PycharmProjects\Selflearning\2019年-京东\京东' + str(q) + '.xlsx'
        data = pd.read_excel(path, sheet_name='Sheet0')
        z = data.columns
        joined = pd.DataFrame(columns=z)
        records = {
            '广东': data[data.一级地址 == '广东']

        }
        for province in records:
            joined = joined.append(records[province])
            out = joined.loc[:, ['商家ID','店铺名称','一级地址','二级地址','三级地址', '店铺地址', '店主','卖家店铺']]

        out = out.drop_duplicates(['店铺名称'])

        out.to_csv('GD.csv', mode='a', header=False, encoding='utf_8_sig')




dss()