#!/usr/bin/env python3

"""Main"""

import pandas as pd


print("test")


FILE_PATH = "2024-01-29T16_27_24.442Z.csv"
data = pd.read_csv(FILE_PATH)

# Splitting the combined column (which is in tuple format) into ID and Church
data["ID"], data["Church"] = zip(*data.index.to_series())

# Reset the index of the dataframe
data.reset_index(drop=True, inplace=True)

data[["Norsk", "Erfaring"]] = data["Age"].str.extract(
    r"norsk: (yes|no)\n\|erfaring: (yes|no)"
)

# Handling NaN values in the "Answers" column
data["Answers"].fillna(False, inplace=True)

# Dropping the original 'Age' column as it's now redundant
data.drop("Age", axis=1, inplace=True)

# Displaying the cleaned data
print(data)

# Return the cleaned data for further use
# cleaned_data = data
# cleaned_data
