def author_minded(working_dir):
    from gitpandas import Repository
    repo = Repository(working_dir=working_dir)
    commits = repo.commit_history()
    authors = set(commits.author)

    tot_lines = float(commits.lines.sum())
    result = {}
    for author in authors:
        specific = commits[commits.author == author]
        result[author] = {
            'first': specific.index.min(),
            'last': specific.index.max(),
            'line_changes': specific.lines.sum() / tot_lines,
            'commits': len(specific) / float(len(commits))
        }
    return result
