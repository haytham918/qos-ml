import datasets
from pathlib import Path
datasets.config.DOWNLOADED_DATASETS_PATH = Path("/newdir/download")
datasets.config.HF_DATASETS_CACHE = Path("/newdir/cache")
dataset = datasets.load_dataset("wikipedia", "20220301.it")