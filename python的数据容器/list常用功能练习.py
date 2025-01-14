def ptf():
    print(age_student)
    return None

age_student = [21, 25, 21, 23 , 22, 20]
ptf()
age_student.append(31)
ptf()
age_student.extend([29, 33, 30])
ptf()
pop1 = age_student.pop(0)
print(pop1)
pop2 = age_student.pop(-1)
print(pop2)
index1 = age_student.index(31)
print(index1)
ptf()