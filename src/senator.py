from model import *
from names import *

class Senator(Model):
    props = [
        "first_name",
        "last_name",
        "state",
        "special_interests",
        "characteristics",
        "resources"
    ]

    characteristics = DictCombinator(
        {
            "sex": RandomSelection([(17, "female"), (83, "male")]),
            "ethnicity": RandomSelection(
                            [
                                (75, "white"),
                                (10, "black"),
                                (10, "hispanic"),
                                (4, "asian"),
                                (1, "native-american")
                            ]
                         ),
            "party": RandomSelection([(1, "republican"), (1, "democrat")]),
            "age": NormalScalar(45, 10)
        }
    )

    # special interest groups
    # abortion
    # agriculture
    # animals and wildlife
    # racial rights
    # arts
    # business

    def __init__(self, *args, **kwargs):
        super(Senator, self).__init__(*args, **kwargs)
    
    first_name = RandomSelection(male_names)
    last_name = RandomSelection(surnames)

    def full_name(self):
        return self.first_name + " " + self.last_name

    def gen_state(self):
        self.state = ""

    def gen_special_interests(self):
        self.special_interests = []

    def gen_resources(self):
        self.resources = []

