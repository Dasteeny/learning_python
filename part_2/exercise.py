# 1. Basics - Try to explain what’s happening in each case
"""
2 ** 16                                         # Outputs the 16's power of 2
2 / 5, 2 / 5.0                                  # Result 1: 0, Result 2: 0.4 [Wrong-1]
"spam" + "eggs"                                 # "spameggs"
S = "ham"                                       # Points var S to object "ham"
"eggs " + S                                     # "eggs ham"
S * 5                                           # "hamhamhamhamham"
S[:0]                                           # None? [Wrong-2]
"green %s and %s" % ("eggs", S)                 # "green eggs and ham"
'green {0} and {1}'.format('eggs', S)           # "green eggs and ham"
('x',)[0]                                       # 'x'
('x', 'y')[1]                                   # 'y'
L = [1,2,3] + [4,5,6]                           # L = [1, 2, 3, 4, 5, 6]
L, L[:], L[:0], L[-2], L[-2:]                   # [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [], 5, [5, 6] 
([1,2,3] + [4,5,6])[2:4]                        # (3, 4) [Wrong-3]
[L[2], L[3]]                                    # [3, 4]
L.reverse(); L                                  # [6, 5, 4, 3, 2, 1]
L.sort(); L                                     # [1, 2, 3, 4, 5, 6]
L.index(4)                                      # 3
{'a':1, 'b':2}['b']                             # 2
D = {'x':1, 'y':2, 'z':3}
D['w'] = 0                                      # D is {'x':1, 'y':2, 'z':3, 'w':0} now
D['x'] + D['w']                                 # 1
D[(1,2,3)] = 4                                  # D is {'x':1, 'y':2, 'z':3, 'w':0, (1,2,3): 4} now
list(D.keys()), list(D.values()), (1,2,3) in D  # ['x', 'y', 'z', 'w', (1,2,3)], [1, 2, 3, 0, 4], True
[[]], ["",[],(),{},None]                        # [[]], ["",[],(),{},None]
"""

# Wrong-1 - In Python 3.X / does not truncate the result, but in Python 2.X does
# Wrong-2 - An empty slice at the front -- [0:0]. Empty of same type as object sliced
# Wrong-3 - [3, 4]


# 2. Indexing and Slicing
L = [0, 1, 2, 3]
# a
try:
    L[4]
except IndexError as e:
    print("We get a 'list index out of range' exception")
# b
try:
    L[-1000:100]
except IndexError as e:
    print("Same here")
finally:
    print(
        "Wrong - slicing out of bounds (e.g., L[-1000:100]) works because Python \
            scales out-of-bounds slices so that they always fit"
    )
# c
L[3:1] = ["?"]  # [0, 1, 2, '?', 3]
"""
Extracting a sequence in reverse, with the lower bound greater than the higher
bound (e.g., L[3:1]), doesn't really work. You get back an empty slice ([ ]) because
Python scales the slice limits to make sure that the lower bound is always less than
or equal to the upper bound (e.g., L[3:1] is scaled to L[3:3], the empty insertion
point at offset 3). Python slices are always extracted from left to right, even if you
use negative indexes (they are first converted to positive indexes by adding the
sequence length). Note that Python 2.3's three-limit slices modify this behavior
somewhat. For instance, L[3:1:-1] does extract from right to left
"""

# 3. Indexing, slicing, and del
L = ["a", "b", "c", "d"]
L[2] = []  # 'c' value will be overwritten by []
L[2:3] = []  # Nothing changes [Wrong]
del L[0]  # ["b", "d"]
del L[1:]  # ["b"]
L = ["a", "b", "c", "d"]
try:
    L[1:2] = 1  # deletes "b" and inserts 1
except TypeError:
    print(
        "Slice assignment expects another sequence, or you'll get a type error; \
            it inserts items inside the sequence assigned, not the sequence itself"
    )

# Wrong - Recall that slice assignment deletes the slice and inserts the new value where it used to be


# 4. Tuple assignment
X = "spam"
Y = "eggs"
X, Y = Y, X  # Swaps variables values - X='eggs', Y='spam'


# 5. Dictionary keys
D = {}
D[1] = "a"
D[2] = "b"
D[(1, 2, 3)] = "c"  # In Python any hashable object can be a dict key


# 6. Dictionary indexing
D = {"a": 1, "b": 2, "c": 3}
try:
    D["d"]
except KeyError as e:
    print("Trying to index non-existent key results in KeyError exception")
D["d"] = "spam"  # New key-value pair will be inserted into the dict


# 7. Generic operations
# a
try:
    "a" + 1
except TypeError as e:
    print("Cannot apply + on different types")
# b
try:
    "a" + {"b": 2, "c": 3}
except TypeError as e:
    print("Cannot apply + on different types")
# c
L = [1, 2, 3]
L.append(4)
try:
    "spam ".append("eggs")
except AttributeError:
    print("str does not support append()")
# d
[1, 2] + [3, 4]  # returns new list
"We seek the Holy Grail!"[12:-1]  # returns new str


# 8. String indexing
S = "holy"
S[0][0][0][0][0]  # S[0] returns a new str('h') and indexing keeps going
["s", "p", "a", "m"][0][0][0][0][0]  # Works too


# 9. Immutable types
S = "spam"
S = S[:1] + "l" + S[2:]
try:
    S[1] = "l"
except TypeError:
    print("str does not support item assignment")


# 10. Nesting
D = {
    "name": {"first": "John", "middle": "K.", "last": "Doe"},
    "age": 24,
    "job": "Pythonista",
    "email": "john.doe@mail.com",
    "phone": "+9053526488",
}
D["age"]
D["name"]["first"]

# 11. Files
with open("myfile.txt", "w") as f:
    f.write("Hello file world!")
with open("myfile.txt") as f:
    print(f.read())
