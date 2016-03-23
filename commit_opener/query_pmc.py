# Query PMC
# README
# Just pass a search string - will return a dictionary
#   hits: number of hits
#   citations: a dataframe of the first n hits with weights
#       for the number of times they have been cited
# - [ ] TODO(2016-03-23): returns 1st 1000 only

import pandas as pd
import json
import requests
import collections

def pmc_query(_query, _type="profile", _format="json", _page_size=10):
    # References
    # API https://europepmc.org/RestfulWebService#search
    # Search tags https://europepmc.org/Help#directsearch
    # Construct query string
    _europmc = "http://www.ebi.ac.uk/europepmc/webservices/rest"
    _search = "/search?query="
    _profile = "/profile?query="
    _format = "&format=json"
    if _type == "profile":
        _url = _europmc + _profile + _query + _format
    elif _type == "search":
        _url = _europmc + _search + _query + _format + "&pageSize=" + str(_page_size)
    else:
        print("_type not one of 'search' or 'profile'")
        return
    resp = requests.get(_url)
    return resp.json()


def pmc_field_filter(_pmc_response, _fields=['id', 'pubYear', 'citedByCount']):
    # Extract the results from the search (needs to be passed a search not a profile object)
    _pmc_dict = _pmc_response["resultList"]["result"]
    def _filter(_dict, _fields=_fields):
        _filtered = dict(((k, v) for k, v in _dict.items() if k in _fields))
        return _filtered
    _pmc_filtered  = [_filter(i) for i in _pmc_dict]
    return _pmc_filtered

def dict_to_df(_dict):
    # Convert list of dictionaries to dict of lists
    result = collections.defaultdict(list)
    for d in _dict:
        for k, v in d.items():
            result[k].append(v)
    return pd.DataFrame(result)

def pmc_data(_search_string, _page_size=10):
    resp = pmc_query(_search_string, _type="search", _page_size=_page_size)
    # resp = pmc_query(_search_string, _type="search")
    pmc_hits = resp["hitCount"]
    pmc_citations = pmc_field_filter(resp)
    pmc_citations = dict_to_df(pmc_citations)
    return {"hits":pmc_hits, "citations":pmc_citations}


