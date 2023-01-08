import os

# Set the input and output directories
input_dir = "./forward_filled_30_aruco_221_gaussian_filter_9_3"
output_dir = "output"

# Iterate over each file in the input directory
for filename in os.listdir(input_dir):
  # Open the input file for reading
  with open(os.path.join(input_dir, filename), "r") as input_file:
    # Open the output file for writing
    with open(os.path.join(output_dir, filename), "w") as output_file:
      # Iterate over each line in the input file
      for line in input_file:
        # Split the line into columns
        col1, col2, col3 = line.strip().split()
        
        # Replace 0 with -100 in the second column
        print(col2)
        if col2 == "0.000000000000000000e+00":
          col2 = "-100"
        if col3 == "0.000000000000000000e+00":
          col3 = "-100"
        
        # Write the modified line to the output file
        output_file.write(f"{col1} {col2} {col3}\n")
