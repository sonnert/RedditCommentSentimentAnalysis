from app.preprocessor import Preprocessor
from app.analyzer import Analyzer
from app.commonwordfilter import Commonwords
from app.parser import Parser

parser = Parser()
#parser.parse()

preprocessor = Preprocessor()
#preprocessor.score()
#preprocessor.finalize()

commonwordfilter = Commonwords()
#commonwordfilter.makewords()

analyzer = Analyzer()
analyzer.analyze()