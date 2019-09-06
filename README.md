# Twitter Stream Exploratory Visualization Analysis

### Intro

This project uses PySpark, Tweepy, and Plotly to create a visualization sentimental analysis on the Twitter tweets. You are able to choose what words you want your tweets to be about, and perform various operations on them.

### Run the analysis

To run the analysis, you need to first get a Twitter developer account, create an app, and generate your Consumer API keys, as well as your Access tokens. This could be found [here](https://developer.twitter.com/en/docs/basics/authentication/guides/access-tokens.html). Include this information in this [file](/your_twitter_credentials.json). Next, you can open up the Jupyter Notebook and follow the instructions there.

### Note

For my stream, I filtered to stream only English tweets that contained the words "instagram", "facebook", or "twitter". I chose not to save the tweets on disk and instead loaded it from Spark to memory because this notebook is not intended for reproducible results, but rather reproducible procedure. This means that, every time I run this project, my collected tweets would be different and would result in different visualizations.

#### Future Plans
- Plotly Dash
