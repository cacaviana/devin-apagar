```python
import csv

def calculate_column_average(file_path, column_name):
    # Initialize a list to store the values from the specified column
    values = []

    # Open the CSV file for reading
    with open(file_path, mode='r', newline='') as csvfile:
        # Create a CSV reader object
        csvreader = csv.DictReader(csvfile)

        # Iterate over each row in the CSV file
        for row in csvreader:
            try:
                # Convert the value in the specified column to a float and append to the list
                value = float(row[column_name])
                values.append(value)
            except ValueError:
                # If conversion fails, print a warning and skip the value
                print(f"Warning: Could not convert value '{row[column_name]}' to float. Skipping.")

    # Calculate the average if there are any valid values collected
    if values:
        average = sum(values) / len(values)
    else:
        average = 0
        print(f"No valid numerical data found in column '{column_name}'.")

    return average

# Specify the path to the CSV file
file_path = 'data.csv'  # Change this to your CSV file path
# Specify the column name whose average you want to compute
column_name = 'column_name'  # Change this to the name of your target column

# Call the function and print the result
average = calculate_column_average(file_path, column_name)
print(f"The average of column '{column_name}' is: {average}")
```

This Python script reads a CSV file and calculates the average of the specified column. It uses the `csv` module to handle CSV files and `float` conversion to ensure numerical calculations. If non-numeric data is encountered in the column, it skips those entries and issues a warning. The result is printed at the end, showing the average of the column's numeric data. Remember to modify `file_path` and `column_name` to fit your needs.