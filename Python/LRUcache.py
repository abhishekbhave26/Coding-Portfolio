#leetcode 146

class LRUCache(object):
    
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.dic={}
        self.queue=[]
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if(key in self.dic):
            self.queue.remove(key)
            self.queue.append(key)
            return self.dic[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if(key in self.dic):
            self.dic[key]=value
            self.queue.remove(key)
            self.queue.append(key)
        else:
            if(len(self.queue)<self.capacity):
                self.dic[key]=value
                self.queue.append(key)
            else:
                del self.dic[self.queue[0]]
                self.queue.pop(0)
                self.dic[key]=value
                self.queue.append(key)
    
    


from collections import OrderedDict
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.LRU = OrderedDict()
        
    def get(self, key: int) -> int:
        if key not in self.LRU:
            return -1
        self.LRU.move_to_end(key,last = True)
        return self.LRU[key]
            
    def put(self, key: int, value: int) -> None:
        if key in self.LRU:
            self.LRU.move_to_end(key,last = True)
        self.LRU[key] = value
        if len(self.LRU) > self.capacity:
            self.LRU.popitem(last = False)  #Pop first item
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)