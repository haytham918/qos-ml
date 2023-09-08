import datasets
from pathlib import Path
datasets.config.DOWNLOADED_DATASETS_PATH = Path("/newdir")
dataset = datasets.load_dataset("discofuse", "discofuse-sport")