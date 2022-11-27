from Samay import samay

def func1(a, b):
    return a+b

def func2(x, y):
    return x**y**x


s1 = samay(func=func1, args=(2,3,))
s2 = samay(func=func2, args=(5,5,))
s1.object_name = "function 1"
s2.object_name = "function 2"
s1.loop = 100
s2.loop = 100


print(s1.get_exe_time())

print(s2.get_exe_time())
print(s1.compare_function(s2))