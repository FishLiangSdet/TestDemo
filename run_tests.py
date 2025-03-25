import pytest
import os

if __name__ == "__main__":
    pytest.main(["-s", "-v", "--alluredir=reports"])
    os.system("allure generate reports -o reports/html --clean")
