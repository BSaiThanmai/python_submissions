# #slicing
# l=[1,2,3,4,5,6,7,8,9]
# print(l[0:5])  # prints elements from index 0 to 4
# print("+++++++++++++++++++++++")
# l1="john"
# print(l1[0:3:2])  # prints characters from index 0 to 2
# print(l1[::2])
# print("+++++++++++++++++++++++")
# l2="chicken"
# print(l2[::-1])
'''
list1=['english','physics',[1,2,3,4,5],'chemistry','maths']
# list1[2][0]=100
# list1[2][0:3:2] no useful
# list1[2][0:3:2]=[100,200]
print(list1[2][0:3:2])
print(list1[2][::2])
print(list1[2][0])
print(list1[-3][::2])
print(list1[-2:5:2])
print(list1[0][::-1])
print(list1[2][::-1])
list1[2][4]=500
print(list1)

'''



d={"a":[56,True,(45,67,"hello")],
   "b":{1:["cricket"],2:["chess"]},
   "c":[67.8,"9898",False,"false"]}

'''
1.False           4.8989
2.hello            5.(67)
3.tcc               6.[56,True,(45,67,"hello")]
 7.fle              8.True
 9.["cricket"]      10.hlo
'''
print(d["c"][2]) #1. False
print(d["a"][1]) #8.True
print(d["a"][2][2])#2.hello
print(d["b"][1][0][-1::-3]) #3.tcc
print(d["c"][1][::-1])#4.8989
print(d["a"][2][1::-2]) #5.(67)
print(d["a"])#6.[56, True, (45, 67, 'hello')]
print(d["c"][3][::2]) #7.fle
print(d["b"][1][0]) #9.["cricket"]
print(d["a"][2][2][::2]) #10.hlo     

l=[
{
 "a":["hockey","volley ball","foot ball"],
 "b":("pushpa","dragon","varanasi","aarya")},
 True,
 "67890",
 "5678.897",
 [78,False]
]                      
'''
1.8.8
2."79"
3.("pushpa","aarya")
4.nasi
5.[78,False]
6.e bl
7.key
8."aphsup"
9.foot
10.True

'''
print(l[3][3:6]) #8.8
print(l[3][:-3:-1])#79
print(l[0]["b"][0:4:3]) #3.("pushpa","aarya")
print(l[0]["b"][2][4:])#4.nasi
print(l[4]) #5.[78,False]
print(l[0]["a"][1][4:10:2]) #6.e bl
print(l[0]["a"][0][3:]) #7.key
print(l[0]["b"][0][::-1]) #8."aphsup"
print(l[0]["a"][2][0:4]) #9.foot
print(l[1]) #10.True









