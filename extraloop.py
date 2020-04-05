import pandas as pd
from pandas import DataFrame

def extra():
    path = r'C:\Users\刘之源\PycharmProjects\Selflearning\2019年-京东\2019年全年-阿里.xlsx'
    data = pd.read_excel(path, sheet_name='按品牌（多选）的订单统计')
    z = data.columns
    joined = pd.DataFrame(columns=z)
    records = {
        '安徽省': data[data.省 == '安徽省'],
        '福建省': data[data.省 == '福建省'],
        '云南省': data[data.省 == '云南省'],
        '广东省': data[data.省 == '广东省'],
        '广西壮族自治区': data[data.省 == '广西壮族自治区'],
        '贵州省': data[data.省 == '贵州省'],
        '河北省': data[data.省 == '河北省'],
        '河南省': data[data.省 == '河南省'],
        '湖北省': data[data.省 == '湖北省'],
        '湖南省': data[data.省 == '湖南省'],
        '江苏省': data[data.省 == '江苏省'],
        '江西省': data[data.省 == '江西省'],
        '山东省': data[data.省 == '山东省'],
        '山西省': data[data.省 == '山西省'],
        '陕西省': data[data.省 == '陕西省'],
        '四川省': data[data.省 == '四川省'],
        '重庆': data[data.省 == '重庆'],
        '北京': data[data.省 == '北京'],
        '浙江省': data[data.省 == '浙江省'],
        '天津': data[data.省 == '天津'],

    }
    for province in records:
        joined = joined.append(records[province])
        out = data.loc[:,[ '分销商名称', '省', '市', '区']]

    out = out.drop_duplicates(['分销商名称'])
    out.to_csv('ALQN.csv', encoding='utf_8_sig')

extra()
