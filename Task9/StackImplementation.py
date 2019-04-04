class Stack:
...   def __init__(self):
...     self.items=[]
...   def push1(self,item):
...     return self.items.append(item)
...   def pop(self):
...     return self.items.pop()
...   def getstack(self):
...     return self.items
... 
>>> s = Stack()
>>> s.push(100)
>>> s.push(200)
>>> s.push('A')
>>> s.pop()
>>> s.getstack()
