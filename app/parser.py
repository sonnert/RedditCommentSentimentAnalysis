import sys, json, os, time, datetime

class Parser:
    def __init__(self):
        self.ipath = os.path.abspath("D:/Programming/Data/RC_2017-11/RC_2017-11.json")
        self.opath = os.path.abspath("D:/Programming/Data/RC_2017-11/Nov2017.json")

    def parse(self):
        print("Starting parser")
        start_time = time.time()

        with open(self.ipath) as f:
            for line in f:
                curline = json.loads(line)
                secs = curline["created_utc"]
                date = time.gmtime(secs)
            
                if (date.tm_year == 2017 and date.tm_mon == 11):
                    newjson = {}
                    newjson['created_utc'] = curline['created_utc']
                    newjson['subreddit'] = curline['subreddit']
                    newjson['score'] = curline['score']
                    newjson['body'] = curline['body']

                    with open(self.opath, "a") as f2:
                        f2.write(json.dumps(newjson))
                        f2.write('\n')

            print("Finished in:")
            secs = time.time() - start_time
            print(str(datetime.timedelta(seconds=secs)))

    def count(self):
        print("Starting counter")
        start_time = time.time()

        with open(self.opath) as f:
            for i, l in enumerate(f):
                pass

            print("Finished in:")
            secs = time.time() - start_time
            print(str(datetime.timedelta(seconds=secs)))
            print("Lines:")
            # 13 255 383 comments (non-completed)
        return i + 1

    def checkdate(self): 
        i = 0
        j = 0
        with open(self.opath) as f:
            for line in f:
                curline = json.loads(line)
                i = i+1
                if (i == 1000000):
                    j += 1
                    print(j, "millionth date:")
                    print(
        datetime.datetime.fromtimestamp(
            int(curline['created_utc'])
        ).strftime('%Y-%m-%d %H:%M:%S')
    )
                    i = 0
