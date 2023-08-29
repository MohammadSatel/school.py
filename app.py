import math
from enum import Enum
import os
import pickle

class Actions(Enum):
    ADD_STUDENT = 0
    ADD_TEST = 1
    PRINT_STUDENT_AVRAGE = 2
    AVRAGE_SORTED = 3
    AVRAGE_SORTED_REVERSE =4
    BEST_STUDENT = 5
    WORST_STUDENT = 6
    PRINT_STUDENTS = 7
    EXIT = 8

class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.average = 0
    
class Test:
    def __init__(self):
        self.testName = ""
        self.testScore = 0
    
def displayMenu():
    for action in Actions:
        print(f"{action.name}-{action.value}")
    return Actions(int(input("Your choice: ")))

def cleanScreen():
    os.system('cls')
        
def menu():
    while True: 
        userSelection = displayMenu()
        if userSelection == Actions.ADD_STUDENT:
            addStudent(studentNameList, studentAgeList, studentAverageList)
        if userSelection == Actions.ADD_TEST: addTest()
        if userSelection == Actions.PRINT_STUDENT_AVRAGE: studentAverage()
        if userSelection == Actions.AVRAGE_SORTED: averageSorted()
        if userSelection == Actions.AVRAGE_SORTED_REVERSE: averageReverse()
        if userSelection == Actions.BEST_STUDENT: bestStudent()
        if userSelection == Actions.WORST_STUDENT: worstStudent()
        if userSelection == Actions.PRINT_STUDENTS: printStudents()
        if userSelection == Actions.EXIT:
            saveInfo()
            break
        
studentNameList = []
studentAgeList = []
studentAverageList = []

def addStudent(student_name_list, student_age_list, student_average_list):
    cleanScreen()
    student = Student()
    student.name = input("Student name: ")
    student.age = int(input("Student age: "))  
    student.average = float(input("Student average: "))

    student_name_list.append(student.name)
    student_age_list.append(student.age)
    student_average_list.append(student.average)

    
def printStudents():
    cleanScreen()
    print("Students ",studentNameList)
    print("Ages ",studentAgeList)
    print("Average ",studentAverageList)
    
testNameList = []
testScoreList = []

def addTest():
    cleanScreen()
    test = Test()
    test.testName = input("Test name: ")
    test.testScore = int(input("Test score: "))

    testNameList.append(test.testName)
    testScoreList.append(test.testScore)

def studentAverage():
    cleanScreen()
    average = sum(studentAverageList) / len(studentAverageList)
    print("Average:", average)

def averageSorted():
    cleanScreen()
    studentAverageList.sort(reverse=True)
    print(studentAverageList)
    
def averageReverse():
    cleanScreen()
    studentAverageList.sort()
    print(studentAverageList)

def bestStudent():
    cleanScreen()
    maxValue = max(studentAverageList)
    print("Best average is :",maxValue)

def worstStudent():
    cleanScreen()
    studentAverageList.sort(reverse=True)
    print("Worst average is :", studentAverageList[-1])
    
def saveInfo():
    data = {
        "studentNameList": studentNameList,
        "studentAgeList": studentAgeList,
        "studentAverageList": studentAverageList,
        "testNameList": testNameList,
        "testScoreList": testScoreList
    }
    with open("school_data.pkl", "wb") as file:
        pickle.dump(data, file)

def loadInfo():
    global studentNameList, studentAgeList, studentAverageList, testNameList, testScoreList
    try:
        with open("school_data.pkl", "rb") as file:
            data = pickle.load(file)
            studentNameList = data.get("studentNameList", [])
            studentAgeList = data.get("studentAgeList", [])
            studentAverageList = data.get("studentAverageList", [])
            testNameList = data.get("testNameList", [])
            testScoreList = data.get("testScoreList", [])
    except FileNotFoundError:
        # Handle the case when the file doesn't exist yet
        pass

if __name__ == "__main__":
    loadInfo()
    menu()

    
    