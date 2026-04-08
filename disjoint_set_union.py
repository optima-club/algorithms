parents = {}
sizes = {}

def make_set(v):
    parents[v] = v
    sizes[v] = 1
    
def find_set(v):
    if parents[v] == v:
        return v
    parents[v] = find_set(parents[v])
    return parents[v]

def union_sets(a, b):
    print(f'Union: {a}, {b}')
    a = find_set(a)
    b = find_set(b)
    if a != b:
        # print(a, b)
        # print(sizes[a], sizes[b])
        if sizes[a] < sizes[b]:
            a, b = b, a
        parents[b] = a
        sizes[a] += sizes[b]
        
for v in [1, 2, 4, 8, 9, 12, 13]:
    make_set(v)

print(f'Parents: {parents}\nSizes: {sizes}\n')

union_sets(8, 9)
print(f'Parents: {parents}\nSizes: {sizes}\n')
assert parents[9] == 8

union_sets(2, 12)
print(f'Parents: {parents}\nSizes: {sizes}\n')
assert parents[12] == 2

union_sets(1, 8)
print(f'Parents: {parents}\nSizes: {sizes}\n')
assert parents[1] == 8

union_sets(12, 1)
print(f'Parents: {parents}\nSizes: {sizes}\n')
assert parents[2] == 8 and parents[12] == 2

find_set(12)
print(f'Parents: {parents}\nSizes: {sizes}\n')
assert parents[2] == 8 and parents[12] == 8
