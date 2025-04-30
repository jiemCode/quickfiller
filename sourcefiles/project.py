import json
import logging
from pathlib import Path
from typing import Tuple

from tinydb import TinyDB

import constants

logging.basicConfig(filename=constants.UTILS_DIR / "process.log",
                    filemode="a",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s'")


class Project:
    DB = TinyDB(constants.UTILS_DIR / "settings.json", indent=4)

    def __init__(self, project_name: str):
        self.project_name = project_name
        self.project_path = self.create_project()[0]
        self.project_settings = self.create_project()[1]
        self.directories = self.create_project()[2]
        self.files = self.create_project()[3]

    def create_project(self) -> Tuple[str, str, dict, dict]:
        Path.mkdir(constants.PROJECTS_DIR, exist_ok=True)
        project_path = Path.joinpath(constants.PROJECTS_DIR / self.project_name)
        Path.mkdir(project_path, exist_ok=True)

        directories = {
            "model": str(Path.joinpath(constants.PROJECTS_DIR / self.project_name / "model")),
            "data": str(Path.joinpath(constants.PROJECTS_DIR / self.project_name / "data")),
            "db": str(Path.joinpath(constants.PROJECTS_DIR / self.project_name / "db")),
            "utils": str(Path.joinpath(constants.PROJECTS_DIR / self.project_name / "utils")),
            "output": str(Path.joinpath(constants.PROJECTS_DIR / self.project_name / "output"))
        }

        for directory in directories.values():
            directory = Path(directory)
            Path.mkdir(directory, exist_ok=True)

        files = {
            "settings": str(Path.joinpath(Path(directories["utils"]) / f"{self.project_name}-settings.json")),
            "process": str(Path.joinpath(Path(directories["utils"]) / f"{self.project_name}-process.log")),
            "model": str(Path.joinpath(Path(directories["model"]) / f"{self.project_name}-model.svg")),
            "data": str(Path.joinpath(Path(directories["data"]) / f"{self.project_name}.csv")),
            "db": str(Path.joinpath(Path(directories["db"]) / f"{self.project_name}-db.json"))
        }

        for file in files.values():
            file = Path(file)
            if not file.exists():
                file.touch()
                if file.suffix == ".json":
                    file.write_text("{}")

        return str(project_path), files.get("settings"), directories, files

    def save(self):
        Project.DB.insert(self.__dict__)
        logging.info(f"New project added : {self.project_name}")


def get_all_project_name():
    with open(constants.UTILS_DIR / "settings.json", "r") as f:
        projects = json.load(f)["_default"]
    return [projects[str(i)].get("project_name") for i in range(1, len(projects) + 1)]


def check_project(project_name: str) -> bool:
    return True if project_name in get_all_project_name() else False


def get_project_info(project_name: str):
    if check_project(project_name=project_name):
        with open(constants.UTILS_DIR / "settings.json", "r") as f:
            projects = json.load(f)["_default"]

        for i in range(1, len(projects) + 1):
            if project_name == projects[str(i)].get("project_name"):
                return projects[str(i)]


def add_new_project(project_name: str):
    if not check_project(project_name=project_name):
        new_project = Project(project_name=project_name)
        new_project.save()
    else:
        print(f"Project {project_name} already exist !")


def this_project():
    with open(constants.UTILS_DIR / "settings.json", "r") as f:
        content = json.load(f)
    current_project = content["current_project"]
    return get_project_info(current_project), current_project


if __name__ == "__main__":
    pass
