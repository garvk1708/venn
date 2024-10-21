from matplotlib_venn import venn2, venn2_circles, venn3, venn3_circles  # Remove deprecated venn2_unweighted
import matplotlib_venn as venn
from matplotlib import pyplot as plt

while True:
  
    print("This algorithm helps you to operate some of the basic set functions on Venn diagrams.")
    function_set = input("Type 'int' for intersection, 'sum' for union of two sets, 'diff' for difference of two sets, and 'sym diff' for symmetric difference of two sets: ")
    number_set = int(input("Enter 2 for operating on a pair of sets and 3 for operating on three sets: "))
    setAA = set()
    setBB = set()
    setCC = set()

    def myvenn2():
        seta_ele = int(input("Enter the number of elements you want in your SET A: "))
        setb_ele = int(input("Enter the number of elements you want in SET B: "))
        
        for i in range(seta_ele):
            tempseta = int(input(f"Enter element {i+1} in set A: "))
            setAA.add(tempseta)
            
        for i in range(setb_ele):
            tempsetb = int(input(f"Enter element {i+1} in set B: "))
            setBB.add(tempsetb)
        
        venn2([setAA, setBB], set_labels=('Set A', 'Set B'))  # Use venn2 instead of venn2_unweighted
        plt.title("Venn Diagram for Set A and Set B")  # Add a meaningful title
        plt.show()

    def myvenn3():
        seta_ele = int(input("Enter the number of elements you want in your SET A: "))
        setb_ele = int(input("Enter the number of elements you want in SET B: "))
        setc_ele = int(input("Enter the number of elements you want in SET C: "))
        
        for i in range(seta_ele):
            tempseta = int(input(f"Enter element {i+1} in set A: "))
            setAA.add(tempseta)
            
        for i in range(setb_ele):
            tempsetb = int(input(f"Enter element {i+1} in set B: "))
            setBB.add(tempsetb)
            
        for i in range(setc_ele):
            tempsetc = int(input(f"Enter element {i+1} in set C: "))
            setCC.add(tempsetc)
        
        venn3([setAA, setBB, setCC], set_labels=('Set A', 'Set B', 'Set C'))  # Use venn3 instead of venn3_unweighted
        plt.title("Venn Diagram for Set A, Set B, and Set C")
        plt.show()

    def union():
        if number_set == 2:
            print("A ∪ B = ", setAA | setBB)
            plt.title("A ∪ B")
        else:
            print("A ∪ B ∪ C = ", setAA | setBB | setCC)
            plt.title("A ∪ B ∪ C")

    def inter():
        if number_set == 2:
            print("A ∩ B = ", setAA & setBB)
            plt.title("A ∩ B")
        else:
            print("A ∩ B ∩ C = ", setAA & setBB & setCC)
            plt.title("A ∩ B ∩ C")

    def diff():
        if number_set == 2:
            print("A - B = ", setAA - setBB)
            plt.title("A - B")
        else:
            print("A - B - C = ", setAA - setBB - setCC)
            plt.title("A - B - C")

    def symdiff():
        if number_set == 2:
            print("A Δ B = ", setAA ^ setBB)
            plt.title("A Δ B")
        else:
            print("A Δ B Δ C = ", setAA ^ setBB ^ setCC)
            plt.title("A Δ B Δ C")

    # Main logic to execute Venn diagram and set operations
    if number_set == 2:
        myvenn2()
        if function_set == "int":
            inter()
        elif function_set == "sum":
            union()
        elif function_set == "diff":
            diff()
        else:
            symdiff()
    elif number_set == 3:
        myvenn3()
        if function_set == "int":
            inter()
        elif function_set == "sum":
            union()
        elif function_set == "diff":
            diff()
        else:
            symdiff()
    else:
        print("Invalid input error")
