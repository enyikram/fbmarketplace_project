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
y = df['price'].fillna(0, inplace=True)

# Creating instance of one-hot-encoder
encoder = OneHotEncoder(handle_unknown='ignore')

# Perform one-hot encoding on 'category' and 'location' columns 
encoder_df1 = pd.DataFrame(encoder.fit_transform(X[['category']]).toarray())
encoder_df2 = pd.DataFrame(encoder.fit_transform(X[['location']]).toarray())
#encoder_df1.columns = encoder.get_feature_names(['category_encoded'])
#encoder_df2.columns = encoder.get_feature_names(['location_encoded'])

#merge one-hot encoded columns back with original DataFrame
final_df = X.join(encoder_df2)
final_df = X.join(encoder_df1)
final_df.drop(['category', 'location', 'id'], axis=1, inplace=True)
final_df.fillna(0, inplace=True)


X_train, X_test, y_train, y_test = train_test_split(final_df, y, test_size=0.4, random_state=101)
X_train = X_train.reshape(1, -1)
X_test = X_test.reshape(1, -1)

model = linear_model.LinearRegression()

model.fit(X_train, y_train)
model.predict(X_test)
