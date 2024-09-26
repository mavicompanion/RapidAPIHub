# Flask App with RapidAPI Integration

This is a starter project for building a Flask application that integrates with an external API using RapidAPI. This project serves as a basic template for beginners looking to understand how to use APIs with Flask.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running the App](#running-the-app)
6. [Project Structure](#project-structure)
7. [Usage](#usage)
8. [Contributing](#contributing)
9. [License](#license)

## Introduction

This project demonstrates how to create a simple Flask web application that makes API requests to an external service via [RapidAPI](https://rapidapi.com/). It covers the basics of setting up a Flask server, configuring the environment, and integrating with an external API.

## Prerequisites

Before you start, make sure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- A RapidAPI account (sign up for free [here](https://rapidapi.com/))

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/flask-rapidapi-starter.git
    cd flask-rapidapi-starter
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

   - **Windows:**

     ```bash
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. **Create a `.env` file in the root directory of the project and add your RapidAPI key:**

    ```
    RAPIDAPI_KEY=your_rapidapi_key
    ```

2. **Configure the API URL and other parameters in `config.py`:**

    ```python
    RAPIDAPI_HOST = "your_rapidapi_host"
    API_URL = "https://example-rapidapi.p.rapidapi.com/api"
    ```

## Running the App

1. **Run the Flask development server:**

    ```bash
    flask run
    ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

## Project Structure

```
flask-rapidapi-starter/
│
├── app.py               # Main Flask app file
├── config.py            # Configuration file for API settings
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (ignored in version control)
├── templates/           # HTML templates for the app
└── static/              # Static files (CSS, JS, images)
```

## Usage

- **Home Page:**
  - Displays a form to input data that will be sent to the external API.
  
- **API Integration:**
  - Sends the user input to the configured RapidAPI endpoint and displays the response.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

