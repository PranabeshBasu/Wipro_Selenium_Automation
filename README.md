# Final Project and Assignment Submission - Wipro Python Automation

## 👨‍🎓 Student Information

| Field | Details |
|---|---|
| **Name** | Pranabesh Basu |
| **Enrollment No.** | 12023002028154 |
| **Department** | CSE (AI & ML) |
| **Section** | C |
| **Roll No.** | 19 |
| **Year** | 4th Year |
| **Semester** | 7th Semester |

---

## 📌 Repository Overview

This repository contains the complete coursework, laboratory assignments, and final capstone project completed as part of the **Wipro Python Automation Training Program**.

It demonstrates the progression of automation skills through multiple modules — starting with Selenium automation and unit testing, progressing through BDD and RESTful automation, Robot Framework, and finally a structured Selenium Python automation framework using **PyTest**, **Unittest**, and the **Page Object Model**.

The repository is divided into two major sections:

1. **Assignments Submission**
2. **Final Capstone Project**

---

## 📂 Repository Structure

```text
Wipro_Selenium_Automation/
│
├── Assignments_Submission/
│   │
│   ├── Module1_Automation_with_Selenium/
│   │   └── MODULE1.ipynb
│   │
│   ├── Module2_Unit_Test_Frameworks/
│   │   ├── login_data.csv
│   │   ├── MODULE2.ipynb
│   │   └── report.html
│   │
│   ├── Module_3_Python_BDD_Restful_Automations_Assignment/
│   │   ├── Module3.ipynb
│   │   └── Module3_BDD_Lab/
│   │       ├── features/
│   │       │   ├── api.feature
│   │       │   ├── data_driven_login.feature
│   │       │   ├── login.feature
│   │       │   ├── pom_login.feature
│   │       │   └── steps/
│   │       │       ├── api_steps.py
│   │       │       ├── login_steps.py
│   │       │       └── pom_login_steps.py
│   │       └── pages/
│   │           ├── __init__.py
│   │           └── login_page.py
│   │
│   └── Module4_Robot_Framework/
│       ├── MODULE4.ipynb
│       └── Module4_Robot_Framework/
│
├── CapstoneAssignment2_Selenium_Python_Framework_Development_Unittest_PyTest_POM/
│   │
│   ├── config/
│   │   └── config.ini
│   │
│   ├── data/
│   │   └── testdata.csv
│   │
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── login_page.py
│   │   ├── home_page.py
│   │   ├── product_page.py
│   │   └── cart_page.py
│   │
│   ├── reports/
│   │   └── report.html
│   │
│   ├── screenshots/
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_login.py
│   │   ├── test_product_search.py
│   │   ├── test_cart.py
│   │   ├── test_invalid_login.py
│   │   └── unittest_config.py
│   │
│   ├── utilities/
│   │   ├── __init__.py
│   │   ├── config_reader.py
│   │   ├── csv_reader.py
│   │   ├── driver_factory.py
│   │   └── screenshot.py
│   │
│   ├── conftest.py
│   ├── pytest.ini
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

> **Note:** `.venv`, `__pycache__`, `.pytest_cache`, generated reports, and generated screenshots are excluded from version control via `.gitignore`.

---

## 📚 Part 1 — Assignments Submission

The `Assignments_Submission/` directory contains the module-wise practical assignments completed during the training.

### Module 1 — Automation with Selenium
`Assignments_Submission/Module1_Automation_with_Selenium/MODULE1.ipynb`

Covers Selenium-based browser automation exercises and demonstrates the foundational concepts required for automating web applications using Selenium WebDriver with Python.

### Module 2 — Unit Test Frameworks
`Assignments_Submission/Module2_Unit_Test_Frameworks/`

| File | Description |
|---|---|
| `MODULE2.ipynb` | Practical exercises related to Python unit testing and automation testing |
| `login_data.csv` | External login test data used for data-driven testing exercises |
| `report.html` | Generated HTML test report for the module's test execution |

### Module 3 — Python BDD & RESTful Automations
`Assignments_Submission/Module_3_Python_BDD_Restful_Automations_Assignment/`

Covers Python automation, Behavior-Driven Development, RESTful automation, feature files, step definitions, and the Page Object Model.

*   **`Module3.ipynb`** — Module 3 practical exercises and demonstrations.
*   **`Module3_BDD_Lab/`** — The BDD laboratory implementation:
    *   **`features/`** — Gherkin feature files describing test scenarios in human-readable form:
        *   `api.feature` — BDD scenarios for API automation.
        *   `data_driven_login.feature` — Data-driven login scenarios.
        *   `login.feature` — Login-related BDD scenarios.
        *   `pom_login.feature` — Login scenarios implemented using the Page Object Model.
    *   **`features/steps/`** — Python step-definition files connecting Gherkin scenarios to executable code:
        *   `api_steps.py`, `login_steps.py`, `pom_login_steps.py`
    *   **`pages/`** — Page Object Model classes used by the BDD implementation (`login_page.py`, `__init__.py`).

### Module 4 — Robot Framework
`Assignments_Submission/Module4_Robot_Framework/`

*   **`MODULE4.ipynb`** — Practical exercises and demonstrations for the Robot Framework module.
*   **`Module4_Robot_Framework/`** — Robot Framework implementation files covering basic syntax, custom keywords, data-driven testing, element verification, text input, and variables. Python custom keyword implementations are included where required.

---

## 🚀 Part 2 — Final Capstone Project: Selenium Python Framework Development

Located at:
`CapstoneAssignment2_Selenium_Python_Framework_Development_Unittest_PyTest_POM/`

A structured Selenium automation framework built with **Python**, **Selenium WebDriver**, **PyTest**, **Unittest**, **Page Object Model**, CSV test data, configuration management, a driver factory, failure screenshot capture, sequential test execution, and HTML reporting.

**Application Under Test:** [TutorialsNinja Demo](https://tutorialsninja.com/demo/)

### 🏗️ Capstone Architecture

```text
                     Test Cases
                         │
                         ▼
                   Page Objects
                         │
                         ▼
                Selenium WebDriver
                         │
                         ▼
                TutorialsNinja Demo
