import json
from pathlib import Path

import project


this_project = project.this_project()[0]
OUTPUT_DIR = Path(this_project["directories"]["output"])
model_file = Path(this_project["files"]["model"])
BD_file = Path(this_project["files"]["db"])


def create_svg(info, file_name: str = "undefined-000"):
    fields = [
                "first_name",
                "last_name",
                # "address",
                "commission_",
                "phone_number",
                # "school",
                "id_number",
            ]

    with open(model_file, 'r') as f:
        data = f.read()
        data = data.replace("EXPORT-FILENAME", f"{file_name}.png")
        for i in range(len(fields)):
            print(f"Replacing {fields[i]} by {info.get(fields[i])}")
            data = data.replace(fields[i], info.get(fields[i]))

    folder = Path.joinpath(OUTPUT_DIR / file_name)
    folder.mkdir(exist_ok=True)

    with open(folder / f"{file_name}.svg", "w") as f:
        print("Writing new data ...")
        f.write(data)


def get_members():
    with open(BD_file, "r") as file:
        data = json.load(file)
        return data["_default"]


def make_files(data: dict = get_members()):
    for i in range(1, len(data) + 1):
        member = data[str(i)]
        print(member)
        if member is not None:
            member_number = member["number"]
            member_name = f'{member["first_name"]}-{member["last_name"]}'
            try:
                member_name = member_name.strip().replace(" ", "-", -1)
            except AttributeError:
                pass

            file_name = f"{member["sex"]}-{member_number}-{member_name}"
            print(file_name)
            create_svg(info=member, file_name=file_name)


if __name__ == "__main__":
    make_files()
