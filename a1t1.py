target_block = 750744
halving_interval = 210000
total_BTC = 0

for i in range(0, target_block+1):
    if i < halving_interval:
        total_BTC += 50
    elif i < halving_interval * 2:
        total_BTC += 25
    elif i < halving_interval * 3:
        total_BTC += 12.5
    else:
        total_BTC += 6.25
        
print("BTC Mined: " + str(total_BTC))
print("BTC Left :  " + str(21000000 - total_BTC))