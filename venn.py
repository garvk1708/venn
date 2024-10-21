from matplotlib_venn import venn2, venn3
from matplotlib import pyplot as plt

while True:
    print("This algorithm helps you to operate some of the basic set functions on Venn diagrams.")
    function_set = input("Type 'int' for intersection, 'sum' for union of two sets, 'diff' for difference of two sets, and 'sym diff' for symmetric difference of two sets: ").strip().lower()
    number_set = int(input("Enter 2 for operating on a pair of sets and 3 for operating on three sets: "))
    
    setAA, setBB, setCC = set(), set(), set()  # Initialize sets

    def get_set_input(set_name, num_elements):
        new_set = set()
        for i in range(num_elements):
            elem = int(input(f"Enter element {i+1} in {set_name}: "))
            new_set.add(elem)
        return new_set

    def myvenn2():
        seta_ele = int(input("Enter the number of elements you want in your SET A: "))
        setb_ele = int(input("Enter the number of elements you want in SET B: "))
        
        global setAA, setBB
        setAA = get_set_input("Set A", seta_ele)
        setBB = get_set_input("Set B", setb_ele)
        
        venn2([setAA, setBB], set_labels=('Set A', 'Set B'))
        plt.title("Venn Diagram for Set A and Set B")
        plt.show()

    def myvenn3():
        seta_ele = int(input("Enter the number of elements you want in your SET A: "))
        setb_ele = int(input("Enter the number of elements you want in SET B: "))
        setc_ele = int(input("Enter the number of elements you want in SET C: "))
        
        global setAA, setBB, setCC
        setAA = get_set_input("Set A", seta_ele)
        setBB = get_set_input("Set B", setb_ele)
        setCC = get_set_input("Set C", setc_ele)
        
        venn3([setAA, setBB, setCC], set_labels=('Set A', 'Set B', 'Set C'))
        plt.title("Venn Diagram for Set A, Set B, and Set C")
        plt.show()

    def union():
        if number_set == 2:
            print("A ∪ B = ", setAA | setBB)
        else:
            print("A ∪ B ∪ C = ", setAA | setBB | setCC)

    def inter():
        if number_set == 2:
            print("A ∩ B = ", setAA & setBB)
        else:
            print("A ∩ B ∩ C = ", setAA & setBB & setCC)

    def diff():
        if number_set == 2:
            print("A - B = ", setAA - setBB)
        else:
            print("A - B - C = ", setAA - setBB - setCC)

    def symdiff():
        if number_set == 2:
            print("A Δ B = ", setAA ^ setBB)
        else:
            print("A Δ B Δ C = ", setAA ^ setBB ^ setCC)

    # Main logic
    if number_set == 2:
        myvenn2()
    elif number_set == 3:
        myvenn3()
    else:
        print("Invalid input: number_set must be 2 or 3.")
        continue

    # Execute the chosen operation
    if function_set == "int":
        inter()
    elif function_set == "sum":
        union()
    elif function_set == "diff":
        diff()
    elif function_set == "sym diff":
        symdiff()
    else:
        print("Invalid operation input. Please choose from 'int', 'sum', 'diff', or 'sym diff'.")
