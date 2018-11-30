import shodan
from webapp.secure import SHODAN_API_KEY
from webapp.utils.ip import is_ip


class ShodanApi(object):
    def __init__(self):
        self.api_key = SHODAN_API_KEY
        self.api = shodan.Shodan(self.api_key)

    @staticmethod
    def search_by_ip(keyword):
        try:
            results = self.api.host(keyword)
            return results
        except shodan.APIError as e:
            print("api error")
            return None

    @staticmethod
    def search_by_host(keyword):
        try:
            results = self.api.search(keyword)
            matches = []
            for result in results['matches']:
                matches.append(result)
            return matches
        except shodan.APIError as e:
            print("")
            return None
