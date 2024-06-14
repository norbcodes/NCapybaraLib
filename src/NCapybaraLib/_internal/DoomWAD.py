"""
NCapybaraLib; By NorbCodes.

A submodule for Doom WAD operations.

https://pypi.org/project/NCapybaraLib/
"""

from os import PathLike
from typing import Literal, Iterator

def is_pwad(filepath: str | PathLike[str]) -> bool:
    """
    Check if the given WAD is a *patch wad*.

    :param filepath: The path to the file.
    :return: True if the given WAD is a PWAD.
    """
    with open(filepath, "rb") as target:
        return target.read(4) == b"PWAD"

def is_iwad(filepath: str | PathLike[str]) -> bool:
    """
    Check if the given WAD is an *internal wad*.

    :param filepath: The path to the file.
    :return: True if the given WAD is a IWAD.
    """
    with open(filepath, "rb") as target:
        return target.read(4) == b"IWAD"

def is_pwad_bytes(b: bytes) -> bool:
    """
    Check if the bytes belong to a *patch wad*.

    :param b: The bytes of the WAD.
    :return: True if the given WAD is a PWAD.
    """
    return b[0:4:1] == b"PWAD"

def is_iwad_bytes(b: bytes) -> bool:
    """
    Check if the bytes belong to an *internal wad*.

    :param b: The bytes of the WAD.
    :return: True if the given WAD is a IWAD.
    """
    return b[0:4:1] == b"IWAD"

class Lump:
    """
    Lump object.
    """
    name: str
    data: bytes

class WAD:
    """
    Doom WAD object by NCapybaraLib.

    For WAD manipulation or reading and analyzing.
    """
    # Header
    _type: Literal["IWAD", "PWAD"]
    _num_lumps: int
    _info_table_offset: int
    _filepath: str | PathLike[str]

    def __init__(self, filepath: str | PathLike[str]) -> None:
        """
        Read the WAD.

        :param filepath: The path to the WAD file.
        """
        self._filepath = filepath
        with open(filepath, "rb") as wad:
            self._type = "IWAD" if is_iwad_bytes(wad.read(4)) else "PWAD"
            self._num_lumps = int.from_bytes(wad.read(4), byteorder="little")  # according to doomwiki, it's little endian
            self._info_table_offset = int.from_bytes(wad.read(4), byteorder="little")

    def get_type(self) -> Literal["IWAD", "PWAD"]:
        """
        :return: The type of the WAD.
        """
        return self._type

    def get_lump_count(self) -> int:
        """
        :return: The amount of lumps in the WAD.
        """
        return self._num_lumps

    def get_lump_at(self, pos: int) -> Lump | None:
        """
        Get the *x*-th lump in the WAD.

        :param pos: The lump index.
        :return: The lump object, or returns None if the lump has 0 size.
        """
        # Find it in the directory
        _pos = self._info_table_offset + pos * 16
        # Directory entry is 16 bytes big
        with open(self._filepath, "rb") as wad:
            wad.seek(_pos)
            _where = int.from_bytes(wad.read(4), byteorder="little")
            _size = int.from_bytes(wad.read(4), byteorder="little")
            # If the lump is 0 size:
            if _size == 0:
                return None
            _name = wad.read(8).decode("ASCII")
            # Ok now do stuff
            _lump = Lump()
            _lump.name = _name
            wad.seek(_where)
            _lump.data = wad.read(_size)
            return _lump

    def get_lumps(self, limit: int = 0) -> Iterator[Lump | None]:
        """
        Read *all* lumps. >:)

        :param limit: Limit to how many lumps to read. 0 means all.
        :return: The lumps.
        """
        if limit == 0:
            limit = self._num_lumps
        for index in range(limit):
            yield self.get_lump_at(index)