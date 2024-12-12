# 1. If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# 2. If the stone is engraved with a number that has an even number of digits, 
# it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# 3. If none of the other rules apply, the stone is replaced by a new stone; 
# the old stone's number multiplied by 2024 is engraved on the new stone.

# Two options -> input into new list or use linked list

#
file_path = "11_short.input"

with open(file_path, "r") as f:
    arr = [int(s) for s in f.read().strip().split(" ")]


def blink(n, stones, blinked=[]):
    
    
    if n == 0:
        print(len(stones))
        return

    for stone in stones:  
        if stone == 0:
            #print("rule 1")
            blinked.append(1)
        elif len(str(stone)) % 2 == 0:
            continue
        if len(str(stone)) % 2 == 0:
            cutoff = len(str(stone)) // 2
            a = int(str(stone)[:cutoff])
            b = int(str(stone)[cutoff:])
            
            print("rule 2:", a, b)

            blinked.append(a)
            blinked.append(b)
            continue

        else:
            blinked.append(2024 * stone)

    blink(n-1, blinked, [])

blink(6, arr)
