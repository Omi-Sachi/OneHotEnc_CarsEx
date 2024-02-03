

# Import dependencies
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Read CSV file
file_path = r'C:\Users\omiam\OneDrive\Python Projects\OneHotEnc_CarsEx\archive\carprices.csv'
df = pd.read_csv(file_path)

# Find columns that need to be one-hot encoded
Cols_to_OH = [cols for cols in df.columns if df[cols].dtype == "object"]

# Apply one-hot encoding to columns
Encoder = OneHotEncoder()
OH_column = pd.DataFrame(Encoder.fit_transform(df[Cols_to_OH]).toarray(), columns=Encoder.get_feature_names_out(Cols_to_OH))  # Changed this line

# Drop original categorical columns
df.drop(Cols_to_OH, axis=1, inplace=True)

# Concatenate one-hot encoded columns to the original DataFrame
df = pd.concat([df, OH_column], axis=1)

# Ensure all columns have string type
df.columns = df.columns.astype(str)

df.rename(columns={'0': 'Car_Model_Category'}, inplace=True)

# Print the updated DataFrame
print(df.head())
print(df.describe())
