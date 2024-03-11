import heapq


def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined = first + second
        total_cost += combined

        heapq.heappush(cables, combined)

    return total_cost


cable_lengths = [5, 2, 4, 8, 6, 1]
print(min_cost_to_connect_cables(cable_lengths))
