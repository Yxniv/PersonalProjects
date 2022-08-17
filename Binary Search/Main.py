def naiveSearch(sortedList, target):
    for index in range(len(sortedList)):
        if sortedList[index] == target:
            return index
    return -1


def binarySearch(sortedList, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(sortedList) - 1

    if high < low:
        return -1

    midpoint = ((low + high) // 2)

    if sortedList[midpoint] == target:
        return midpoint
    elif target < sortedList[midpoint]:
        return binarySearch(sortedList, target, low, midpoint - 1)
    else:
        return binarySearch(sortedList, target, midpoint + 1, high)


if __name__ == "__main__":
    sortedList = [1, 2, 4, 5, 6, 10]
    target = 4
    print("Naive Search: Located in index ", naiveSearch(sortedList, target))
    print("Binary Search: Located at index ", binarySearch(sortedList, target))
