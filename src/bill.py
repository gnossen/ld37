from model import Model

class Bill(Model):
    props = [
        "utility_matrix"
    ]

    def __init__(self, *args, **kwargs):
        super(Bill, self).__init__(*args, **kwargs)

    def gen_utility_matrix(self):
        self.utility_matrix = []
