def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    for i in range(length):
        dict[weights[i]] = i

    for j in range(length):
        weight_of_ship = limit - weights[j]

        if weight_of_ship in dict:
            return(max(j, dict[weight_of_ship]), min(j, dict[weight_of_ship]))
    return None