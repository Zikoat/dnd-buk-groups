#!/usr/bin/env python3
"""Main"""
import pandas as pd


column_headers = [
    "Id",
    "Church",
    "Person",
    "Gender",
    "Age",
    "Type",
    "Timeslot",
    "Answers",
    "NotUsed",
]

FILE_PATH = "src/2024-01-29T16_27_24.442Z.csv"
data = pd.read_csv(FILE_PATH, names=column_headers, header=0)

data["Answers"] = data["Answers"].astype(str)
data["Answers"] = data["Answers"].str.replace(r"\n\|", "|", regex=True)


def convert_to_boolean(value):
    """Converts the answer column to a boolean value"""
    if value in ["yes", "1"]:
        return "true"
    return "false"


data["Norsk"] = data["Answers"].str.extract(r"norsk: (\w+)")[0].map(convert_to_boolean)
data["Erfaring"] = (
    data["Answers"].str.extract(r"erfaring: (\w+)")[0].map(convert_to_boolean)
)

data.drop("Answers", axis=1, inplace=True)
data.drop("NotUsed", axis=1, inplace=True)
data.drop("Person", axis=1, inplace=True)

expected_first_row = {
    "Id": "01247fd1-a130-4244-a336-378e6559f956",
    "Church": "Bergen",
    # "Person": "Klara Skutle",
    "Person": None,
    "Gender": "F",
    "Age": 13,
    "Timeslot": "All days",
    "Type": "mentee",
    "Norsk": "true",  # or True, depending on how it's represented in your DataFrame
    "Erfaring": "false",  # or False
}

first_row = data.iloc[0].to_dict()


def dict_diff(d1, d2):
    """Returns the differences between two dictionaries. Useful for snapshot testing."""
    diffs = {}
    for key in d1.keys():
        if d1[key] != d2.get(key, None):
            diffs[key] = {"Expected": d1[key], "Actual": d2.get(key, None)}
    return diffs


differences = dict_diff(expected_first_row, first_row)

assert (
    not differences
), f"First row of the DataFrame does not match expected values. Differences: {differences}"

EXPECTED_NORSK_VALUE = "true"
actual_norsk_value = data.loc[4, "Norsk"]
assert actual_norsk_value == EXPECTED_NORSK_VALUE, (
    f"Assertion failed: The 'Norsk' value of the 5th entry is expected to be "
    f"'{EXPECTED_NORSK_VALUE}', but it was '{actual_norsk_value}'."
)

print(data)

print("\nDataFrame Info:")
data.info()

print("\nUnique Values in 'Type' Column:")
print(data["Type"].unique())

# Example: Creating gender-balanced teams
TEAM_SIZE = 5  # Adjust as per requirements
data["Team"] = data.groupby("Gender").cumcount() // (TEAM_SIZE // 2) + 1

print(data.groupby(["Team", "Gender"]).size())
