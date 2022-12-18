'''
https://adventofcode.com/2022/day/11
'''

import math

filename = 'testinput.txt'
filename = 'input.txt'
def filereader(filename):
    for line in open(filename, "r"):
        yield line


class Monkey():
    def __init__(self, monkey_id):
        self.monkey_id = monkey_id
        self.items: list
        self.operation_string: list
        self.test_val: int           # divisible by x
        self.test_val_true: int      # target monkey if divisible by x
        self.test_val_false: int     # target monkey not if divisible by x
        self.inspected = 0           # how often inspected an item

    def turn(self):
        #print("Monkey", self.monkey_id, ":")
        while len(self.items) > 0:
            item = self.items.pop(0)
            #print("  Monkey inspects an item with a worry level of ", item)
            item = self.update_worry(item)
            target_monkey = str(self.do_test(item))
            item = item % gcd
            monkeys[target_monkey].items.append(str(item))
            self.inspected = self.inspected + 1
        #print("===============")

    def update_worry(self, item):
        execstr = list(self.operation_string)
        for i in range(len(execstr)):
            if execstr[i] == 'old': execstr[i] = item
        #print("    Worry level is multiplied by ", execstr[2], "to", eval(" ".join(execstr)))
        #print("    Monkey gets bored with item. Worry level is divided by 3 to", math.floor(eval(" ".join(execstr))))
        return math.floor(eval(" ".join(execstr)))

    def do_test(self, item):
        #print("    Current worry level is not divisible by ", self.test_val)
        if item % self.test_val == 0:
            #print("    Item with worry level", item, "is thrown to monkey", self.test_val_true)
            return self.test_val_true
        else:
            #print("    Item with worry level", item, "is thrown to monkey", self.test_val_false)
            return self.test_val_false


    def show(self):
        #print("Monkey " + self.monkey_id +
        #      ":\n  Starting items: " + ",".join(self.items) +
        #      "\n  Operation: new = : " + "".join(self.operation_string) +
        #      "\n  Test: divisible by " + str(self.test_val) +
        #      "\n    If true: throw to monkey " + str(self.test_val_true) +
        #      "\n    If false: throw to monkey " + str(self.test_val_false) + "\n")
        pass





def round(monkeys):
    for i in monkeys.values():
        i.turn()


input = filereader(filename)
monkeys = dict()
monkey_business = list()
gcd = 1

for line in input:
    id = line[-3:-2]
    monkeys[id] = Monkey(id)
    monkeys[id].items = next(input)[18:-1].split(",")
    monkeys[id].operation_string = next(input)[19:-1].split(" ")
    monkeys[id].test_val = int(next(input).split()[-1])
    monkeys[id].test_val_true = int(next(input).split()[-1])
    monkeys[id].test_val_false = int(next(input).split()[-1])
    gcd = gcd * monkeys[id].test_val
    try:
        next(input)
    except StopIteration:
        pass


for i in range(10000):
    if (i == 1) or (i == 20) or (i % 1000 == 0) and (i != 0):
        pass
        print("== After round", i, "==")
        for id in monkeys:
#            print("Monkey", id, ":", monkeys[id].items)
            print("Monkey", id, ":", monkeys[id].inspected)
            monkey_business.append(monkeys[id].inspected)
    round(monkeys)

print("=======\n\nfinish")
for id in monkeys:
#    print("Monkey", id, ":", monkeys[id].items)
    print("Monkey", id, ":", monkeys[id].inspected)
    monkey_business.append(monkeys[id].inspected)

print(sorted(monkey_business)[-2:-1][0] * sorted(monkey_business)[-1:][0])
