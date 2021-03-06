# Stats - 4266 games of Wordle

Stats for different tweaks to the solver.

## Don't penalize vowels

Vowels have normal frequency.

Unsolved Wordles: 300
Solved 92.97%
Average attempts: 4.568
1 attemps: 1
2 attemps: 117
3 attemps: 915
4 attemps: 1573
5 attemps: 947
6 attemps: 413

## Penalize vowels to 1/2 - better

Wovels have frequency lowered to 1/2:

```python
if c in {'a', 'e', 'i', 'o', 'u'}:
    f = f / 16
```

Unsolved Wordles: 206
Solved 95.17%
Average attempts: 4.402
1 attemps: 1
2 attemps: 108
3 attemps: 996
4 attemps: 1613
5 attemps: 991
6 attemps: 351

## Penalize vowels to 1/4 - better but more guesses

Wovels have frequency lowered to 1/4.

Unsolved Wordles: 195
Solved 95.43%
Average attempts: 4.492
1 attemps: 1
2 attemps: 102
3 attemps: 824
4 attemps: 1601
5 attemps: 1125
6 attemps: 418

## Penalize vowels to 1/16 - better but more guesses

Wovels have frequency lowered to 1/16.

Unsolved Wordles: 188
Solved 95.59%
Average attempts: 4.622
1 attemps: 1
2 attemps: 79
3 attemps: 636
4 attemps: 1532
5 attemps: 1339
6 attemps: 491

## Pick suggestion from possible words only - best so far

Wovels have frequency lowered to 1/16.

Unsolved Wordles: 146
Solved 96.58%
Average attempts: 4.274
1 attemps: 1
2 attemps: 126
3 attemps: 1023
4 attemps: 1714
5 attemps: 939
6 attemps: 317

## Pick one of top 3 suggestions at random - slighly worse as expected

Wovels have frequency lowered to 1/16.

Unsolved Wordles: 177
Solved 95.85%
Average attempts: 4.286
1 attemps: 1
2 attemps: 135
3 attemps: 1072
4 attemps: 1660
5 attemps: 937
6 attemps: 284

## Use "raise" as first guess

combo:

Statistics:
1 attemps: 1
2 attemps: 91
3 attemps: 1168
4 attemps: 2077
5 attemps: 657
6 attemps: 177
Unsolved Wordles: 95
Solved 97.72%
Average attempts: 3.918

## Always use "learn" and "sight" as the first two guesses - best

Wovels have frequency lowered to 1/16.
We get almost the same result with vowels frequency lowered to 1/2.

Unsolved Wordles: 121
Solved 97.16%
1 attemps: 1
2 attemps: 1
3 attemps: 1270
4 attemps: 1864
5 attemps: 776
6 attemps: 233

---

learn, sight combo:

1 attemps: 1
2 attemps: 1
3 attemps: 1017
4 attemps: 2430
5 attemps: 666
6 attemps: 117
Unsolved Wordles: 34
Solved 99.20%
Average attempts: 3.971

and if we only look at 10 suggestions, we get 5x faster runtime and slightly worse results:

Statistics:
1 attemps: 1
2 attemps: 1
3 attemps: 1059
4 attemps: 2309
5 attemps: 708
6 attemps: 137
Unsolved Wordles: 51
Solved 98.79%
Average attempts: 3.981

---

## Always use "coast" and "liner" as the first two guesses - tradeoff

These are the 10 most common characters in English based on a [webpage I found](https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html):
e a r i o t n s l c

Here are some pairs of words which cover all of them:
coast, liner
react, lions
score, latin
sonic, alert

We solve words in fewer attempts but there are now 59 more words we don't solve:

Unsolved Wordles: 180
Solved 95.78%
Average attempts: 4.210
1 attemps: 1
2 attemps: 1
3 attemps: 1399
4 attemps: 1714
5 attemps: 722
6 attemps: 249

## Always use "lions" and "earth" as the first two guesses - worse

These are the 10 most common characters in English based on another [webpage I found](https://www.wired.com/story/best-wordle-tips/):
e a r i o t n s l h (The only difference is c is replaced by h.)

Here are some pairs of words which cover all of them:
latin, horse
lions, earth
lions, heart
short, alien
stale, rhino

We solve words in fewer attempts but there are now 59 more words we don't solve:

Unsolved Wordles: 178
Solved 95.83%
Average attempts: 4.227
1 attemps: 1
2 attemps: 1
3 attemps: 1374
4 attemps: 1694
5 attemps: 757
6 attemps: 261

combo:

1 attemps: 1
2 attemps: 1
3 attemps: 1168
4 attemps: 2180
5 attemps: 681
6 attemps: 168
Unsolved Wordles: 67
Solved 98.40%
Average attempts: 3.963

## Always use "saint" and "older" as the first two guesses - tailored to our test set but still does not beat "learn" and "sight"

These are the 10 most common characters in our words file:
e s a r o l i t n d (The only difference is c got replaced by d)

Here are some pairs of words which cover all of them:
intro, deals
noted, lairs
rails, noted
saint, older
satin, older
tails, drone
tilde, sonar
tired, salon
tried, salon

This makes us more likely to solve in 3 attempts but slightly increases our unsolved count:

Unsolved Wordles: 148
Solved 96.53%
Average attempts: 4.150
1 attemps: 1
2 attemps: 1
3 attemps: 1428
4 attemps: 1745
5 attemps: 702
6 attemps: 241

## Wordle word list, fast suggestion (learn, sight)

Played 200 games of Wordle..
3 attemps: 50
4 attemps: 98
5 attemps: 42
6 attemps: 7
Played 200 games of Wordle.
Unsolved Wordles: 3
Solved 98.50%
Average attempts: 4.120

## Wordle word list, combo of fast (top 50) and then slow suggestion

raise:

Played 200 games of Wordle..
Statistics:
2 attemps: 6
3 attemps: 68
4 attemps: 110
5 attemps: 13
6 attemps: 3
Unsolved Wordles: 0
Solved 100.00%
Average attempts: 3.695

lions, earth:

Played 200 games of Wordle..
Statistics:
3 attemps: 78
4 attemps: 100
5 attemps: 19
6 attemps: 2
Unsolved Wordles: 1
Solved 99.50%
Average attempts: 3.724

Played 2315 games of Wordle..
Statistics:
2 attemps: 1
3 attemps: 816
4 attemps: 1253
5 attemps: 206
6 attemps: 32
Unsolved Wordles: 7
Solved 99.70%
Average attempts: 3.763

lions, earth naive:

Played 2315 games of Wordle..
Statistics:
2 attemps: 1
3 attemps: 837
4 attemps: 1012
5 attemps: 365
6 attemps: 82
Unsolved Wordles: 18
Solved 99.22%
Average attempts: 3.865

## Wordle word list, optimal (very slow)

Played 200 games of Wordle..
Statistics:
2 attemps: 5
3 attemps: 65
4 attemps: 114
5 attemps: 16
Unsolved Wordles: 0
Solved 100.00%
Average attempts: 3.705
