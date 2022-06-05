import pandas as pd
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
golf_df = pd.read_csv("weather.csv")
"""
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
"""
y = golf_df['Play']
data = golf_df.iloc[:,0:4]
# #print(data)
# target=golf_df.iloc[:,4]
# #print(target)
# print('Apply K-Nearest Neighbors (K-NN) Classifier:')
# clf =  RandomForestClassifier()
# scores = cross_val_score(clf, data, y, cv=5)
# print(f"> Accuracy: {scores.mean()}")
# print(scores)

X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=0.3, random_state=0)
print(X_train)