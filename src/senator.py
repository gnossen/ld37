from model import Model

class Senator(Model):
    props = [
        "name",
        "state",
        "special_interests",
        "resources"
    ]

    def __init__(self, *args):
        super(Model, self).__init__(*args)
    
    def gen_name(self):
        self.name = ""

    def gen_state(self):
        self.state = ""

    def gen_special_interests(self):
        self.special_interests = []

    def gen_resources(self):
        self.resources = []

