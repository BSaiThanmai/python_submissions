number=25
num1=15.2
print(type(number))
print(type(num1))
print(int(num1))
print(float(number))
print(bool(number))
print(bool(num1))
print(complex(number))
print(complex(num1))
print(str(number))
                      #in int we cant typecast to list, tuple, set, dict, etc.
                      # but we can typecast to float, bool, complex and str.
#-----------float--------------
print(float(num1))
print(int(num1))
print(bool(num1))
print(complex(num1))
print(str(num1))
                           #in float we cant typecast to list, tuple, set, dict, etc.
                           # but we can typecast to int, bool, complex and str.
b=True
print(int(b))
print(float(b))
print(complex(b))
print(str(b))
print(bool(b))
                        #in bool we cant typecast to list, tuple, set, dict, etc.
c=1+2j
print(complex(c))
print(str(c))
print(bool(c))
                        #in complex we cant typecast to list, tuple, set, dict,int,float etc.
                        #but it if typecasted in to str,complex,bool.

#-----------------list------------------
l=[1,2,3,4,5]
print(type(l))
print(bool(l))
print(str(l))
print(tuple(l))
print(set(l))
                  # print(dict(l))
                           #in list we cant typecast to int, float, complex,dict etc.
                           #but we can typecast to bool and str.
#------------------tuple------------------
t=(1,2,3,4,5)
print(type(t))
#                              # print(int(t))
#                              # print(float(t))
print(bool(t))
#                              # print(complex(t))
print(str(t))
print(list(t))
print(set(t))
#                              # print(dict(t))
                        #in tuple we cant typecast to int, float, complex,dict etc.
                        #but we can typecast to bool, str, list and set.
#------------------set------------------
s={1,2,3,4,5}
print(type(s))
# print(int(s))
# print(float(s))
print(bool(s))
# print(complex(s))
print(str(s))
print(list(s))
print(tuple(s))
# print(dict(s))
                           # in set we cant typecast to int, float, complex,dict etc.
                           # but we can typecast to bool, str, list and tuple.
    
# -------------------()------------------
f=()
print(type(f))
                         # print(int(f))
                        # print(float(f))
                         # print(complex(f))
print(str(f))
print(bool(f))
print(list(f))
print(tuple(f))
print(set(f))
print(dict(f))
                         # in empty () we cant typecast to int, float, complex, 
                         # but we can typecast to str, bool, list, tuple,
                         #  set and dict.
                  
# -------------dict-----------------
d={1:'a',2:'b',3:'c'}
print(type(d))
                # print(int(d))
                # print(float(d))
print(bool(d))
                # print(complex(d))
print(str(d))
print(list(d))
print(tuple(d))
print(set(d))
print(dict(d))
                   # in dict we cant typecast to int, float, complex,
                   # but we can typecast to str, bool, list, tuple, set and dict.