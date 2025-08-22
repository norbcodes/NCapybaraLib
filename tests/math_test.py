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

from src.NCapybaraLib.Math import *

def test_get_xy_in_2d_grid():
    assert get_xy_in_2d_array(0, 8) == (0, 0)
    assert get_xy_in_2d_array(8, 8) == (0, 1)
    assert get_xy_in_2d_array(9, 8) == (1, 1)

def test_get_pos_in_2d_grid():
    assert get_index_in_2d_array(0, 0, 8) == 0
    assert get_index_in_2d_array(0, 1, 8) == 8
    assert get_index_in_2d_array(0, 2, 8) == 16
    assert get_index_in_2d_array(8, 1, 8) == 16

def test_tetra():
    assert tetration(1, 1) == 1
    assert tetration(1, 2) == 1
    assert tetration(1, 3) == 1
    assert tetration(2, 1) == 2
    assert tetration(2, 2) == 4
    assert tetration(2, 3) == 16
    assert tetration(3, 1) == 3
    assert tetration(3, 2) == 27
    assert tetration(3, 3) == 7625597484987
    assert tetration(4, 1) == 4
    assert tetration(4, 2) == 256
    assert tetration(4, 3) == 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096

def test_clamp():
    assert clamp(5, 1, 6) == 5
    assert clamp(0, 1, 6) == 1
    assert clamp(8, 1, 6) == 6

def test_range_scale():
    assert range_scale(5, 1, 10, 10, 100) == 50
    assert range_scale(0.5, 0, 1, 0, 10) == 5
    assert range_scale(0.5, 0, 1, 1, 2) == 1.5
    assert range_scale(1, 1, 2, 2, 4) == 2.0
    assert range_scale(1, 0, 10, 0, 100) == 10

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