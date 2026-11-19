import os
import shutil
from pathlib import Path

# copy the finished front page of Thursday 19 November 2026 to the output folder
# (/output in the make.fun sandbox; MAKEFUN_OUTPUT_DIR when testing locally).
# No network and no randomness, so every run writes the same bytes.
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
shutil.copyfile(Path(__file__).parent / "entry.png", out_dir / "entry.png")
