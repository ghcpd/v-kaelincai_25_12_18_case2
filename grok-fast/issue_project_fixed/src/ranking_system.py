"""
Student Grade Ranking System - Fixed Version
Correctly handles tied scores using standard competition ranking rules
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
        Calculate rankings using standard competition ranking rules
        Students with same score get same rank, next rank = number of people ahead + 1
        """
        # Sort by score in descending order
        sorted_students = sorted(self.students, key=lambda s: s.score, reverse=True)
        
        # Fixed ranking logic: handle ties correctly
        rank = 1
        for i in range(len(sorted_students)):
            if i > 0 and sorted_students[i].score < sorted_students[i-1].score:
                rank = i + 1
            sorted_students[i].rank = rank
        
        return sorted_students
        
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