import os
import subprocess
import pandas as pd
import json
from pathlib import Path

def download_and_process():
    """Download FakeNewsNet and process PolitiFact dataset to CSV."""
    fakenews_dir = Path("data/fakenewsnet")
    if not fakenews_dir.exists():
        subprocess.run(["git", "clone", "https://github
