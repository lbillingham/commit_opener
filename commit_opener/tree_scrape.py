def author_minded(working_dir, frequency=None):
    from numpy import median, min, max, diff, nan, timedelta64
    from pandas import DataFrame
    from gitpandas import Repository
    from itertools import groupby

    if frequency is None:
        frequency = timedelta64(0, 'D')

    repo = Repository(working_dir=working_dir)
    commits = repo.commit_history()
    authors = set(commits.author)

    tot_lines = float(commits.lines.sum())
    result = {'first': [], 'last': [], 'line_changes': [], 'commits': [],
              'median_commit_frequency': [], 'max_dry_stretch': [],
              'max_dayly_commit_run': []}
    for author in authors:
        specific = commits[commits.author == author]
        result['first'].append(specific.index.min())
        result['last'].append(specific.index.max())
        result['line_changes'].append(specific.lines.sum() / tot_lines)
        result['commits'].append(len(specific) / float(len(commits)))

        deriv = diff(specific.index[::-1])
        if len(deriv) == 0:
            result['median_commit_frequency'].append(nan)
            result['max_dry_stretch'].append(nan)
            result['max_dayly_commit_run'].append(nan)
        else:
            result['median_commit_frequency'].append(median(deriv).astype('timedelta64[D]'))
            result['max_dry_stretch'].append(max(deriv).astype('timedelta64[D]'))
            result['max_dayly_commit_run'].append(
                max([
                    len(list(u)) for k, u in groupby(deriv.astype('timedelta64[D]'))
                    if k <= frequency
                ])
            )

    return DataFrame(result, index=authors)
