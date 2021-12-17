import os
import requests


class Request(object):
    def __init__(self):
        self.headers = {
                "user-agent": "shodan-angent",
                "content-type": "appliction/json"
        }

    def send_get(self, url):
        try:
            res = requests.get(url=url, headers=self.headers, timeout=5)
            if res.status_code == 200:
                return res.json()
            return None
        except requests.exceptions.RequestException:
            return None

    def send_post(self, url, post_data):
        try:
            res = requests.post(url=url, headers=self.headers, data=post_data, timeout=5)
            if res.status_code == 200:
                return res.json()
            return None
        except requests.exceptions.RequestException:
            return None


class ShodanClient(object):
    def __init__(self):
        self.api_key = os.getenv("SHODAN_API_KEY")
        self.base_url = "https://api.shodan.io"
        self.request = Request()

    def info(self):
        target_url = f"{self.base_url}/api-info?key={self.api_key}"
        return self.request.send_get(target_url)

    def search_host_from_ipaddress(self, ipaddress):
        target_url = f"{self.base_url}/shodan/host/{ipaddress}?key={self.api_key}"
        return self.request.send_get(target_url)

    def search_query_facets_count(self, query, facets):
        target_url = f"{self.base_url}/shodan/host/count?key={self.api_key}/&query={query}&facets={facets}"
        return self.request.send_get(target_url)

    def search_query_facets_search(self, query, facets):
        target_url = f"{self.base_url}/shodan/host/search?key={self.api_key}&query={query}&facets={facets}"
        return self.request.send_get(target_url)

