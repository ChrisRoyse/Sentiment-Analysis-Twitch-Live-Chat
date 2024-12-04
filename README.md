
# Twitch Data Sentiment Analysis

A Python-based tool that performs sentiment analysis on Twitch chat data. This script processes a dataset containing Twitch messages, analyzes the sentiment of each message using multiple sentiment analysis libraries, and aggregates the results on a daily and weekly basis. The final sentiment scores are saved into separate CSV files for further analysis.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Environment Setup](#environment-setup)
  - [Prerequisites](#prerequisites)
  - [Step-by-Step Setup Guide](#step-by-step-setup-guide)
    - [1. Install Python](#1-install-python)
    - [2. Create a Virtual Environment (Optional but Recommended)](#2-create-a-virtual-environment-optional-but-recommended)
    - [3. Upgrade pip](#3-upgrade-pip)
    - [4. Install Required Python Packages](#4-install-required-python-packages)
    - [5. Download Additional NLTK Data](#5-download-additional-nltk-data)
- [Usage](#usage)
  - [1. Prepare Your Dataset](#1-prepare-your-dataset)
  - [2. Configure the Script](#2-configure-the-script)
  - [3. Run the Script](#3-run-the-script)
  - [4. View the Results](#4-view-the-results)
- [Sample Output](#sample-output)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This tool automates the sentiment analysis of Twitch chat data by leveraging multiple sentiment analysis libraries. By processing large datasets of Twitch messages, it provides insights into the overall sentiment trends on a daily and weekly basis. The results are saved into CSV files, making it easy to visualize and analyze the sentiment data.

## Features

- **Multiple Sentiment Analysis Methods:** Utilizes NLTK's Vader, TextBlob, and Afinn for comprehensive sentiment analysis.
- **Large Dataset Processing:** Efficiently handles large CSV files containing Twitch messages.
- **Daily and Weekly Aggregation:** Aggregates sentiment scores on both daily and weekly intervals.
- **Detailed Logging:** Maintains logs of the scraping and analysis process for easy debugging and monitoring.
- **CSV Output:** Generates separate CSV files for each sentiment analysis method with aggregated results.

## Environment Setup

Setting up the environment correctly is crucial for the smooth running of this tool. Follow the step-by-step guide below to set up your environment on a Windows machine.

### Prerequisites

- **Operating System:** Windows 10 or higher
- **Python:** Version 3.6 or higher
- **Git:** For cloning the repository (optional)

### Step-by-Step Setup Guide

#### 1. Install Python

Ensure Python 3.6 or higher is installed on your system. You can download it from the [official website](https://www.python.org/downloads/).

After installation, verify the installation by running:

```bash
python --version
```

#### 2. Create a Virtual Environment (Optional but Recommended)

It's good practice to use a virtual environment to manage dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

- **Command Prompt:**

  ```bash
  venv\Scripts\activate
  ```

- **PowerShell:**

  ```powershell
  .\venv\Scripts\Activate.ps1
  ```

#### 3. Upgrade pip

Ensure you have the latest version of pip:

```bash
pip install --upgrade pip
```

#### 4. Install Required Python Packages

Create a `requirements.txt` file with the following content:

```plaintext
requests
beautifulsoup4
nltk
textblob
afinn
```

Then, install the dependencies:

```bash
pip install -r requirements.txt
```

#### 5. Download Additional NLTK Data

The script requires specific NLTK datasets. Run the following Python commands:

```python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
```

Alternatively, you can run the script once, and it will download the necessary NLTK data automatically.

## Usage

### 1. Prepare Your Dataset

Ensure you have a CSV file containing Twitch data with at least the following columns:

- `timestamp`: The timestamp of the message in the format `%Y-%m-%dT%H:%M:%S.%fZ` (e.g., `2023-10-12T14:23:45.123Z`).
- `messageText`: The text content of the Twitch message.

**Example Directory Structure:**

```plaintext
your-repo-name/
├── dataset/
│   └── twitch_data1.csv
├── sentiment_analysis.py
├── requirements.txt
└── README.md
```

### 2. Configure the Script

Open `sentiment_analysis.py` and update the following line to match the path to your input CSV file:

```python
input_file = 'd:/twitchdata/dataset/twitch_data1.csv'
```

If your dataset is located elsewhere, modify the `input_file` path accordingly.

### 3. Run the Script

Execute the script using Python:

```bash
python sentiment_analysis.py
```

The script will perform the following actions:

1. Initialize sentiment analyzers (Vader, TextBlob, Afinn).
2. Open and process the input CSV file line by line.
3. Calculate sentiment scores for each message using the specified methods.
4. Aggregate sentiment scores daily and weekly.
5. Save the aggregated results into separate CSV files for each sentiment analysis method.

### 4. View the Results

After the script completes execution, navigate to the directory where the script was run. You will find the following output CSV files:

- `vader_sentiment.csv`
- `textblob_sentiment.csv`
- `afinn_sentiment.csv`

These files contain the aggregated sentiment scores categorized by period (Daily or Weekly) and sentiment type.

**Example `vader_sentiment.csv`:**

| Period    | Type   | Average_Sentiment |
|-----------|--------|--------------------|
| 2023-10-12| Daily  | 0.25               |
| 2023-W42  | Weekly | 0.30               |
| ...       | ...    | ...                |

## Sample Output

Below is a sample of the output CSV file for Vader sentiment analysis:

**vader_sentiment.csv**

| Period     | Type   | Average_Sentiment |
|------------|--------|--------------------|
| 2023-10-12 | Daily  | 0.25               |
| 2023-10-13 | Daily  | 0.10               |
| 2023-W42   | Weekly | 0.18               |
| 2023-W43   | Weekly | 0.22               |
| ...        | ...    | ...                |

Each CSV file follows a similar structure, providing an easy-to-analyze format for sentiment trends over time.

## Dependencies

- **Python 3.6 or Higher**

- **Python Libraries:**
  - [requests](https://pypi.org/project/requests/)
  - [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
  - [nltk](https://www.nltk.org/)
  - [TextBlob](https://textblob.readthedocs.io/en/dev/)
  - [Afinn](https://pypi.org/project/afinn/)

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## Configuration

- **Input File Path:**

  Ensure the `input_file` variable in the script points to the correct path of your input CSV file.

  ```python
  input_file = 'd:/twitchdata/dataset/twitch_data1.csv'
  ```

- **Output Directory:**

  By default, the script saves the output CSV files in the current working directory. To change this, modify the `output_files` paths in the script.

  ```python
  output_files = {
      'Vader': 'vader_sentiment.csv',
      'TextBlob': 'textblob_sentiment.csv',
      'Afinn': 'afinn_sentiment.csv',
  }
  ```

- **Logging Configuration:**

  The script logs detailed information to `sentiment_analysis.log` in the current working directory. You can change the log file location by modifying the `filename` parameter in the `logging.basicConfig` setup:

  ```python
  logging.basicConfig(
      filename='path/to/your/sentiment_analysis.log',
      level=logging.INFO,
      format='%(asctime)s:%(levelname)s:%(message)s'
  )
  ```

## Troubleshooting

- **Missing Dependencies:**

  - **Issue:** Import errors for missing Python libraries.
  - **Solution:** Ensure all required packages are installed by running `pip install -r requirements.txt`.

- **NLTK Data Errors:**

  - **Issue:** The script cannot find NLTK data like `vader_lexicon`.
  - **Solution:** Ensure you have downloaded the necessary NLTK data by running the following in Python:

    ```python
    import nltk
    nltk.download('vader_lexicon')
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    ```

- **File Not Found:**

  - **Issue:** The input CSV file path is incorrect.
  - **Solution:** Verify that the `input_file` path in the script points to the correct location of your dataset.

- **Permission Issues:**

  - **Issue:** The script cannot create or write to output directories/files.
  - **Solution:** Run the script with appropriate permissions or choose an output directory where you have write access.

- **Encoding Errors:**

  - **Issue:** Errors related to file encoding when reading or writing CSV files.
  - **Solution:** Ensure that your CSV files are encoded in UTF-8. You can specify the encoding in the script if necessary.

- **Performance Issues:**

  - **Issue:** The script is running slowly with large datasets.
  - **Solution:** Ensure your machine has sufficient resources. Consider optimizing the script or processing the data in smaller batches.

## Contributing

Contributions are welcome! Please follow these steps to contribute to the project:

1. **Fork the Repository**

2. **Create a New Branch**

   ```bash
   git checkout -b feature/YourFeature
   ```

3. **Commit Your Changes**

   ```bash
   git commit -m "Add your feature"
   ```

4. **Push to the Branch**

   ```bash
   git push origin feature/YourFeature
   ```

5. **Open a Pull Request**

   Describe your changes and submit the pull request for review.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Happy Analyzing! 📊*
```
