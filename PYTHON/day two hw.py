#............list........
#ordered,mutable(changeable),and allows duplicate elements,
#list are used to store multiple items in a single variable.


#list create
lst=[1,2,3,4,5,6]

#mix list
mix_lst=[1,3.14,"mansi",True]

#accessing list
print(lst[0])
print(lst[1])
print(lst[3])
print(lst[4])

#adding element

a=[]

a.append(10)
print("after append(10):",a)

#indexing
a.insert(0,5)
print("after insert(0.5):",a)

#adding multiple elements
a.extend([15,20,25])
print("after extend([15,20,25]):",a)

#updating element
a=[10,20,30,40,50]

a[1]=25

print(a)

a=[10,20,30,40,50]

#remove the first occurrence of 30
a.remove(30)
print("after remove(30):",a)

#removes the elements at index 1(20)
popped_val=a.pop(1)
print("popped element:",popped_val)
print("after pop(1):",a)

#deletes the first element(10)
del a[0]
print("after del a[0]:",a)

#>>>>>>>>>>>>>>>TUPLE>>>>>>>>>>>>>>>>>.

#a tuple is a built-in python data structure used to store multiple items in a single variable,
#just like a list-bt tuples are immutable,meaning they cannot be change after creation.

tpl=(10,20,30)#1st typeto create tuple
_tpl=40,50,60 #2nd type to create tuple

print(tpl)
print(_tpl)

print(len(tpl))
print(type(tpl))
print(tpl.count(10))


#>>>>>>>>>>>>>>>>>>>>>>DICTIONARY>>>>>>>>>>

#unordered,mutable,and indexed collection of key-value pairs,

student ={
    "name":"mansi",
    "age":20,
    "collage":"raffles"
}
# accessing values
print(student["name"])
print(student.get("age"))

