from pytest import fixture

@fixture
def working_dir():
    return "git@github.com:Turbo87/utm"

def test_author_minded(working_dir):
    from tree_scrape import author_minded
    authors = author_minded(working_dir)
    assert 'unknown' in authors.index
    assert 'Tobias Bieniek' in authors.index

    assert authors.loc['Tobias Bieniek', 'first'] < authors.loc['Tobias Bieniek', 'last']
    assert all(authors.line_changes <= 1)
    assert all(authors.line_changes >= 0)
    assert all(authors.commits <= 1)
    assert all(authors.commits >= 0)
