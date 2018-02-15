import string, collections, json, os

class Analyzer:
    def analyze(self):
        ipathf = os.path.abspath("D:/Programming/Data/RC_2017-11/finalized1m.json")
        ipathc = os.path.abspath("D:/Programming/Data/RC_2017-11/common_words.json")

        with open(ipathc) as f3:
            cdata = json.load(f3)
        clist = cdata['commonwords']
        clist2 = [i[0] for i in clist]
        commonwords = set(clist2)

        while True:
            term = input("Term to analyze: ")
            term = term.lower()
            print("Analyzing", term, "...")

            pos = 0
            neg = 0
            neu = 0
            wordcount_pos = dict()
            wordcount_neg = dict()
            wordcount_neu = dict()

            with open(ipathf) as f:
                for line in f:
                    curline = json.loads(line)
                    comment = curline['body']
                    score = curline['score']
                    
                    if term in comment:
                        if score == 'POS':
                            pos += 1
                            for token in comment:
                                if token != term and token not in commonwords:
                                    if token not in wordcount_pos:
                                        wordcount_pos[token] = 1
                                    else:
                                        wordcount_pos[token] += 1
                        elif score == 'NEG':
                            neg += 1
                            for token in comment:
                                if token != term and token not in commonwords:
                                    if token not in wordcount_neg:
                                        wordcount_neg[token] = 1
                                    else:
                                        wordcount_neg[token] += 1
                        else:
                            neu += 1
                            for token in comment:
                                if token != term and token not in commonwords:
                                    if token not in wordcount_neu:
                                        wordcount_neu[token] = 1
                                    else:
                                        wordcount_neu[token] += 1

                total = pos + neg + neu
                counter_pos = collections.Counter(wordcount_pos)
                counter_neg = collections.Counter(wordcount_neg)
                counter_neu = collections.Counter(wordcount_neu)
                topwords_pos = counter_pos.most_common(3)
                topwords_neg = counter_neg.most_common(3)
                topwords_neu = counter_neu.most_common(3)

                print("*****")
                print("Term analyzed:", term)
                if total == 0:
                    print("No occurences of term")
                else:
                    print(term, "appeared in", total, "comments.")
                    print("Positive score:", "{0:.0f}%".format(pos/total * 100))
                    print("Neutral score:", "{0:.0f}%".format(neu/total * 100))
                    print("Negative score:", "{0:.0f}%".format(neg/total * 100))
                    if pos != 0:
                        print("Top 3 positive words:", topwords_pos)
                    if neu != 0:
                        print("Top 3 neutral words:", topwords_neu)
                    if neg != 0:
                        print("Top 3 negative words:", topwords_neg)
                print("*****")
