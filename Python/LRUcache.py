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
                

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)