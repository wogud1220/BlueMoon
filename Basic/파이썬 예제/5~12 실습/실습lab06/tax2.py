def tax(amount):
    if amount <= 1200:
        total = amount * 0.06
                
    elif 1200 < amount <= 4600:
        total = 72 + (amount - 1200) * 0.15
                
    elif 4600 < amount <= 8800:
        total = 582 + (amount - 4600) * 0.24
                
    elif 8800 < amount <= 15000:
        total = 1590 + (amount - 8800) * 0.35
                
    elif 15000 < amount <= 30000:
        total = 3760 + (amount - 15000) * 0.38
                
    elif 30000 < amount <= 50000:
        total = 9460 + (amount - 30000) * 0.4
                
    elif 50000 < amount <= 100000:
        total = 17460 + (amount - 50000) * 0.42
                
    else:
        total = 38460 + (amount - 100000) * 0.45
        
    return int(total)

