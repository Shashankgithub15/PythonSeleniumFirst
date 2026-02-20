import pytest

@pytest.mark.usefixtures("setup")
class OnceDeclaredFixtureUsedInAllMethods:

    def FirstMethod(self):
        print("First Method is used.")

    def SecondMethod(self):
        print("Second Method is used.")

    def ThirdMethod(self):
        print("Third Method is used.")

    def FourthMethod(self):
        print("Fourth Method is used.")