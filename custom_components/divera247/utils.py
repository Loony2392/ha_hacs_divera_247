"""Utils Module for Divera 24/7 Integration."""

from __future__ import annotations

from yarl import URL


def remove_params_from_url(url: URL | str | None) -> str:
    """
    Remove parameters from a URL.

    The query string carries the Divera accesskey, so it must never reach the
    logs. Stripping it must not raise either, because this runs inside
    exception handlers.

    Args:
        url (URL | str | None): The URL from which parameters need to be removed.

    Returns:
        str: URL without the parameters part, or "unknown" if it cannot be parsed.
    """
    if url is None:
        return "unknown"
    try:
        return URL(url).with_query(None).human_repr()
    except (TypeError, ValueError):
        return "unknown"
