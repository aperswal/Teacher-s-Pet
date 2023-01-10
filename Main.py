import Objects
import Visualizations

def main():
    # Database Inputs
    while True:
        class_number = input("Enter the class number: ")
        name = input("Enter the student's name: ")
        homework_grades = input("Enter the student's homework grades (separated by spaces): ").split()
        test_grades = input("Enter the student's test grades (separated by spaces): ").split()

        Objects.add_student(class_number, name, homework_grades, test_grades)

        another = input("Add another student (y/n)? ")
        if another.lower() == "n":
            break
    
    # Full Table View
    full_look_up = input("Would you like to see all your classes grades? (y/n) ")
    full_look_up.lower()
    if (full_look_up=="y"):
        Objects.print_grades()     
    
    # Class View  
    class_look_up = input("Would you like to see the grades of a particular class (y/n)? ")
    class_look_up.lower()
    if (class_look_up=="y"):
        class_checker = input("Which class you want to inquire about? (Numbers only) ")
        print(f"Class Number: {class_checker}")
        Objects.print_grades_by_class_num(class_checker)
    
    # Student View
    student_look_up = input("Would you like to see the grades of a student? (y/n) ")
    student_look_up.lower()
    if (student_look_up=="y"):
        student_checker = input("What is the name of the student you want to inquire about? ")
        Objects.print_grades_by_student(student_checker)
        
    # Full Test Bar Chart
    full_test_table_look_up = input("Would you like to see a bar chart of every student's test scores? (y/n) ")
    full_test_table_look_up.lower()
    if (full_test_table_look_up=="y"):
        Visualizations.test_bar_chart()
          
    # Specific Student Test Bar Chart
    test_student_look_up = input("Would you like to see the test grades of a student? (y/n) ")
    test_student_look_up.lower()
    if (test_student_look_up=="y"):
        test_student_checker = input("What is the name of the student you want to inquire about? ")
        Visualizations.student_test_bar_chart(test_student_checker)
        
    # Full Homework Line graph
    full_homework_graph_look_up = input("Would you like to see a line graph of every student's homework scores? (y/n) ")
    full_homework_graph_look_up.lower()
    if (full_homework_graph_look_up=="y"):
        Visualizations.homework_line_graph()
        
    # Specific Student Homework Line Chart
    homework_student_look_up = input("Would you like to see the homework grades of a student? (y/n) ")
    homework_student_look_up.lower()
    if (homework_student_look_up=="y"):
        homework_student_checker = input("What is the name of the student you want to inquire about? ")
        Visualizations.student_homework_line_graph(homework_student_checker)
    
    # Full Test Normal Distribution
    full_test_distribution_look_up = input("Would you like to see a normal distribution of every student's test scores? (y/n) ")
    full_test_distribution_look_up.lower()
    if (full_test_distribution_look_up=="y"):
        Visualizations.test_normal_distribution()
        
    #Full Homework Normal Distribution
    full_homework_distribution_look_up = input("Would you like to see a normal distribution of every student's homework scores? (y/n) ")
    full_homework_distribution_look_up.lower()
    if (full_homework_distribution_look_up=="y"):
        Visualizations.homework_normal_distribution()
        
    # Specific Class Test Normal Distribution
    
    # Specific Class Homework Normal Distribution
    
    
    
main()