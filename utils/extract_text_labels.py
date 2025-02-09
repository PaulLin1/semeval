import pandas
import numpy
import json

emotions = ['anger', 'fear', 'joy', 'sadness', 'surprise']

def extract_features_labels(df):
    train_labels = train_df[emotions].values.tolist()
    train_text = train_df['text'].tolist()

    data = {}

    for t, l in zip(train_labels, train_text):
        examples[i] = {
            'text' = t,
            'label' = l,
        }

    with open("../data/train_features_labels.json", "w") as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    train_df = pd.read_csv('../data/train.csv')
    extract_features_labels(train_df)
