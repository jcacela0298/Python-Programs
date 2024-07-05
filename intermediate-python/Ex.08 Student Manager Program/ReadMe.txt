Features:


This student.py file focuses on the class and object paradigm for Python programming where we include getters, setters, the __init__ method to initialize a new student object, and the __str__ method which returns the string representation of the object with the characteristics and instance variables at a given time.

An interesting part of the __str__ method includes the following line of code:

" ".join(map(str, self.scores)) 

which helps construct a space-separated string of the scores, where we use "map" to implement the string function to each score in the array.

At the end, this file also includes this code:

if __name__ == "__main__":
    # Example usage:
    student1 = Student("John Doe", 5)
    student1.setScore(1, 80)
    student1.setScore(2, 75)
    student1.setScore(3, 90)
    
    print("Student:", student1.getName())
    print("Scores:", student1.getScore(1), student1.getScore(2), student1.getScore(3))
    print("Average score:", student1.getAverage())
    print("Highest score:", student1.getHighScore())


Which is one way of testing the program -- When this program is run directly, and not imported as a module, it will run the code under:

if __name__ == "__main__":

and it will create an example student, printing the student's details to prove that the methods function properly.





Usage:


To run this program, simply run the student.py file and observe the output in terminal. If you wish to change the output, make sure to modify the code within the 

if __name__ == "__main__":

section, and re run the file.





Example:

If the "if __name__ == "__main__":" section is this:

if __name__ == "__main__":

    student1 = Student("John Doe", 3)
    student1.setScore(1, 80)
    student1.setScore(2, 75)
    student1.setScore(3, 90)
    
    print("Student:", student1.getName())
    print("Scores:", student1.getScore(1), student1.getScore(2), student1.getScore(3))
    print("Average score:", student1.getAverage())
    print("Highest score:", student1.getHighScore())



Then the terminal output will be:

Student: John Doe
Scores: 80 75 90
Average score: 81.66666666666667
Highest score: 90

