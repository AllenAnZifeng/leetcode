'''
IXL has a search bar that allows students to search for skills. When the search is complete, we end up with a large list of skills
that are prioritized based on how well they matched the search. We want to display these skills on the results page,
but there is only space on the results page for a limited number of lines of text.
This means that all of the skills might not be included in the results page.
Additionally, we want to format the results in a way that is convenient for the user, grouping skills from the same "subject" together.

Each skill has a "priority", a "name", and a "subject". In Java, it might look like this:

public class Skill {
    public int "priority"; //Higher number = higher "priority", unique
    public String "name";
    public String "subject";
}

We need to write a function which, given a list of Skills, and the line limit for the results page,
produces the best possible list of lines of text for the results page. To determine this, we use the following rules:

A line of text is either (1) the "name" of a skill or (2) a piece of special text used to organize the results.
Skills that have the same "subject" should be grouped together. All skill "name"s from a given "subject" should be contiguous in the output list. We call this group a ""subject" bundle".
Before each "subject" bundle, there should be a line of special text that reads "<"subject" "name"> skills:"
At the end of each "subject" bundle, if not all of the skills from that "subject" have been included, there should be a line of special text that reads "And <n> more!" where n is the number of skills from that "subject" not included in the results list.
We should only include a skill on the results page if we’re also including all higher-"priority" skills (from any "subject") on the results page.
We should only include a "subject" bundle on the results page if either (1) we’re including at least 2 skills from that "subject", or (2) we’re including only one skill from that "subject", and there were no other skills from that "subject" in the input list.
We should make sure to include the "name"s of as many skills as possible without breaking any other rules or going over the line limit

Your output should be a list of Strings, one string per line. In Java, your function might look like:

/**
 * Produces a list of lines with size no greater than maxLines.
 */
public List<String> results(List<Skill> skills, int maxLines) {
}

Here is an example input and output:
Input:
maxLines = 13,
skills =
{"name": "Learn to count to 5", "subject": "Math", "priority": 14},
{"name": "Skip counting by twos", "subject": "Math", "priority": 10},
{"name": "Skip counting", "subject": "Math", "priority": 8},
{"name": "Multiply by 5", "subject": "Math", "priority": 5},
{"name": "Reducing fractions", "subject": "Math", "priority": 3},
{"name": "Using commas", "subject": "Language arts", "priority": 12},
{"name": "Parts of speech", "subject": "Language arts", "priority": 9},
{"name": "Parts of a book", "subject": "Language arts", "priority": 2},
{"name": "The Civil War", "subject": "History", "priority": 6},
{"name": "The Panama Canal", "subject": "History", "priority": 1},
{"name": "States of matter", "subject": "Science", "priority": 11}

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

maxLines = 13
skills = [
    {"name": "Learn to count to 5", "subject": "Math", "priority": 14},
    {"name": "Skip counting by twos", "subject": "Math", "priority": 10},
    {"name": "Skip counting", "subject": "Math", "priority": 8},
    {"name": "Multiply by 5", "subject": "Math", "priority": 5},
    {"name": "Reducing fractions", "subject": "Math", "priority": 3},
    {"name": "Using commas", "subject": "Language arts", "priority": 12},
    {"name": "Parts of speech", "subject": "Language arts", "priority": 9},
    {"name": "Parts of a book", "subject": "Language arts", "priority": 2},
    {"name": "The Civil War", "subject": "History", "priority": 6},
    {"name": "The Panama Canal", "subject": "History", "priority": 1},
    {"name": "States of matter", "subject": "Science", "priority": 11}
]
import heapq


class Skill:
    def __init__(self, skill: dict):
        self.name = skill['name']
        self.subject = skill['subject']
        self.priority = skill['priority']

    def __str__(self):
        return f' {self.priority=}'
        # return f'{self.name=}, {self.subject=}, {self.priority=}'

    def __repr__(self):
        return self.__str__()


class Display:
    def __init__(self, skills, maxLines):
        self.skills = {}
        self.maxLines = maxLines
        self.curLines = 0
        for skill in skills:
            if skill['subject'] not in self.skills:
                self.skills[skill['subject']] = []
            self.skills[skill['subject']].append(Skill(skill))

        for subject in self.skills.keys():
            self.skills[subject].sort(key=lambda x: x.priority, reverse=True)

        print(self.skills)
        self.remaining_skills = copy.deepcopy(self.skills)
        self.to_print:dict[str:[Skill]] = {}  # subject: [Skill]

    def get_highest_priority_skill_from_all_subjects(self):
        t = Skill({'name': '', 'subject': '', 'priority': -1})
        for subject, skill_arr in self.remaining_skills.items():
            if len(skill_arr) > 0 and skill_arr[0].priority > t.priority:
                t = skill_arr[0]
        self.remaining_skills[t.subject] = self.remaining_skills[t.subject][1:]
        return t

    def get_highest_priority_skill_from_subject(self, subject: str):
        t = self.remaining_skills[subject][0]
        self.remaining_skills[subject] = self.remaining_skills[subject][1:]
        return t

    def printing(self):
        output = []
        for subject, skill_arr in self.to_print.items():
            if len(skill_arr) == 0:
                continue
            output.append(f'{subject} skills:')
            for skill in skill_arr:
                output.append(skill.name)
            if len(self.remaining_skills[subject]) != 0:
                output.append(f"And {len(self.remaining_skills[subject])} more!")

        print(len(output))
        print(self.remaining_skills)
        for row in output:
            print(row)


    def add_print(self):
        counter = 0
        while True:
            counter+=1
            print(counter,self.remaining_skills)
            line = 0
            skill = self.get_highest_priority_skill_from_all_subjects()
            if skill.subject not in self.to_print:
                # buffer.append(f'{skill.subject} skills:')  # "subject": "Math",
                line += 1
                self.to_print[skill.subject] = []

                if len(self.skills[skill.subject]) == 1:
                    # buffer.append(skill.name)
                    line += 1
                    if line + self.curLines > self.maxLines:
                        return
                    self.to_print[skill.subject].append(skill)


                elif len(self.skills[skill.subject]) > 1:
                    if len(self.skills[skill.subject]) > 2:
                        # buffer.append(f"And {self.remaining_skills[skill.subject]} more!")
                        line+=1

                    line+=2
                    if line + self.curLines > self.maxLines:
                        return

                    # buffer.append(skill.name)
                    self.to_print[skill.subject].append(skill)

                    second_skill = self.get_highest_priority_skill_from_subject(skill.subject)
                    self.to_print[skill.subject].append(second_skill)
                    # buffer.append(second_skill.name)


            else:
                # buffer.append(skill.name)
                line += 1
                if line + self.curLines > self.maxLines:
                    return

                self.to_print[skill.subject].append(skill)
                if len(self.remaining_skills[skill.subject]) == 0: # minus "And 1 more!"
                    # buffer.pop()
                    line -= 1

            self.curLines += line





display = Display(skills, maxLines)

display.add_print()
display.printing()

