"""
This will generate the result of a school for all the classes entered by the teacher
School class will create the stack of classes with special details to be asked while 
taking student's details as input.

Each class will take total subject and MAX MARKS of each subject and then it will 
take each student's details, marks in each subject and at the same time it will be calculating the result of that 
student.

At last after all inputs for all the classes is generated you can see the result of either complete school
or complete result of a complete class or result of a single students or a list of students 

"""
from datetime import datetime
import time 
import sys

class School:
    def __init__(self, name, class_count, min_marks_percent): 
        self.name = name
        self.class_count = class_count
        self.min_marks_percent = min_marks_percent

    def generate(self):
        print("Started Generating Class....")
        for i in range(self.class_count):
            setattr(self, f"class_{i}", Class(self.name, i+1))
        
    def __repr__(self):
        s = f"""# --------- {self.name} --------- #
        """
        for next_key, next_val in zip(tuple(self.__dict__.keys())[3:], tuple(self.__dict__.values())[3:]):

            if next_key != "school_efficiency" and next_key != "class_result" and next_key != "avg":
                s += "{}\n{}".format("Min Marks: "+str(self.min_marks_percent), next_val)
        # printing about the school

        #efficiency of the school
        s += "\nOverall School performance-\n"
        s += "\n{} : {}\n".format("School Efficiency".ljust(20), str(self.school_efficiency).ljust(20))
        
        # result of the each complete class
        s += "\nSorted list of the overall result of each class - "
        for i in self.class_result:
            s += "\n{} : AVERAGE => {}, EFFICIENCY => {}".format(i[-1].ljust(20), str(i[0]).ljust(20), str(i[1]).ljust(20))

        # average of whole school
        s += "\n{} : {}".format("Average result of school".ljust(20), str(self.avg).ljust(20))
        return s
        

class Class:
    def __init__(self,school, index = None): 
        try:
            self.school = school
            self.name = input(f"\n\nEnter the name of class_{index}.\n@{self.school}>>> ")

            print("\nEnter subjects (comma seperated). Example: Sub1 Sub2 Sub2")
            self.subject = [[sub.strip()] for sub in input(f"@{self.school}\\{self.name}>>> ").strip().split(",")]

            print("\nEnter the MAXIMUN MARKS of all the above subjects.")
            n = len(self.subject)
            count = 0
            while count < n:
                max_mark = input(f"@{self.school}\\{self.name}\\{self.subject[count][0]}>>> ")
                if max_mark.isnumeric():
                    self.subject[count].append(float(max_mark))
                    count += 1
                else:
                    print("Error: Maximum marks should be number.")

            print("\nEnter number of students.")
            self.student_count = int(input(f"@{self.school}\\{self.name}>>> "))
            student_index = 0
            while student_index < self.student_count:
                print(f"Enter Roll number of student{student_index + 1}.")
                try:
                    roll = int(input(f"@{self.school}\\{self.name}>>> "))
                except ValueError:
                    print("Roll number should be a number")
                    continue
                print(f"Enter student's name{student_index + 1}.")
                try:
                    student_name = input(f"@{self.school}\\{self.name}\\{roll}>>> ").strip()
                except ValueError:
                    student_index -= 1
                    continue
                
                student = Student(roll, student_name)

                print("\nEnter obtained marks in-")
                n = len(self.subject)
                count = 0
                while count < n:
                    try:
                        i = self.subject[count]
                        mark = input(f"@{self.school}\\{self.name}\\{roll}\\{student_name}\\{i[0]}>>> ")
                        if float(mark) <= i[1]:
                            student.add_mark(i[0],mark)
                            count += 1
                        else:
                            print("Error: Obtained mark can't be greater than Maximum Marks.")
                    except:
                        print("Error: Obtained marks should be number.")
                setattr(self, f"student_{student_index+1}", student)
                student_index += 1

        except ValueError:
            print("Invalid input! input should be an integer.")
            sys.exit()
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("Invalid action while initializing class.")
            sys.exit(0)

    def __repr__(self):
        s = "\n\n#------------------{}-------------------#".format("Class - "+self.name)
        for key,student in zip(tuple(self.__dict__.keys())[4:],tuple(self.__dict__.values())[4:]):
            if key != "avg" and key != "max" and key != "min" and key != "passed" and key != "failed" and key != "result_status" and key !="class_efficiency":
                s += str(student)
        
        # Average of the class
        s += "\n\t{} : {}".format("Average".ljust(30), str(self.avg).ljust(30))

        # Max marks obtainer of the class
        s += "\n\t{} : {}".format("First Rank".ljust(30), str(self.max).ljust(30))

        #Lowest mark obtainer of the class
        s += "\n\t{} : {}".format("Lowest Rank".ljust(30), str(self.min).ljust(30))

        # Total Passed students in the class
        s += "\n\t{} : {}".format("Passed Students".ljust(30), str(self.passed).ljust(30))

        # Total Failed students in the class
        s += "\n\t{} : {}".format("Failed Students".ljust(30), str(self.failed).ljust(30))

        # sorted list of the student with maximum to lowest marks
        s += "\n\n\tShort view of the result of the class"
        s += "\n\t{} : {}".format("Roll No.[Name]".ljust(40), "Total / Status".ljust(40))
        for val in self.result_status: # 2 3 1 0
            s += "\n\t{} : {}".format(f"{val[2]}[{val[3]}]".ljust(40), f"{val[1]} / {val[0]}".ljust(40))

        # printing the efficiency of the class
        s += "\n\t{} : {}".format("Class Efficiency".ljust(30), str(self.class_efficiency).ljust(30))
        return s+"\n\n"


