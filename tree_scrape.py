def author_minded(working_dir):
    from pandas import DataFrame
    from gitpandas import Repository
    repo = Repository(working_dir=working_dir)
    commits = repo.commit_history()
    authors = set(commits.author)

    tot_lines = float(commits.lines.sum())
    result = {'first': [], 'last': [], 'line_changes': [], 'commits': []}
    for author in authors:
        specific = commits[commits.author == author]
        result['first'].append(specific.index.min())
        result['last'].append(specific.index.max())
        result['line_changes'].append(specific.lines.sum() / tot_lines)
        result['commits'].append(len(specific) / float(len(commits)))

    return DataFrame(result, index=authors)
