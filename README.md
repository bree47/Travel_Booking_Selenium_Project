# Travel Booking Automation Project

This project automates the process of booking a flight on a travel booking website using Selenium WebDriver in Python. The automation covers login, flight selection, passenger details input, payment processing, and booking confirmation.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Running the Tests](#running-the-tests)
- [Test Flow](#test-flow)
- [Report Generation](#report-generation)
- [Contributors](#contributors)

## Project Overview

This is an end-to-end automation script that interacts with a travel booking website. The script uses Selenium to automate the web interactions, making it easier to test booking flows without manual intervention. It logs into the site, selects flights, enters passenger details, completes payment, and finally verifies the successful booking.

## Features

- Automates flight booking from login to payment
- Includes data-driven testing with multiple inputs for different scenarios
- Customizable for different sets of test data
- Uses Pytest framework for running and managing test cases

## Prerequisites

Before running the project, ensure you have the following:

- Python 3.x installed
- Chrome or Firefox browser installed with the corresponding WebDriver (Chromedriver/Geckodriver)
- Internet connection for accessing the travel booking website
- Basic knowledge of Selenium WebDriver and Pytest framework

## Setup

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/travel-booking-automation.git
    ```

2. Navigate into the project directory:
    ```bash
    cd travel-booking-automation
    ```

3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    ```

4. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

5. Ensure you have downloaded and placed the ChromeDriver or GeckoDriver (for Firefox) in your PATH.

## Running the Tests

To run the test cases, use the following command:
```bash
pytest -v
