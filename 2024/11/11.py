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
    print(n, "at start:", a_counter)
    
    if n == 0:
        #print(a_counter.values)
        print(f"memoization: {a_counter}")
        print(sum(a_counter.values))
        return

    for stone in a_counter.non_zero:
        count = a_counter.get(stone)
        
        for i in range(count):
            print(f"i: {i}, count of stones {a_counter.get(stone)}")
            if a_counter.contains(stone):
                if stone == 0:
                    a_counter.add(1)
                    print("stone 0 updated to 1")
                elif len(str(stone)) % 2 == 0:
                    cutoff = len(str(stone)) // 2
                    a = int(str(stone)[:cutoff])
                    b = int(str(stone)[cutoff:])
                    a_counter.add(a)
                    a_counter.add(b)
                    print(f"split {stone} into {a} and {b}")
                else:
                    a_counter.add(2024 * stone)
                    print(f"multiplied", stone)

                a_counter.remove(stone)
                print("removed", stone)
                
    memo_blink(n-1, a_counter)

def dic_add(dic, key):
    if key in dic:
        dic[key] = dic[key] + 1
    else: 
        dic[key] = 1
    return dic

def dic_remove(dic, key):
    if key in dic:
        dic[key] = dic[key] - 1
    if dic[key] < 0:
        dic[key] = 0
    return dic

def memo_blink_dic(n, dic):
    print(n, "at start:", dic)
    
    if n == 0:
        #print(a_counter.values)
        print(f"memoization_DIC: {dic}")
        print(sum(dic))
        return
    temp = list(dic.keys()).copy()
    for stone in temp:
        count = dic[stone]
        
        for i in range(count):
            print(f"i: {i}, count of stones {dic[stone]}")
            if stone in dic.keys():
                if stone == 0:
                    dic = dic_add(dic, 1)
                    print("stone 0 updated to 1")
                elif len(str(stone)) % 2 == 0:
                    cutoff = len(str(stone)) // 2
                    a = int(str(stone)[:cutoff])
                    b = int(str(stone)[cutoff:])
                    dic = dic_add(dic, a)
                    dic = dic_add(dic, b)
                    print(f"split {stone} into {a} and {b}")
                else:
                    dic = dic_add(dic, (2024 * stone))
                    print(f"multiplied", stone)

                dic_remove(dic, stone)
                print("removed", stone)
                
    memo_blink_dic(n-1, dic)

n_blinks = 7
print("puzzle 1:")
#blink(n_blinks, arr)

#print("****")

counter = Counter(arr)

#memo_blink(n_blinks, counter)
dic = {}
for a in arr:
    if a in dic:
        dic[a] = dic[a] + 1
    else:
        dic[a] = 1
print(dic)
memo_blink_dic(n_blinks, dic)