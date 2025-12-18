# Student Ranking System (Fixed Version)

This repository contains a fixed implementation of the Student Grade Ranking System.
The original project contained a known bug: tied scores were assigned different
ranks because the implementation used list indices directly. That bug has been
fixed in this version; rankings now follow "standard competition ranking" rules
(also known as "1224" ranking).

Status: BUG FIX APPLIED — all tests pass.

Quick start
1. Create a virtual environment (optional)
2. Install test dependency:
   pip install -r requirements.txt
3. Run tests:
   pytest tests/test_ranking.py -v

What was fixed
- The ranking algorithm in src/ranking_system.py was updated so students with
  the same score receive the same rank and the next different score gets the
  correct rank equal to the number of people ahead + 1.

Project structure
- src/: Implementation (fixed)
- tests/: Original test suite (kept unchanged)
- data/: Sample JSON data used by tests
- FIXED.md: Detailed explanation of the fix

For details about the change and verification steps, see FIXED.md.
