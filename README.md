# QA Automation Project – Selenium + Pytest + Allure Framework

This project contains automated UI tests using **Selenium WebDriver**, **Pytest**, and **Allure Reports**.

---

## 🚀 Tech Stack

- **[Selenium Webdriver]** – for browser automation
- **[Pytest ]** – Test runner
- **[Allure Reporter]** – Test reporting
- **[Webdriver Manager]** – auto-manages ChromeDriver versions

---

## 📁 Folder Structure
```
.
├── tests/
│   └── test_sample.py
├── screenshots/
├── allure-results/
├── allure-report/
├── conftest.py
├── run_tests.sh
├── requirements.txt
└── README.md

```

# ⚙️ Setup & Installation

1. Clone the repository
    ```
    git clone https://github.com/ujale/opendoors.git
    cd opendoors
    ```
2. Install Python Dependencies
    ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
    ```

3. Install Chrome & ChromeDriver
   ```
   brew install chromedriver
   ```

# ▶️ Running Tests

Run Test
```
./run_tests.sh
```

Run Specific Test
```
python3 -m pytest tests/test_login.py --alluredir=allure-results
```

# 📸 Screenshots on Failure
```
Screenshots of failed tests are saved to the screenshots/ folder and attached to Allure reports automatically.
```

# 📊 Allure Report

- Reports are stored in /allure-results/

