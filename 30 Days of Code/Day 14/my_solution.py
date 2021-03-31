class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        result = 0
        
        for a in self.__elements:
            for b in self.__elements:    
                temp = a - b
                if result < 0:
                    result = result * (-1)
                if temp > result:
                    result = temp
        self.maximumDifference = result
    
        # Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
