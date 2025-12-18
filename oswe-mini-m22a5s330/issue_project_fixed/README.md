# Student Ranking System (Fixed Version)

This is the fixed version of the Student Ranking System. The original project had a bug in the ranking calculation logic: tied scores were not assigned the same rank and subsequent ranks were incorrect. This repository corrects the ranking calculation and all provided tests now pass.

Key fixes:
- Implemented Standard Competition Ranking ("1224" style): students with the same score share the same rank; next different score gets rank = number of people ahead + 1
- Kept original public interface (RankingSystem.add_student, get_rankings_dict, clear)
- Added documentation describing the fix and verification steps

Quick start
------------
1. Create a virtual environment and install dependencies:

   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt

2. Run tests:

   pytest tests/test_ranking.py -v

You should see all tests pass.

Comparison to original project
------------------------------
- The core logic in `src/ranking_system.py` (method `calculate_rankings`) was modified to correctly handle tied scores while preserving other functionality.

See `FIXED.md` for a detailed description of what was changed and why.
