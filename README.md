
# Samay

Samay is a powerful Python module designed to help you effectively measure the execution time of your functions, compare them side by side, and optimize their performance. With Samay, you can gain valuable insights into the efficiency of your code and make informed decisions to improve its speed and effectiveness.


## Features

- Measure the execution time of a single function with ease.
- Compare multiple functions simultaneously and get accurate timing results.
- Highly customizable with options to adjust the number of loops for increased accuracy.
- Visualize results with interactive bar charts.

## Installation

Install Samay with pip

```bash
  pip install samay
```
Download [Samay](https://pypi.org/project/Samay/) from PyPI.

## Usage/Examples
Importing Samay
```python
from Samay.Samay import samay
```
Example array
```python
array = [x for x in range(1000)]
```
Assuming we have two or more functions.

Function Declaration - Linear Search
```python
def linearSearch(array, n, x):
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1
```
Function Declaration - Binary Search
```python
def binarySearch(array, x, low, high):
	while low <= high:
		mid = low + (high - low)//2
		if array[mid] == x:
			return mid
		elif array[mid] < x:
			low = mid + 1
		else:
			high = mid - 1
	return -1
```
Function Declaration - Interpolation Search
```python
def interpolationSearch(arr, lo, hi, x):
	if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
		pos = lo + ((hi - lo) // (arr[hi] - arr[lo]) *
					(x - arr[lo]))
		if arr[pos] == x:
			return pos
		if arr[pos] < x:
			return interpolationSearch(arr, pos + 1,hi, x)
		if arr[pos] > x:
			return interpolationSearch(arr, lo,pos - 1, x)
	return -1
```
Getting execution time of single function.

Example - Linear Search
```python
linear_Search = Samay(
                  func=linearSearch,
                  function_name="Linear Search", 
                  args=(array, 999, 525)
                  )

```
**_NOTE_** : Giving value to function_name is optional.
```python
exe_time = linearS_earch.get_exe_time(loops=100)
```
```python
print(exe_time)
```

## Result
```python
0.003091573715209961
```

**_NOTE_** : Increase the number of loops to increase accuracy, default numbers of loops is 10.

Testing two or more functions at once using Samay_Bulk class.
```python
data = [
	(linearSearch, "Linear Search",(array, 999, 525)),
	(binarySearch, "Binary Search",(array,525, 0, 999)),
	(interpolationSearch,"Interpolation Search", (array, 0, 999, 525)),
]
```
```python
result = Samay_Bulk(data)
```
```python
result.test_bulk(10000)
```
```python
print(result.result)
```
## Result
```python
{'Linear Search': 0.16191744804382324, 'Binary Search': 0.015738725662231445, 'Interpolation Search': 0.005555152893066406}
```
## Visualizing the result
```python
result.bar_chart()
```
## Result
![Bar Chart](https://github.com/saurav-2k01/Samay/blob/master/Example_test.png)

**_NOTE_**: Any function can be tested, as Samay is not limited to only searching algorithms.
## Feedback
if you have any feedback, please reach out to me at sv19projects@gmail.com

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

- [@saurav-2k01](https://github.com/saurav-2k01)

## License
Samay is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Get Started with Samay

Start optimizing your code and gaining insights into your function's performance today. Install Samay, measure execution times, compare different approaches, and unlock the full potential of your Python projects.

    "Time is of the essence. Measure it with Samay."
