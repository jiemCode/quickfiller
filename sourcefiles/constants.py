from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROJECTS_DIR = Path.joinpath(BASE_DIR.parent.parent / "Projects")
UTILS_DIR = Path.joinpath(BASE_DIR / "utils")