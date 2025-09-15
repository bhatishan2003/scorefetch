# scorefetch <!-- omit in toc -->

A simple Python CLI tool to fetch live weather data from any city using the OpenWeather API.

![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
[![Python CI](https://github.com/bhatishan2003/scorefetch/actions/workflows/python-app.yml/badge.svg)](https://github.com/bhatishan2003/scorefetch/actions/workflows/python-app.yml)

## Table of Contents <!-- omit in toc -->

- [Installation](#installation)
  - [Create and activate a virtual environment:](#create-and-activate-a-virtual-environment)
- [Usage](#usage)
  - [Command Line Usage](#command-line-usage)

---

## Installation

-   Clone the repository:

    ```bash
    git clone https://github.com/bhatishan2003/scorefetch
    cd scorefetch
    ```

### Create and activate a virtual environment:

1. **Create a Virtual Environment [Optional, but recommended]**

    Run the following command to create a [virtual environment](https://docs.python.org/3/library/venv.html):

    ```bash
    python3 -m venv .venv
    ```

-   **Activate:**

    -   **Windows (PowerShell):**

        ```bash
        .venv\Scripts\activate
        ```

    -   **Linux/Mac (Bash):**

        ```bash
        source .venv/bin/activate
        ```

-   **Deactivate:**

    ```bash
    deactivate
    ```

-   **Install the package:**

    ```bash
    pip install .
    ```

-   **For development (editable mode):**

    ```bash
    pip install -e .
    ```

## Usage

### Command Line Usage

-   Following commands should be entered to get live score

    -   To get list of currently available matches.

        ```bash
        scorefetch --list
        ```

    -   To get live match score we want to see from the list.
        ```bash
        scorefetch --match 1
        ```
