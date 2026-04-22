class StudentData:
    def __init__(self):
        self.name = ""
        self.score = 0


if "__main__" == __name__:
    char = ""
    class_list = list[StudentData]()
    while "0" != char:
        data = StudentData()
        data.name = str(input("Nhap ten: "))
        data.score = float(input("Nhap diem: "))
        class_list.append(data)
        char = str(input("Press 0 to stop, and press any key to continue: "))
    sum = 0
    no = 0
    max_score = 0
    for student in class_list:
        sum = sum + student.score
        no = no + 1
        if max_score <= student.score:
            max_score = student.score
    average = sum / no
    print("Diem trung binh la: ", average)
    for student in class_list:
        if student.score == max_score:
            print("Sinh vien %s co diem cao nhat" % student.name)
            break

    f = open("diem_thi.txt", "w")
    f.write("Class List:\n")
    for student in class_list:
        f.write("%s\t%.2f\n" % (student.name, student.score))
    f.close()
