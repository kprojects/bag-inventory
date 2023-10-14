#!/usr/bin/env python3

import pandas as pd
from tabulate import tabulate
import sys

# Path to the CSV file
file_path = '/tmp/bag_inventory.csv'

# Read the file, ignore lines starting with #
with open(file_path, 'r') as file:
    lines = [line for line in file if not line.startswith('#')]

# Create a DataFrame from the cleaned lines
from io import StringIO
df = pd.read_csv(StringIO(''.join(lines)))

# Function to display the inventory based on given filters
def display_inventory(filter_column=None, filter_value=None):
    if filter_column and filter_value:
        filtered_df = df[df[filter_column].str.contains(filter_value, case=False, na=False)]
    else:
        filtered_df = df

    print(tabulate(filtered_df, headers='keys', tablefmt='pretty', showindex=False))

# Check if a command-line argument is provided
if len(sys.argv) > 1:
    bag_name = sys.argv[1]
    print(f"Items in {bag_name} bag:")
    display_inventory("bag", bag_name)
else:
    print("Full Inventory:")
    display_inventory()

    print("\nItems in small sling bag:")
    display_inventory("bag", "sling")

    print("\nItems in large bag:")
    display_inventory("bag", "large")

