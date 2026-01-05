# Project Repair Task Prompt

## Task Overview

Please create a **complete fixed version project** based on the provided student ranking system project with a known bug. The fixed version should resolve the ranking calculation error in the original project and ensure all test cases pass.

---

## Original Project Problem Description

**Project Name:** Student Ranking System (With Known Bug)

**Bug Type:** Functional Bug - Incorrect Tied Ranking Calculation

**Problem Manifestation:**
- When multiple students have the same score, they should receive the same rank
- The next student with a different score should have rank = "total number of people ahead + 1"
- **Actual Behavior:** The code uses array indices directly as ranks, causing non-consecutive ranks after ties

**Example:**
```
Student Scores: Alice 95, Bob 95, Charlie 90
Expected Ranks: Rank 1, Rank 1, Rank 2
Actual Ranks: Rank 1, Rank 2, Rank 3 ❌ (Wrong!)
```

**Bug Location:**
- File: `src/ranking_system.py`
- Function: `RankingSystem.calculate_rankings()`
- Problem Code: Directly uses `index + 1` as rank, doesn't handle ties

**Test Results:**
- ✅ No-ties scenario test passes
- ❌ Two students tied for first test fails
- ❌ Multiple tied groups complex scenario test fails
- ❌ All students same score test fails
- ❌ Using JSON data test fails

---

## Fix Requirements

### Functional Requirements
1. **Correctly Implement Standard Competition Ranking Rules**
   - Students with the same score get the same rank
   - Next different score rank = number of people already ranked + 1
   - Example: 1, 1, 3, 3, 3, 6 (not 1, 2, 3, 4, 5, 6)

2. **Maintain Original Functionality**
   - Student addition and management
   - Score validation (between 0-100)
   - Ranking dictionary export
   - Data clearing function

3. **Pass All Test Cases**
   - All original tests should pass
   - Test cases themselves should not be modified

### Code Quality Requirements
1. Code should be clear and readable with appropriate comments
2. Follow Python coding standards (PEP 8)
3. Maintain good class design and encapsulation
4. Error handling should be robust

### Documentation Requirements
1. Update README.md to indicate bug has been fixed
2. Create FIXED.md document detailing:
   - What problem was fixed
   - What fix approach was adopted
   - Before/after comparison
   - How to verify the fix is successful

---

## Fixed Version Project Structure

Please create a complete fixed version project named **`issue_project_fixed`** with the following directory structure:

```
issue_project_fixed/
├── src/
│   ├── __init__.py
│   └── ranking_system.py          # ✅ Fixed core code
├── tests/
│   ├── __init__.py
│   └── test_ranking.py            # Keep same test cases as original project
├── data/
│   └── students.json              # Sample data (same as original project)
├── .gitignore                     # Git ignore file configuration
├── requirements.txt               # Dependencies (same as original project)
├── README.md                      # ✅ Updated project description (marked as bug fixed)
└── FIXED.md                       # ✅ New: Detailed fix explanation document
```

### File Descriptions

#### 1. `src/ranking_system.py` (Core Fix)
- **Must Fix:** Ranking calculation logic in `calculate_rankings()` method
- Keep original class structure: `Student` class and `RankingSystem` class
- Keep original public interface methods unchanged

#### 2. `tests/test_ranking.py` (Keep Unchanged)
- Completely copy test cases from original project
- Should not modify any test code
- All tests should pass after fix

#### 3. `data/students.json` (Keep Unchanged)
- Completely copy sample data from original project

#### 4. `README.md` (Updated)
- Remove "With Known Bug" wording
- Update project description to "Fixed Version"
- Indicate bug has been fixed
- Update test results description (all tests pass)
- Keep quick start guide
- Add comparison with original project

#### 5. `FIXED.md` (New)
Should contain the following sections:
- **Fix Overview**: Brief description of what problem was fixed
- **Original Problem Analysis**: Why the original code was wrong
- **Fix Solution**: Adopted solution and algorithm logic
- **Code Comparison**: Key code comparison before and after fix
- **Test Validation**: How to run tests to verify fix is successful
- **Edge Case Handling**: How various special cases are handled

#### 6. `.gitignore`
Standard Python project ignore configuration:
- `__pycache__/`, `*.pyc`
- `.pytest_cache/`
- `.venv/`, `venv/`
- IDE configuration files, etc.

#### 7. `requirements.txt` (Keep Unchanged)
```
pytest>=7.4.0
```

---

## Acceptance Criteria

The fixed version project should meet the following standards:

### 1. Functional Correctness
```powershell
# Run tests, all tests should pass
pytest tests/test_ranking.py -v

# Expected output: All test cases show PASSED
```

### 2. Example Run Results
```python
from src.ranking_system import RankingSystem

system = RankingSystem()
system.add_student("Alice", 95)
system.add_student("Bob", 95)
system.add_student("Charlie", 90)

rankings = system.get_rankings_dict()

# Expected output:
# [
#   {"name": "Alice", "score": 95, "rank": 1},
#   {"name": "Bob", "score": 95, "rank": 1},
#   {"name": "Charlie", "score": 90, "rank": 2}
# ]
```

### 3. Documentation Completeness
- README.md clearly states this is a fixed version
- FIXED.md explains the fix process in detail
- Code comments are sufficient, explaining fix logic

### 4. Code Quality
- Passes basic code style checks
- No new bugs introduced
- Code readability is good

---

## Important Notes

1. **Do Not Modify Test Cases**: Test cases represent correct business requirements; tests should pass by modifying implementation code
2. **Maintain Interface Compatibility**: Fixes should not change the public interface of classes
3. **Complete Project**: Generated output should be a complete, independently runnable project
4. **Detailed Documentation**: FIXED.md should be detailed enough for other developers to understand the fix approach
5. **Verifiability**: Anyone should be able to verify the fix is successful by running pytest

---

## Output Format

Please provide the complete content of each file according to the above directory structure. For the fixed core code (`src/ranking_system.py`), please specifically mark the modified parts and fix logic.
