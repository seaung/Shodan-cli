import shodan
from webapp.secure import SHODAN_API_KEY
from webapp.utils.ip import is_ip


class ShodanApi(object):
    def __init__(self):
        self.api_key = SHODAN_API_KEY
        self.api = shodan.Shodan(self.api_key)

    @staticmethod
    def is_host_or_ip(keyword):
        if is_ip(keyword):
            self._search_host_by_ip(keyword)
        else:
            self._search_host_by_name(keyword)

    def _search_host_by_name(self, keyword):
        try:
            results = []
            hosts = self.api.search(keyword)
            total = hosts['total']
            results.append(total)

            for host in hosts['matches']:
                results.append({"IP": host["ip_str"], "data": host["data"]})
            return results
        except shodan.APIError:
            data = "Not Found"
            return data

    def _search_host_by_ip(self, keywrod):
        try:
            results = []
            hosts = self.api.host(keyword)
            results.append({"IP": hosts["ip_str"], "Organization": hosts.get("org", "n/a"), "system": hosts.get("os", "n/a")})

            for item in hosts["data"]:
                results.append({"PORT": item["port"], "BANNER": item["data"]})
            return results
        except shodan.APIError:
            data = "Not Found."
            return data

