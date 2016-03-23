# -*- coding: utf-8 -*-
import click
import os
import pandas as pd

FAKE_CONTRIB_DATA = pd.Series(
    index=['J. Doe'],
    data={'1st':pd.datetime(2000, 1, 1),
          'last':pd.datetime.now(),
          'fraction':0.98}
)

OUT_FOLDER = 'contrib_data'

def verify_local_repo_location(repo):
    if not os.path.isdir(repo):
        raise IOError('could not locate repository {}'.format(repo))


def make_output_folder(repo_name, out_path=None):
    if out_path is None:
        out_path = os.path.abspath(os.curdir)
    if not os.path.isdir(out_path):
        raise IOError('could not locate output folder {}'.format(out_path))
    os.mkdir(os.path.join(out_path, repo_name, OUT_FOLDER))


@click.command()
@click.option('--repo', prompt='git repository location', help='path to git repository')
def main(repo):
    """  """
    verify_local_repo_location(repo)
    repo_name = os.path.basename(repo)
    make_output_folder(repo_name)
    contributor_data = FAKE_CONTRIB_DATA


if __name__ == '__main__':
    main()
