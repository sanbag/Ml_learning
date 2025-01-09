import pandas as pd

# Path to the input .pkl file
input_path = '/Users/santoshbaggon/Downloads/scrub_cut.pkl'

# Path to save the output .csv file
output_path = '/Users/santoshbaggon/Downloads/sanbag.csv'

# Load the .pkl file into a DataFrame
df = pd.read_pickle(input_path)

# Save the DataFrame as a pipe-delimited CSV file
df.to_csv(output_path, sep='|', index=False)

print(f"File successfully saved as pipe-delimited CSV at {output_path}.")
