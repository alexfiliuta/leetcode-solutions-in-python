import random

class RandomizedSet(object):

    def __init__(self):
        self.hashMap = {}
        self.list = []
    
    def insert(self, val):
        res = val not in self.hashMap
        if res:
            self.hashMap[val] = len(self.list)
            self.list.append(val)
        return res
        """
        :type val: int
        :rtype: bool
        """

    def remove(self, val):
        res = val in self.hashMap
        if res:
            idx = self.hashMap[val]
            last = self.list[len(self.list)-1]
            self.list[idx] = last
            self.list.pop()
            self.hashMap[last] = idx
            del self.hashMap[val]
        return res
        """
        :type val: int
        :rtype: bool
        """

    def getRandom(self):
        return random.choice(self.list)
        """
        :rtype int
        """

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()   