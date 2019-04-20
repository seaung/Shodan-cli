import shodan

from ShodanApp.config.security import SHODAN_API_KEY


class MShodan(object):
    def __init__(self):
        self.api_key = SHODAN_API_KEY
        self.shodan_api = shodan.Shodan(self.api_key)

    def look_up_a_host(self, keyword):
        try:
            information = {}
            host = self.shodan_api.host(keyword)
            information['IP'] = host['ip_str']
            information['org'] = host.get('org', 'n/a')
            information['os'] = host.get('os', 'n/a')
            information['banner'] = host['data']
            return information
        except shodan.exception.APITimeout as e:
            print(f'exception info => {e}')
            return None

    def searching_shodan(self, keyword):
        try:
            information = {}

            items = self.shodan_api.search(keyword)

            information['total'] = items['total']

            for item in items['matches']:
                information['ip'] = item['ip_str']
                information['data'] = item['data']

            return information
        except shodan.exception.APIError as e:
            print(f'api exception error => {e}')
            return None