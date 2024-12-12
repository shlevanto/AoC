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
            blinked.append(1)
            continue
        if len(str(stone)) % 2 == 0:
            cutoff = len(str(stone)) // 2
            a = int(str(stone)[:cutoff])
            b = int(str(stone)[cutoff:])
            blinked.append(a)
            blinked.append(b)
            continue

        else:
            blinked.append(2024 * stone)

    blink(n-1, blinked, [])

class Counter:
    def __init__(self):
        self.dic = {}
    
    def add(self, number):
        if number in self.dic.keys():
            self.dic[number] = self.dic[number] + 1
        else:
            self.dic[number] = 1

    def remove(self, number):
        if number in self.dic.keys():
            self.dic[number] = self.dic[number] - 1
            if self.dic[number] < 0:
                self.dic[number] = 0
    
    @property
    def values(self):  
         return list(self.dic.values())

    @property
    def keys(self):  
         return list(self.dic.keys()) 
    
    def non_zero(self):
        return list([a for a in self.keys() if self.dic[a] > 0])

    def __str__(self):
        return str(self.dic)


def memo_blink(n, a_counter):
    #print(a_counter)
    if n == 0:
        print(sum(a_counter.values))
  
        return


    for stone in a_counter.keys:
        if stone == 0:
            a_counter.add(1)

        if len(str(stone)) % 2 == 0 and len(str(stone)) > 1:
            cutoff = len(str(stone)) // 2
            a = int(str(stone)[:cutoff])
            b = int(str(stone)[cutoff:])
            a_counter.add(a)
            a_counter.add(b)

        else:
            a_counter.add(2024 * stone)
            
        a_counter.remove(stone)
        

    memo_blink(n-1, a_counter)


print("puzzle 1:")
#blink(25, arr)

print("****")

counter = Counter()

for s in arr:
    counter.add(s)


memo_blink(6, counter)
