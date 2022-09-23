import sys

import pytest


@pytest.mark.smoke
def test_1():
    a = 5
    b = 5.0
    assert a == int(b), "Test Failed..."


@pytest.mark.regression
def test_2():
    name = "Selenium"
    title = "selenium with Python"
    assert name.lower() in title, "{} not in {}".format(name, title)


@pytest.mark.skip
def test_3():
    assert "Python" in "Hello Python!"


@pytest.mark.skipif(sys.version_info < (3, 11), reason="Python version not supported")
def test_4():
    assert "J" in "Jython!"


@pytest.mark.xfail
def test_5():
    assert "fail" in "Xail!"


@pytest.mark.parametrize("username, password",
                         [
                             ("selenium", "webdriver"),
                             ("python", "pytest"),
                             ("java", "testng"),
                             ("API", "web automation")
                         ]
                         )
def test_6(username, password):
    print(username)
    print(password)
