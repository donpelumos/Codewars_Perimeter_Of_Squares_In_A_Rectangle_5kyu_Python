__author__ = 'Don Pelumos'
'''URL FOR THE KATA - https://www.codewars.com/kata/perimeter-of-squares-in-a-rectangle/train/python'''
def perimeter(n):
    st = 1
    st2 = 1
    fibList = [st,st2]
    sum = 0
    for i in range(1,n,1):
        new =st+st2
        st = st2
        st2 = new
        fibList.append(st2)
    #print(fibList)
    for i in range(0,len(fibList),1): sum=sum+fibList[i]
    return sum*4
print(perimeter(100))