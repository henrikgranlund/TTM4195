import pandas as pd
pd.set_option('display.max_rows', None)

# Read in the dataset
blocks_df = pd.read_csv('../datasets/blocks23aug2022.tsv', sep='\t')

# Convert the 'time' column to datetime
blocks_df['time'] = pd.to_datetime(blocks_df['time'])
blocks_df = pd.DataFrame(blocks_df, columns=['time'])

# check if a given block has following block(s) within 10 minutes. 
# If the interval contains more 3 or more blocks, return the interval
def seek_interval(block):
    test_block = block + 1
    current_interval = [block]
    while blocks_df['time'].iloc[test_block] - blocks_df['time'].iloc[block] < pd.Timedelta(minutes=10):
        current_interval.append(test_block)
        test_block += 1
    if len(current_interval) > 2:
        return current_interval
        
# Loop through all the blocks and find the non-overlapping intervals
non_overlapping_intervals = []
i = 0
while i < blocks_df.shape[0] - 1:
    interval = seek_interval(i)
    if interval is not None:
        non_overlapping_intervals.append(interval)
        print("Interval found: " + str(interval))
        i = interval[-1]+1  # skip the blocks in the interval to avoid overlapping
    else:
        i += 1
        
# print the number of non-overlapping intervals which contain 3 or more blocks
print("\n--------------------------------------")
print("Number of Non-overlapping intervals: " + str(len(non_overlapping_intervals)))
print("--------------------------------------\n")