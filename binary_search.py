
def result(list,target):
    while True:
        
        length= len(list)
        mid = length//2
        # print(mid)
        p = list[mid]
        # print(p)
        if p==target:
            print('given number has found:',target)
            break
        elif p<target:
            list=list[mid:]
        elif p>target:
            list = list[:mid]

l = [2,3,21,34,56,67,1,54,34,32,78,9,86,56,32,90,76,56,32,21,10,43]
l.sort()
tar = 67 # target must be in given list(l)
result(l,tar)