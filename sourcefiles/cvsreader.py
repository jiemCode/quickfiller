import csv
import logging

import constants, project
from add_member import _get_member
from member import Member

logging.basicConfig(filename=constants.UTILS_DIR / "process.log",
                    filemode="a",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def read(project_name: str):
    this_project = project.get_project_info(project_name=project_name) if project.check_project(project_name) else None

    try:
        with open(this_project["files"]["data"], "r") as f:
            content = csv.reader(f)
            number = 0
            for row in content:
                number += 1
                # print(number)
                data = {
                    "number": number,
                    "first_name": row[1],
                    "last_name": row[2],
                    "phone_number": row[3],
                    "address": "null",
                    # "school": row[4],
                    # "promo": row[5],
                    "commission_": row[4],
                    "sex": row[0],
                    "project_name": project_name,
                }

                member = Member(**_get_member(**data))
                # print(member.get_user_info())
                member.save_member()

    except ValueError:
        print("Unable to read file")


if __name__ == "__main__":
    name = project.this_project()[1]
    print(name)
    read(project_name="islaahu_daarayni")
    pass
