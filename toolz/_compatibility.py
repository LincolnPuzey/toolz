"""
Private module for managing compatibility across python versions.

Everything defined here is considered private API, and may change at any time.
"""

__all__ = (
    "Collection",
    "Dict",
    "Iterable",
    "Iterator",
    "List",
    "Literal",
    "Protocol",
    "Self",
    "Tuple",
)

import sys

if sys.version_info >= (3, 8):
    from typing import Literal, Protocol
else:
    from typing_extensions import Literal, Protocol


if sys.version_info >= (3, 9):
    from collections.abc import Collection, Iterable, Iterator
    Dict = dict
    List = list
    Tuple = tuple
else:
    from typing import Collection, Iterable, Iterator, Dict, List, Tuple


if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self
