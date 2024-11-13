#!/usr/bin/env python3

"""
Simple helper function
"""

import csv
import math
from typing import Tuple, List, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_page: returns the page range for a page

    page: the number of page
    page_size: the total page size agreed upon

    Return:
        tuple(int int): holding the range of index to return
    """
    return tuple(((page - 1) * page_size, page_size * page))


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes the Fake Server class
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """

        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        get_page: get a range of objects to view in page list

        Args:
            page: (int) the page number
            page_size: (int) the number of content per page

        Return:
            Nested list of all records in csv file
        """

        assert isinstance(page, int)
        assert isinstance(page_size, int)

        assert page > 0 and page_size > 0

        self.dataset()

        start_idx, end_idx = index_range(page, page_size)

        return self.__dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        get_hyper: gets a range of object to view in page list

        Args:
            page: (int) the page number
            page_size: (int) the number of content per page

        Return:
            Nested list of all records in csv file
        """
        response = {}

        datasets = self.get_page(page, page_size)
        total_size = len(self.__dataset)
        total_pages = math.ceil(total_size / page_size)

        response['page_size'] = len(datasets)
        response['page'] = page
        response['data'] = datasets
        response['next_page'] = (page + 1) if page < total_pages else None
        response['prev_page'] = (page - 1) if (page - 1) > 0 else None
        response['total_pages'] = total_pages

        return response
