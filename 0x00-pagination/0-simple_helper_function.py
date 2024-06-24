#!/usr/bin/env python3
"""0. Simple helper function"""


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index"""
    end = page * page_size
    return (end - page_size, end)
