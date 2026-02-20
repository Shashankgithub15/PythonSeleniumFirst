import  pytest

@pytest.mark.usefixtures("loadData")
class TestDataIsLoaded:

    def test_showUsers(self, loadData):
        print(loadData)

