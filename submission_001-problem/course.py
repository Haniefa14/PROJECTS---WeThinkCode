
def create_outline():

    #Step 1: Topics

    print("Course Topics:")

    topics = set(["Introduction to Python", "Tools of the Trade", "How to make decisions", "How to repeat code", "How to structure data", "Functions", "Modules"])
    list_topics = list(topics)
    list_topics.sort()
    for topics in list_topics:
        print("* " + topics)

    #Step 2: Adding Problems

    def tasks(i):
        return i+ " : Problem 1, Problem 2, Problem 3"
    print("Problems: ")

    mapping = map(tasks, list_topics)
    mapping = list(mapping)

    for map_list in mapping:
        print("*", map_list)
    
    #step 3: Keeping track

    print("Student Progress:")

    #student_name = ("Haniefa", "Adam", "Nyari", "Brian")
    #status = ("STARTED", "GRADED", "COMPLETED")

    student1 = (" Haniefa- ", "Functions- ", "Problem 1- ","[STARTED] ")
    student2 = (" Adam- ","Modules- ", "Problem 2- ","[GRADED] ")
    student3 = (" Nyari- ", "How to structure data- ","Problem 3- ","[COMPLETED] ")


    #Step 4 Sorting

    sorted_list1 = ''.join(sorted(student1))
    sorted_list2 = ''.join(sorted(student2))
    sorted_list3 = ''.join(sorted(student3))

    print("1.", sorted_list1)
    print("2.", sorted_list2)
    print("3.", sorted_list3)

    print()

if __name__ == "__main__":
    create_outline()