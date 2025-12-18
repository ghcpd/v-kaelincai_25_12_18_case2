FIX Overview
============

Fix applied: Corrected ranking calculation so that tied students receive the
same rank and the next different score's rank equals the number of people
already ranked + 1 (standard competition ranking).

Original problem analysis
==========================
The original implementation (in the buggy project) assigned ranks by using
index + 1 in the sorted list. This means ties received increasing ranks
(e.g., 1, 2 for two people with the same score) which is incorrect per
standard ranking rules. Tests in tests/test_ranking.py highlighted this issue.

Fix solution
============
Algorithm adopted:
- Sort students by score descending
- Iterate the sorted list keeping track of the previous student's score and
  their assigned rank
- For the first student assign rank 1
- If the current student's score equals the previous score, assign the same
  rank (tie)
- Otherwise assign rank = current index + 1 (which equals number of people
  ahead + 1)

Code comparison (key snippet)
=============================
Before (buggy):
    for index, student in enumerate(sorted_students):
        student.rank = index + 1  # <-- this caused incorrect ranks for ties

After (fixed):
    prev_score = None
    prev_rank = None
    for index, student in enumerate(sorted_students):
        if index == 0:
            student.rank = 1
        else:
            if student.score == prev_score:
                student.rank = prev_rank
            else:
                student.rank = index + 1
        prev_score = student.score
        prev_rank = student.rank

Test validation
===============
Run the existing test suite (tests were kept unchanged):

$ pytest tests/test_ranking.py -v

All tests should pass. The tests check multiple scenarios including:
- No ties
- Two-way tie
- Multiple tie groups
- All students tied
- Loading from JSON data

Edge case handling
==================
- Input validation ensures scores are numeric and between 0 and 100.
- Empty student list -> calculate_rankings() returns an empty list.
- Stable ordering among equal scores: students with the same score are kept
  in a deterministic order according to Python's sort (stable); they share
  the same rank.

Notes
=====
- Tests were intentionally left unchanged to validate the fix against the
  original specification.
- The public interface of RankingSystem was preserved (no changes to method
  signatures).
