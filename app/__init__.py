from app.client.shodan import ShodanClient


class Runner(object):
    def __init__(self):
        self.shodan = ShodanClient()

    def start(self, options):
        if (options.inf and options.domain and options.query and options.query and options.facets and options.Query and
                options.Facets) is None:
            print("[!] please select options !")
            return

        if options.inf is not None and options.inf == "show":
            self.shodan.info()
        else:
            print("[!] To see the API information, set the value of the -I/-Inf option to show")

        if options.domain is not None:
            self.shodan.search_host_from_ipaddress(options.domain)
        else:
            print("[!] provided a target domain please !")

        if options.query is not None and options.facets is not None:
            self.shodan.search_query_facets_count(options.query, options.facets)
        else:
            print("[!] Two parameters, -q/-query and -f/facets, must be provided")

        if options.Query is not None and options.Facets is not None:
            self.shodan.search_query_facets_search(options.Query, options.Facets)
        else:
            print("[!] Two parameters, -Q/-Query and -F/-Facets, must be provided")

