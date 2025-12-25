import pandas as pd

df = pd.read_csv('Bank Customer Churn Prediction.csv')

# Drop unnecessary columns
df = df.drop(columns=['customer_id'])
print(df.shape)
# One-hot encode the 'gender' column
gender_condition = df.gender == 'Female'
gender_mapper = {True : 1 , False:0}
df['Female'] , df['Male'] = gender_condition.map(gender_mapper) , (~gender_condition).map(gender_mapper)
# mean encoding the 'country' column
'''
country_mapper = df['country'].value_counts().to_dict()
for country in country_mapper.keys():
    country_mapper[country] = country_mapper[country] / df.shape[0]
df['country'] = df['country'].map(country_mapper)
'''
# Drop original columns
df = df.drop(columns=['gender' , 'country'])
df.to_csv('prepped_data.csv', index=False)
# py prep_data.py