# FIXED.md — Fix Overview & Details

## Fix Overview
- The original `RankingSystem.calculate_rankings()` used `index + 1` as the rank, which broke tie handling.
- This fix implements **standard competition ranking** so tied scores share the same rank and the next different score's rank
  equals the number of students already ranked + 1.

## Original Problem Analysis
- **Bug location**: `src/ranking_system.py` → `calculate_rankings()`
- **Root cause**: The rank was set directly from the array index, so you’d get non-consecutive ranks (e.g., `95,95,90` resulted in ranks `1,2,3` instead of `1,1,3`).
- **Impact**: Wrong ranking for tie groups, potentially leading to unfair scholarship/honor roll decisions.

## Fix Solution
- The new algorithm:
  1. Sort students by `score` descending.
  2. Walk through the sorted list incrementing a `num_processed` counter.
  3. When the score changes, set `current_rank = num_processed`.
  4. Assign `current_rank` to the student. (Same score → same rank)
- This produces standard competition ranking results:
  - Examples: 
    - `95,95,90` → `1,1,3` (two tied → next rank 3 as 2 people already ranked)
    - `95,95,85,85,85,80` → `1,1,3,3,3,6`

## Code Comparison
**Before (buggy)**
```py
for index, student in enumerate(sorted_students):
    student.rank = index + 1
```

**After (fixed)**
```py
prev_score = None
current_rank = 0
num_processed = 0
for student in sorted_students:
    num_processed += 1
    if student.score != prev_score:
        current_rank = num_processed
        prev_score = student.score
    student.rank = current_rank
```

## Test Validation
- `pytest tests/test_ranking.py -q` outputs **7 passed**.
- Example run:
```py
from src.ranking_system import RankingSystem
system = RankingSystem()
system.add_student("Alice", 95)
system.add_student("Bob", 95)
system.add_student("Charlie", 90)
print(system.get_rankings_dict())
# -> [{'name': 'Alice', 'score': 95, 'rank': 1},
#     {'name': 'Bob', 'score': 95, 'rank': 1},
#     {'name': 'Charlie', 'score': 90, 'rank': 3}]
```

## Edge Case Handling
- **All same score**: All students get rank `1`.
- **Single student**: Rank is `1`.
- **Multiple ties**: Tied students share a rank; next rank honors the number of people already ranked (not just number of distinct scores).
- **Score validation**: Inputs outside 0-100 raise `ValueError` (unchanged).
