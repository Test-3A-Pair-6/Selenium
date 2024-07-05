# Tobeto Automation Testing with Python-Selenium

This project demonstrates the use of Python-Selenium for automating tests for the Tobeto website. The tests cover various functionalities such as language addition, deletion, and password change operations, utilizing Allure for test reporting.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)

## Project Overview <a name="project-overview"></a>

The purpose of this project is to create a robust automation test suite for the Tobeto website. The tests are written in Python using the Selenium WebDriver and are designed to ensure the website's functionalities work as expected. Allure is used for generating comprehensive test reports.

## Installation <a name="installation"></a>

1. **Clone the repository:**
```
git clone https://github.com/Test-3A-Pair-6/Selenium.git
cd Selenium
```

2. **Create a virtual environment:**
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install the required dependencies:**
```
pip install -r requirements.txt
```

## Usage <a name="usage"></a>

1. **Run the tests:**
```
pytest --alluredir=reports -k <related_test_name>
```

2. **Generate the Allure report:**
```
allure serve reports
```

3. **Viewing Test Results:**
The Allure report will be served on a local server, where you can view detailed results of the test executions.

## Contributors <a name="contributors"></a>

* [Tuba Turak](https://github.com/tubaturak)
* [Miray Sönmez](https://github.com/chiturca)
* [İsmet Acar](https://github.com/acarismet)
* [Hilal Cebel](https://github.com/hilalcebel)
* [Ercan Deniz](https://github.com/ercdeniz)
* [Büşra Nur Tozak](https://github.com/busratozak)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Test-3A-Pair-6/Selenium/blob/master/LICENSE) file for details.
