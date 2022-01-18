# Stats

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
