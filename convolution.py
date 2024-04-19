from scipy import signal
import numpy as np
import os



# Read the CSV file into lines
with open('data_convolution.csv', 'r') as file:
    lines = file.readlines()

# Remove the header if necessary
lines = lines[1:]  # Assuming the header is present

# Replace commas with periods in each line
lines = [line.replace(',', '.') for line in lines]


# Parse the lines into numpy arrays
data = np.genfromtxt(lines, delimiter=';')

# Assuming the first column is for j and the second column is for h
j = data[:, 1]
h = data[:, 2]

# Convolution 
y=signal.convolve(h, j)
print(y)

# Replace periods with commas in the result
y_str = [str(val).replace('.', ',') for val in y]

# Save result to CSV file (set the file name between '')
result_file_path = 'convolution_result.csv'

np.savetxt(result_file_path, y_str,fmt='%s', delimiter=';')

# Open the result file
os.system('start "" "' + result_file_path + '"')