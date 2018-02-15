import nltk, os, json, time, string, datetime
import nltk.sentiment
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

class Preprocessor:
    def __init__(self):
        self.ipath = os.path.abspath("D:/Programming/Data/RC_2017-11/Nov2017.json")
        self.opathv = os.path.abspath("D:/Programming/Data/RC_2017-11/vadered1m.json")
        self.opathf = os.path.abspath("D:/Programming/Data/RC_2017-11/finalized1m.json")

    def score(self):
        print("Starting vader polarity scoring")
        start_time = time.time()

        with open(self.ipath) as f:
            head = [next(f) for x in range(1000000)]
            with open(self.opathv, "a") as f2:
                for line in head:
                    curline = json.loads(line)
                    comment = curline['body']

                    vader = nltk.sentiment.vader.SentimentIntensityAnalyzer()

                    newline = {}
                    newline['vader'] = vader.polarity_scores(comment)
                    newline['body'] = comment

                    f2.write(json.dumps(newline))
                    f2.write('\n')

            print("Finished in:")
            secs = time.time() - start_time
            print(str(datetime.timedelta(seconds=secs)))

    def finalize(self):
        print("Starting raw score assessment and tokenization")
        start_time = time.time()

        with open(self.ipath) as f:
            with open(self.opathf, "a") as f2:
                for line in f:
                    curline = json.loads(line)
                    comment = curline['body']
                    rawscore = curline['vader']
                    stop_words = set(stopwords.words('english'))
                    punctuator = comment.maketrans('', '', string.punctuation)
                    tokenizer = RegexpTokenizer(r'\w+')

                    no_punc = comment.translate(punctuator)
                    lowered = no_punc.lower()
                    tokenized = tokenizer.tokenize(lowered)
                    no_stopw = [w for w in tokenized if not w in stop_words]

                    newline = {}
                    if rawscore['compound'] >= 0.5:
                        newline['score'] = "POS"
                    elif rawscore['compound'] <= -0.5:
                        newline['score'] = "NEG"
                    else:
                        newline['score'] = "NEU"

                    newline['body'] = no_stopw

                    f2.write(json.dumps(newline))
                    f2.write('\n')

            print("Finished in:")
            secs = time.time() - start_time
            print(str(datetime.timedelta(seconds=secs)))