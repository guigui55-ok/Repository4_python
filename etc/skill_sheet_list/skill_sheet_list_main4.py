import pandas as pd
from io import StringIO

from skill_sheet_list_data import SKILL_LIST_BASE
buf = SKILL_LIST_BASE

# The data in a structured text format (replace the string below with your actual data)
data = """
Your_Data_Here
"""

# Creating a DataFrame to manage the data
df = pd.read_csv(StringIO(data), sep="\t", header=None)
df.columns = ['large_cat', 'mid_cat', 'ignore1', 'sub_cat', 'ignore2']

# Dropping unnecessary columns
df = df.drop(['ignore1', 'ignore2'], axis=1)

# Dropping rows where 'mid_cat' is just a dash (indicates no mid_cat present)
df = df[df['mid_cat'] != '-']

# Generating the CSV output format
output_df = pd.DataFrame(columns=['large_cat', 'mid_cat'])

# Iterating through unique large categories
for large_cat in df['large_cat'].unique():
    if pd.notna(large_cat):
        mid_cats = df[df['large_cat'] == large_cat]['mid_cat'].unique()
        for mid_cat in mid_cats:
            if pd.notna(mid_cat):
                output_df = output_df.append({'large_cat': large_cat, 'mid_cat': mid_cat}, ignore_index=True)

# Save the DataFrame to a CSV file
output_df.to_csv('path_to_your_output.csv', index=False)