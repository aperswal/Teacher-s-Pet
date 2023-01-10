import matplotlib.pyplot as plt
import Objects
import numpy as np

def test_bar_chart():
    # Get the names and test grades for all students
    names = [student.name for student in Objects.students]
    test_grades = [student.test_grades for student in Objects.students]

    # Get the number of tests for each student
    num_tests = [len(student.test_grades) for student in Objects.students]
    max_tests = max(num_tests)

    # Create a list of colors for the bars
    colors = ['red', 'blue', 'green', 'purple', 'yellow']

    # Create the bar chart
    fig, ax = plt.subplots()
    for i, name in enumerate(names):
        for j, test_grade in enumerate(test_grades[i]):
            # Use the colors list to set the color of the bar
            color = colors[j % len(colors)]
            ax.bar(i + j/max_tests, test_grade, width=0.4, color=color)
    plt.show()

    
def student_test_bar_chart(student_name):
    # Get the names of all students
    names = [student.name for student in Objects.students]
    
    # Find the student with the given name
    for student in Objects.students:
        if student.name == student_name:
            test_grades = student.test_grades
            break
    else:
        print(f"Error: student with name {student_name} not found.")
        return

    # Get the number of tests for the chosen student
    num_tests = len(test_grades)

    # Create the bar chart
    fig, ax = plt.subplots()
    for i in range(num_tests):
        ax.bar(i, test_grades[i], width=0.4, color='b')
    plt.xticks(range(num_tests))
    plt.xlabel('Tests')
    plt.ylabel('Scores')
    plt.title(f'{student_name}\'s Test Grades')
    plt.show()


def homework_line_graph():
    # Get the names and homework grades for all students
    names = [student.name for student in Objects.students]
    homework_grades = [student.homework_grades for student in Objects.students]

    # Get the number of homework assignments for each student
    num_assignments = [len(student.homework_grades) for student in Objects.students]
    max_assignments = max(num_assignments)

    # Create the line chart
    fig, ax = plt.subplots()

    # Create a unique color for each student
    colors = np.random.rand(len(Objects.students),3)
    for i, name in enumerate(names):
        # make sure all lines are plotted to the same x-axis point
        x_axis = range(len(homework_grades[i]))
        ax.plot(x_axis, homework_grades[i], label=name, color=colors[i])

    # Add flags at the end of each line to indicate the student's name
    for i, name in enumerate(names):
        ax.annotate(name, xy=(len(homework_grades[i])-1, homework_grades[i][-1]), xytext=(len(homework_grades[i])+1, homework_grades[i][-1]),
                    arrowprops=dict(facecolor='black', shrink=0.05))

    plt.xlabel("Assignment Number")
    plt.ylabel("Grade")
    plt.title("Homework Grades by Student")
    plt.legend()
    plt.show()

def student_homework_line_graph(name):
    student_homework_grades = []
    for student in Objects.students:
        if student.name == name:
            student_homework_grades = student.homework_grades
    # Plot the line graph using the filtered homework grades
    plt.plot(student_homework_grades)
    plt.xlabel('Homework Assignments')
    plt.ylabel('Grades')
    plt.title(f'{name}\'s Homework Grades')
    plt.show()
    
def test_normal_distribution():
    test_scores = [grade for student in Objects.students for grade in student.test_grades]

    mean = np.mean(test_scores)
    std_dev = np.std(test_scores)

    plt.hist(test_scores, bins=20, density=True, color='g', alpha=0.6)
    plt.xlabel("Test Scores")
    plt.ylabel("Density")
    plt.title("Test Scores Normal Distribution")

    # Plot the normal distribution curve
    x = np.linspace(np.min(test_scores), np.max(test_scores), 100)
    plt.plot(x, 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std_dev**2) ), linewidth=2, color='r')

    plt.text(0.5, 0.5, f"Mean: {mean}\nStandard Deviation: {std_dev}",
                fontsize=12, transform=plt.gca().transAxes)
    plt.show()

    
def homework_normal_distribution():
    homework_scores = [grade for student in Objects.students for grade in student.homework_grades]

    mean = np.mean(homework_scores)
    std_dev = np.std(homework_scores)

    plt.hist(homework_scores, bins=20, density=True, color='g', alpha=0.6)
    plt.xlabel("Homework Scores")
    plt.ylabel("Density")
    plt.title("Homework Scores Normal Distribution")

    # Plot the normal distribution curve
    x = np.linspace(np.min(homework_scores), np.max(homework_scores), 100)
    plt.plot(x, 1/(std_dev * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std_dev**2) ), linewidth=2, color='r')

    plt.text(0.5, 0.5, f"Mean: {mean}\nStandard Deviation: {std_dev}",
                fontsize=12, transform=plt.gca().transAxes)
    plt.show()
    
