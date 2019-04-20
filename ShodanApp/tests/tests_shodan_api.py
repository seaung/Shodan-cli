import json
import shodan

from ShodanApp.config.security import SHODAN_API_KEY

def main():
    api = shodan.Shodan(SHODAN_API_KEY)


    try:
        results = api.search('nginx')
        print('\n')
        print(f'found {results["total"]}')
        print('\n')
        for result in results["matches"]:
            ip = result['ip_str']
            data = result['data']
            res = dict(ip=ip, data=data)
            print(f'res => {res}')

    except shodan.APIError as e:
        print(f'error => {e}')

if __name__ == '__main__':
    main()