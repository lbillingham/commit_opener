"""
Extract the dependencies from the repository 

Issue:
work out dependencies #3
https://github.com/lbillingham/commit_opener/issues/3

"""

def get_dependencies(name, url):
    
    # Let's instantiate the repo object, so we can parse through it.
    myrepo = repo.Repo(name, url)
    
    



def reqs_from_file(contents, file_type=None):
    """
    Original depsy.models.python 
    
    Taken a copy to implement searching for import statements.
    
    """
    if file_type is None:
        # we can auto-detect the file type prolly, but don't need to yet.
        pass
    
    if contents is None:
        return []
    
    if file_type == "requirements.txt":
        return parse_requirements_txt(contents)
    
    elif file_type == "setup.py":
        try:
            return parse_setup_py(contents)
        except SyntaxError:
            # we couldn't read the file.
            print "\n******  setup.py parse error!  ******\n"
            return []
    else:
        # Neither the requirements.txt nor setup.py exist
        # Let's export the repo and do a quick text search
        
