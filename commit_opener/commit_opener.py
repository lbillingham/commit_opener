# -*- coding: utf-8 -*-
import click
import os
import pandas as pd
from shutil import rmtree


from commit_opener.grab_dependencies import get_dependencies
from commit_opener.tree_scrape import author_minded
from commit_opener.query_pmc import pmc_data as pubmed_data

OUT_SUBFOLDER = 'contrib_data'
AUTHOR_DATA = 'author_data.json'


def verify_local_repo_location(repo):
    if not os.path.isdir(repo):
        raise IOError('could not locate repository {}'.format(repo))


def build_out_path(repo_name, parent_path=None):
    if parent_path is None:
        parent_path = os.path.abspath(os.curdir)
    out_path = os.path.join(parent_path, repo_name, OUT_SUBFOLDER)
    return out_path


def make_output_folder(path_, overwrite):
    if not os.path.exists(path_):
        os.mkdir(path_)
    else:
        rmtree(path_)
        os.mkdir(path_)


@click.command()
@click.option('--repo', prompt='git repository location',
              help='path to folder containing .git repository or url')
@click.option('--out_dir', default=None,
              help='parent dir for output data, default same as .git folder scraped')
@click.option('--clobber_output', default=True,
              help='should we overwrite existing data?, default True')
@click.option('--verbose/--no-verbose', default=True)
def main(repo, out_dir, clobber_output, verbose):
    """  """
    import logging
    from gitpandas import Repository
    if verbose:
        logging.getLogger().setLevel(10)

    if repo.find("git@") == 0:
        logging.info("Cloning repo %s" % repo)
        repository = Repository(working_dir=repo)
        repo = repository.git_dir
        logging.info("Repo located at %s" % repo)

    if out_dir is None:
        out_dir = os.path.join(os.getcwd(), OUT_SUBFOLDER)

    verify_local_repo_location(repo)
    repo_name = os.path.basename(repo)
    make_output_folder(out_dir, overwrite=clobber_output)
    contributor_data = author_minded(repo)
    citation_data = pubmed_data('SPSS')
    depends_data = get_dependencies(repo_name, repo)
    logging.info("output path: %s" % os.path.join(out_dir,
                                                  'contributor_data.json'))
    contributor_data.to_json(os.path.join(out_dir,
                                          'contributor_data.json'),
                             date_format='iso')
    citation_data['citations'].to_json(os.path.join(out_dir,
                                                    'citation_data.json'))
    depends_data.to_json(os.path.join(out_dir, 'dependencies_data.json'))

if __name__ == '__main__':
    main()
