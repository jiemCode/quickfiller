from project import add_new_project


def initialization():
    pass


if __name__ == "__main__":
    project_name = input("Entre un nom de projet (sans espaces) : ")
    add_new_project(project_name=project_name)
