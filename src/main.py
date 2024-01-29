#!/usr/bin/env python3

"""Main"""

import pandas as pd


print("test")


FILE_PATH = "src/2024-01-29T16_27_24.442Z.csv"
data = pd.read_csv(FILE_PATH)

data["Answers"] = data["Answers"].str.replace("\n\|", "|", regex=True)
data[["Norsk", "Erfaring"]] = data["Answers"].str.extract(
    "norsk: (yes|no)\|erfaring: (yes|no)"
)

data.drop("Answers", axis=1, inplace=True)

# Displaying the cleaned data
print(data)

# Return the cleaned data for further use
# cleaned_data = data
# cleaned_data
