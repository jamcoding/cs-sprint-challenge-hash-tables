#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    dict = {}

    route = [None] * length

    x = 1

    for i in range(length):
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
        elif tickets[i].destination == "NONE":
            route[length - 1] = tickets[i].source
        else:
            dict[tickets[i].source] = tickets[i].destination

    for source, destination in dict.items():
        if x == length - 1:
            break

        route[x] = dict[route[x - 1]]
        x += 1

    route[length - 1] = "NONE"

    return route
