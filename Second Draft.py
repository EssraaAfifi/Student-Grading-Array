#Task 1 Improved/Shortened

e = int(3)
Student_Names = []
Test_One_Marks = []
Test_Two_Marks = []
Test_Three_Marks = []
Total_Scores = []


for i in range (e):
    print ("Insert ",i+1," Student's Name")
    Name = str(input())
    Student_Names.insert(i,Name)
    
    print("Insert ",Student_Names[i],"'s First Test Grades")
    Grade1 = int(input())
    Test_One_Marks.insert(i,Grade1)
    
    print("Insert ",Student_Names[i],"'s Second Test Grades")
    Grade2 = int(input())
    Test_Two_Marks.insert(i,Grade2)

    print("Insert ",Student_Names[i],"'s Third Test Grades")
    Grade3 = int(input())
    Test_Three_Marks.insert(i,Grade3)

    Total= int(Test_One_Marks[i]+Test_Two_Marks[i]+Test_Three_Marks[i])
    Total_Scores.insert(i,Total)

    print("\n")

#Priting All Together
for at in range (e):
    print("\n\n")
    print(Student_Names[at],"Got: \n",Test_One_Marks[at]," in her First test \n",Test_Two_Marks[at]," in her Second test \n",Test_Three_Marks[at]," in her Third test \n","And finally, ",Total_Scores[at]," When all are added up")
