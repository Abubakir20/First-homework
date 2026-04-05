import json

f = open('exercise1.json')

# 1
# data = json.load(f)
# branches = data['branches']
# for branch in branches:
#   print(branch['name'])
# --------------------------------------------

# 2
# data = json.load(f)
# branches = data['branches']
# for branch in branches:
#     for teacher in branch['teachers']:
#         if teacher['subject'] == 'Python':
#             print(f"Ism: {teacher['name']}, Branch: {branch['name']}, Tajriba: {teacher['experience']} yil")
# --------------------------------------------

# 3
# data = json.load(f)
# for branch in data['branches']:
#         print(f"Branch: {branch['name']}\nO'quvchilar soni: {len(branch['students'])} ta")
# --------------------------------------------

# 4
# data = json.load(f)
# for branch in data['branches']:
#     max_s = max(branch['students'], key = lambda x: x['payment'])
#     name = max_s['name']
#     payment = max_s['payment']
#     print(f"Branch: {branch['name']}, Ism: {name}, Payemant: {payment}")
# --------------------------------------------

# 5
# data = json.load(f)
# for branch in data['branches']:
#     total = sum(student['payment'] for student in branch['students'])
#     print(f"Branch: {branch['name']} - Umumiy tushum: {total}")
# --------------------------------------------

# 6
# data = json.load(f)
# for branch in data['branches']:
#     for teacher in branch['teachers']:
#         if teacher['experience'] > 5:
#             print(f"Branch: {branch['name']}\nIsm: {teacher['name']} - Tajriba: {teacher['experience']} yil")
# --------------------------------------------

# 7
# data = json.load(f)
# for branch in data['branches']:
#     course = {students['course'] for students in branch['students']}
#     if course == {'Python'}:
#         print(f"Branch: {branch['name']}")
# --------------------------------------------

f.close()