from datasets import load_dataset
datasets.config.DOWNLOADED_DATASETS_PATH = Path("/newdir")
dataset = load_dataset("discofuse", "discofuse-sport")