def is_match(t1, t2):
    
    return all(a >= b for a, b in zip(t1, t2))

t1 = [0,1,1,0,0,0,1,1]
t2 = [0,1,0,0,0,0,1,1]

print(is_match(t1, t2))  # True