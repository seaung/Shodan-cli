import os
import requests


class ShodanClient(object):
    def __init__(self):
        self.api_key = os.getenv("SHODAN_API_KEY")
        self.base_url = "https://api.shodan.io"

    def search_host_from_ipaddress(self, ipaddress):
        target_url = f"{self.base_url}/shodan/host/{ipaddress}?key={self.api_key}"
        return requests.get(url=target_url)

    def search_query_facets_count(self, query, facets):
        target_url = f"{self.base_url}/shodan/host/count?key={self.api_key}/&query={query}&facets={facets}"
        return requests.get(url=target_url)

    def search_query_facets_search(self, query, facets):
        target_url = f"{self.base_url}/shodan/host/search?key={self.api_key}&query={query}&facets={facets}"
        return requests.get(url=target_url)
