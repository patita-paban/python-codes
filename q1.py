# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
total_height = 0
for height in student_heights:
  total_height += height

number_of_stud = 0
for len in student_heights:
  number_of_stud += 1
  
average = total_height/number_of_stud
print(f"the average heigh is :{average}")
  




