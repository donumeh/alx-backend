#!/usr/bin/env python3

"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """

        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                    i: dataset[1] for i in range(len(dataset))
                    }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        get_hyper_index: the the indexed result of a dataset
        and print it out

        Args:
            index: the index to start printing from
            page_size: the total items on a page
        """

        assert 0 <= index < len(self.indexed_dataset())

        data = []
        current_index = index
        collected = 0

        while collected < page_size and
        current_index < len(self.__indexed_dataset):
            if current_index in self.__indexed_dataset:
                data.append(self.__indexed_dataset[current_index])
                collected += 1
            current_index += 1

        next_index = (
            current_index
            if current_index < len(self.__indexed_dataset) else None
        )

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
