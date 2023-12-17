# [MetaHackerCup-2023](https://www.facebook.com/codingcompetitions/hacker-cup) ![Language](https://img.shields.io/badge/language-Python3-orange.svg) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE) ![Progress](https://img.shields.io/badge/progress-29%20%2F%2029-ff69b4.svg) ![Visitors](https://visitor-badge.laobi.icu/badge?page_id=kamyu104.metahackercup.2023)

* Python3 solutions of Meta Hacker Cup 2023. Solution begins with `*` means it will get TLE in the largest data set.
* Total computation amount > `10^8`, which is not friendly for Python3 to solve in 5 ~ 15 seconds. A `6-minute` timer is set for uploading the result this year.
* A problem was marked as `Very Hard` means that it was an unsolved one during the contest and may not be that difficult.


## Rounds

* [Hacker Cup 2022](https://github.com/kamyu104/MetaHackerCup-2022)
* [Practice Round](https://github.com/kamyu104/MetaHackerCup-2023#practice-round)
* [Round 1](https://github.com/kamyu104/MetaHackerCup-2023#round-1)
* [Round 2](https://github.com/kamyu104/MetaHackerCup-2023#round-2)
* [Round 3](https://github.com/kamyu104/MetaHackerCup-2023#round-3)
* [Final Round](https://github.com/kamyu104/MetaHackerCup-2023#final-round)

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
|B1| [Sum 41 (Chapter 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B1)| [Python3](./Round%201/sum_41_chapter_1.py3) [Python3](./Round%201/sum_41_chapter_1-2.py3) [Python3](./Round%201/sum_41_chapter_1-3.py3) | precompute: _O(sqrt(MAX_P))_<br> runtime: _O(logP + sqrt(P)/log(sqrt(P)))_ | _O(sqrt(MAX_P) + K)_ | Easy | | Constructive Algorithms, Greedy, Number Theory, `Linear Sieve of Eratosthenes`, Backtracking, Unique Partitions, Pruning |
|B2| [Sum 41 (Chapter 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/B2)| [Python3](./Round%201/sum_41_chapter_2.py3) [Python3](./Round%201/sum_41_chapter_2-2.py3) | _O(89166 + K^2)_ | _O(K)_ | Medium | | Backtracking, Unique Partitions, Pruning |
|C1| [Back in Black (Chapter 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C1)| [Python3](./Round%201/back_in_black_chapter_1.py3) | _O(NlogN + Q)_ | _O(N)_ | Easy | | Number Theory, Greedy |
|C2| [Back in Black (Chapter 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/C2)| [Python3](./Round%201/back_in_black_chapter_2.py3) | _O(NlogN + Q)_ | _O(N)_ | Medium | | Number Theory, Greedy |
|D| [Today is Gonna be a Great Day](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/D)| [Python3](./Round%201/today_is_gonna_be_a_great_day.py3) | _O(NlogN + QlogN)_ | _O(N)_ | Medium | | Segment Tree |
|E| [Bohemian Rap-sody](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-1/problems/E)| [PyPy3](./Round%201/bohemian_rapsody.py3) | _O(QlogN + QlogQ + (L + Q) * sqrt(N))_ | _O(Q + N)_ | Hard | | Trie, Offline Solution, Binary Search, Sqrt Decomposition, `Mo's Algorithm`, Freq Table, Prefix Sum, Math |

## Round 2
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A1| [Ready, Go (Part 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/A1)| [Python3](./Round%202/ready_go_part_1.py3) | _O(R * C)_ | _O(R * C)_ | Easy | | BFS |
|A2| [Ready, Go (Part 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/A2)| [Python3](./Round%202/ready_go_part_2.py3) | _O(R * C)_ | _O(R * C)_ | Easy | | BFS, DP |
|B| [Meta Game](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/B)| [Python3](./Round%202/meta_game.py3) | _O(N)_ | _O(1)_ | Easy | | Array |
|C| [Wiki Race](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/C)| [Python3](./Round%202/wiki_race.py3) [Python3](./Round%202/wiki_race2.py3) | _O(N + SUM_LEN_S)_ | _O(N + SUM_LEN_S)_ | Medium | | DFS, Freq Table, Tree DP |
|D| [Tower Rush](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-2/problems/D)| [Python3](./Round%202/tower_rush.py3) | precompute: _O(MAX_N + max(MAX_D, MAX_H) * log(max(MAX_D, MAX_H)))_<br>runtime: _O(N + (max_h) * log(max_h))_ | _O(MAX_N + max(MAX_D, MAX_H) * log(max(MAX_D, MAX_H)))_ | Hard | | Number Theory, `Bézout's Identity`, Combinatorics, Inclusion-Exclusion Principle, `Möbius Function`, `Linear Sieve of Eratosthenes` |

## Round 3
| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A| [Spooky Splits](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/A)| [Python3](./Round%203/spooky_splits.py3) | _O(S * sqrt(N) * logN)_ | _O(S * sqrt(N))_ | Easy | | BFS, Backtracking, Pruning, Hash Table |
|B| [Hash Slinger](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/B)| [Python3](./Round%203/hash_slinger.py3) | _O(N^2 + M^2)_ | _O(N * M)_ | Medium | | DP, `Dijkstra's Algorithm` |
|C| [Krab-otage](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/C)| [Python3](./Round%203/krabotage.py3) | _O(R * C * (R + C))_ | _O(R * C)_ | Hard | | DP, Prefix Sum |
|D| [Double Stars](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/D)| [Python3](./Round%203/double_stars.py3) [Python3](./Round%203/double_stars2.py3) | _O(N)_ | _O(N)_ | Hard | | DFS, BFS, Prefix Sum, Tree DP, Sort, Counting Sort, Freq Table, Two Pointers, Greedy |
|E| [Similar Ships](https://www.facebook.com/codingcompetitions/hacker-cup/2023/round-3/problems/E)| [Python3](./Round%203/similar_ships.py3) [Python3](./Round%203/similar_ships2.py3) | _O(N)_ | _O(N)_ | Hard | | Constructive Algorithms, Tree Diameter, BFS, Tree DP |

## Final Round
You can relive the magic of the 2023 Hacker Cup World Finals by watching the [Live Stream Recording](https://www.facebook.com/hackercup/videos/1475477143295894) of the announcement of winners.

| # | Title | Solution | Time | Space | Difficulty | Tag | Note |
|---| ----- | -------- | ---- | ----- | ---------- | --- | ---- |
|A1| [Programming Paths (Part 1)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/A1)| [Python3](./Final%20Round/programming_paths_part_1.py3) | precompute: _O(R * C + logK)_<br>runtime: _O(R * C)_ | _O(R * C)_ | Easy | | Constructive Algorithms, BFS, Bitmasks |
|A2| [Programming Paths (Part 2)](https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/A2)| [Python3](./Final%20Round/programming_paths_part_2.py3) [Python3](./Final%20Round/programming_paths_part_2_2.py3) | precompute: _O(R * C + K^2 * D)_<br>runtime: _O(R * C)_ | _O(R * C + K^2)_ | Hard | | Constructive Algorithms, BFS, DP, Backtracing |
|B| [Transposing Tiles](https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/B)| [PyPy3](./Final%20Round/transposing_tiles.py3) | _O(R * C * 3136)_ | _O(R * C + 16)_ | Easy | | Freq Table, DP |
|C| [Resisting Robots](https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/C)| [Python3](./Final%20Round/resisting_robots.py3) | _O(NlogN + M)_ | _O(N + M)_ | Easy | | Sort, Union Find, DSU, DP |
|D| [Nearly Nim](https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/D)| [Python3](./Final%20Round/nearly_nim.py3) | _O(N)_ | _O(N)_ | Medium | | Game, Prefix Sum, Greedy |
|E| [Dealing Decks](https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/E)| [PyPy3](./Final%20Round/dealing_decks.py3) | _O(NlogN)_ | _O(NlogN)_ | Medium | | Game, `Sprague-Grundy Theorem`, Persistent Trie, Binary Search |
|F| [Cacti Cartography](https://www.facebook.com/codingcompetitions/hacker-cup/2023/final-round/problems/F)| [Python3](./Final%20Round/cacti_cartography.py3) [Python3](./Final%20Round/cacti_cartography2.py3) | _O(N^2 * min(K, L))_ | _O(N^2)_  | Hard | | Cactus Graph, BFS, DFS, Tree DP, Linear Programming |
