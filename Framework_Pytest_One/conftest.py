import pytest
#fixture are used for setup and tear down test cases
#conftest name is used to use this setup  in every file
# if we pass (scope = "class") as argument to fixture function then that will execute once before the class and then when class ends
#we can load the data before running the test case as a part of prerequisite
#data driven and parametrization can be done with return statement tupe format






def test_Fixture(setup):
    print("setup will run first of all from other files.")

@pytest.fixture(params=[("chrome","Shashank"),"edge"])
def crossBrowser(request):
    return request.param


@pytest.fixture()
def loadData():
    print("Data Loading")
    return {"name":"Shashank","age":24}

@pytest.fixture()
def setup():
    print("it will execute before execution of test case is started where test this setup is used")
    yield
    print("it will execute after execution of test case is completed where test this setup was used")
