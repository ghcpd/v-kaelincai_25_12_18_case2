"""
Student Grade Ranking System - Fixed Version

This module fixes the ranking calculation for tied scores so that it follows
standard competition ranking rules:
	- Students with the same score receive the same rank
	- The next different score rank = number of people already ranked + 1

The previous implementation used array indices directly as ranks which caused
non-consecutive ranks after ties.
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
        """Add a student. Score must be between 0 and 100 inclusive."""
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.students.append(Student(name, score))

    def calculate_rankings(self) -> List[Student]:
        """Calculate rankings using standard competition ranking rules.

        This implementation ensures that students with the same score share the
        same rank, and the next distinct score receives a rank equal to the
        number of students already ranked + 1.
        """
        # Sort by score in descending order
        sorted_students = sorted(self.students, key=lambda s: s.score, reverse=True)

        prev_score = None
        num_processed = 0

        for student in sorted_students:
            num_processed += 1
            if student.score != prev_score:
                # New score seen - rank equals number of items processed so far
                current_rank = num_processed
                prev_score = student.score
            # Assign the current rank (same rank for equal scores)
            student.rank = current_rank

        return sorted_students

    def get_rankings_dict(self) -> List[Dict]:
        """Get ranking dictionary list"""
        ranked = self.calculate_rankings()
        return [
            {
                "name": s.name,
                "score": s.score,
                "rank": s.rank
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
