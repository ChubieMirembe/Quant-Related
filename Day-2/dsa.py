arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

new_arr = {x for x in arr if x % 3 == 0 }

for i in new_arr:
    print(i, end=" ")