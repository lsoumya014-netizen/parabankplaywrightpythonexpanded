# 🏦 Banking Application Test Automation – ParaBank

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Playwright](https://img.shields.io/badge/Playwright-Python-green)
![Pytest](https://img.shields.io/badge/Pytest-Testing-orange)
![Git](https://img.shields.io/badge/Git-Version%20Control-red)

## 📌 Project Overview

This project is an **end-to-end UI test automation suite** developed using **Playwright with Python and Pytest** for **ParaBank**, a demo online banking application provided by Parasoft.

The project focuses on automating and validating common banking workflows such as user registration, authentication, account management, fund transfers, bill payments, loan requests, and transaction history.

The automation framework follows the **Page Object Model (POM)** approach to improve code organization, reusability, and maintainability.

---

## 🌐 Application Under Test

**Application:** ParaBank – Demo Online Banking Application

**Website:** https://parabank.parasoft.com/parabank/index.htm

**Project Repository:**
https://github.com/lsoumya014-netizen

> **Note:** ParaBank is a publicly available demo application intended for software testing and automation practice.

---

## 🎯 Project Objectives

* Automate important end-to-end banking workflows.
* Validate positive and negative user scenarios.
* Verify form validations and application responses.
* Validate account and transaction-related information.
* Practice real-world UI automation using Playwright.
* Implement a maintainable automation structure using POM.
* Generate test execution reports using Pytest.
* Identify potential functional regressions through repeatable automated tests.

---

## 🧪 Testing Scope

### 1. User Registration

Automated scenarios related to:

* New user registration
* Required field validation
* Registration form submission
* Registration success response
* User account creation

### 2. Login & Authentication

Test scenarios include:

* Valid login
* Invalid username/password
* Authentication error validation
* Login form validation
* Account overview access after successful login

### 3. Account Overview

Validated:

* Account overview page
* Account information
* Available account details
* Navigation between banking modules

### 4. Fund Transfer

Automated:

* Selecting source account
* Selecting destination account
* Entering transfer amount
* Submitting fund transfer
* Validating transaction confirmation

### 5. Bill Payment

Automated scenarios covering:

* Payee information
* Account details
* Payment amount
* Bill payment submission
* Payment confirmation

### 6. Loan Request

Automated:

* Loan request form
* Loan amount entry
* Down payment information
* Account selection
* Loan request submission
* Response/confirmation validation

### 7. Open New Account

Validated:

* New account navigation
* Account type selection
* Account creation submission
* Newly created account information

### 8. Transaction History

Automated:

* Accessing transaction history
* Selecting an account
* Viewing transaction records
* Validating transaction listing information

---

## 🛠️ Tech Stack

| Technology                  | Purpose                               |
| --------------------------- | ------------------------------------- |
| **Python**                  | Programming language                  |
| **Playwright**              | Web UI automation                     |
| **Pytest**                  | Test execution and assertions         |
| **Page Object Model (POM)** | Framework design and code reusability |
| **Git**                     | Version control                       |
| **GitHub**                  | Source code management                |
| **HTML Reports**            | Test execution reporting              |

---

## 🏗️ Framework Design

The project uses the **Page Object Model (POM)** design pattern.

POM separates:

* Page locators
* Page actions
* Test scenarios
* Test execution logic

This makes the automation framework easier to maintain and extend.

### Example Structure

```text
ParaBank-Automation/
│
├── tests/
│   ├── test_registration.py
│   ├── test_login.py
│   ├── test_accounts.py
│   ├── test_transfer.py
│   ├── test_bill_payment.py
│   ├── test_loan.py
│   └── test_transactions.py
│
├── pages/
│   ├── login_page.py
│   ├── registration_page.py
│   ├── account_page.py
│   ├── transfer_page.py
│   ├── bill_payment_page.py
│   ├── loan_page.py
│   └── transaction_page.py
│
├── test_data/
│   └── test_data.py
│
├── reports/
│   └── report.html
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

> Modify the folder/file names above to match your actual GitHub project structure.

---

## ⚙️ Key Automation Features

### 🔹 Page Object Model

Reusable page classes are used to organize:

* Locators
* Click actions
* Form interactions
* Navigation methods
* Validation methods

### 🔹 Positive & Negative Testing

The suite includes both:

* Positive test scenarios
* Negative test scenarios
* Invalid credential validation
* Form validation
* Transaction/workflow validation

### 🔹 Headed & Headless Execution

Tests can be executed in:

**Headless mode**

```bash
pytest
```

**Headed mode**

```bash
pytest --headed
```

> Use the headed command only if your Pytest configuration supports the `--headed` option.

### 🔹 HTML Reporting

Pytest HTML reporting can be used to generate an execution report containing:

* Test cases executed
* Pass/Fail status
* Execution details
* Test results

Example:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 💻 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <your-ParaBank-repository-url>
```

```bash
cd ParaBank-Automation
```

### Step 2: Create a Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Install Playwright Browsers

```bash
playwright install
```

---

## ▶️ Running the Tests

Run the complete test suite:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

Run tests in headed mode:

```bash
pytest --headed
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## 📊 Test Scenarios

| Module           | Scenarios                                              |
| ---------------- | ------------------------------------------------------ |
| Registration     | User registration, form validation                     |
| Login            | Valid login, invalid credentials                       |
| Account Overview | Account information validation                         |
| Fund Transfer    | Account selection, amount entry, transfer confirmation |
| Bill Payment     | Payee details, payment submission, confirmation        |
| Loan             | Loan request and response validation                   |
| New Account      | Account type selection and account creation            |
| Transactions     | Transaction history and listing validation             |

---

## 📸 Test Evidence / Media

Screenshots and test execution evidence can be added to this repository to demonstrate the automation results.

Recommended structure:

```text
screenshots/
├── login-test.png
├── registration-test.png
├── fund-transfer-test.png
├── bill-payment-test.png
└── test-report.png
```

You can display screenshots in this README using:

```markdown
![Login Test](screenshots/login-test.png)
```

You can also add screenshots of the **Pytest HTML report** to demonstrate successful test execution.

---

## 🔍 QA Skills Demonstrated

* Web UI Automation
* End-to-End Testing
* Functional Testing
* Regression Testing
* Positive Testing
* Negative Testing
* Form Validation
* Authentication Testing
* Account Management Testing
* Transaction Testing
* Workflow Validation
* Data Validation
* Page Object Model
* Test Case Design
* Test Execution
* Test Reporting
* Cross-module Workflow Testing

---

## 🧠 Key Learning Outcomes

Through this project, I gained practical experience in:

* Building a UI automation framework using Playwright and Python.
* Creating reusable page objects and automation methods.
* Automating real-world banking workflows.
* Designing positive and negative test scenarios.
* Performing validation using automated assertions.
* Running tests in headed and headless modes.
* Generating and analyzing HTML test reports.
* Managing automation source code using Git and GitHub.

---

## 🚀 Future Enhancements

Planned improvements may include:

* Adding API automation using Playwright API testing.
* Implementing reusable fixtures and test data management.
* Adding parameterized test cases.
* Integrating the framework with CI/CD pipelines.
* Adding cross-browser execution.
* Improving screenshot and trace collection for failed tests.
* Adding structured logging.
* Integrating automated reports with CI/CD execution.

---

## 👩‍💻 Author

**Soumya L**

B.E. – Computer Science & Engineering

**QA / Software Testing Portfolio**

GitHub:
https://github.com/lsoumya014-netizen

---

## 📌 Disclaimer

This project was created for **software testing and automation learning/practice purposes** using the publicly available ParaBank demo application.

No real customer, financial, or confidential banking data is used.
