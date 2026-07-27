from src.validation.validate_data import validate_data


def test_validate_data():

    # If validation fails, an exception will be raised.
    # If no exception occurs, the test passes.
    validate_data()

    assert True