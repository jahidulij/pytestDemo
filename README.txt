1. Go to https://docs.qameta.io/allure-report/
2. Then in 2.1.4 Manual installation go to "Maven Central"
3. Go to the highest version
4. Download the zip of highest version
5. Add the bin folder location the the [System Variables > path > bin folder location]
6. From PyCharm install the package "allure-pytest" &/ "pytest-allure-adaptor"
7. run the script using: pytest -s -v --alluredir="C:/Users/JahidulIslam/PycharmProjects/pytestDemo/reports/" .\test_cases\test_fixtures.py
8. run following command from reports location: allure serve folder location