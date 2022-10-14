from typing import List


# 1. Coding basic loops
# a.
def get_ASCII_code(S: str) -> None:
    for ch in S:
        print(ord(ch), end=" ")


# b.
def get_ASCII_sum(S: str) -> int:
    return sum(map(ord, S))


# c.1
def get_ASCII_list_1(S: str) -> List[int]:
    new_list = []
    for ch in S:
        new_list.append(ord(ch))
    return new_list


# c.2
def get_ASCII_list_2(S: str) -> List[int]:
    return map(ord, S)


# c.3
def get_ASCII_list_3(S: str) -> List[int]:
    return [ord(c) for c in S]


# 3. Sorting dictionaries
# 3.1
d = {
    "k": ord("k"),
    "e": ord("e"),
    "v": ord("v"),
    "i": ord("i"),
    "n": ord("n"),
}
sorted_keys = list(d.keys())
sorted_keys.sort()
for k in sorted_keys:
    print(k, "=>", d[k])

# 3.2
sorted(d.values())

# 4. Program logic alternatives
# a.
L = [1, 2, 4, 8, 16, 32, 64]
X = 5
found = False
i = 0
while not found and i < len(L):
    if 2**X == L[i]:
        print("at index", i)
        break
    i = i + 1
else:
    print(X, "not found")

# b.
for i in L:
    if 2**X == i:
        print("at index", L.index(i))
        break
else:
    print(X, "not found")

# c.
if 2**X in L:
    print("at index", L.index(2**X))
else:
    print(X, "not found")

# d.
L_2 = [2**p for p in range(7)]

# e.
L_2 = [2**p for p in range(7)]
X = 5
found = False
i = 0
power_of_X = 2**X
while not found and i < len(L):
    if power_of_X == L[i]:
        print("at index", i)
        break
    i = i + 1
else:
    print(X, "not found")
