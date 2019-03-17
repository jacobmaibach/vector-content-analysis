import pathlib
import glob
import re

RELATIVE_DIR = str(pathlib.Path(__file__).parents[0].absolute())
_index_ = RELATIVE_DIR.rfind('/')+1
MAIN_DIR = RELATIVE_DIR[:_index_]
INPUT_DIR = MAIN_DIR + 'data/input/'
OUTPUT_DIR = MAIN_DIR + 'data/output/'

##

def load_sentences(sep = '.',direc = None):
    if(direc is None):
        direc = INPUT_DIR
    direc = direc + ('/' if direc[-1]!='/' else '')
    file_format = '*.txt'
    file_list = glob.glob(direc + file_format)
    out = []
    for name in file_list:
        with open(name,'r') as file:
            line_list = [l.strip() for l in file]
        for line in line_list:
            if(sep in line):
                new = line.split(sep)
                new = [s for s in new if s]
            else:
                new = [line] if line else []
            out.extend(new)
    return out

class Corpus:
    def __init__(self,listed=None,listed_func=None,total=None):
        self._listed = listed
        self._listed_func = listed_func
        self.total = total

    @property
    def listed(self):
        if(self._listed is not None):
            return self._listed
        else:
            return self._listed_func()

    def __iter__(self):
        yield from self.listed
                
        
