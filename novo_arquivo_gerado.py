Certainly! To achieve this task, we will create a Python script that reads a CSV file and calculates the average of a specified column. This script will utilize the `csv` module for reading the CSV file and some basic list operations for computing the average.

Here is the script:

```python
import csv

def calculate_average(filename, column_name):
    try:
        with open(filename, mode='r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            
            # Ensure the column exists
            if column_name not in csvreader.fieldnames:
                raise ValueError(f"Column '{column_name}' not found in CSV file.")
            
            total = 0
            count = 0
            
            for row in csvreader:
                try:
                    value = float(row[column_name])
                    total += value
                    count += 1
                except ValueError:
                    print(f"Skipping row with invalid data: {row[column_name]}")
                    
            if count == 0:
                raise ValueError(f"No valid data found for column '{column_name}' to calculate average.")
            
            average = total / count
            return average
            
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(e)

# Usage example
filename = 'data.csv'
column_name = 'price'

average = calculate_average(filename, column_name)
if average is not None:
    print(f"The average of column '{column_name}' is: {average}")
```

### Explanation:

1. **Function Definition:** The script defines a function `calculate_average` which takes two arguments: `filename` and `column_name`.
2. **Opening the CSV File:** The function opens the file using the `csv.DictReader`, which allows us to access the data using column headers.
3. **Column Check:** We first check if the specified column exists in the CSV file. If not, raise a `ValueError`.
4. **Calculating Average:** 
   - Iterate through each row, attempt to convert the column value to a float, and accumulate the total and count.
   - If data cannot be converted to a float, handle it gracefully by printing a message and skipping the row.
5. **Compute Average:** Once all rows are processed, compute the average. If no valid data is encountered, raise a `ValueError`.
6. **Error Handling:** Use try-except blocks to handle potential errors such as file not being found or data conversion issues.

### Usage:

Change `filename` and `column_name` to your CSV file name and the column you are interested in, respectively. This script calculates the average and prints it out. Adjust accordingly to fit your specific CSV file structure and data.