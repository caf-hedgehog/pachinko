from common.data_fetch import data_fetch
import logging
import sys


class Fetch:
    async def run(self):
        return data_fetch(
            "https://papimo.jp/h/00031715/hit/index_sort/122070007/0-4-642013"
        )
