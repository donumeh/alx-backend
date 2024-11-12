#!/usr/bin/env python3

"""
Simple helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_page: returns the page range for a page

    page: the number of page
    page_size: the total page size agreed upon

    Return:
        tuple(int int): holding the range of index to return
    """
    return tuple(((page - 1) * page_size, page_size * page))


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
