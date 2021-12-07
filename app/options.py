import argparse


def options():
    parser = argparse.ArgumentParser(usage="python3 shodan [options]", add_help=False)

    api_info = parser.add_argument_group("info", "shodan api information")
    api_info.add_argument("I", dest="inf", help="show shoan api information")

    search = parser.add_argument_group("search", "search xxx from shodan engine.")
    # /shodan/host/ip
    search.add_argument("D", dest="domain", help="provider a domain or hostname address.")

    # /shodan/host/count
    search.add_argument("q", dest="query", help="provider a query string")
    search.add_argument("f", dest="facets", help="provider a facets string")

    # /shodan/host/search
    search.add_argument("Q", dest="Query", help="provider a Query string.")
    search.add_argument("F", dest="Facets", help="provider a Facets string.")

    return parser.parse_args()
