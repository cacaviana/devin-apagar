```python
import csv

def calculate_average_column(csv_file_path, column_name):
    """
    This function reads a CSV file, extracts the data of a specified column,
    and calculates the average of that column.
    
    :param csv_file_path: str, the path to the CSV file.
    :param column_name: str, the name of the column to calculate the average for.
    :return: float, the average of the specified column.
    """
    
    # Initialize variables to calculate the average
    total = 0
    count = 0
    
    # Open the CSV file for reading
    with open(csv_file_path, newline='') as csvfile:
        # Create a CSV reader object
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV file
        for row in reader:
            # Extract the value from the specified column
            value = row[column_name]
            
            # Convert the value to float and add it to the total
            # We use try/except to handle cases where conversion may fail
            try:
                total += float(value)
                count += 1
            except ValueError:
                # If conversion fails, skip this row
                pass
    
    # Calculate the average. If count is zero, return 0 to avoid division by zero
    if count == 0:
        return 0.0
    else:
        return total / count

# Example usage:
# Assume you have a CSV file "data.csv" with a column named "price"
# csv_file_path = 'data.csv'
# column_name = 'price'
# average = calculate_average_column(csv_file_path, column_name)
# print(f"The average {column_name} is {average}")
```

This script uses Python's built-in `csv` module to read a CSV file specified by the `csv_file_path`. It calculates the average of a specified column by iterating over the rows, summing up the values, and counting the entries. The final average is returned, with necessary error-checking included to handle non-numeric entries gracefully.