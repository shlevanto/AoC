file_path = "09.input"

with open(file_path, "r") as f:
    input_string = f.read()

arr = [int(n) for n in input_string if n != "\n"]

result = []
values = []

for i, x in enumerate(arr):
    if i % 2 == 0:
        values.append(i//2)

counter = 0

while arr and values:
    a = arr.pop(0)
    
    if counter % 2 != 0:
        v_1 = -1
    else:
        v_1 = values.pop(0)

    for i in range(a):
        result.append(v_1)

    counter += 1     

for i, r in enumerate(result):
    if r < 0:
        k = result.pop(-1)
        if k < 0:
            while k < 0:
                k = result.pop(-1)
        result[i] = k

print(sum(i * x for i, x in enumerate(result)))




