for a in range(1, 100):
    if a % 2 != 0:
        continue
    for b in range(1, 101):
        if b % 2 == 0:
            continue
        print(f"{a * b}")
        
