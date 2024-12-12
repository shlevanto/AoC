# 1. If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# 2. If the stone is engraved with a number that has an even number of digits, 
# it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
# 3. If none of the other rules apply, the stone is replaced by a new stone; 
# the old stone's number multiplied by 2024 is engraved on the new stone.

# Two options -> input into new list or use linked list
from copy import deepcopy
#
file_path = "11.input"

with open(file_path, "r") as f:
    arr = [int(s) for s in f.read().strip().split(" ")]

#arr = [int(s) for s in "2024".split()]
def blink(n, stones, blinked=[]):
    if n == 0:
        print(len(stones))
        print(f"brute: {Counter(stones)}")
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
    dic = dict
    
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

    def get(self, number):
        if number in self.dic.keys():
            return self.dic.copy()[number]
        return 0
  
    def contains(self, number):
        return self.dic[number] > 0
    @property
    def values(self):  
         return list(self.dic.values())

    @property
    def keys(self):  
         return list(self.dic.keys()) 
    
    @property
    def non_zero(self):
        return list([a for a in self.keys if self.dic[a] > 0])

    def to_dict(self):
        return dict(self.dic)
    
    def __str__(self):
        return str(self.dic)
    
    def __init__(self, arr):
        self.dic = {}
        for e in arr:
            if e in self.dic.keys():
                self.dic[e] = self.dic[e] + 1
            else:
                self.dic[e] = 1
    
    

def memo_blink(n, a_counter):
    print(n)
    incoming = deepcopy(a_counter)

    if n == 0:
        print(sum(a_counter.values))
        return

    for stone in incoming.non_zero:
        count = incoming.get(stone)

        if incoming.get(stone) > 0:
            if stone == 0:
                for i in range(count):
                    a_counter.add(1)
                    a_counter.remove(stone)
            elif len(str(stone)) % 2 == 0:
                cutoff = len(str(stone)) // 2
                a = int(str(stone)[:cutoff])
                b = int(str(stone)[cutoff:])
                for i in range(count):
                    a_counter.add(a)
                    a_counter.add(b)
                    a_counter.remove(stone)
            else:
                for i in range(count):
                    a_counter.add(2024 * stone)
                    a_counter.remove(stone)            
    memo_blink(n-1, a_counter)


n_blinks = 75

print("puzzle 1:")
#blink(n_blinks, arr)

print("****")

counter = Counter(arr)
memo_blink(n_blinks, counter)

