from pytest import fixture

@fixture
def working_dir():
    return "git@github.com:Turbo87/utm"

def test_author_minded(working_dir):
    from tree_scrape import author_minded
    authors = author_minded(working_dir)
    assert 'unknown' in authors
    assert 'Tobias Bieniek' in authors

    assert authors['Tobias Bieniek']['first'] < authors['Tobias Bieniek']['last']
    assert all(u['line_changes'] <= 1 for u in authors.values())
    assert all(u['line_changes'] >= 0 for u in authors.values())
    assert all(u['commits'] <= 1 for u in authors.values())
    assert all(u['commits'] >= 0 for u in authors.values())
