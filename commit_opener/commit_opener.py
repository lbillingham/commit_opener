# -*- coding: utf-8 -*-
import click
import os
import pandas as pd
from shutil import rmtree

from . tree_scrape import author_minded

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

def build_out_path(repo_name, parent_path=None):
    if parent_path is None:
        parent_path = os.path.abspath(os.curdir)
    out_path = os.path.join(parent_path, repo_name, OUT_FOLDER)
    return out_path

def make_output_folder(path_, overwrite):
    if not os.path.exists(path_):
        os.mkdir(path_)
    else:
        rmtree(path_)
        os.mkdir(path_)


@click.command()
@click.option('--repo_dir', prompt='git repository location', help='path to folder containing  .git repository')
@click.option('--out_dir', default=None,
    help='parent dir for output data, default same as .git folder scraped')
@click.option('--clobber_output', default=True,
        help='should we overwrite existing data?, default True')

def main(repo_dir, out_dir, clobber_output):
    """  """
    verify_local_repo_location(repo_dir)
    repo_name = os.path.basename(repo_dir)
    outpath = build_out_path(repo_dir, out_dir)
    make_output_folder(outpath, overwrite=clobber_output)
    contributor_data = author_minded(repo_dir)
    contributor_data.to_json(os.path.join(outpath,'contributor_data.json'))


if __name__ == '__main__':
    main()
