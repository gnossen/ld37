from model import *
from pytest import *
from mock import MagicMock

class Plant(Model):
    props = [
        "stem_length",
        "petal_length"
    ]

    def __init__(self, *args, **kwargs):
        super(Plant, self).__init__(*args, **kwargs)

    stem_length = NormalScalar(4, 1)

    def gen_petal_length(self):
        self.petal_length = 4

@yield_fixture()
def mock_normalvariate():
    mock_nv = MagicMock(return_value=0)
    old_nv = random.normalvariate
    random.normalvariate = mock_nv
    yield mock_nv
    random.normalvariate = old_nv

def test_gen_scalar_property(mock_normalvariate):
    plant = Plant()
    mock_normalvariate.assert_called_once_with(4, 1)
    assert plant.stem_length == 0
    assert plant.petal_length == 4

def test_explicit_property():
    plant = Plant(stem_length=1)
    assert plant.stem_length == 1

    plant2 = Plant(props={"stem_length": 1})
    assert plant.stem_length == 1

def test_model_seed():
    seed = 1234
    random.seed(seed)
    expected_value = random.normalvariate(4, 1)
    random.seed(0)
    plant = Plant(seed=seed)
    assert plant.stem_length == expected_value
    assert plant.petal_length == 4

def test_random_selection():
    name = RandomSelection([
        (1, "Mark"),
        (2, "John"),
        (3, "James")
    ])
    # for i in range(20):
    #     print name()