class Student:
    def __init__(self, roll, student_name):
        self.roll = roll
        self.student_name = student_name

    def add_mark(self,subject, mark):
        setattr(self, subject, float(mark))

    def __repr__(self):
        s = "\n__________________________________________\n"
        for key, value in zip(self.__dict__.keys(), self.__dict__.values()):
            if key == "roll":
                s += "\t\t{}: {}\n".format("Roll No.".ljust(30), str(value).ljust(20))
            elif key == "student_name":
                s += "\t\t{}: {}\n".format("Student Name.".ljust(30), str(value).ljust(30))
            elif key =="result_status":
                for status in value:
                    s += "\t\t{}: {} => {}\n".format(status[1].ljust(30),str(status[0]).ljust(30), status[-1].rjust(2))
            elif key == "total":
                s += "\t\t{}: {}\n".format("Total Marks".ljust(30), str(value).ljust(30))
            elif key == "max":
                s += "\t\t{}: {}\n".format("Max of all the subjects".ljust(30), str(value).ljust(30))
            elif key == "min":
                s += "\t\t{}: {}\n".format("Min of all the subjects".ljust(30), str(value).ljust(30))
            elif key == "avg":
                s += "\t\t{}: {}\n".format("Average of all the subjects".ljust(30), str(value).ljust(30))
            elif key =="passed_in":
                s += "\t\t{}: {}\n".format("Passed Subjects".ljust(30), str(value).ljust(30))
            elif key == "failed_in":
                s += "\t\t{}: {}\n".format(key.ljust(30), str(value).ljust(30))

            elif key == "efficiency":
                s += "\t\t{}: {}\n".format(key.title().ljust(30), str(value).ljust(30))
        return s
        

class ResultGenerator:
    """
    This class is responsible for generating the result.
    Sets the calculated result to the school object so that it can be accessed later.
    """
    def __init__(self, school):
        self.school = school

    def calculate(self):
        min_marks_percent = self.school.min_marks_percent # minimum marks percentage
        school_sum = school_average = school_efficiency =  0
        school_result_status = []

        for current_key, current_class in zip(tuple(self.school.__dict__.keys())[3:self.school.class_count + 3], tuple(self.school.__dict__.values())[3:self.school.class_count + 3]):
            class_total = passed_student = 0
            class_result_status = []
            for current_student_key, current_student in zip(tuple(current_class.__dict__.keys())[4:current_class.student_count + 4], tuple(current_class.__dict__.values())[4:current_class.student_count + 4]):
                sum = avg = count =  0
                result_status, max, min = [], [], []
                status, final_result  = None, "Pass"
                passed_subject = 0
                for current_subject, current_subject_mark in zip(tuple(current_student.__dict__.keys())[2:len(current_class.subject) + 2], tuple(current_student.__dict__.values())[2:len(current_class.subject)+2]):
                    sum += current_subject_mark # totaling the marks of the student

                    if current_subject_mark >= current_class.subject[count][-1] * (min_marks_percent / 100):
                        status = "Pass"
                        passed_subject += 1
                    else:
                        status = final_result = "Fail"

                    result_status.append([current_subject_mark, current_subject, status])

                    # incrementing the count of subject in the current class    
                    count += 1

                    result_status.sort() # sorting the result to get ordered result
                    max, min = result_status[-1], result_status[0]
                    
                    #setting max min and result status to the student object
                    setattr(current_student, "result_status", result_status)
                    setattr(current_student, "max", max)
                    setattr(current_student, "min", min)
                
                #average of the student's marks
                avg = sum / count

                # efficiency of the student
                total_marks = 0
                for i in current_class.subject:
                    total_marks += i[-1]

                student_efficiency = sum / total_marks

                # Adding average and efficiency , passed , failed of  the student to the student object
                setattr(current_student, "total", sum)
                setattr(current_student, "avg", avg)
                setattr(current_student, "efficiency", student_efficiency)
                setattr(current_student, "passed_in", passed_subject)
                setattr(current_student, "failed_in", len(current_class.subject) - passed_subject)
                
                # adding sum of the students' total marks
                class_result_status.append([final_result, sum, current_student.roll, current_student.student_name])

                #Class Total marks(to help in finding average of the complete class performance)    
                class_total += sum

                # taking pass count of the students
                if final_result == "Pass":
                    passed_student += 1

            class_result_status.sort(reverse=True) # sorting the result to get ordered result

            class_avg = class_total / current_class.student_count

            setattr(current_class, "avg", class_avg)
            setattr(current_class, "max", class_result_status[0])
            setattr(current_class, "min", class_result_status[-1])
            setattr(current_class, "result_status", class_result_status)
            setattr(current_class, "passed", passed_student)
            setattr(current_class, "failed", current_class.student_count - passed_student)
            setattr(current_class, "class_efficiency", passed_student / current_class.student_count)

            # adding average of the of the average of each class to be used later to get the average performance of the school
            school_sum += class_avg
            
            school_efficiency += current_class.class_efficiency
            school_result_status.append([current_class.avg, current_class.class_efficiency, current_class.name])
        school_result_status.sort()
        setattr(self.school, "class_result", school_result_status)
        setattr(self.school,"avg",school_sum/self.school.class_count)
        setattr(self.school, "school_efficiency", school_efficiency / self.school.class_count)



