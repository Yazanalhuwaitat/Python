
import pandas
#import statistics as st
df = pandas.read_excel('Book1.xlsx')
"""
g= df['price'].tolist()
print(st.mean(g))
print(sum(g)/len(g))
total=0
for i in df['price']:
    total +=i
import datetime as dt
d=  {'date':[
     dt.datetime(2022,5,8),dt.datetime(2021,5,8),dt.datetime(2020,5,8),dt.datetime(2019,5,8)],
    'price':[30,20,40,24]
    }
#print(d)
df=pandas.DataFrame(d)
df.to_excel("goldprices.xlsx",index=False)
gold=pandas.read_excel("goldprices.xlsx")
print(gold.mean())
print(round("goldprices.xlsx",d.mean())
"""
print(df)
print("Sum: ",df["price"].sum()) 
print("Mean: ",df["price"].mean())
print("Maximum: ",df["price"].max())
print("Minimum: ",df["price"].min())