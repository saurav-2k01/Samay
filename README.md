
# Samay

Samay is a python module, that can help to get execution time of a function, or can be used to compare two different function at the same time with respect to time.




## Usage/Examples
Creating object
```python
import samay from Samay
def func1(a, b):
    pass

S1 = samay(func=func1, args=(a,b,))

```
Getting execution time of a function
```python
exe_time = S1.get_exe_time()

```
Creating another object
```python
def func2(x, y):
    pass

S2 = samay(func=func2, args=(x,y,))

```
Setting Object name 

```python
S1.object_name = "object1"
S2.object_name = "object2"
```
Setting loop
```python
S1.loop = 100
S2.loop = 100
```
Comparing two functions with respect to time
```python
Result = S1.compare_function(S2)
```

## Authors

- [@saurav-2k01](https://github.com/saurav-2k01)