```

Supporting framework components:

```text
Configuration Management → config_reader.py
Test Data Management      → csv_reader.py
Browser Management        → driver_factory.py
Failure Handling          → screenshot.py
Test Execution            → PyTest / Unittest
```

### ⚙️ Configuration — `config/config.ini`

Stores the application URL, defines the browser used for execution, and keeps configuration values separate from test code.

```ini
[DEFAULT]
base_url = https://tutorialsninja.com/demo/
browser = chrome
```

### 📊 Test Data — `data/testdata.csv`

External CSV-based test data containing fields for test case, username, password, expected result, product, and quantity. Separates test data from test logic for easier maintenance.

> **Security:** Real passwords or sensitive credentials should never be committed to a public repository.

### 📄 Page Object Model — `pages/`

| File | Responsibilities |
|---|---|
| `login_page.py` | Locates the *My Account* menu, navigates to Login, locates email/password fields and the Login button, performs login |
| `home_page.py` | Locates the search box/button, enters a product name, performs product searches (`search_product()`) |
| `product_page.py` | Retrieves the displayed product name, locates *Add to Cart*, adds products, opens the cart |
| `cart_page.py` | Locates the quantity field, updates quantity, clicks *Update*, retrieves the updated quantity |
| `__init__.py` | Marks `pages` as a Python package |

### 🛠️ Utilities — `utilities/`

| File | Responsibilities |
|---|---|
| `config_reader.py` | Reads base URL/browser values from `config.ini` |
| `csv_reader.py` | Reads external test data from `testdata.csv` |
| `driver_factory.py` | Creates the Selenium WebDriver (Chrome/Firefox), applies maximization & implicit wait |
| `screenshot.py` | Creates the `screenshots/` directory, timestamps and captures failures |
| `__init__.py` | Marks `utilities` as a Python package |

### 🧪 Test Cases — `tests/`

| Test | Flow | Result |
|---|---|---|
| `test_login.py` | Open App → My Account → Login → Enter Credentials → Validate Login | ✅ Passed |
| `test_product_search.py` | Read Product from CSV → Search → Retrieve Name → Validate | ✅ Passed |
| `test_cart.py` | Add to Cart → Open Cart → Validate → Update Quantity → Validate Updated Quantity | ✅ Passed |
| `test_invalid_login.py` | Invalid Login → Failure → Screenshot captured via PyTest hook | ▶️ Run Separately |
| `unittest_config.py` | Unittest framework demonstration | ✅ Passed |

**Failure Flow:**
```text
Invalid Login → Test Failure → PyTest Failure Hook → Screenshot Utility → Screenshot Captured
```

### 🔌 `conftest.py`

Contains PyTest fixtures and the failure-handling mechanism:

*   **Driver Fixture** — reads the browser from config, creates the WebDriver via the Driver Factory, opens the application URL, and closes the browser after the session.
*   **Failure Screenshot Hook** — checks whether a test has failed and automatically triggers the screenshot utility, without requiring screenshot code in every test.

### ⚙️ `pytest.ini`

Configures test execution and HTML reporting. Report is generated at `reports/report.html`.

### 📦 `requirements.txt`

| Package | Purpose |
|---|---|
| `selenium` | Browser automation |
| `pytest` | Primary test execution framework |
| `pytest-html` | HTML test report generation |
| `pytest-order` | Controls execution order of main test cases |

### 📋 Test Execution Order

```text
1. Login → 2. Product Search → 3. Add Product to Cart
```
Order is enforced using `pytest-order`.

---

## 🚀 How to Run the Capstone Project

**1. Navigate to the Capstone Directory**
```bash
cd CapstoneAssignment2_Selenium_Python_Framework_Development_Unittest_PyTest_POM
```

**2. Create a Virtual Environment**
```bash
python -m venv .venv
```

**3. Activate the Virtual Environment (Windows)**
```bash
.venv\Scripts\activate
```

**4. Install Dependencies**
```bash
pip install -r requirements.txt
```

**5. Configure the Browser**

Edit `config/config.ini`:
```ini
[DEFAULT]
base_url = https://tutorialsninja.com/demo/
browser = chrome   # or firefox
```

**6. Run the Three Main Valid Test Cases**
```bash
pytest tests/test_login.py tests/test_product_search.py tests/test_cart.py
```
Expected result: `3 passed`

**7. View the HTML Report**

Open `reports/report.html` after execution.

**8. Run the Invalid Login Test (Failure Demonstration)**
```bash
pytest tests/test_invalid_login.py
```
Check `screenshots/` for the captured failure screenshot (named with test name + timestamp).

**9. Run the Unittest**
```bash
python -m unittest tests.unittest_config
```
Expected output:
```text
.
----------------------------------------------------------------------
Ran 1 test

