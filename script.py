import logging
import collections

print("-" * 50 + "\nLoad Balance")


class LoadBalance:
    def __init__(self):
        self.tick = 10

    def checkInputFile(self):
        list = []
        with open('input.txt', 'r') as filePointer:
            for row in iter(filePointer.readline, ''):
                list.append(int(row))
        return list

    def newtest(self, a):
        if a[0] >= 10 or a[1] >= 10:
            return print('Error')
        ttask = a[0]
        a.pop(0)
        umax = a[1]
        a.pop(0)
        input = a
        # print(input, a)
        self.calcule(input, ttask, umax, self.tick)

    def calcule(self, input, ttask, umax, tick):
        axes = collections.namedtuple('Ttask', 'x y')
        x = collections.deque()
        server = collections.deque()
        n = 0
        for i in input:
            # print(f'N {n} ' + '-' * 50)
            x.append(axes(ttask, i))
            test = [y for y in x]
            update = [up._replace(x=up.x - 1) for up in test]
            if n == 0:
                server.append(update[n].y)
            elif update[n].y == 0:
                server.append(server[-1])
            else:
                server.append((update[n].y + server[-1]))
            # print(server)
            # print(update)
            n += 1
            # print(i)
        print(update)
        print(server)

test = LoadBalance()
b = test.checkInputFile()
test.newtest(b)
