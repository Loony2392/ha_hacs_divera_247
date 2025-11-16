"""Base implementation."""

from functools import lru_cache
from ipaddress import AddressValueError, IPv4Address, IPv6Address, NetmaskValueError
from typing import Optional, Union

from .backports.functools import cached_property


class CachedIPv4Address(IPv4Address):
    def __str__(self) -> str:
        """Return the string representation of the IPv4 address."""
        return self._str

    @cached_property
    def _str(self) -> str:
        """Return the string representation of the IPv4 address."""
        return super().__str__()

    @cached_property
    def is_link_local(self) -> bool:  # type: ignore[override]
        """Return True if this is a link-local address."""
        return super().is_link_local

    @cached_property
    def is_unspecified(self) -> bool:  # type: ignore[override]
        """Return True if this is an unspecified address."""
        return super().is_unspecified

    @cached_property
    def is_loopback(self) -> bool:  # type: ignore[override]
        """Return True if this is a loopback address."""
        return super().is_loopback

    @cached_property
    def is_multicast(self) -> bool:  # type: ignore[override]
        """Return True if this is a multicast address."""
        return super().is_multicast

    @cached_property
    def reverse_pointer(self) -> str:  # type: ignore[override]
        """Return the reverse DNS pointer name for the IPv4 address."""
        return super().reverse_pointer


class CachedIPv6Address(IPv6Address):
    def __str__(self) -> str:
        """Return the string representation of the IPv6 address."""
        return self._str

    @cached_property
    def _str(self) -> str:
        """Return the string representation of the IPv6 address."""
        return super().__str__()

    @cached_property
    def is_link_local(self) -> bool:  # type: ignore[override]
        """Return True if this is a link-local address."""
        return super().is_link_local

    @cached_property
    def is_unspecified(self) -> bool:  # type: ignore[override]
        """Return True if this is an unspecified address."""
        return super().is_unspecified

    @cached_property
    def is_loopback(self) -> bool:  # type: ignore[override]
        """Return True if this is a loopback address."""
        return super().is_loopback

    @cached_property
    def is_multicast(self) -> bool:  # type: ignore[override]
        """Return True if this is a multicast address."""
        return super().is_multicast

    @cached_property
    def reverse_pointer(self) -> str:  # type: ignore[override]
        """Return the reverse DNS pointer name for the IPv6 address."""
        return super().reverse_pointer


@lru_cache(maxsize=535)
def _cached_ip_addresses(
    address: Union[str, bytes, int]
) -> Optional[Union[IPv4Address, IPv6Address]]:
    """Cache IP addresses."""
    try:
        return CachedIPv4Address(address)
    except (AddressValueError, NetmaskValueError):
        pass

    try:
        return CachedIPv6Address(address)
    except (AddressValueError, NetmaskValueError):
        return None


cached_ip_addresses_wrapper = _cached_ip_addresses
cached_ip_addresses = cached_ip_addresses_wrapper

__all__ = ("cached_ip_addresses",)