OK
```

---

## 🔄 Complete Capstone Execution Flow

```text
Start
  │
  ▼
Read Configuration
  │
  ▼
Create WebDriver
  │
  ▼
Open TutorialsNinja
  │
  ▼
Login Test → Product Search Test → Cart Test
  │
  ▼
Generate HTML Report
  │
  ▼
Close Browser
```

**Failure Handling:**
```text
Test Failure → PyTest Report Hook → Screenshot Utility → Capture Browser Screenshot → Save Screenshot
```

---

## 📈 Capstone Test Summary

| Test | Description | Execution |
|---|---|---|
| `test_login.py` | Valid user login | ✅ Passed |
| `test_product_search.py` | Product search validation | ✅ Passed |
| `test_cart.py` | Add product and update quantity | ✅ Passed |
| `test_invalid_login.py` | Invalid login / failure demonstration | ▶️ Run separately |
| `unittest_config.py` | Unittest framework demonstration | ✅ Passed |

---

## ✨ Key Features

- Selenium WebDriver automation
- Python-based automation framework
- PyTest integration
- Unittest integration
- Page Object Model
- Driver Factory
- Configuration management
- CSV-based test data
- Sequential test execution
- Reusable page objects
- Failure screenshot capture
- HTML test reporting
- Modular project structure
- Valid and invalid test scenarios

---

## 🗂️ Generated Files (Not Source Controlled)

```text
.pytest_cache/
__pycache__/
reports/
screenshots/
```

The repository's `.gitignore` prevents generated files, virtual environments, caches, and other unnecessary artifacts from being committed.

---

## 🔐 Security Note

The CSV files used by the assignments and Capstone contain test data. Real passwords, API keys, tokens, or other sensitive credentials should never be committed to a public GitHub repository. Use dummy credentials or environment-based configuration for public repos.

---

## 👨‍💻 Author

**Pranabesh Basu**
Enrollment No.: 12023002028154
Department: CSE (AI & ML) | Section: C | Roll No.: 19
Year: 4th Year | Semester: 7th Semester

---

## 🎓 Conclusion

This repository represents the coursework, practical assignments, and final capstone project completed during the **Wipro Python Automation Training Program**. The assignments demonstrate progression from Selenium automation and unit testing to BDD, RESTful automation, and Robot Framework. The final capstone project demonstrates a structured Selenium Python automation framework using PyTest, Unittest, Page Object Model, external CSV test data, configuration management, a Driver Factory, sequential test execution, automatic failure screenshots, and HTML reporting — providing a modular and maintainable approach to web automation.
