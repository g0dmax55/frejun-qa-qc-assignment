# 🌟 Frejun QA QC Assignment 

This repository for the Frejun QA/QC assignment utilizes **Playwright** and **Pytest** to support automated testing processes. Comprehensive details regarding test coverage and setup instructions are outlined below.

## ✅ Test Coverage

Our test suite includes **40 test cases** covering essential functionality:

- **🔑 Login**
- **↕️ Sorting of Items**
- **🖼️ Verify Product Display**
- **🛒 Add to Cart & Validate Totals**
- **🛍️ Checkout Process**
- **🚪 Logout**
- **❗ Negative and Edge Case Tests**

## 🔧 Prerequisites

Ensure you have the following installed:

- **Python 3.8** or above
- **pip**
- **Git**

## 🚀 Setup Instructions

Follow these steps to get started with the project:

1. **Clone the Repository**

   Clone the project to your local machine:

   ```bash
   git clone https://github.com/g0dmax55/frejun-qa-qc-assignment.git
   cd frejun-qa-qc-assignment
   ```

2. **Create and Activate a Virtual Environment**

   Set up a virtual environment to manage dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**

   Install the necessary Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers**

   If Playwright is not already installed, execute:

   ```bash
   playwright install
   ```

5. **Run the Tests**

   Execute tests in parallel and generate an HTML report:

   ```bash
   pytest -n 2 --html=report.html
   ```

   - **`-n 2`**: Runs tests using 2 parallel workers, speeding up the testing process.
   - **`--html=report.html`**: Generates a comprehensive HTML report for easy review and sharing.
  
  
