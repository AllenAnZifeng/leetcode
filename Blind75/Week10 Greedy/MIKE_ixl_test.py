import unittest
from mike_ixl import Skill, SkillPageProducer

class TestSkillPageProducer(unittest.TestCase):
    def generate_skills(self):
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

    def setUp(self):
        self.skills = self.generate_skills()
        self.producer = SkillPageProducer()

    def test_grouping_by_subject(self):
        grouped_skills = self.producer.group_skills_by_subject(self.skills)
        self.assertEqual(len(grouped_skills), 4)
        self.assertEqual(len(grouped_skills["Math"]), 5)
        self.assertEqual(len(grouped_skills["Language arts"]), 3)

    def test_valid_line_count(self):
        result = self.producer.results(self.skills, 10)
        self.assertTrue(len(result) <= 10)  # Check that the result respects the max line limit
        result = self.producer.results(self.skills, 0)
        self.assertTrue(len(result) <= 0)

    def test_empty_skills(self):
        result = self.producer.results([], 10)
        self.assertEqual(len(result), 0)

    def test_skill_prioritization(self):
        # Test that skills are prioritized correctly
        result = self.producer.results(self.skills, 10)
        self.assertIn("Math skills", result[0])
        self.assertIn("Learn to count to 5", result[1])

    def test_subject_bundle_rules(self):
        # Test that single skills from a unique subject are included
        unique_skill = [Skill(15, "Explore galaxies", "Astronomy")]
        result = self.producer.results(unique_skill, 3)
        self.assertIn("Astronomy skills", result[0])
        self.assertIn("Explore galaxies", result[1])

    def test_tight_max_lines(self):
        # Test case given in the interview prompt
        result = self.producer.results(self.skills, 13)
        self.assertEqual(len(result), 11)

    def test_large_max_lines(self):
        # Test that the result with a large maxLines includes all skills
        result = self.producer.results(self.skills, 100)
        self.assertEqual(len(result), len(self.skills) + 4)  # 4 subjects


if __name__ == '__main__':
    unittest.main()
