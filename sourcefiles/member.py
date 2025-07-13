import logging
import json

from tinydb import TinyDB
from tinydb.storages import JSONStorage

from constants import UTILS_DIR
from project import this_project

logging.basicConfig(filename=UTILS_DIR / "process.log",
                    filemode="a",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class UnescapedJSONStorage(JSONStorage):
    def write(self, data):
        with open(self._handle.name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class Member:
    """Create a member with information below:
        -   number;
        -   first_name;
        -   last_name;
        -   address;
        -   phone_number;
        -   school;
        -   sex;
        # -   commission;
        # -   promo;
        # -   id_number;
    """

    DB = TinyDB(this_project()[0]["files"]["db"], indent=4, storage=UnescapedJSONStorage)

    def __init__(self,
                 project_name: str,
                 number: str,
                 first_name: str,
                 last_name: str,
                 phone_number: str,
                 school: str = "null",
                 address: str = "null",
                 sex: str = "",
                 commission_: str = "",
                 promo: str = "null"
                 ):
        self.number = number
        self.first_name = self.reformat_first_name(first_name)
        self.last_name = last_name.upper()
        self.address = address.strip().title()
        self.phone_number = self.reformat_phone_number(phone_number)
        # self.school = school.upper().strip()
        self.sex = sex
        self.commission_ = commission_.strip().upper()
        # self.promo = promo.strip()
        self.id_number = self.get_id_number()
        self.project_name = project_name
        # print("initialize...")
        if len(first_name) > 20:
                    print(f"{number} - {first_name}")

    @staticmethod
    def reformat_phone_number(number: str) -> str:
        number_char = list(number)
        number_digits = [char for char in number_char if char.isdigit()]
        if len(number_digits) == 9:
            return "{0}{1} {2}{3}{4} {5}{6} {7}{8}".format(*number_digits)

        logging.warning("Got invalid number")
        return "7X XXX XX XX"

    @staticmethod
    def reformat_first_name(first_name) -> str:
        parts = [part.capitalize() for part in first_name.split(" ")]
        first_name = " ".join(parts)
        return first_name

    def get_id_number(self) -> str:
        # schools = {
        #     "DSTI": 1,
        #     "DGAE": 2,
        #     "ST2AN": 3,
        #     "DGO": 4,
        #     "DU2ADT": 5,
        #     "TECNA": 6,
        #     "STA": 7,
        #     "SEG":8
        # }
        # school_number = schools.get(self.school)

        # id_number = f"{self.sex}-{str(self.number).zfill(3)}-{str(school_number).zfill(2)}-{str(self.promo).zfill(2)}"
        # id_number = f"{self.sex}-{str(self.promo).zfill(2)}-{str(self.number).zfill(3)}"
        id_number = f"{self.sex}-{str(self.number).zfill(4)}"
        return id_number

    def get_user_info(self):
        return {
            'NUMBER': self.number,
            'FIRSTNAME': self.first_name,
            'LASTNAME': self.last_name,
            # 'ADDRESS': self.address,
            'COMMISSION_': self.commission_,
            'PHONE-NUMBER': self.phone_number,
            # 'SCHOOL': self.school,
            # 'PROMO': self.promo,
            'ID-NUMBER': self.id_number
        }

    def save_member(self):
        logging.info(f"Saving member -- No : {self.number}")
        Member.DB.insert(self.__dict__)
        # print("saving...")
        return 1


if __name__ == "__main__":
    try:
        import Faker
        for _ in range(10):
            member = Member(
                sex="1/2",
                first_name=Faker().first_name(),
                last_name=Faker().last_name(),
                address="Dakar",
                commission_="Communication",
                phone_number=Faker().phone_number(),
                school="ESTI",
                promo="PX",
                number="000",
                project_name="Test_117"
            )
            member.save_member()
    except ImportError:
        pass
