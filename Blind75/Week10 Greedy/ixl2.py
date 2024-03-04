from typing import List

maxLines = 13
skills = [
    {"name": "Learn to count to 5", "subject": "Math", "priority": 14}, # 1
    {"name": "Skip counting by twos", "subject": "Math", "priority": 10}, # 4
    {"name": "Skip counting", "subject": "Math", "priority": 8},
    {"name": "Multiply by 5", "subject": "Math", "priority": 5},
    {"name": "Reducing fractions", "subject": "Math", "priority": 3},
    {"name": "Using commas", "subject": "Language arts", "priority": 12}, # 2
    {"name": "Parts of speech", "subject": "Language arts", "priority": 9},
    {"name": "Parts of a book", "subject": "Language arts", "priority": 2},
    {"name": "The Civil War", "subject": "History", "priority": 6},
    {"name": "The Panama Canal", "subject": "History", "priority": 1},
    {"name": "States of matter", "subject": "Science", "priority": 11} # 3
]
'''
Output:
   "Math skills:",
   "Learn to count to 5",
   "Skip counting",
   "Skip counting by twos",
   "And 2 more!",
   "Science skills:",
   "States of matter",
   "Language arts skills:",
   "Using commas",
   "Parts of speech",
   "And 1 more!"
'''
import copy

skills.sort(key=lambda x: x['priority'], reverse=True)

f:dict[str,List] = {}
for skill in skills:
    if skill['subject'] not in f:
        f[skill['subject']] = []
    f[skill['subject']].append(skill)

print([[k,len(v)] for k,v in f.items()])

cur = 0
p = {}
for i in range(len(skills)):
    read_skills:dict[str, [[str,int]]] = {}  # subject: []
    # to_print:dict[str,List] = {}
    line = 0
    if i == len(skills)-1:
        remain_max_priority = 0
    else:
        remain_max_priority = skills[i+1]['priority']

    for k in range(i + 1):
        subject = skills[k]['subject']
        if subject not in read_skills:
            read_skills[subject] = []
        read_skills[subject].append([skills[k]['name'], skills[k]['priority']])

    prev_number = sum([len(v) for k,v in read_skills.items()])
    while True:

        for subject, arr in read_skills.items():
            remain = len(f[subject]) - len(arr)
            if len(arr) == 1 and remain > 0:
                # invalid
                # print(subject,'invalid')
                remain_max_priority = max(remain_max_priority,arr[0][1])
                read_skills[subject] = []
                continue

            for name,priority in arr:
                if priority < remain_max_priority:
                    read_skills[subject].remove([name,priority])


        if prev_number == sum([len(v) for k,v in read_skills.items()]):
            break

        prev_number = sum([len(v) for k,v in read_skills.items()])

    for subject, arr in read_skills.items():
        if len(arr) == 0:
            continue
        if len(f[subject]) - len(arr) > 0:
            line +=1
        line += 1 + len(arr)




    if cur < line <= maxLines:

        cur = line
        for subject in read_skills:
            p[subject] = read_skills[subject][:]

    # print(f'{i=}, {cur=}, {line=}')
    # for k,v in p.items():
    #     print(k,v)
    # print('=='*10)

output = []
for subject, arr in p.items():
    output.append(f'{subject} skills:')
    for x in arr:
        output.append(x[0])
    if len(f[subject]) - len(arr) > 0:
        output.append(f'remain {len(f[subject]) - len(arr)}')

for x in output:
    print(x)

print(len(output))