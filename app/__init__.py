from app.client.shodan import ShodanClient


class Runner(object):
    def __init__(self):
        self.shodan = ShodanClient()

    def start(self, options):
        if options.inf:
            pass

        if options.domain:
            self.shodan.search_host_from_ipaddress(options.domain)

        if options.query is not None and options.facets is not None:
            self.shodan.search_query_facets_count(options.query, options.facets)

        if options.Query is not None and options.Facets is not None:
            self.shodan.search_query_facets_search(options.Query, options.Facets)

