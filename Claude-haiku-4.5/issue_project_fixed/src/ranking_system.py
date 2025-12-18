"""
Student Grade Ranking System (FIXED VERSION)
Corrected ranking calculation for tied scores
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
        """Add a student"""
        if not isinstance(score, (int, float)) or score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.students.append(Student(name, score))
    
    def calculate_rankings(self) -> List[Student]:
        """
        Calculate rankings with proper tie handling.
        
        ✅ FIX: Implements standard competition ranking (1, 1, 3, 3, 3, 6)
        - Students with identical scores receive the same rank
        - The next rank after a tie equals the number of people ahead + 1
        
        Algorithm:
        1. Sort students by score (descending)
        2. Assign rank based on position in sorted list (1-indexed)
        3. For students with same score as previous, use the same rank
        """
        # Sort by score in descending order
        sorted_students = sorted(self.students, key=lambda s: s.score, reverse=True)
        
        if not sorted_students:
            return sorted_students
        
        # ✅ FIX: Handle ties correctly using position-based ranking
        sorted_students[0].rank = 1
        
        for index in range(1, len(sorted_students)):
            current_student = sorted_students[index]
            previous_student = sorted_students[index - 1]
            
            # If same score as previous student, assign same rank
            if current_student.score == previous_student.score:
                current_student.rank = previous_student.rank
            else:
                # If different score, rank = current position (1-indexed)
                # This handles ties: if 2 people are rank 1, next is rank 3
                current_student.rank = index + 1
        
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
