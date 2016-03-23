from pytest import fixture

@fixture(scope='module')
def working_dir():
    return "git@github.com:Turbo87/utm"


@fixture(scope='module')
def authors(working_dir):
    from commit_opener.tree_scrape import author_minded
    return author_minded(working_dir)


def test_basic_author_minded(authors):
    assert 'unknown' in authors.index
    assert 'Tobias Bieniek' in authors.index

    assert authors.loc['Tobias Bieniek', 'first'] < authors.loc['Tobias Bieniek', 'last']
    assert all(authors.line_changes <= 1)
    assert all(authors.line_changes >= 0)
    assert all(authors.commits <= 1)
    assert all(authors.commits >= 0)


def test_frequencies(authors):
    from numpy import timedelta64
    from pandas import isnull
    assert authors.loc['Tobias Bieniek', 'max_dry_stretch'] == timedelta64(374, 'D')
    assert isnull(authors.loc['unknown', 'max_dry_stretch'])
