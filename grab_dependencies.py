"""
Extract the dependencies from the repository 

Issue:
work out dependencies #3
https://github.com/lbillingham/commit_opener/issues/3

"""

def catfile(filename):
    """Get text contents of a file."""
    
    with open(filename, 'r') as fhandle:
        return "\n".join(fhandle.read())
    

def get_dependencies(name, url):
    
    # Let's instantiate the repo object, so we can parse through it.
    myrepo = repo.Repo(name, url)
    
    # Extract a local copy
    myrepo.extract_local_copy()

    # Note: the file has to be opened and read before passing to depsy 
    # functions.
    if myrepo.has("requirements.txt"):
        filetext = catfile(myrepo.has("requirements.txt"))    
        reqs = depsy.models.python(filetext)
    elif myrepo.has("setup.py"):
        filetext = catfile(myrepo.has("setup.py"))    
        reqs = depsy.models.parse_setup_py(filetext)
    else:
        # No standard descriptions of the dependencies so let's try to work 
        # them out for ourselves.
        pass


