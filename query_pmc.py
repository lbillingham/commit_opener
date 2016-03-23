# Query PMC

def pmc_query(_query, _type="profile", _format="json"):
    # References
    # API https://europepmc.org/RestfulWebService#search
    # Search tags https://europepmc.org/Help#directsearch
    import requests
    # Construct query string
    _europmc = "http://www.ebi.ac.uk/europepmc/webservices/rest"
    _search = "/search?query="
    _profile = "/profile?query="
    _format = "&format=json"

    if _type == "profile":
        _url = _europmc + _profile + _query + _format
    elif _type == "search":
        _url = _europmc + _search + _query + _format
    else:
        print("_type not one of 'search' or 'profile'")
        return

    resp = requests.get(_url)
    return resp

# full text search (AND combination)
# resp = pmc_query("ghorashian harris", _type="search")

# example of tagged search
# resp = pmc_query("auth:ghorashian")

# example of AND search with tags
# resp = pmc_query("auth:ghorashian pub_year:2010")

# resp = pmc_query("ghorashian harris", _type="profile")
# print resp.text.encode('ascii', 'ignore')


