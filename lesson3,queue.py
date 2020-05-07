'''
    队列：
    是一系列有顺序的元素集合，新元素加入队列的一端，这一端叫做队尾(rear)已有元素的移除发生在队列的另一端，叫做队首(front)。当一个元素被加入队列之后，它就从队尾向队首前进，知道它成为下一个即将被移除队列的元素
    先进先出(FIFO):最新被加入的元素处于队尾，在队列中停留最长时间的元素处于队首
    -----------
    rear     front
    -----------

    抽象数据类型(ADT):
        Queue() 创建一个空队列对象，无需参数，返回空的队列
        enqueue(item) 将数据项添加到队尾，无返回值
        dequeue() 从队首移除数据项，无需参数，返回值为队首数据项
        isEmpty() 是否队列为空，无需参数，返回值为布尔值
        size() 返回队列中的数据项的个数，无需参数

    用python list实现队列
    队尾在列表0的位置
    enqueue insert() O(n)
    dequeue pop()   O(1)

'''

# class Queue():
#     def __init__(self):
#         self.items = []
#
#     def enqueue(self,item):
#         self.items.insert(0,item)
#
#     def dequeue(self):
#         return self.items.pop()
#
#     def isEmpty(self):
#         return self.items == []
#
#     def size(self):
#         return len(self.items)
#
# q = Queue()
# q.enqueue('hello')
# q.enqueue('dog')
# q.enqueue(3)
# print(q.size())
# print(q.isEmpty())
# print(q.dequeue())

'''
    马铃薯游戏（击鼓传花）选定一个人作为开始的人，经过num个人后，将此人淘汰 
'''
from pythonds.basic.queue import Queue

name_list = ['红','明','强','丽','马','王','赵','三','四','五','啦']
num = 7

def send_flower(name_list,num):
    q = Queue()
    for name in name_list:
        q.enqueue(name)
        print(q)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        n = q.dequeue()
        print(n)
        print('--------')
    return q.dequeue()

send_flower(name_list,num)


'''

'''
