A = [1, 2, 0, 0, 3, 4, 5, -1, 0, 2, -1, -3, 0, 0, 0, 0, 0, 0, 0, 2, -3, -4, -5, 0, 0, 0]
idx=[0, 1, 2, 3, 4, 5, 6,  7, 8, 9]

count = 0                           # 0
prev = 0                            # 7
indexend = 0                        # 14
for i in range(0, len(A)):          # i = 14
    if A[i] == 0:                   # False
        count += 1                  # count = 0
    else:
        if count > prev:            # True
            prev = count            # Prev = 7
            indexend = i            # 
        count = 0                   # 
 
print("The longest sequence of 0's is " + str(prev))
print("index start at: " + str(indexend - prev))
print("index ends at: " + str(indexend - 1)

