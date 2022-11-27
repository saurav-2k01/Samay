
# Samay

Samay is a python module, that can help to get execution time of a function, or can be used to compare two different function at the same time with respect to time.




## Usage/Examples
Creating object
```python
from Samay import samay
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
<<<<<<< HEAD
=======

>>>>>>> a05c43f704a9349017625c06a3232291161465b4
Setting loop
```python
S1.loop = 100
S2.loop = 100
```
<<<<<<< HEAD
**_NOTE_** : Increase the numbers of loops to increase accuracy. 
=======
**_NOTE_** : Increase the number of loops to increase accuracy.
>>>>>>> a05c43f704a9349017625c06a3232291161465b4

Comparing two functions with respect to time
```python
Result = S1.compare_function(S2)
```

## Authors

- [@saurav-2k01](https://github.com/saurav-2k01)

