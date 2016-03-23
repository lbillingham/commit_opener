"""
Extract the dependencies from the repository 

Issue:
work out dependencies #3
https://github.com/lbillingham/commit_opener/issues/3

The key function is get_dependencies().

"""
import re

# THis is an import depsy, but it's not a proper package.
import models as depsymodels

#import commit_opener.repo
import repo

def catfile(filename):
    """Get text contents of a file."""
    
    with open(filename, 'r') as fhandle:
        print("Opening file {} and reading contents".format(filename))
        return "\n".join(fhandle.read())
    

def get_dependencies(name, url):
    """
    Get the dependecies for a git repository or any local python package.
    
    """
    # Let's instantiate the repo object, so we can parse through it.
    myrepo = repo.Repo(name, url)
    print("Created a repository instance for {}".format(url)) 
    
    # Extract a local copy
    myrepo.extract_local_copy()
    print("Local copy now available here: {}".format(myrepo.tmpdir))

    # Note: the file has to be opened and read before passing to depsy 
    # functions.
    if myrepo.has("requirements.txt"):
        print("Repository has a requirements.txt file")
        filetext = catfile(myrepo.has("requirements.txt"))    
        reqs = depsymodels.python(filetext)
    elif myrepo.has("setup.py"):
        print("Repository has a setup.py file")
        filetext = catfile(myrepo.has("setup.py"))    
        reqs = depsymodels.parse_setup_py(filetext)
    else:
        # No standard descriptions of the dependencies so let's try to work 
        # them out for ourselves.
        print("No req or setup file, so determining dependencies ourselves.")
        reqs = search_files_for_imports(myrepo)

    print("Found the following imports: {}".format("\n".join(reqs)))

def search_files_for_imports(repo_instance):
    """
    Walk all the python files in the repository and extract the import info.
    
    """
    dep_list = []
    for f in repo_instance.file_list:
        if ".py" in f:
            print("Looking in {} for imports".format(os.basename(f))) 
            filetext = catfile(f)
            dep_list.extend(find_imports(filetext))

    return dep_list
            
    
def find_imports(text):
    """Apply regular expression searching to a file"""
    # list of regexes
    reexps = [re.compile(r'^import\s+(\w+)', re.MULTILINE),
              re.compile(r'^from\s+(\w+)', re.MULTILINE)
              ]
    import_list = []          
    for myregex in reexps:
        import_list.extend(re.findall(myregex, text))
    return import_list
