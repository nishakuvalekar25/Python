# Continue statement skips the rest of the code inside the loop for the current iteration and continues with the next iteration.

for i in range(10):
    if i == 4:
        continue
    print(i)

# Output 

# 0
# 1
# 2
# 3
# 5
# 6
# 7
# 8
# 9