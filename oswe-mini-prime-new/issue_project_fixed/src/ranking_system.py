"""
Student Grade Ranking System - Fixed Version

This module implements the standard competition ranking ("1224" style) where
students with the same score receive the same rank and the next different score
receives rank = number of students already ranked + 1.

The original project had a bug: it assigned ranks using list indices (index+1),
which produced incremental ranks even when scores were tied.

This file keeps the original public API and corrects the ranking logic.
"""

from typing import List, Dict


class Student:
    """Student class"""

    def __init__(self, name: str, score: float):
        self.name = name
        self.score = score
        self.rank = None

    def __repr__(self):
        return f"Student(name='{self.name}', score={self.score}, rank={self.rank})"


class RankingSystem:
    """Grade ranking system"""

    def __init__(self):
        self.students: List[Student] = []

    def add_student(self, name: str, score: float):
        """Add a student with validation"""
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.students.append(Student(name, score))

    def calculate_rankings(self) -> List[Student]:
        """
        Calculate rankings using **standard competition ranking** rules ("1224" style):

        - Students are sorted by score (descending)
        - Students with the same score receive the same rank
        - When the score changes, the rank is set to the number of students
          already processed + 1 (so the ranks skip appropriately)

        This replaces the previous (buggy) implementation that used index+1
        which produced different ranks for tied scores.
        """
        # Sort by score in descending order
        sorted_students = sorted(self.students, key=lambda s: s.score, reverse=True)

        # FIXED: Implement standard competition ranking
        # Keep track of the previous score, current assigned rank, and how many
        # students have been processed so far.
        prev_score = None
        current_rank = 0
        processed_count = 0

        for student in sorted_students:
            processed_count += 1
            if prev_score is None or student.score != prev_score:
                # New score group: rank is number of people already processed
                # (i.e., processed_count) → this produces the correct skip after ties
                current_rank = processed_count
                student.rank = current_rank
                prev_score = student.score
            else:
                # Same score as previous student: same rank
                student.rank = current_rank

        return sorted_students

    def get_rankings_dict(self) -> List[Dict]:
        """Get ranking dictionary list"""
        ranked = self.calculate_rankings()
        return [
            {
                "name": s.name,
                "score": s.score,
                "rank": s.rank,
            }
            for s in ranked
        ]

    def clear(self):
        """Clear all students"""
        self.students = []


def main():
    """Example usage"""
    system = RankingSystem()

    # Add test data
    system.add_student("Alice", 95)
    system.add_student("Bob", 95)
    system.add_student("Charlie", 90)

    # Calculate rankings
    rankings = system.get_rankings_dict()

    print("Student Ranking Results:")
    print("-" * 40)
    for item in rankings:
        print(f"Rank {item['rank']}: {item['name']} - {item['score']} points")


if __name__ == "__main__":
    main()
