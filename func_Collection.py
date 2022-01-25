# coding = utf-8

def merge(left, right, lt):
    """Assumes left and right are sorted lists.
    lt defines an ordering on the elements of the lists.
    :return a new sorted(by lt) list containing the same elements
    as (left + right) would contain."""
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if lt(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result


def sort(L, lt=lambda x, y: x < y):
    """ Return a new sorted list containing the same elements as L
        L : given List
        lt : inside func as named lambda"""
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = sort(L[:middle], lt)
        right = sort(L[middle:], lt)
        # print("About to merge ", left, "and", right)
        return merge(left, right, lt)


def stdDev(X: list) -> float:
    mean = sum(X) / float(len(X))
    tot = 0.0  # tot = total
    for x in X:  # A =Σ(x∈X)
        tot += (x - mean) ** 2  # B =(x-μ)^2
    return (tot / len(X)) ** 0.5  # sqrt(1/abs(x)*Σ(x∈X)*(x-μ)^2))


def cal_prob_per_roll(glist):
    L = [0, 0, 0, 0, 0, 0]
    for i in glist:
        for j in i:
            for k in range(len(L)):
                if j == k + 1:
                    L[k] += 1
    return L


def main():
    temp = [2,3,1,23,5,64,1,23,4314,2]
    print (sort(temp))

    L1 = [[1,2,3,4,5,6],[2,3,3,4,4,5]]
    print(cal_prob_per_roll(L1))


if __name__ == '__main__':
    main()
