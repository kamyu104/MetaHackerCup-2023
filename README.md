# [MetaHackerCup-2023](https://www.facebook.com/hackercup/past_rounds/) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-12%20%2F%2012-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.metahackercup.2023)

* Python3 solutions of Meta Hacker Cup 2023. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8`, which is not friendly for Python3 to solve in 5 ~ 15 seconds. A `6-minute` timer is set for uploading the result this year.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.


## Rounds

* [Hacker Cup 2022](https://github.com/kamyu104/MetaHackerCup-2022)
* [Practice Round](https://github.com/kamyu104/MetaHackerCup-2032#practice-round)
* [Round 1](https://github.com/kamyu104/MetaHackerCup-2032#round-1)

## Practice Round
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A1| [Cheeseburger Corollary 1](https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A1)| [Python3](./Practice%20Round/cheeseburger_corollary_1.py3) | _O(1)_ | _O(1)_ | Easy | | Math |
|A2| [Cheeseburger Corollary 2](https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/A2)| [Python3](./Practice%20Round/cheeseburger_corollary_2.py3) | _O(1)_ | _O(1)_ | Medium | | Math |
|B| [Dim Sum Delivery](https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/B)| [Python3](./Practice%20Round/dim_sum_delivery.py3) | _O(1)_ | _O(1)_ | Easy | | Game |
|C| [Two Apples a Day](https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/C)| [Python3](./Practice%20Round/two_apples_a_day.py3) | _O(NlogN)_ | _O(1)_ | Easy | | Sort, Two Pointers |
|D| [Road to Nutella](https://www.facebook.com/codingcompetitions/hacker-cup/2023/practice-round/problems/D)| [Python3](./Practice%20Round/road_to_nutella.py3) [Python3](./Practice%20Round/road_to_nutella2.py3) | _O(N + M + QlogQ)_ | _O(N + M + Q)_ | Hard | | `Tarjan's Algorithm`, Biconnected Components, DFS, Bipartite Coloring, BFS, LCA, Binary Lifting, Counting Sort, Union Find, DSU |

## Round 1
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Here Comes Santa Claus](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/A)| [Python3](./Round%201/here_comes_santa_claus.py3) | _O(N)_ | _O(1)_ | Easy | | Math |
|B1| [Sum 41 (Chapter 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1)| [Python3](./Round%201/sum_41_chapter_1.py3) [Python3](./Round%201/sum_41_chapter_1-2.py3) [Python3](./Round%201/sum_41_chapter_1-3.py3) | precompute: _O(sqrt(MAX_P))_<br> runtime: _O(logP + sqrt(P)/log(sqrt(P)))_ | _O(sqrt(MAX_P) + K)_ | Easy | | Constructive Algorithms, Greedy, Number Theory, `Linear Sieve of Eratosthenes`, Backtracking, Unique Partitions |
|B2| [Sum 41 (Chapter 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B2)| [Python3](./Round%201/sum_41_chapter_2.py3) [Python3](./Round%201/sum_41_chapter_2-2.py3) | _O(89166 + K^2)_ | _O(K)_ | Medium | | Backtracking, Unique Partitions |
|C1| [Back in Black (Chapter 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C1)| [Python3](./Round%201/back_in_black_chapter_1.py3) | _O(NlogN + Q)_ | _O(N)_ | Easy | | Number Theory, Greedy |
|C2| [Back in Black (Chapter 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C2)| [Python3](./Round%201/back_in_black_chapter_2.py3) | _O(NlogN + Q)_ | _O(N)_ | Medium | | Number Theory, Greedy |
|D| [Today is Gonna be a Great Day](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/D)| [Python3](./Round%201/today_is_gonna_be_a_great_day.py3) | _O(NlogN + QlogN)_ | _O(N)_ | Medium | | Segment Tree |
|E| [Bohemian Rap-sody](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/E)| [PyPy3](./Round%201/bohemian_rapsody.py3) | _O(QlogN + QlogQ + (L + Q) * sqrt(N))_ | _O(Q + N)_ | Hard | | Trie, Offline Solution, Binary Search, Sqrt Decomposition, `Mo's Algorithm`, Freq Table, Prefix Sum, Math |
