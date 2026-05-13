# Playwright Python UI Testing Framework

A generic and reusable UI testing framework built with Playwright (Python), Docker, and GitHub Actions CI/CD.
This project is designed to support scalable browser-based UI automation testing for different web applications and can easily be integrated into CI pipelines.

---

# Features

- Playwright UI testing with Python
- Dockerized test execution
- GitHub Actions workflow integration
- Generic project structure for reusable automation setups
- Headless browser execution for CI/CD environments
- Easy local execution for debugging

---

# POM page object module 

this project is following the POM designpattern for UI testing-
more informations about page object module under :

https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b

---

# Install Dependencies

pip install -r requirements.txt   
then install Playwright browser using :
playwright install

---

# Running Tests Locally

Run all tests using the following command :
python main.py

---

# Running in Chromium Window Mode (Non-Headless)

If you want to run tests locally with the Chromium browser window visible for debugging purposes:

Open conftest.py
Change the headless flag to False:
browser = p.chromium.launch(headless=False)

---

# Important Note About Headless Mode

Before pushing changes or building the Docker image, make sure to return the headless flag back to false

---

# Running Tests with Docker

Build Docker Image using the command:

docker build -t playwright-testing-pipeline .

Run Tests Inside Docker

docker run playwright-testing-pipeline

---

# GitHub Actions CI Pipeline

This project includes a GitHub Actions workflow that automatically:

- Installs dependencies
- Installs Playwright browsers
- Runs UI tests
- saves the Test Reports and Screenshots as artifact

Workflow files can be found in:

.github\workflows\main.yml

---

# Test Location

All UI tests are located inside the tests/ directory.

Currently, the project contains:
One sample UI test

You can extend the framework by adding more tests into the same folder structure.

---

# Goal of This Project

The purpose of this framework is to provide a reusable and scalable starting point for:

- UI automation projects
- Browser-based regression testing
- CI/CD testing pipelines
- Dockerized test execution
- Cross-project UI testing setups

---

# Future Improvements

- Parallel execution using python xdist 
- Environment-based configurations from .env file
- video capture on failures