def initialize(school = None, schools = []):
    try:
        if school is None:
            print("\nHello dear teacher! Its time to initialize your school...")
            school_name = input("Enter the name of your school: ") 
            class_count = int(input(f"Enter total number of classes.\n@{school_name}>>> "))
            min_marks_percent = int(input(f"Enter minimum passing percentage.\n@{school_name}>>> ")) if class_count > 0 else 0
            school = School(school_name, class_count, min_marks_percent)
            
            # Generating a Complete School Structure
            school.generate()

            #calculating the result for this school
            result = ResultGenerator(school) # Generating object

            print("Starting Calculation...")
            result.calculate() # calculating the result
            print("Calculation Completed")

            print(school)
            schools.append(school)
            return initialize(school, schools)
        else:
            print("Use 'exit' to close the program, 'new' to initialize new school, 'help' to get help, 'print' to print the complete result of current school")
            command = input(f"#{school.name}>>> ")
            if command == "exit":
                return False
            elif command == "new":
                return True
            else:
                cmdl = command.split()
                if len(cmdl) > 1 or cmdl[0] == "help" or cmdl[0] == "print":
                    if cmdl[0] == "use":
                        if len(cmdl) > 2:
                            print(f"Error: cannot use [{' '.join(cmdl[1:])}] schools at the same time. Choose only one school at a time\n")

                        else:
                            for check in schools:
                                if isinstance(check,School) and check.name == cmdl[1]:
                                    return initialize(check, schools)
                            print("Error: school '{}' is not found.".format(cmdl[1]))
                            return initialize(school, schools)

                    elif cmdl[0] == "show":
                        if len(cmdl) > 1 and len(cmdl) < 3:
                            for check in schools:
                                for cls_check in check.__dict__.values():
                                    if isinstance(cls_check,Class) and cls_check.name == cmdl[1]:
                                        print(cls_check)
                                        return initialize(school, schools)
                            print("Error:class {} is not found.".format(cmdl[1]))
                            return initialize(school,schools)
                        elif len(cmdl) > 2:
                            for check in schools:
                                cls_check = None
                                for cls_check in check.__dict__.values():
                                    if isinstance(cls_check,Class) and cls_check.name == cmdl[1]:
                                        for student in cls_check.__dict__.values():
                                            if cmdl[2].strip().isalpha():
                                                if isinstance(student,Student) and student.student_name == " ".join(cmdl[2:]):
                                                    print(student)
                                                    return initialize(school,schools)
                                            else:
                                                if isinstance(student,Student) and student.roll == int(cmdl[2].strip()):
                                                    print(student)
                                                    return initialize(school,schools)

                                        break
                                print("Error:class {} is not found.".format(cmdl[1]))
                                return initialize(school,schools)
                        else:
                            print("Error: only two arguments can follow show keyword.")      
                            return initialize(school,schools)
                    elif cmdl[0] == "help":
                        help = "{} : {}\n".format("new".ljust(15), "used to create new school instance.")
                        help += "{} : {}\n".format("use <school>".ljust(15), "used to use any previously created school instance with its name(Case sensitive).")
                        help += "{} : {}\n".format("help".ljust(15),"used to get help.")
                        help += "{} : {}\n".format("show <c> <s>".ljust(15),"used to print the complete result of a selected student(to select a student either use name(Case sensitive) or roll number.)")
                        help += "{} : {}\n".format("show <c>".ljust(15),"used to print the complete result of a selected class(Case sensitive).")
                        help += "{} : {}\n".format("print".ljust(15), "used to print the result of the current class")
                        print(help)
                        return initialize(school,schools)

                    elif cmdl[0] == "print":
                        print(school)
                        return initialize(school,schools)

                elif len(cmdl) == 1:
                    if cmdl[0] == "use":
                        print("Error: 'use' keyword should be followed by a school name.")
                        return initialize(school,schools)
                    else:
                        print("Error: 'show' keyword should be followed by class name or class name and student name or roll number.")
                        return initialize(school,schools)
                else:
                    initialize(school,schools)
    except KeyboardInterrupt:
        sys.exit()
    except ValueError:
        print("Invalid input! input should be an integer.")
    except Exception as e:
        return False


if __name__ =="__main__":
    while True:
        try:
            rttype = initialize()
            if not rttype:
                break
        except:
            print("Invalid operation")
            break