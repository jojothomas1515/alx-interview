# interview question

## making change
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total

## Prototype
```python
def makeChange(coins: list, total: int) -> int
```
## Returns 
The fewest number of coin needed to meet  $total$

If total is 0 or less than 0 return 0.
If total cannot be met by any number of coin int the coins list return -1
## Notes
* The value of a coin will always be an integer greater than 0
* You can assume you have an infinite number of each denomination of coin in the list
*Your solution’s runtime will be evaluated in this task
