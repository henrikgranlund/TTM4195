import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)

# Read in the dataset
blocks_df = pd.read_csv('../datasets/blocks23aug2022.tsv', sep='\t')

# Create a DataFrame with the 'time' column
df = pd.DataFrame(blocks_df, columns=['time'])

# Convert the 'time' column to a datetime format
df['time'] = pd.to_datetime(df['time'])

# Calculate the time difference between each entry
df['time_diff'] = df['time'].diff()

# Sort the DataFrame by the time difference
df_sorted = df.sort_values(by='time_diff')
print(df_sorted)
print("\n")

# Print the number of rows where the time difference is greater than 20 and 30 minutes
print("Inter block time > 20 min: " + str(df_sorted[df_sorted['time_diff'] > '00:20:00'].shape[0]))
print("Inter block time > 30 min: " + str(df_sorted[df_sorted['time_diff'] > '00:30:00'].shape[0]))

# extract the minutes from the time difference and place into an array
minutes = []
for i in range(0, df_sorted.shape[0]-1):
    minutes.append(df_sorted['time_diff'].iloc[i].seconds / 60)
 
average = sum(minutes) / len(minutes)
print("Average inter block time: " + str(average) + " minutes")

# Plot the inter block time
plt.plot(minutes)
plt.ylabel('Inter block time (minutes)')
plt.xlabel('Block number')
plt.show()

