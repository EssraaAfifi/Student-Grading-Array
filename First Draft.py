#Task 1

e = int(3)
Student_Names = []
Test_One_Marks = []
Test_Two_Marks = []
Test_Three_Marks = []
Total_Scores = []

#Student Names
for i in range (e):
    print ("Insert ",i+1," Student's Name")
    Name = str(input())
    Student_Names.insert(i,Name)

#First Grade
for x in range (e):
    print("Insert ",Student_Names[x],"'s First Test Grades")
    Grade1 = int(input())
    Test_One_Marks.insert(x,Grade1)

#Second Grade
for y in range (e):
    print("Insert ",Student_Names[y],"'s Second Test Grades")
    Grade2 = int(input())
    Test_Two_Marks.insert(y,Grade2)

#Third Grade
for z in range (e):
    print("Insert ",Student_Names[z],"'s Third Test Grades")
    Grade3 = int(input())
    Test_Three_Marks.insert(z,Grade3)

#Total Scores
for xyz in range (e):
    Total= int(Test_One_Marks[xyz]+Test_Two_Marks[xyz]+Test_Three_Marks[xyz])
    Total_Scores.insert(xyz,Total)

#Priting All Together
for at in range (e):
    print("\n")
    print("\n")
    print(Student_Names[at],"Got: \n",Test_One_Marks[at]," in her First test \n",Test_Two_Marks[at]," in her Second test \n",Test_Three_Marks[at]," in her Third test \n","And finally, ",Total_Scores[at]," When all are added up")
