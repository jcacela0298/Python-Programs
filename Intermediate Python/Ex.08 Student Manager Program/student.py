"""
Program: student.py 
Author: Jack Cacela 
This file contains the blueprints to manage a student's name and test scores.  
"""

class Student(object):
    """Represents a student."""
    
    def __init__(self, name, number):
        """Constructor creates a Student with the given
        name, number of scores, and sets all scores
        to 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name

    def setScore(self, i, score):
        """Sets the ith score, counting from 1 for simple user interface."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1 for simple user interface."""
        return self.scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

    def __str__(self):
        """Returns the student's string representation."""
        return "Name: " + self.name + "\nScores: " + " ".join(map(str, self.scores))

if __name__ == "__main__":

    student1 = Student("John Doe", 3)
    student1.setScore(1, 80)
    student1.setScore(2, 75)
    student1.setScore(3, 90)
    
    print("Student:", student1.getName())
    print("Scores:", student1.getScore(1), student1.getScore(2), student1.getScore(3))
    print("Average score:", student1.getAverage())
    print("Highest score:", student1.getHighScore())