"""
Private module for types used in toolz.

Everything defined here is considered private API, and may change at any time.
"""

from collections.abc import Hashable
from typing import Any, TypeVar, Union

from toolz._compatibility import Protocol, Self

# Basic TypeVars for any type.
T = TypeVar("T")
V = TypeVar("V")

# TypeVar for dictionary key types which must be hashable.
Key = TypeVar("Key", bound=Hashable)
KeyElement = TypeVar("KeyElement", bound=Hashable)

# TypeVar for any type which must be hashable.
T_Hashable = TypeVar("T_Hashable", bound=Hashable)


# TypeVars and Generic Protocol for types that supports __getitem__() with
# a particular type signature.
KeyType_contra = TypeVar("KeyType_contra", contravariant=True)
ValueType_co = TypeVar("ValueType_co", covariant=True)


class SupportGetItem(Protocol[KeyType_contra, ValueType_co]):
    def __getitem__(self: Self, __index: KeyType_contra) -> ValueType_co: ...


# Protocols for types that can be compared with < or >
class SupportsLT(Protocol):
    def __lt__(self, __other: Any) -> bool: ...


class SupportsGT(Protocol):
    def __gt__(self, __other: Any) -> bool: ...


SupportsComparison = Union[SupportsLT, SupportsGT]
SupportsComparisonT = TypeVar("SupportsComparisonT", bound=SupportsComparison)
