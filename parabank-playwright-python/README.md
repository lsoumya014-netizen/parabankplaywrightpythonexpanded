# ParaBank Playwright Automation Project

This project uses **Python, Playwright, pytest, Page Object Model, JSON test data, screenshots, and HTML reports** to automate the ParaBank demo application.

## Project structure

```text
parabank-playwright-python/
├── .venv/                         # local virtual environment; create locally
├── tests/
│   ├── test_login.py
│   ├── test_registration.py
│   ├── test_accounts.py
│   └── test_transfer.py
├── pages/
│   ├── login_page.py
│   ├── registration_page.py
│   ├── accounts_page.py
│   └── transfer_page.py
├── utils/
│   └── test_data.py
├── testdata/
│   └── test_data.json
├── screenshots/                   # filled-state and failure screenshots
├── reports/                       # pytest HTML report
├── .env
├── .gitignore
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

```bash
cd parabank-playwright-python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
```

For Linux systems that need browser dependencies:

```bash
python -m playwright install --with-deps chromium
```

## Run all tests with a report

```bash
pytest -vv --html=reports/pytest-report.html --self-contained-html
```

Run only smoke tests:

```bash
pytest -m smoke -vv --html=reports/smoke-report.html --self-contained-html
```

Run only authenticated regression tests:

```bash
pytest -m regression -vv --html=reports/regression-report.html --self-contained-html
```

## Where to see filled details

After execution, open the PNG files in `screenshots/`. The suite captures screenshots after filling:

- Valid login username and password.
- Invalid login username and password.
- Every available ParaBank registration field: first name, last name, address, city, state, ZIP code, phone, SSN, username, password, and confirmation password.
- Authenticated accounts overview.
- Transfer amount, source account, and destination account.

ParaBank does not currently expose an email field in its registration form. The JSON includes an email value for completeness and future form extensions, but Playwright fills every field that actually exists on the live ParaBank page.

The transfer test intentionally stops after filling the form and taking the screenshot. It does not commit a live transfer on the public demo account.

## Test data

Edit `testdata/test_data.json` to change values. No values are hard-coded in the test functions.

The default authenticated demo credentials are `john` / `demo`, which are the seeded credentials available on the public ParaBank demo. The registration test fills the form but does not submit it because the public demo registration database may reject new users during maintenance.

## Configuration

`.env` contains:

```text
BASE_URL=https://parabank.parasoft.com/parabank
HEADLESS=false
SLOW_MO=150
DEFAULT_TIMEOUT_MS=10000
TEST_DATA_FILE=testdata/test_data.json
```

Set `HEADLESS=true` for CI. Keep `HEADLESS=false` locally if you want to visibly watch Playwright fill the fields.

## Authenticated pages covered

After logging in with the seeded `john` / `demo` account, ParaBank exposes seven customer pages. The project covers all seven: **Open New Account, Accounts Overview, Transfer Funds, Bill Pay, Find Transactions, Update Contact Info, and Request Loan**. Together with valid login, invalid login, and registration-form coverage, the suite currently contains **10 passing tests**.

The form tests stop after filling and screenshotting the data. They do not submit account-opening, transfer, bill-payment, profile-update, or loan requests against the shared public demo account.
