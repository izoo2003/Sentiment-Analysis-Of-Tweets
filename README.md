# Twitter Sentiment Analysis Pipeline

A Python-based NLP project that processes Twitter data to classify public sentiment and evaluate model performance.

## 📌 Project Overview
This project extracts insights from a dataset of tweets, categorizing them into **Positive**, **Negative**, and **Neutral** sentiments. It utilizes Python's data science stack to perform text preprocessing, sentiment classification, and statistical evaluation.

## 📊 Key Features
* **Data Processing:** Cleaned and parsed raw tweet data from CSV format.
* **Sentiment Classification:** Leveraged NLP libraries to categorize text into three distinct fields.
* **Performance Metrics:** Calculated **Accuracy** and **Precision** ratings to validate model reliability.
* **Data Visualization:** Generated distribution charts and performance graphs using **Matplotlib**.

## 📂 File Structure
* `Sentiment_Analysis.ipynb`: The core Jupyter Notebook containing the analysis logic and visualizations.
* `twitter_training.csv`: The dataset containing the tweet statements used for training/testing.
* `tweetclaw_to_training_csv.py`: Optional converter for TweetClaw JSON, JSONL, NDJSON, or CSV exports.
* `README.md`: Project documentation.

## 🛠️ Requirements
To run this project, you will need the following Python libraries:
* `pandas`
* `matplotlib`
* `nltk` (or `textblob`/`vaderSentiment` depending on your specific script)
* `scikit-learn`

## 🚀 How to Use
1. Clone this repository to your local machine.
2. Ensure `twitter_training.csv` is in the same directory as the notebook.
3. Open `Sentiment_Analysis.ipynb` in Jupyter Notebook or Google Colab.
4. Run all cells to see the analysis and generated charts.

## Optional TweetClaw Export Input
TweetClaw can collect public X/Twitter search results from OpenClaw with explicit user approval. To try those exports in this notebook, convert a TweetClaw export into the same 4-column CSV shape used by `twitter_training.csv`:

```bash
python3 tweetclaw_to_training_csv.py tweetclaw-export.jsonl \
  --topic "Brand Monitor" \
  --sentiment Neutral \
  --output tweetclaw_training.csv
```

The converter accepts `.json`, `.jsonl`, `.ndjson`, and `.csv` files. It writes `Tweet_ID`, `Topic`, `Sentiment`, and `Tweet_Content`, skips blank tweet text, and de-duplicates repeated text. Use `--overwrite` only when replacing a generated output file is intentional.

TweetClaw exports usually do not contain human-verified sentiment labels. The `--sentiment` value is a notebook-compatible placeholder for exploration, not a ground truth label for accuracy or precision claims.
