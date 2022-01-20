
from pylib import datasets


def test_read_dataset():

    # EXERCISE
    df = datasets.read_excel("tests/data/dataset_test.xlsx")

    # ASSERT
    assert df.columns.tolist() == ["date", "values"]
