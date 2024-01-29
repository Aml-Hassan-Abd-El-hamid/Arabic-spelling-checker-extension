# Arabic-spelling-checker-extension
That project started as a task from WideBot comapny, that was the email that I recived:

```
For our second task, we're looking at spelling correction - a vital feature for any text-based service. Your mission is to build a super-efficient spelling correction API. It should take a word as input and return a list of probable corrections, sorted by likelihood, or the word itself if it's already correct. Wrap this functionality up nicely in an API, and you're golden!

Constraints<br>
* The response time for each word should be between 50-200 ms.
* Feel free to use any technique or approach - whether it's a ready-made solution or something you build from scratch. We're looking for efficiency and precision.
```

I chose to go with Flask giving the fact that I had an experience using it in that [cute project](https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website) I actully can't remember anything regarding Flask from it but at least I can use the codebase from it.

Due to some calculation issue, I have 1 day to finish that project, I found a very fast starting solution by using that library called [ar_corrector](https://github.com/basselkassem/ar_corrector) and even given the time constraints it was still a valid solution!

### Note: That's how I measured the time
```
import time
from ar_corrector.corrector import Corrector

corr = Corrector()

start = time.time()

corr.spell_correct('بختب')

end = time.time()

print(end - start)
```