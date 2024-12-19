# Import the necessary library for handling CSV files
import csv

# Define the function to read the CSV file and calculate the mean of the specified column
def calculate_column_mean(file_path, column_name):
    try:
        # Open the CSV file in read mode
        with open(file_path, mode='r') as file:
            # Create a CSV reader object to iterate over lines in the file
            csv_reader = csv.DictReader(file)
            
            # Initialize a list to store the values of the specified column
            column_values = []

            # Iterate over each row in the CSV
            for row in csv_reader:
                
                # Check if the column exists in the current row
                if column_name in row:
                    # Attempt to convert the value to a float and append to the list
                    try:
                        value = float(row[column_name])
                        column_values.append(value)
                    except ValueError:
                        # If conversion fails, print a warning and skip the value
                        print(f"Warning: Non-numeric data found in column '{column_name}' and row skipped.")

            # Calculate the mean if there are valid values collected
            if len(column_values) > 0:
                mean_value = sum(column_values) / len(column_values)
                return mean_value
            else:
                return "No valid numeric data found in the specified column."

    except FileNotFoundError:
        # Handle the case where the file path is incorrect
        return "Error: The file was not found. Please check the file path."
    except Exception as e:
        # Handle any other unexpected exceptions
        return f"An error occurred: {str(e)}"

# Example usage (uncomment to run):
# result = calculate_column_mean('example.csv', 'column_name')
# print(f"The mean of the column is: {result}")