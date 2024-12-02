# Twitch Live Chat Sentiment Analysis

This project performs sentiment analysis on a large dataset of Twitch.tv live chat messages collected between September 1, 2024, and November 8, 2024. It utilizes multiple sentiment analysis tools to calculate the sentiment of each message and provides average daily and weekly sentiment scores. The goal is to identify shifts in sentiment over time and highlight days with significant sentiment changes.

## Features

- **Massive Dataset Processing:** Analyzes **723 million messages** from Twitch live chats.
- **Multiple Sentiment Analysis Methods:**
  - **VADER (Valence Aware Dictionary and sEntiment Reasoner)**
  - **TextBlob**
  - **Afinn**
- **Time-Based Aggregation:** Computes average sentiment scores on a **daily** and **weekly** basis.
- **Progress Logging:** Logs processing progress and errors for transparency and debugging.
- **Output Reports:** Generates CSV files with sentiment scores for further analysis and visualization.

## Table of Contents

- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Methodology](#methodology)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Requirements

- **Python 3.x**
- **Libraries:**
  - `nltk`
  - `textblob`
  - `afinn`
  - `datetime`
  - `csv`
  - `logging`

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Twitch-Live-Chat-Sentiment-Analysis.git
   cd Twitch-Live-Chat-Sentiment-Analysis
