from itertools import combinations


def blackJ():
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    temp = []

    for com in combinations(cards, 3):
        if sum(com) <= m:
            temp.append(sum(com))
    return max(temp)


print(blackJ())