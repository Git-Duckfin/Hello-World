def student_clac(student) :
    tot = student["kor"]+student["eng"]+student["math"]
    avg = tot/3
    if 90 <= avg <= 100 : grade = "A"
    elif 80 <= avg < 90 : grade = "B"
    elif 70 <= avg < 80 : grade = "C"
    elif 60 <= avg < 70 : grade = "D"
    else : grade = "F"
    student["tot"] = tot
    student["avg"] = avg
    student["grade"] = grade

def student_output(student) :
    print('이름     국어    영어    수학    총점    평균    평점')
    print(f'{student["irum"]}\t{student["kor"]}\t{student["eng"]}', end='\t')
    print(f'{student["math"]}\t{student["tot"]}', end='\t')
    print(f'{student["avg"]:.2f}\t{student["grade"]}')

def student_input(student) :
    irum = input('Name : ')
    kor = int(input('Korean : '))
    eng = int(input('English : '))
    math = int(input('Math : '))
    student["irum"] = irum
    student["kor"] = kor
    student["eng"] = eng
    student["math"] = math

student = {}
student_input(student)
student_clac(student)
student_output(student)
print(student)