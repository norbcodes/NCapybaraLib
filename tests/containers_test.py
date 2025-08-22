# MIT License
#
# Copyright (c) 2024 NorbCodes (a.k.a norb3695 or Norb)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import pytest
from src.NCapybaraLib.Containers import *

# ---------- map_inputs ----------

def test_map_inputs_basic_mapping():
    keys = ["a", "b", "c", "d"]
    vals = [1, 2]
    result = map_inputs(keys, vals)
    assert set(result.keys()) == set(keys)
    assert all(v in vals for v in result.values())

def test_map_inputs_single_value():
    keys = ["x", "y", "z"]
    vals = [99]
    result = map_inputs(keys, vals)
    assert result == {"x": 99, "y": 99, "z": 99}

def test_map_inputs_more_values_than_keys_raises():
    with pytest.raises(Exception):
        map_inputs(["a"], [1, 2])

def test_map_inputs_empty_list_raises():
    with pytest.raises(ValueError):
        map_inputs([], [1])
    with pytest.raises(ValueError):
        map_inputs(["a"], [])

def test_map_inputs_odd_lengths():
    keys = ["a", "b", "c"]
    vals = [1, 2, 3]
    result = map_inputs(keys, vals)
    assert isinstance(result, dict)
    assert set(result.keys()) == set(keys)

# ---------- contains ----------

def test_contains_in_single_container():
    assert contains(3, [1, 2, 3])
    assert not contains(4, [1, 2, 3])

def test_contains_in_strings():
    assert not contains("x", ["abc", "xyz"])
    assert not contains("x", ["abc", "yz"])

# ---------- not_contains ----------

def test_not_contains_in_single_container():
    assert not_contains(4, [1, 2, 3])
    assert not not_contains(3, [1, 2, 3])

def test_not_contains_in_multiple_containers():
    assert not_contains("q", ["abc", "xyz"])
    assert not not_contains("a", ["abc", "xyz"])

# ---------- clean ----------

def test_clean_list():
    arr = ["a", "", "b", ""]
    assert clean(arr) == ["a", "b"]

def test_clean_tuple():
    arr = ("", "foo", "", "bar")
    assert clean(arr) == ("foo", "bar")

def test_clean_set():
    arr = {"", "hello", ""}
    result = clean(arr)
    assert result == {"hello"}

def test_clean_dict():
    arr = {"a": "x", "b": "", "": "y"}
    result = clean(arr)
    assert result == {"a": "x"}

def test_clean_unknown_type_returns_none():
    class Dummy: pass
    assert clean(Dummy()) is None

# MIT License
#
# Copyright (c) 2024 NorbCodes (a.k.a norb3695 or Norb)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.