import json, os, collections, string

class Commonwords:
    def makewords(self):
        ipath = os.path.abspath("D:/Programming/Data/RC_2017-11/finalized1m.json")
        opath = os.path.abspath("D:/Programming/Data/RC_2017-11/common_words.json")

        wordcount = dict()
        with open(ipath) as f:
            for line in f:
                curline = json.loads(line)
                comment = curline['body']
                for token in comment:
                    if token not in wordcount:
                        wordcount[token] = 1
                    else:
                        wordcount[token] += 1

            counter = collections.Counter(wordcount)

            with open(opath, "w") as f2:
                    newjson = {}
                    newjson['commonwords'] = counter.most_common(100)

                    f2.write(json.dumps(newjson))
                