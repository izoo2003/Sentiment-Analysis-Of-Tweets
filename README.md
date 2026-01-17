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
