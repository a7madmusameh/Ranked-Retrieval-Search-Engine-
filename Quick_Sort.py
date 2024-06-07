import random
def Portition(lest, P, R):
    pivot = lest[P]
    k = P + 1
    j = R
    while j >= k:
        up = lest[k]
        down = lest[j]
        if up >= pivot:
            k += 1
        elif down <= pivot:
            j -= 1
        else:
            lest[k], lest[j] = lest[j], lest[k]
    if j < k or lest[j] <= pivot:
        lest[P], lest[j] = lest[j], lest[P]
        Q = j
        return Q
def Randomaized_Partition(lest, P, R):
    Rand = random.randint(P, R)
    lest[P], lest[Rand] = lest[Rand], lest[P]
    Q = Portition(lest, P, R)
    return Q
def Quick_Sort(lest, P, R):
    if P < R:
        Q = Randomaized_Partition(lest, P, R)
        Quick_Sort(lest, P, Q-1)
        Quick_Sort(lest, Q+1, R)
