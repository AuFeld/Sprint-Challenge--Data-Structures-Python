# Task 2 | Runtime Optimization 

# (Hint: You might try importing a data structure you built during the week)
# Initial Run Time = 5.5 seconds

import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = set(f.read().split("\n"))  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure


# Replace the nested for loops below with your improvements
'''
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)
'''

bst = BSTNode('name entries')

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

'''
Current run time of the starter code has nested for loops, which makes our inner
loop run each time. Our outer loop is running, and they are the same length of
10,000, we are looking at 0(n^2). By implementing our binary search tree, it has
an 0(log n) time complexity. 
'''

# Improved Run Time = 0.006 seconds

'''
if time permits:
    return Stretch_Goal
else:
    return Complete
'''
# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
