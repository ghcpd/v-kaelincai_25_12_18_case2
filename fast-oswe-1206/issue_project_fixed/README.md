
# Student Ranking System (Fixed Version)

This is the **fixed** version of the Student Ranking System project. The original project contained a deliberate bug where tied scores were not ranked correctly (each student received `index + 1` as the rank, leading to non-consecutive ranks after ties).

## ✅ Fix
- Ranking calculation has been updated to follow **standard competition ranking rules**: students with the same score receive the same rank, and the next distinct score gets a rank equal to the number of students already ranked plus one.

## Quick Start

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Run Tests

```powershell
pytest tests/test_ranking.py -v
```

All tests should now **PASS**.

### 3. Run the Example Program

```powershell
python src/ranking_system.py
```

Expected output:

```
Student Ranking Results:
----------------------------------------
Rank 1: Alice - 95 points
Rank 1: Bob - 95 points
Rank 3: Charlie - 90 points
```

## Project Structure

```
issue_project_fixed/
├── src/
│   ├── __init__.py
│   └── ranking_system.py      # ✅ Fixed core code
├── tests/
│   ├── __init__.py
│   └── test_ranking.py        # Original tests (unchanged)
├── data/
│   └── students.json          # Sample data
├── .gitignore                 # Git ignore
├── requirements.txt           # Dependencies
├── README.md                  # ✅ This README
└── FIXED.md                   # ✅ Fix explanation document
```

## Why the Fix Matters

In the original implementation students with the same score did **not** share a rank (e.g., `95, 95, 90` resulted in ranks `1, 2, 3` instead of `1, 1, 2`). This could incorrectly affect scholarship decisions, honor roll eligibility, and fairness. The fix ensures consistent, expected ranking results.

## Test Results

```
pytest tests/test_ranking.py -q
... 7 passed
```

For more detailed information on the fix, see `FIXED.md`.
