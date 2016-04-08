import pytest
import alg_binary_search as binary_search

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

