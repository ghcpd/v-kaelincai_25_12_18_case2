# Student Ranking System (Fixed Version)

## Project Overview

This is a school grade management system that correctly implements standard competition ranking rules for tied scores. This is the **fixed version** of the original project that had a ranking calculation bug.

## Problem Solved

**Original Bug:** Incorrect ranking calculation for tied scores (Off-by-one in ranking logic)

**Manifestation:**
- When multiple students have the same score, they should receive the same rank
- The next student with a different score should have rank = "total people ahead + 1"
- **Original Behavior:** The code used array indices as ranks directly, causing non-consecutive ranks after ties

**Example:**
```
Student Scores: Alice 95, Bob 95, Charlie 90
Expected Ranks: Rank 1, Rank 1, Rank 3
Original Ranks: Rank 1, Rank 2, Rank 3 ❌ (Wrong!)
Fixed Ranks: Rank 1, Rank 1, Rank 3 ✅ (Correct!)
```

## Project Structure

```
issue_project_fixed/
├── src/
│   ├── __init__.py
│   └── ranking_system.py      # Core code (fixed)
├── tests/
│   ├── __init__.py
│   └── test_ranking.py        # Test cases (all pass)
├── data/
│   └── students.json          # Sample data
├── requirements.txt
├── README.md                  # This file
└── FIXED.md                   # Detailed fix explanation
```

## Quick Start

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 2. Run Tests (All Pass)

```powershell
pytest tests/test_ranking.py -v
```

### 3. Run Main Program to See Correct Rankings

```powershell
python src/ranking_system.py
```

**Expected Output (fixed):**
```
Student Ranking Results:
----------------------------------------
Rank 1: Alice - 95 points
Rank 1: Bob - 95 points
Rank 3: Charlie - 90 points
```

## Test Description

The project contains 7 test cases, all passing:

✅ **test_simple_ranking_no_ties** - No ties scenario (Pass)  
✅ **test_two_students_tied_first_place** - Two students tied for first (Pass)  
✅ **test_multiple_ties_complex** - Multiple groups of ties (Pass)  
✅ **test_all_students_same_score** - All same score (Pass)  
✅ **test_with_json_data** - Using JSON data (Pass)  
✅ **test_invalid_score_negative** - Input validation (Pass)  
✅ **test_invalid_score_over_100** - Input validation (Pass)

## Fix Details

**File:** [src/ranking_system.py](src/ranking_system.py#L37)  
**Function:** `RankingSystem.calculate_rankings()`  
**Fixed Logic:**

```python
current_rank = 1
for i, student in enumerate(sorted_students):
    if i == 0 or student.score != sorted_students[i-1].score:
        # New rank for different score
        student.rank = current_rank
    else:
        # Same rank for tied score
        student.rank = sorted_students[i-1].rank
    current_rank += 1
```

**Key Changes:**
- Track current rank separately from array index
- Compare scores to detect ties
- Assign same rank for tied scores
- Increment rank counter for each student (not just unique ranks)

## Tech Stack

- Python 3.8+
- pytest 7.4+
- Windows 11 (compatible with other systems)

## Related Documentation

For detailed fix analysis, see [FIXED.md](FIXED.md)