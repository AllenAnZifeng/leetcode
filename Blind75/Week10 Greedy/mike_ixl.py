'''
IXL has a search bar that allows students to search for skills. When the search is complete, we end up with a large list of skills that are prioritized based on how well they matched the search. We want to display these skills on the results page, but there is only space on the results page for a limited number of lines of text. This means that all of the skills might not be included in the results page. Additionally, we want to format the results in a way that is convenient for the user, grouping skills from the same subject together.

Each skill has a priority, a name, and a subject. In Java, it might look like this:

public class Skill {
    public int priority; //Higher number = higher priority, unique
    public String name;
    public String subject;
}

We need to write a function which, given a list of Skills, and the line limit for the results page, produces the best possible list of lines of text for the results page. To determine this, we use the following rules:

A line of text is either (1) the name of a skill or (2) a piece of special text used to organize the results.
Skills that have the same subject should be grouped together. All skill names from a given subject should be contiguous in the output list. We call this group a “subject bundle”.
Before each subject bundle, there should be a line of special text that reads “<subject name> skills:”
At the end of each subject bundle, if not all of the skills from that subject have been included, there should be a line of special text that reads “And <n> more!” where n is the number of skills from that subject not included in the results list.
We should only include a skill on the results page if we’re also including all higher-priority skills (from any subject) on the results page.
We should only include a subject bundle on the results page if either (1) we’re including at least 2 skills from that subject, or (2) we’re including only one skill from that subject, and there were no other skills from that subject in the input list.
We should make sure to include the names of as many skills as possible without breaking any other rules or going over the line limit

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
{name: “Learn to count to 5”, subject: “Math”, priority: 14}, 1
{name: “Skip counting by twos”, subject: “Math”, priority: 10}, 4
{name: “Skip counting”, subject: “Math”, priority: 8}, 6
{name: “Multiply by 5”, subject: “Math”, priority: 5},
{name: “Reducing fractions”, subject: “Math”, priority: 3},
{name: “Using commas”, subject: “Language arts”, priority: 12}, 2
{name: “Parts of speech”, subject: “Language arts”, priority: 9}, 5
{name: “Parts of a book”, subject: “Language arts”, priority: 2},
{name: “The Civil War”, subject: “History”, priority: 6}, 7
{name: “The Panama Canal”, subject: “History”, priority: 1},
{name: “States of matter”, subject: “Science”, priority: 11} 3

Output:
   “Math skills:”,
   “Learn to count to 5”,
   “Skip counting”,
   “Skip counting by twos”,
   “And 2 more!”,
   “Science skills:”,
   “States of matter”,
   “Language arts skills:”,
   “Using commas”,
   “Parts of speech”,
   “And 1 more!”
'''


class Skill:
    def __init__(self, priority, name, subject):
        self.priority = priority
        self.name = name
        self.subject = subject

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority


class SkillPageProducer:
    def group_skills_by_subject(self, skills):
        """
        Groups a list of Skill objects by their subject.

        Parameters:
            skills (list of Skill): A list of Skill objects to be grouped.

        Returns:
            dict: A dictionary where each key is a subject name (str) and each value
            is a list of Skill objects that belong to that subject.
        """
        skills_by_subject = {}  # {subject: [skills]}
        for skill in skills:
            if skill.subject not in skills_by_subject:
                skills_by_subject[skill.subject] = []
            skills_by_subject[skill.subject].append(skill)
        return skills_by_subject

    def sort_subjects_by_priority(self, skills_by_subject):
        """
        Sorts a dictionary of skills by subject by the priority of the first skill in each subject's list.

        Parameters:
            skills_by_subject (dict): A dictionary grouping all available Skill objects by their subject.

        Returns:
            list: A list of subject names sorted by the priority of the first skill in each subject's list.
        """
        for subject in skills_by_subject:
            skills_by_subject[subject].sort(reverse=True)
        return sorted(skills_by_subject, key=lambda subject: skills_by_subject[subject][0], reverse=True)

    def is_valid(self, current_skills, skills_by_subject, maxLines):
        """
        Determines if a subset of skills can be validly displayed within a given line limit.

        Parameters:
            current_skills (list of Skill): A list of Skill objects to be displayed.
            skills_by_subject (dict): A dictionary grouping all available Skill objects by their subject.
            maxLines (int): The maximum number of lines available.

        Returns:
            bool: True if the skills can be validly displayed within the maxLines constraint, False otherwise.
        """
        lines_used = 0
        current_skills_by_subject = self.group_skills_by_subject(current_skills)

        for subject, included_skills in current_skills_by_subject.items():
            total_count = len(skills_by_subject[subject])
            included_count = len(included_skills)

            if total_count == 1:
                lines_used += 2  # Subject title + 1 skill
            elif included_count < total_count:
                if included_count == 1:  # Invalid case
                    return False
                lines_used += 2 + included_count  # Subject title + skills + "And more"
            else:
                lines_used += 1 + included_count  # Subject title + skills

        return lines_used <= maxLines

    def results(self, skills, maxLines):
        """
        Produces a formatted list of skills, grouped by subject, to be displayed on the results page.

        Parameters:
            skills (list of Skill): The list of Skill objects to be processed.
            maxLines (int): The maximum number of lines that can be displayed on the results page.

        Returns:
            list of str: A list of strings, where each string represents a line on the results page.
        """
        sorted_skills = sorted(skills, reverse=True)
        skills_by_subject = self.group_skills_by_subject(sorted_skills)

        res_skills = []
        for i in range(min(maxLines, len(sorted_skills))):
            if self.is_valid(sorted_skills[:i + 1], skills_by_subject, maxLines):
                res_skills = sorted_skills[:i + 1]

        result = []
        included_skills_by_subject = self.group_skills_by_subject(res_skills)
        for subject in self.sort_subjects_by_priority(included_skills_by_subject):
            included_skills = sorted(included_skills_by_subject[subject], reverse=True)
            result.append(f"{subject} skills:")
            for skill in included_skills:
                result.append(skill.name)
            not_displayed = len(skills_by_subject[subject]) - len(included_skills)
            if not_displayed > 0:
                result.append(f"And {not_displayed} more!")
        return result


def generate_skills():
    skills = []
    data = [
        {'name': "Learn to count to 5", 'subject': "Math", 'priority': 14},
        {'name': "Skip counting by twos", 'subject': "Math", 'priority': 10},
        {'name': "Skip counting", 'subject': "Math", 'priority': 8},
        {'name': "Multiply by 5", 'subject': "Math", 'priority': 5},
        {'name': "Reducing fractions", 'subject': "Math", 'priority': 3},
        {'name': "Using commas", 'subject': "Language arts", 'priority': 12},
        {'name': "Parts of speech", 'subject': "Language arts", 'priority': 9},
        {'name': "Parts of a book", 'subject': "Language arts", 'priority': 2},
        {'name': "The Civil War", 'subject': "History", 'priority': 6},
        {'name': "The Panama Canal", 'subject': "History", 'priority': 1},
        {'name': "States of matter", 'subject': "Science", 'priority': 11}
    ]
    for d in data:
        skills.append(Skill(d['priority'], d['name'], d['subject']))
    return skills


if __name__ == '__main__':
    maxLines = 13
    skills = generate_skills()
    producer = SkillPageProducer()
    results = producer.results(skills, maxLines)
    for r in results:
        print(r)
