# Exercise_1 
class TextFile:
  	# Add type hints to TextFile"s __init__() method
    def __init__(self, name: str) -> None:
        self.text = Path(name).read_text()

	# Type annotate TextFile"s get_lines() method
    def get_lines(self) -> List[str]:
        return self.text.split("\n")

help(TextFile)

--------------------------------------------------
# Exercise_2 
class MatchFinder:
  	# Add type hints to __init__()'s strings argument
    def __init__(self, strings: List[str]) -> None:
        self.strings = strings

	# Type annotate get_matches()'s query argument
    def get_matches(self, query: Optional[str] = None) -> List[str]:
        return [s for s in self.strings if query in s] if query else self.strings

help(MatchFinder)

--------------------------------------------------
# Exercise_3 
def get_matches(word_list: List[str], query:str) -> List[str]:
    ("Find lines containing the query string.\nExamples:\n\t"
     # Complete the docstring example below
     ">>> get_matches(['a', 'list', 'of', 'words'], 's')\n\t"
     # Fill in the expected result of the function call
     "['list', 'words']")
    return [line for line in word_list if query in line]

help(get_matches)

--------------------------------------------------
# Exercise_4 
def obtain_words(string: str) -> List[str]:
    ("Get the top words in a word list.\nExamples:\n\t"
     ">>> from this import s\n\t>>> from codecs import decode\n\t"
     # Use obtain_words() in the docstring example below
     ">>> obtain_words(decode(s, encoding='rot13'))[:4]\n\t"
     # Fill in the expected result of the function call
     "['The', 'Zen', 'of', 'Python']") 
    return ''.join(char if char.isalpha() else ' ' for char in string).split()
  
help(obtain_words)

--------------------------------------------------
# Exercise_5 
def nbuild(filenames: List[str]) -> nbformat.notebooknode.NotebookNode:
    """Create a Jupyter notebook from text files and Python scripts."""
    nb = new_notebook()
    nb.cells = [
        # Create new code cells from files that end in .py
        new_code_cell(Path(name).read_text()) 
        if name.endswith(".py")
        # Create new markdown cells from all other files
        else new_markdown_cell(Path(name).read_text()) 
        for name in filenames
    ]
    return nb
    
pprint(nbuild(["intro.md", "plot.py", "discussion.md"]))

--------------------------------------------------
# Exercise_6 
def nbconv(nb_name: str, exporter: str = "script") -> str:
    """Convert a notebook into various formats using different exporters."""
    # Instantiate the specified exporter class
    exp = get_exporter(exporter)()
    # Return the converted file"s contents string 
    return exp.from_filename(nb_name)[0]
    
pprint(nbconv(nb_name="mynotebook.ipynb", exporter="html"))

--------------------------------------------------
# Exercise_7 
# Fill in the decorator for the test_nbuild() function 
@pytest.mark.parametrize("inputs", ["intro.md", "plot.py", "discussion.md"])
# Pass the argument set to the test_nbuild() function
def test_nbuild(inputs):
    assert nbuild([inputs]).cells[0].source == Path(inputs).read_text()

show_test_output(test_nbuild)

--------------------------------------------------
# Exercise_8 
@pytest.mark.parametrize("not_exporters", ["htm", "ipython", "markup"])
# Pass the argument set to the test_nbconv() function
def test_nbconv(not_exporters):
     # Use pytest to confirm that a ValueError is raised
    with pytest.raises(ValueError):
        nbconv(nb_name="mynotebook.ipynb", exporter=not_exporters)

show_test_output(test_nbconv)

--------------------------------------------------
