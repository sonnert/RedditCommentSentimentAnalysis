Working solution. Exchange abs paths or add argparse solution, I'm running in VS debugger atm.

Before running, reddit data needs to be downloaded from pushfiles.io. Then run, in order:
```
Parser        .parse
              (.count checks number of parsed comments)
              (.checkdate prints date of every millionth comment)
Preprocessor  .score 
              .finalize
Commonwords   .makewords
```


Now, run 
```
Analyzer      .analyze
```
any number of times.
