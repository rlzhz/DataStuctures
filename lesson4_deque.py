'''
    栈：后进先出（顶部进顶部出）
    队列：先进先出（队尾进，队首出）
    双端队列（Deque）
'''
class Deque:
    def __init__(self):
        self.items = []

    def isEmpyt(self):
        return self.items == []
    def size(self):
        return len(self.items)
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)

d = Deque()
print(d.isEmpyt())
d.addRear(4)
d.addFront('dog')
d.addFront('cat')
d.addFront((True))
print(d.size())
print(d.isEmpyt())
d.addRear(8.4)
print(d.removeRear())