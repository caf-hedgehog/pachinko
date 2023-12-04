from common.data_fetch import get_html_data


class Fetch:
    async def run(self, target_url: str):
        return get_html_data(target_url)
