from src.util.struct_stream import StructStream
from typing import Any, BinaryIO


class int8(int, StructStream):
    PACK = "!b"


class uint8(int, StructStream):
    PACK = "!B"


class int16(int, StructStream):
    PACK = "!h"


class uint16(int, StructStream):
    PACK = "!H"


class int32(int, StructStream):
    PACK = "!l"


class uint32(int, StructStream):
    PACK = "!L"


class int64(int, StructStream):
    PACK = "!q"


class uint64(int, StructStream):
    PACK = "!Q"


class uint1024(int):
    @classmethod
    def parse(cls, f: BinaryIO) -> Any:
        return cls(int.from_bytes(f.read(128), "big"))

    def stream(self, f):
        f.write(self.to_bytes(128, "big"))