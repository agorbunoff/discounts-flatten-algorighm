from collections import defaultdict


def index(l, x):
    try:
        return l.index(x)
    except ValueError:
        return -1


def flatten(l):
    wages = defaultdict(int)
    pairs = set()

    for row in l:
        # calculate wages (sum occurrences)
        for i in row:
            wages[i] += 1

        # add unique pairs to the set: {(1, 2), (2, 4), ...}
        for x, y in zip(row, row[1:]):
            if x != y:
                pairs.add((x, y))

    # sort set of pairs by wage x and then y
    pairs = sorted(pairs, key=lambda x: (-wages[x[0]], -wages[x[1]]))

    # build list of uniques values in correct order
    temp_out = []
    for pair in pairs:
        x, y = pair
        # X and Y
        if (ind_x := index(temp_out, x)) > -1 and (ind_y := index(temp_out, y)) > -1:
            if ind_x > ind_y:
                print(f"swapping {x} and {y}")
                temp_out[ind_x] = y
                temp_out[ind_y] = x
        # X and not Y
        elif (ind_x := index(temp_out, x)) > -1 and y not in temp_out:
            print(f"inserting {y} to index {ind_x + 1}")
            temp_out.insert(ind_x + 1, y)
        # not X and Y
        elif x not in temp_out and (ind_y := index(temp_out, y)) > -1:
            print(f"inserting {x} to index {ind_y}")
            temp_out.insert(ind_y, x)
        # not X not Y
        else:
            print(f"extend list by {x} and {y}")
            temp_out.extend(pair)

    # build final list: repeat x times of each unique value
    out = []
    for x in temp_out:
        out.extend([x] * wages[x])

    return out


l1 = [[1, 1, 1, 2],
      [2, 2, 2, 3],
      [1, 1, 1, 3],
      [4, 1, 1, 3]]

assert flatten(l1) == [4, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]

l2 = [[1, 1, 1, 2],
      [2, 2, 2, 3],
      [1, 1, 1, 3],
      [4, 1, 1, 3],
      [5, 5, 5, 1]]

assert flatten(l2) == [5, 5, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]

l3 = [[1, 1, 1, 2],
      [2, 2, 2, 3],
      [1, 1, 1, 3],
      [4, 1, 1, 3],
      [5, 5, 5, 1],
      [6, 6, 3, 3]]

assert flatten(l3) == [5, 5, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 6, 6, 3, 3, 3, 3, 3]

l4 = [[1, 1, 1, 2],
      [2, 2, 2, 3],
      [1, 1, 1, 3],
      [4, 1, 1, 3],
      [5, 5, 5, 1],
      [6, 6, 3, 3],
      [6, 7],
      ["x", 7],
      ["y", "x", "c"]]

assert flatten(l4) == [5, 5, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 6, 6, 6, 'y', 'x', 'x', 'c', 7, 7, 3, 3, 3, 3, 3]

l5 = [[1, 1, 1, 2],
      [2, 2, 2, 3],
      [1, 1, 1, 3],
      [4, 1, 1, 3],
      [5, 5, 5, 1],
      [6, 6, 3, 3],
      [6, 7],
      [4, 5]]

assert flatten(l5) == [4, 4, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 6, 6, 6, 7, 3, 3, 3, 3, 3]
