class RandomizedSet:

    def __init__(self):
        #instantiate list and a hashmap
        self.numList = []
        self.numMap = {}
        
    def insert(self, val: int) -> bool:
        # if there -> False
        res = val not in self.numMap
        # if not there -> true
        if res: 
            # add it to hashmap mapping to last index of list. which is the length of the list
            self.numMap[val]= len(self.numList)
            # append to the list
            self.numList.append(val)
        return res

    def remove(self, val: int) -> bool:
        # if not there ->  false
        res = val in self.numMap
        # if there - > true
        if res: 
            # get 'idx' index of the val from the hashMap
            idx = self.numMap[val]
            # store the last value in the list. 
            lastVal = self.numList[-1]
            # swap the idx value with last value
            self.numList[idx] = lastVal
            # pop the list 
            self.numList.pop()
            # update the lastval's mapping in the hashmap with idx
            self.numMap[lastVal] = idx
            # del val from hashmap
            del self.numMap[val] 
        return res

    def getRandom(self) -> int:
        #use random function for this 
        return random.choice(self.numList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
