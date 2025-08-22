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

from src.NCapybaraLib.ROT import *

def test_rot13_roundtrip():
    text = "Hello, World!"
    encrypted = Rot13(text)
    decrypted = Rot13(encrypted)
    assert decrypted == text

def test_full_rot13():
    data = b"\x00\x7f\xffABCxyz"
    encrypted = FullRot13(data)
    encrypted2 = FullRotN(FullRotN(data, 7), 6)
    assert encrypted == encrypted2

def test_rot_n_roundtrip():
    text = "Hello, World!"
    encrypted = RotN(text, 13)
    decrypted = RotN(encrypted, 13)
    assert decrypted == text

def test_full_rot_n_roundtrip():
    data = b"\x00\x7f\xffABCxyz"
    encrypted = FullRotN(data, 100)
    decrypted = FullRotN(encrypted, 156)  # 100 + 156 = 256 mod 256
    assert decrypted == data

def test_rot13_known_values():
    assert Rot13("Hello") == "Uryyb"
    assert Rot13("Uryyb") == "Hello"
    assert Rot13(b"abcXYZ") == b"nopKLM"

def test_rot_n_custom_rotation():
    assert RotN("abc", 1) == "bcd"
    assert RotN("xyz", 3) == "abc"
    assert RotN(b"XYZ", 2) == b"ZAB"

def test_full_rot_n_custom_rotation():
    assert FullRotN(b"\x00\x01\x02", 1) == b"\x01\x02\x03"
    assert FullRotN(b"\xff", 1) == b"\x00"
    result = FullRotN("abc", 2)
    assert isinstance(result, bytes)
    assert result == b"cde"

def test_non_alpha_characters_unchanged():
    text = "1234!@#$"
    assert Rot13(text) == text
    assert RotN(text, 5) == text

def test_str_and_bytes_equivalence():
    text = "Python3!"
    assert Rot13(text) == Rot13(text.encode()).decode()
    assert RotN(text, 7) == RotN(text.encode(), 7).decode()

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