def pontos(l1,l2):
    if l1 == l2:
        return 25
    elif (l1[0] != l1[1] and l2[0] != l2[1]) and (max(l1) == max(l2)):
        return 18
    elif abs(l1[0] - l1[1]) == abs(l2[0] - l2[1]):
        return 15
    elif (l1[0] != l1[1] and l2[0] != l2[1]) and (min(l1) == min(l2)):
        return 12
    elif (l1[0] != l1[1] and l2[0] != l2[1]) and (l1.index(max(l1)) == l2.index(max(l2))):
        return 10
    elif (l1[0] == l1[1] and l2[0] == l2[1]):
        return 5
    else:
        return 0
