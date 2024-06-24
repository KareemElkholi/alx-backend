#!/usr/bin/env python3
"""3. Deletion-resilient hypermedia pagination"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return dictionary"""
        indexed_dataset = self.indexed_dataset()
        index = index if index else 0
        assert index >= 0 and index <= list(indexed_dataset.keys())[-1]
        keys = []
        [keys.append(i) for i in indexed_dataset.keys()
         if i >= index and len(keys) <= page_size]
        data = [indexed_dataset[i] for i in keys[:-1]]
        return {"index": index, "data": data, "page_size": len(data),
                "next_index": keys[-1] if len(keys) > page_size else None}
