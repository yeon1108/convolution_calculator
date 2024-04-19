import tkinter as tk
from tkinter import ttk, filedialog, IntVar
import numpy as np
from scipy import signal
import os

def load_csv():
    # Prompt user to select a CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    entry_csv_path.delete(0, tk.END)
    entry_csv_path.insert(0, file_path)

def perform_convolution():
    # Get the CSV file path from the entry widget
    file_path = entry_csv_path.get()

    # Read the CSV file into lines
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Remove the header if necessary
        # Determine if there is a header based on the checkbox value
    if header_checkbox.get() == 1:
        lines = lines[1:]  # Remove the header
    else :
        lines = lines[0:]

    # Replace commas with periods in each line
    lines = [line.replace(',', '.') for line in lines]

    # Parse the lines into numpy arrays
    data = np.genfromtxt(lines, delimiter=';')

    # Extract j and h columns based on user input
    j_column = int(entry_j_column.get())-2  
    h_column = int(entry_h_column.get())-2

    j = data[:, j_column]
    h = data[:, h_column]

    # Perform convolution 
    result = signal.convolve(j, h)  # Adjust mode as needed
  
    # Replace periods with commas in the result
    y_str = []

    if number_checkbox.get() == 1:
        y_str = [str(val).replace('.', ',') for val in result]
    else : 
        y_str = [str(val) for val in result]

    # Save result to CSV file (set the file name between '')
    if y_str:
        result_file_path = 'convolution_result.csv'
        np.savetxt(result_file_path, y_str,fmt='%s', delimiter=';')

    # Open the result CSV file
        os.system('start "" "' + result_file_path + '"')

# Create the main window
root = tk.Tk()
root.title("Convolution Calculator")

# Create a label and entry widget for CSV file location
label_csv_path = ttk.Label(root, text="CSV File Location:")
label_csv_path.pack(pady=5)
entry_csv_path = ttk.Entry(root, width=40)
entry_csv_path.pack(pady=5)

# button to browse and load CSV file
button_load_csv = ttk.Button(root, text="Browse", command=load_csv)
button_load_csv.pack(pady=5)

# frame for header checkbox
header_frame = ttk.Frame(root)
header_frame.pack(pady=5)

# Create a checkbox for header
header_checkbox = IntVar()
checkbox_header = ttk.Checkbutton(header_frame, text="Check if Header exist", variable=header_checkbox)
checkbox_header.pack(side="left")

# frame for french excel checkbox
number_frame = ttk.Frame(root)
number_frame.pack(pady=5)

# Create a checkbox for french excel
number_checkbox = IntVar()
checkbox_number = ttk.Checkbutton(number_frame, text="Check if excel is french version (ex. 3,456)", variable=number_checkbox)
checkbox_number.pack(side="left")

# Create a frame to hold the widgets for selecting the column for j
frame_j_column = ttk.Frame(root)
frame_j_column.pack(pady=5, fill="x")

# Create a label for selecting the column for j
label_j_column = ttk.Label(frame_j_column, text="Column for j: ")
label_j_column.pack(side="left")

# Create an entry widget for selecting the column for j
entry_j_column = ttk.Entry(frame_j_column, width=10)
entry_j_column.pack(side="left")
entry_j_column.insert(0, "1")  # Default value is 1

# Create a frame to hold the widgets for selecting the column for h
frame_h_column = ttk.Frame(root)
frame_h_column.pack(pady=5, fill="x")

# Create a label for selecting the column for h
label_h_column = ttk.Label(frame_h_column, text="Column for h:")
label_h_column.pack(side="left")

# Create an entry widget for selecting the column for h
entry_h_column = ttk.Entry(frame_h_column, width=10)
entry_h_column.pack(side="left")
entry_h_column.insert(0, "2")  # Default value is 2

# Create a button to perform convolution
button_convolution = ttk.Button(root, text="Perform Convolution", command=perform_convolution)
button_convolution.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()