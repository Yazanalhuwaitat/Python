import pandas as pd
golf_df = pd.DataFrame()
# Add outlook column:
golf_df['Outlook'] = ['sunny','sunny','overcast','rainy','rainy',
'rainy', 'overcast', 'sunny','sunny','rainy',
'sunny','overcast','overcast','rainy']
# Add Temperature column:
golf_df['Temperature'] = ['hot','hot','hot','mild','cool','cool',
'cool','mild','cool','mild','mild','mild','hot','mild']
# Add Humidity column:
golf_df['Humidity'] = ['high','high','high','high','normal','normal',
'normal','high','normal','normal','normal','high','normal','high']
# Add Windy column:
golf_df['Windy'] = ['false','true','false','false','false','true',
'true','false','false','false','true','true','false','true']
# Finally Add Play column:
golf_df['Play'] = ['no','no','yes','yes','yes','no','yes',
'no','yes','yes','yes','yes','yes','no']
#Print/show the new data:
#print(golf_df)

#golf_df.to_csv("weather.csv",index=False)
data= pd.read_csv("weather.csv")  
data.replace(to_replace="hot", 
                 value = 0, 
                  inplace = True)
data.replace(to_replace="sunny", 
                 value = 0, 
                  inplace = True)
data.replace(to_replace="high", 
                 value = 0, 
                  inplace = True)
data.replace(to_replace="False", 
                 value = str("0"), 
                  inplace = False)
data.replace(to_replace="no", 
                 value = 0, 
                  inplace = True)

data.replace(to_replace="overcast", 
                 value = 1, 
                  inplace = True)
data.replace(to_replace="mild", 
                 value = 1, 
                  inplace = True)
data.replace(to_replace="normal", 
                 value = 1, 
                  inplace = True)
data.replace(to_replace="True", 
                 value = str("1"), 
                  inplace = True)
data.replace(to_replace="yes", 
                 value = 1, 
                  inplace = True)

data.replace(to_replace="rainy", 
                 value = 2, 
                  inplace = True)
data.replace(to_replace="cool", 
                 value = 2, 
                  inplace = True)


data.to_csv('outputfile1.csv', 
                 index = False)