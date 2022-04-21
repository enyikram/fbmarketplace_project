from sklearn import linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split
from clean_tabular import products
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

df=products.__deepcopy__()

# Creating X features and y target
df.drop('product_name', axis=1, inplace=True)
df.drop('page_id', axis=1, inplace=True)
df.drop('create_time', axis=1, inplace=True)
df.drop('product_description', axis=1, inplace=True)


X = df[['id', 'category', 'location']]
y = df['price']

# Creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')

# Perform one-hot encoding on 'category' and 'location' columns 
encoder_df1 = pd.DataFrame(encoder.fit_transform(X[['category']]).toarray())
encoder_df2 = pd.DataFrame(encoder.fit_transform(X[['location']]).toarray())

#merge one-hot encoded columns back with original DataFrame
final_df = X.join(encoder_df1)

print(df.head())

model = linear_model.LinearRegression()

#model.fit(X, y)
#y_pred = model.predict(X)

#print(y_pred[:5], "\n", y[:5])