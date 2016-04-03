###Python testing

Recently I was implementing a binary search algorithm from its description. Here it is:

```
# Attempt to implement the binary search

def search(n, arr):
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = int(lo + (hi - lo) / 2)
        if n < arr[mid]:
            hi = mid - 1
        elif n > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
```

Ok, now it is time to test it.

```
import pytest
from search import binary_search

bin_search = [3, 15, 33, 45, 89, 122, 192]

def test_bs_low():
    assert binary_search.search(3, bin_search) == 0

def test_bs_low_non_existent():
    assert binary_search.search(1, bin_search) == -1

def test_bs_mid():
    assert binary_search.search(45, bin_search) == 3

def test_bs_mid_non_existent():
    assert binary_search.search(48, bin_search) == -1

def test_bs_mid_hi():
    assert binary_search.search(122, bin_search) == 5

def test_bs_hi():
    assert binary_search.search(192, bin_search) == len(bin_search) - 1

def test_bs_hi_non_existent():
    assert binary_search.search(200, bin_search) == -1
```

Execute `py.test`

```
============================= test session starts ==============================
platform darwin -- Python 3.5.1, pytest-2.9.0, py-1.4.31, pluggy-0.3.1
rootdir: /Users/pvlbzn/Dropbox/d_src/py/algorithm, inifile: 
collected 7 items 

tests/test_search.py .......

=========================== 7 passed in 0.05 seconds ===========================
```

Ok, we cool. This approach I took from [flask tests](https://github.com/pallets/flask/tree/master/tests) because it's clean. Always remember about `__init__.py` if you want to test something as module.



TODO: Read [this](http://docs.python-guide.org/en/latest/writing/tests/).



