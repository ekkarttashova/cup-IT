import pandas as pd
df = pd.read_csv('данные.csv')
data = pd.DataFrame(df)
sum_by_store_product = data.groupby(['site_key', 'prod_key', 'Date', 'Time'])['units_on_hand'].sum()
sum_by_store_product = sum_by_store_product.reset_index()
df = pd.DataFrame(sum_by_store_product)
df1 = pd.DataFrame(columns=['site_key', 'prod_key', 'Date', 'Time', 'sum'])
total_items = 0
previous_time = 0
j = 0
average1 = 0
average2 = 0

for i in range(100143):
    a, b, c = map(int, df['Time'][i].split(':'))
    time = a * 3600 + b * 60 + c
    if 43200 >= previous_time and time >= 43200:
        df1.loc[j] = [df['site_key'][i - 1], df['prod_key'][i - 1], df['Date'][i - 1], '12:00:00', total_items]
        average1 += total_items
        total_items = 0
        j += 1

    elif time < previous_time:
        df1.loc[j] = [df['site_key'][i - 1], df['prod_key'][i - 1], df['Date'][i - 1], '00:00:00', total_items]
        average2 += total_items
        total_items = 0
        j += 1

    previous_time = time
    total_items += df['units_on_hand'][i]
df1.loc[j] = [df['site_key'][100142], df['prod_key'][100142], df['Date'][100142], '12:00:00', total_items]
average1 += total_items
average1 = int(average1 / 2135)
average2 = int(average2 / 2134)
arr = []

for i in range(4269):
    if i % 2 == 0:
        if df1['sum'][i] >= average2:
            arr.append(df1['sum'][i] - average2)
        else:
            arr.append(df1['sum'][i])
    else:
        if df1['sum'][i] > average1:
            arr.append(df1['sum'][i] - average1)
        else:
            arr.append(df1['sum'][i])

df1['difference'] = arr
print(df1)
df1.to_csv('output.csv')
print(average1, average2)