from src.ranking_system import RankingSystem
import json

print('=' * 60)
print('FIXED VERSION - Test with JSON Data')
print('=' * 60)

system = RankingSystem()
with open('data/students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)
    for student in students:
        system.add_student(student['name'], student['score'])

rankings = system.get_rankings_dict()
for item in rankings:
    print('Rank %d: %-6s - %3d points' % (item['rank'], item['name'], item['score']))

print()
print('Expected ranks:')
print('Rank 1: 小明, 小红 (95 points)')
print('Rank 3: 小李 (90 points)')
print('Rank 4: 小张, 小王, 小刘 (85 points)')
print('Rank 7: 小陈 (80 points)')
