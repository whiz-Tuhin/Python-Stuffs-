def kadane_algorithm(arr):
    max1 = 0
    max2 = 0
    st_index = 0
    end_index = 0
    for i in range(0,len(arr)):
        max1 += arr[i];

        if max1 < 0:
            max1 = 0
            st_index = i
        if max2 < max1:
            max2 = max1
            end_index = i

    l = [max2,st_index,end_index]
    return l


if __name__ == "__main__":
    l = [-2,-3,4,-1,-2,1,5,-3]
    l1 = kadane_algorithm(l)
    print l1


#{-2, -3, 4, -1, -2, 1, 5, -3}
