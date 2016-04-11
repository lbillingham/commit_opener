"""
This module contains a class that allows us to interact with the
repository of interest.

"""
import tempfile
import shutil
import subprocess
import os
import os.path


class Repo(object):
    """
    Interact with a repository: attributes, extract a copy, cleanup.

    This could maybe be re-written as a context manger so the cleanup happens
    automatically.

    """

    def __init__(self, name, url, rtype="git"):
        """
        name - Name of the project
        url - url of the project
        rtype - type of the repository. This will mostly be git.

        """
        self.name = name
        self.url = url
        self.rtype = rtype

        self.local_resources = []
        self.extracted = False
        self.file_list = []
        self.tmpdir = None

    def extract_local_copy(self):
        """Extract a local copy of the repository"""
        if "http" not in self.url:
            if os.path.exists(self.url):
                print("Repository exists locally")
                self.tmpdir = self.url
                self.extracted = True
                return
            else:
                raise IOError("Path to repository doesn't exist")

        else:
            print("Extracting local copy of repository")
            self.tmpdir = tempfile.mkdtemp()
            self.local_resources.append(self.tmpdir)
            print("Created temporary directory")
            if self.rtype is "git":
                extract_cmd = "git clone {url} {odir}".format(url=self.url,
                                                              odir=self.tmpdir)
            else:
                # We could implement SVN here, a quick svn export would do.
                raise NotImplemented

            try:
                subprocess.check_call(extract_cmd.split())
            except subprocess.CalledProcessError:
                raise IOError("Unable to extract a local copy of repository")
            else:
                self.extracted = True

    def has(self, filename):
        """
        Does the repository have a file matching a particular name? If it does
        then return the filename, otherwise return False.

        """
        if not self.extracted:
            self.extract_local_copy()

        if not self.file_list:
            self._get_filelist()

        for f in self.file_list:
            if filename in f:
                return f

        return False

    def _get_filelist(self):
        """Just get a list of the files in the repo."""

        if not self.extracted:
            self.extract_local_copy()

        for root, dirs, files in os.walk(self.tmpdir, topdown=True):
            for name in files:
                print(os.path.join(root, name))
                self.file_list.append(os.path.join(root, name))

    def cleanup(self):
        """Remove any local resources"""

        for resource in self.local_resources:
            try:
                shutil.rmtree(resource)
            except:
                print("Unable to remove: {}".format(resource))
