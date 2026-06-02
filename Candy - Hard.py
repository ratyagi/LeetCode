def candy(ratings: list[int]) -> int:
    arr = [1] * len(ratings)

    # pass 1: left to right
    for i in range( 1, len(ratings)):
        if ratings[i] > ratings [i-1]:
            arr[i] = arr[i-1] +1

    # pass 2: right to left
    for i in range (len(ratings)-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            arr[i] = max(arr[i], arr[i+1]+1)

    return sum(arr)

#test case
ratings = [1,0,2]
print(candy(ratings))# Output: 5
