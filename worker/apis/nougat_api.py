import os, sys
from pathlib import Path
here = Path(__file__).parent.absolute()
sys.path.append(f'{here.parent}') 
from deploy import hai_model
from functools import partial
from repos.nougat.nougat import NougatModel
from repos.nougat.nougat.postprocessing import markdown_compatible, close_envs
from repos.nougat.nougat.utils.dataset import ImageDataset
from repos.nougat.nougat.utils.checkpoint import get_checkpoint
from repos.nougat.nougat.utils.device import move_to_device, default_batch_size

