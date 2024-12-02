import csv
import logging
import datetime
from collections import defaultdict
# Sentiment Analysis Libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
from afinn import Afinn
# from nltk.corpus import sentiwordnet as swn  # Commented out for now
from nltk.tokenize import word_tokenize
from nltk import pos_tag, download

# Download necessary NLTK data
# Commented out since packages are already up-to-date
# nltk.download('vader_lexicon')
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('sentiwordnet')
# nltk.download('averaged_perceptron_tagger')

# Setup logging
print('Setting up logging...')
logging.basicConfig(filename='sentiment_analysis.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
print('Logging is set up.')

def sentiwordnet_score(text):
    # Commented out for diagnostic purposes
    pass

def pattern_sentiment(text):
    try:
        from pattern.en import sentiment
        score = sentiment(text)[0]
        return score
    except ImportError:
        return None

def main():
    print('Entered main function.')
    input_file = 'd:/twitchdata/dataset/twitch_data1.csv'
    
    # Output files for each method
    output_files = {
        'Vader': 'vader_sentiment.csv',
        'TextBlob': 'textblob_sentiment.csv',
        'Afinn': 'afinn_sentiment.csv',
        # 'SentiWordNet': 'sentiwordnet_sentiment.csv',  # Commented out
        # 'Pattern': 'pattern_sentiment.csv',  # Uncomment if using Pattern library
    }

    # Initialize sentiment analyzers
    print('Initializing sentiment analyzers...')
    logging.info('Initializing sentiment analyzers...')
    vader_analyzer = SentimentIntensityAnalyzer()
    print('Vader analyzer initialized.')
    afinn_analyzer = Afinn()
    print('Afinn analyzer initialized.')

    methods = ['Vader', 'TextBlob', 'Afinn']
    analyzers = {
        'Vader': lambda text: vader_analyzer.polarity_scores(text)['compound'],
        'TextBlob': lambda text: TextBlob(text).sentiment.polarity,
        'Afinn': lambda text: afinn_analyzer.score(text) / 10,  # Normalize if necessary
        # 'SentiWordNet': sentiwordnet_score,  # Commented out
        # 'Pattern': pattern_sentiment,  # Uncomment if using Pattern library
    }

    # Data structures to hold sentiment totals and counts
    daily_totals = {method: defaultdict(float) for method in methods}
    daily_counts = {method: defaultdict(int) for method in methods}
    weekly_totals = {method: defaultdict(float) for method in methods}
    weekly_counts = {method: defaultdict(int) for method in methods}

    # Open output CSV files
    output_writers = {}
    for method in methods:
        csvfile = open(output_files[method], 'w', newline='', encoding='utf-8')
        writer = csv.DictWriter(csvfile, fieldnames=['Period', 'Type', 'Average_Sentiment'])
        writer.writeheader()
        output_writers[method] = (csvfile, writer)
    print('Output CSV files are ready.')

    # Open the input CSV file
    logging.info('Starting to process the CSV file...')
    print('Opening input CSV file...')
    with open(input_file, 'r', encoding='utf-8') as csvfile:
        print('Input CSV file opened.')
        reader = csv.DictReader(csvfile)
        line_count = 0

        for row in reader:
            line_count += 1
            try:
                timestamp = row['timestamp']
                message = row['messageText']

                # Parse timestamp to get date and week number
                date_obj = datetime.datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
                date_str = date_obj.date().isoformat()
                week_str = f"{date_obj.isocalendar()[0]}-W{date_obj.isocalendar()[1]}"

                # Calculate sentiment scores using each method
                for method in methods:
                    score = analyzers[method](message)
                    if score is not None:
                        daily_totals[method][date_str] += score
                        daily_counts[method][date_str] += 1
                        weekly_totals[method][week_str] += score
                        weekly_counts[method][week_str] += 1

                if line_count % 100000 == 0:
                    logging.info(f'Processed {line_count} lines.')
                    print(f'Processed {line_count} lines.')

            except Exception as e:
                logging.error(f'Error processing line {line_count}: {e}')
                print(f'Error processing line {line_count}: {e}')

    logging.info('Finished processing CSV file.')
    print('Finished processing CSV file.')

    # Write averages to output files
    logging.info('Calculating averages and writing to output files...')
    print('Calculating averages and writing to output files...')
    for method in methods:
        csvfile, writer = output_writers[method]

        # Write daily averages
        for date_str in sorted(daily_totals[method].keys()):
            if daily_counts[method][date_str] > 0:
                average = daily_totals[method][date_str] / daily_counts[method][date_str]
                writer.writerow({
                    'Period': date_str,
                    'Type': 'Daily',
                    'Average_Sentiment': average
                })

        # Write weekly averages
        for week_str in sorted(weekly_totals[method].keys()):
            if weekly_counts[method][week_str] > 0:
                average = weekly_totals[method][week_str] / weekly_counts[method][week_str]
                writer.writerow({
                    'Period': week_str,
                    'Type': 'Weekly',
                    'Average_Sentiment': average
                })

        # Close the output file
        csvfile.close()

    logging.info('Sentiment analysis completed successfully.')
    print('Sentiment analysis completed successfully.')

if __name__ == "__main__":
    main()
