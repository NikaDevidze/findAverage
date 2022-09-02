def findAverage(list):
    sum = 0
    for i in list:
        sum = sum + i 
    avg = sum/len(list)
    return avg

print(findAverage([1, 6, 9, 8, 3]))
