# Arabic-spelling-checker-extension
That project started as a task from WideBot company, that was the email that I received:

```
For our second task, we're looking at spelling correction - a vital feature for any text-based service. Your mission is to build a super-efficient spelling correction API. It should take a word as input and return a list of probable corrections, sorted by likelihood, or the word itself if it's already correct. Wrap this functionality up nicely in an API, and you're golden!

Constraints:
* The response time for each word should be between 50-200 ms.
* Feel free to use any technique or approach - whether it's a ready-made solution or something you build from scratch. We're looking for efficiency and precision.
```

I chose to go with Flask given the fact that I had an experience using it in that [cute project](https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website) I actually can't remember anything regarding Flask from it but at least I can use the codebase from it.

Due to some calculation issue, I had 1 day to finish that project, I found a very fast starting solution by using that library called [ar_corrector](https://github.com/basselkassem/ar_corrector) and even given the time constraints it was still a valid solution!

So the only thing left to do here is to remember how to actually build API! I found those 2 tutorials on LinkedIn learning that are really good and love to share them here in order to go back to them in case I need any refreshers on Flask in the future -that's very useful given the fact that I have such a short memory-:<br>
1- [Flask essential training](https://www.linkedin.com/learning/flask-essential-training)<br>
2- [Building RESTful APIs with Flask](https://www.linkedin.com/learning/building-restful-apis-with-flask)

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
![Screenshot from 2024-01-29 18-33-12](https://github.com/Aml-Hassan-Abd-El-hamid/Arabic-spelling-checker-extension/assets/66205928/accd9ab1-e3ec-44c2-a0fb-ffb5152e4580)
