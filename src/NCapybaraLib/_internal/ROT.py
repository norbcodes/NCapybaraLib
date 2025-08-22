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

"""
NCapybaraLib; By NorbCodes.

Submodule for ROT13 and ROT-N.

https://pypi.org/project/NCapybaraLib/
"""

def Rot13(string: str | bytes, format: str = "utf-8") -> str | bytes:
    """
    Uses the ROT13 "encryption" algorithm on the specified string.
    If string is a `str` it does .encode() and .decode() for you.
    This is the classic implementation of the ROT13 algo, which only shifts letters across the alphabet.

    :param string: String to "encrypt".
    :param format: Format option to pass into .encode() and .decode() str methods. Defaults to "utf-8".
    :return: "Encrypted" string.
    """
    if isinstance(string, bytes):
        out = []
        for char in string:
            if 65 <= char <= 90:
                # Uppercase letter range
                char -= 65
                out.append( (char + 13) % 26 + 65 )
            elif 97 <= char <= 122:
                # Lowercase letter range
                char -= 97
                out.append((char + 13) % 26 + 97)
            else:
                out.append(char)
        return bytes(out)
    else:
        out = []
        for char in string.encode("utf-8"):
            if 65 <= char <= 90:
                # Uppercase letter range
                char -= 65
                out.append((char + 13) % 26 + 65)
            elif 97 <= char <= 122:
                # Lowercase letter range
                char -= 97
                out.append((char + 13) % 26 + 97)
            else:
                out.append(char)
        return bytes(out).decode(format)

def FullRot13(string: str | bytes, format: str = "utf-8") -> bytes:
    """
    Uses the ROT13 "encryption" algorithm on the specified string.
    If string is a `str` it does .encode() for you.
    This one shifts across the whole byte range, therefore it can only return `bytes` object.

    :param string: String to "encrypt".
    :param format: Format option to pass into .encode() str method. Defaults to "utf-8".
    :return: "Encrypted" string.
    """
    if isinstance(string, bytes):
        return bytes( [(b + 13) % 256 for b in string] )
    else:
        return bytes( [(b + 13) % 256 for b in string.encode(format)] )

def RotN(string: str | bytes, n: int, format: str = "utf-8") -> str | bytes:
    """
    Uses the ROT13 "encryption" algorithm on the specified string, with user specified rotation amount.
    If string is a `str` it does .encode() and .decode() for you.
    This is the classic implementation of the ROT13 algo, which only shifts letters across the alphabet.

    :param string: String to "encrypt".
    :param n: Rotation amount.
    :param format: Format option to pass into .encode() and .decode() str methods. Defaults to "utf-8".
    :return: "Encrypted" string.
    """
    if isinstance(string, bytes):
        out = []
        for char in string:
            if 65 <= char <= 90:
                # Uppercase letter range
                char -= 65
                out.append( (char + n) % 26 + 65 )
            elif 97 <= char <= 122:
                # Lowercase letter range
                char -= 97
                out.append((char + n) % 26 + 97)
            else:
                out.append(char)
        return bytes(out)
    else:
        out = []
        for char in string.encode("utf-8"):
            if 65 <= char <= 90:
                # Uppercase letter range
                char -= 65
                out.append((char + n) % 26 + 65)
            elif 97 <= char <= 122:
                # Lowercase letter range
                char -= 97
                out.append((char + n) % 26 + 97)
            else:
                out.append(char)
        return bytes(out).decode(format)

def FullRotN(string: str | bytes, n: int, format: str = "utf-8") -> bytes:
    """
    Uses the ROT13 "encryption" algorithm on the specified string, with user specified rotation amount.
    If string is a `str` it does .encode() for you.
    This one shifts across the whole byte range, therefore it can only return `bytes` object.

    :param string: String to "encrypt".
    :param n: Rotation amount.
    :param format: Format option to pass into .encode() str method. Defaults to "utf-8".
    :return: "Encrypted" string.
    """
    if isinstance(string, bytes):
        return bytes( [(b + n) % 256 for b in string] )
    else:
        return bytes( [(b + n) % 256 for b in string.encode(format)] )

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