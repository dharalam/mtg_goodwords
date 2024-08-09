# MTG Goodwords
![Goodwords logo](static/mtg_goodwords_logo.jpg)

Hello everyone! I created MTG Goodwords as a personal project for fun that will allow anyone to assess the relative "goodness" of any Magic: the Gathering card given information on it.

## Goodwords Feature Roadmap
Here is a list of features that I have implemented and that I hope to implement in the future
- [x] Web App interface
- [x] Text Classification model for ratings
- [ ] Card database
- [ ] Card lookup by name (fuzzy search)
- [ ] Form field autofill for cards in database
- [ ] Card images for cards in database
- [ ] Similarity reports
- [ ] Accounts
- [ ] Community Rankings
- [ ] Updated model

## Technical Stuff
I created the initial dataset by using Gatherer Extractor (available for download [here](https://www.mtgsalvation.com/forums/magic-fundamentals/other-magic-products/third-party-products/337224-mtg-gatherer-extractor-v7-3c-database-pics)), which allows for anyone to pull data straight from Magic: the Gathering's official card database, [Gatherer](https://gatherer.wizards.com/Pages/Default.aspx), and a popular fan database [Scryfall](https://scryfall.com/). I then prepared and cleaned the dataset, shown in the attached [jupyter notebook](all_mtg_cards_sentiment_analysis.ipynb). You can find the final output of the data cleaning [here](https://huggingface.co/datasets/dharalam/mtg_goodwords_full). The ratings for each card were pulled from Gatherer, and are therefore subject to inaccuracies or biases. I used Hugging Face's transformers API and fine-tuned a pre-trained DistilBERT model trained on the full card text minus the flavor text (if applicable). Two models were trained for this project. The first was trained only on the samples that already had ratings, and was used to classify all samples that did not have a rating. The second model was trained on the rated samples and classified samples combined into a single dataset, and is used for all the predictions the application makes. Because of this, I must acknowledge that there may be significant bias involved in the ranking of the cards. The distribution of the rankings of cards in the full dataset is greatly skewed towards a rank of 5/6, coming in at about 65% of the samples. The second most frequent rating is a 4/6, at only 17.1%. The highest (6/6) and lowest (0/6) ends of the rankings appear in <0.17% and <0.1% of the samples respectively.
