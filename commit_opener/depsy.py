import re
import pickle
import ast
import os.path
import errno
import requests

# """Functions from depsy"""


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
        '^(?!file:|-|\.)\s*([\w\.-]+)',
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
                    if keyword.arg == "install_requires":
                        print("found requirements in setup.py 'install_requires' arg")
                        for elt in keyword.value.elts:
                            ret.append(_clean_setup_req(elt.s))

                    if keyword.arg == "requires":
                        print("found requirements in setup.py 'requires' arg")
                        for elt in keyword.value.elts:
                            ret.append(_clean_setup_req(elt.s))

                    if keyword.arg == "extras_require":
                        print("found requirements in setup.py 'extras_require' arg")
                        for my_list in keyword.value.values:
                            for elt in my_list.elts:
                                ret.append(_clean_setup_req(elt.s))

        except AttributeError:
            continue

    return sorted(ret)


class PythonStandardLibs():

    def __init__(self):
        self.url = "https://docs.python.org/2.7/py-modindex.html"
        self.data_dir = os.path.join(os.path.dirname(__file__),
                                     "../../data")

        self.pickle_path = os.path.join(self.data_dir,
                                        "python_standard_libs.pickle")
        self.libs = None

    def _mkdir(self):
        try:
            os.makedirs(self.data_dir)
        except OSError as exp:
            if exp.errno != errno.EEXIST:
                raise
        self.pickle_path = os.path.join(self.data_dir,
                                        "python_standard_libs.pickle")

    def retrieve_from_web(self):
        # only needs to be used once ever, here for tidiness
        # checked the result into source control as python_standard_libs.pickle
        html = requests.get(self.url).text
        exp = r'class="xref">([^<]+)'
        matches = re.findall(exp, html)
        self.libs = [m for m in matches if '.' not in m]

    def pickle_libs(self):

        if self.libs is None:
            self.retrieve_from_web()

        self._mkdir()
        with open(self.pickle_path, "w") as f:
            pickle.dump(self.libs, f)

        print("saved these to file: {}".format(self.libs))

    def get(self):
        if self.libs is None:
            try:
                with open(self.pickle_path, "r") as f:
                    print("Loading list of Stdandard Python Libraries from pickle file")
                    self.libs = pickle.load(f)
            except:
                self.retrieve_from_web()
                self.pickle_libs()

    def clean(self):
        try:
            os.remove(self.pickle_path)
        except:
            pass


def save_python_standard_libs(clean=False):
    pystdlibs = PythonStandardLibs()
    if clean:
        pystdlibs.clean()
    pystdlibs.get()

    # to show the thing works
    new_libs_obj = PythonStandardLibs()
    new_libs_obj.get()
    print("got these from pickled file: {}".format(new_libs_obj.libs))
