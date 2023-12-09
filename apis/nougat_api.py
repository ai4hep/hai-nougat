
import os, sys
from pathlib import Path
here = Path(__file__).parent.absolute()

sys.path.append(f'{here.parent}/repos/nougat')  # insert(0, xx)

from ..repos.nougat.train import train