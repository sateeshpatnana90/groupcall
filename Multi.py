# print the 5 multiples till the given value.
class value:
    def multiple(self,limit):
        for i in range(5,limit+1,5):
            print(i)
            i=5
            while i<limit:
              i=i+5
limit=int(input("enter value"))
obj=value()
obj.multiple(limit)