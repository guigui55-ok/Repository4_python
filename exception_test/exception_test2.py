
# from _typeshed import (
#     AnyStr_co,
#     FileDescriptorOrPath,
#     OpenBinaryMode,
#     OpenBinaryModeReading,
#     OpenBinaryModeUpdating,
#     OpenBinaryModeWriting,
#     OpenTextMode,
#     ReadableBuffer,
#     Self,
#     SupportsAdd,
#     SupportsAiter,
#     SupportsAnext,
#     SupportsDivMod,
#     SupportsIter,
#     SupportsKeysAndGetItem,
#     SupportsLenAndGetItem,
#     SupportsNext,
#     SupportsRAdd,
#     SupportsRDivMod,
#     SupportsRichComparison,
#     SupportsRichComparisonT,
#     SupportsTrunc,
#     SupportsWrite,
# )

# from typing import (  # noqa: Y022
#     IO,
#     Any,
#     BinaryIO,
#     ByteString,
#     ClassVar,
#     Generic,
#     Mapping,
#     MutableMapping,
#     MutableSequence,
#     NoReturn,
#     Protocol,
#     Sequence,
#     SupportsAbs,
#     SupportsBytes,
#     SupportsComplex,
#     SupportsFloat,
#     SupportsInt,
#     TypeVar,
#     overload,
#     type_check_only,
# )
# from types import CodeType, TracebackType, _Cell
# import sys

# class TestClassB:
#     args: tuple[Any, ...]
#     __cause__: BaseException | None
#     __context__: BaseException | None
#     __suppress_context__: bool
#     __traceback__: TracebackType | None
#     def __init__(self, *args: object) -> None: ...
#     def __setstate__(self, __state: dict[str, Any] | None) -> None: ...
#     def with_traceback(self: Self, __tb: TracebackType | None) -> Self: ...
#     if sys.version_info >= (3, 11):
#         # only present after add_note() is called
#         __notes__: list[str]
#         def add_note(self, __note: str) -> None: ...

from typing import (  # noqa: Y022
    IO,
    Any,
)
# from types import CodeType, TracebackType, _Cell
from types import CodeType, TracebackType

class TestClassB:
    args: tuple[Any, ...]
    __cause__: 'TestClassB' | None
    __context__: 'TestClassB' | None
    __suppress_context__: bool
    __traceback__: TracebackType | None
    def __init__(self, *args: object) -> None: ...
