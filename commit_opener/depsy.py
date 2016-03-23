import re
import requests
import pickle
import ast
from pathlib import Path



"""Functions from depsy"""
def parse_requirements_txt(contents):
    # see here for spec used in parsing the file:
    # https://pip.readthedocs.org/en/1.1/requirements.html#the-requirements-file-format
    # it doesn't mention the '#' comment but found it often in examples.
    # not using this test str in  the function, just a handy place to keep it.
    test_str = """# my comment
file://blahblah
foo==10.2
baz>=3.6
# other comment
foo.bar>=3.33
foo-bar==2.2
foo_bar==1.1
foo == 5.5
.for some reason there is a dot sometimes
--index-url blahblah
-e http://blah
  foo_with_space_in_front = 1.1"""

    reqs = re.findall(
        r'^(?!file:|-|\.)\s*([\w\.-]+)',
        contents,
        re.MULTILINE | re.IGNORECASE
    )
    return sorted(reqs)


def parse_setup_py(contents):
    parsed = ast.parse(contents)
    ret = []
    # see ast docs: https://greentreesnakes.readthedocs.org/en/latest/index.html
    for node in ast.walk(parsed):
        try:
            if node.func.id == "setup":
                for keyword in node.keywords:
                    if keyword.arg=="install_requires":
                        print "found requirements in setup.py 'install_requires' arg"
                        for elt in keyword.value.elts:
                            ret.append(_clean_setup_req(elt.s))
    
                    if keyword.arg=="requires":
                        print "found requirements in setup.py 'requires' arg"
                        for elt in keyword.value.elts:
                            ret.append(_clean_setup_req(elt.s))
    
                    if keyword.arg == "extras_require":
                        print "found requirements in setup.py 'extras_require' arg"
                        for my_list in keyword.value.values:
                            for elt in my_list.elts:
                                ret.append(_clean_setup_req(elt.s))
    
        except AttributeError:
            continue

    return sorted(ret)



class PythonStandardLibs():
    """ NOT using yet but will be useful to remove standard libs"""
    url = "https://docs.python.org/2.7/py-modindex.html"
    data_dir = Path(__file__, "../../data").resolve()
    pickle_path = Path(data_dir, "python_standard_libs.pickle")

    @classmethod
    def save_from_web(cls):  
        # only needs to be used once ever, here for tidiness
        # checked the result into source control as python_standard_libs.pickle
        html = requests.get(cls.url).text
        exp = r'<tt class="xref">([^<]+)'
        matches = re.findall(exp, html)
        libs = [m for m in matches if '.' not in m]

        with open(str(cls.pickle_path), "w") as f:
            pickle.dump(libs, f)

        print "saved these to file: {}".format(libs)

    @classmethod
    def get(cls):
        with open(str(cls.pickle_path), "r") as f:
            return pickle.load(f)


def save_python_standard_libs():
    PythonStandardLibs.save_from_web()

    # to show the thing works
    print "got these from pickled file: {}".format(PythonStandardLibs.get())


