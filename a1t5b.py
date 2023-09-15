import pandas as pd
pd.set_option('display.max_rows', None)

# Read in the dataset
blocks_df = pd.read_csv('../datasets/blocks23aug2022.tsv', sep='\t')

# split day into 10-minute intervals and count the number of blocks in each interval
blocks_df['time'] = pd.to_datetime(blocks_df['time'])
blocks_df['time'] = blocks_df['time'].dt.floor('10min')
blocks_df = blocks_df.groupby('time').size().reset_index(name='count')
blocks_df = blocks_df.set_index('time').asfreq('10min', fill_value=0).reset_index()
print(blocks_df)

# count the number of intervals with 3 or more blocks
print("\nNumber of intervals with 0 blocks: " + str(blocks_df[blocks_df['count'] == 0].shape[0]))
print("Number of intervals with 1 blocks: " + str(blocks_df[blocks_df['count'] == 1].shape[0]))
print("Number of intervals with 2 blocks: " + str(blocks_df[blocks_df['count'] == 2].shape[0]))
print("Number of intervals with 3 blocks: " + str(blocks_df[blocks_df['count'] == 3].shape[0]))
print("Number of intervals with 3 or more blocks: " + str(blocks_df[blocks_df['count'] >= 3].shape[0]) + "\n")

# print the percentage of each type of interval
print("Percentage of intervals with 0 blocks: " + str(blocks_df[blocks_df['count'] == 0].shape[0] / blocks_df.shape[0] * 100))
print("Percentage of intervals with 1 blocks: " + str(blocks_df[blocks_df['count'] == 1].shape[0] / blocks_df.shape[0] * 100))
print("Percentage of intervals with 2 blocks: " + str(blocks_df[blocks_df['count'] == 2].shape[0] / blocks_df.shape[0] * 100))
print("Percentage of intervals with 3 blocks: " + str(blocks_df[blocks_df['count'] == 3].shape[0] / blocks_df.shape[0] * 100))