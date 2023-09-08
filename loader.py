from datasets import load_dataset
from pathlib import Path
datasets.config.DOWNLOADED_DATASETS_PATH = Path("/newdir")
dataset = load_dataset("discofuse", "discofuse-sport")