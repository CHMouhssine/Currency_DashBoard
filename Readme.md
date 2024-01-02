# Currency Exchange Rate Tracker

## Introduction

The Currency Exchange Rate Tracker is a Django web application that allows users to track and visualize exchange rates between the Euro (EUR) and other currencies. Users can customize the date range and choose specific currencies to analyze. The application utilizes a currencies API to fetch exchange rate data.

## Features

- **Currency Selection**: Choose any currency to compare against the Euro.
- **Date Range Selection**: View exchange rates on a weekly, monthly, yearly, or custom basis.
- **Interactive Line Graph**: Visualize exchange rate trends using Chart.js.
- **API Integration**: Fetch real-time exchange rate data from a currencies API.
- **Responsive Design**: User-friendly interface accessible on various devices.

## Technologies Used

- **Django**: Backend web framework for Python.
- **Chart.js**: JavaScript library for interactive charts.
- **Currencies API**: External API for fetching exchange rate data.
- **Python Requests Library**: Used for making API requests.

## Installation

1. Clone the repository to your local machine.
2. Create a virtual environment and install dependencies (`pip install -r requirements.txt`).
3. Obtain an API key from the chosen currencies API and configure it in the Django settings.
4. Run migrations to set up the database (`python manage.py migrate`).
5. Start the development server (`python manage.py runserver`).

