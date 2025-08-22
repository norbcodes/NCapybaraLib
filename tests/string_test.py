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

from src.NCapybaraLib.String import *

# ---------- insert ----------

def test_insert_middle():
    assert insert("hello", "X", 2) == "heXllo"

def test_insert_start():
    assert insert("world", "X", 0) == "Xworld"

def test_insert_end():
    assert insert("abc", "XYZ", 10) == "abcXYZ"

def test_insert_empty_string():
    assert insert("", "foo", 0) == "foo"

# ---------- string_similarity ----------

def test_string_similarity_exact_match():
    assert string_similarity("hello", "hello") == 1.0

def test_string_similarity_case_insensitive():
    # case sensitive → mismatch
    assert string_similarity("Hello", "hello", case_sensitivity=True) < 1.0
    # case insensitive → match
    assert string_similarity("Hello", "hello", case_sensitivity=False) == 1.0

def test_string_similarity_partial_match():
    score = string_similarity("hello", "hEllo", case_sensitivity=True)
    assert 0 < score < 1

def test_string_similarity_rounding():
    score = string_similarity("abc", "axc", case_sensitivity=True, round_output=2)
    assert isinstance(score, float)
    assert round(score, 2) == score

def test_string_similarity_list_input():
    results = string_similarity("hello", ["hello", "world"], case_sensitivity=False)
    assert isinstance(results, list)
    assert results[0] == 1.0
    assert all(0 <= r <= 1 for r in results)

# ---------- is_palindrome ----------

def test_is_palindrome_simple():
    assert is_palindrome("racecar")
    assert not is_palindrome("python")

def test_is_palindrome_with_spaces():
    assert is_palindrome("a toyota", also_spaces=False)  # ignore spaces
    assert not is_palindrome("a toyota", also_spaces=True)

def test_is_palindrome_case_sensitivity():
    assert is_palindrome("RaceCar", case_sensitive=False)
    assert not is_palindrome("RaceCar", case_sensitive=True)

def test_is_palindrome_ignore_non_letters():
    assert is_palindrome("do geese see god?", ignore_non_letters=True)
    assert not is_palindrome("do geese see god?", ignore_non_letters=False)

def test_is_palindrome_numbers_allowed():
    assert is_palindrome("12321")
    assert not is_palindrome("123421")

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