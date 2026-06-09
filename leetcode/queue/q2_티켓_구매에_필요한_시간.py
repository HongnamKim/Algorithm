from collections import deque

def timeRequiredToBuy(tickets, k):
    time = 0
    tickets = deque(tickets)

    while tickets:
        time += 1
        tickets[0] -= 1
        if tickets[k] == 0:
            break

        if tickets[0] != 0:
            tickets.append(tickets.popleft())
        else:
            tickets.popleft()

        if k != 0:
            k -= 1
        else:
            k = len(tickets) - 1

        print(list(tickets), k, "| time: " + str(time))

    return time

t = [5,1,1,1]
index = 0
print(timeRequiredToBuy(t, index))