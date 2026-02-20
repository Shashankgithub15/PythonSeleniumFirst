import pytest

@pytest.mark.smoke
#@pytest.mark.skip
#@pytest.mark.xfail
def test_msgcheck():
    msg="hello"
    assert msg=="hello","test failed message is not matched"

def test_secondment():
    msg="hello"
    assert msg=="hello","test failed message is not matched"