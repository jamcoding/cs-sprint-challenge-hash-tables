def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    dict = {}

    for i in range(len(a)):
        if a[i] > 0:
            dict[a[i]] = None

    for i in range(len(a)):
        if a[i] < 0:
            absolute_value = abs(a[i])
            if absolute_value in dict:
                result.append(absolute_value)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
