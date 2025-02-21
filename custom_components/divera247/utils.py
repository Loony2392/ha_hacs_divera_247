"""Utils Module for Divera 24/7 Integration."""

from yarl import URL


def remove_params_from_url(url: URL) -> str:
    """
    Remove parameters from a URL.

    Args:
        url (URL): The URL from which parameters need to be removed.

    Returns:
        str: URL without the parameters part.
    """
    url.with_query()
    url_str: str = url.human_repr()
    return url_str
