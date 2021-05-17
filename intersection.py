
from matplotlib_venn import  venn2 , venn2_circles ,venn3 ,venn3_circles , venn3_unweighted 
import matplotlib_venn as venn   
from matplotlib import pyplot as plt
print("This algorithm  helps you to operate some of the basic set functions on venn diagrams")  
function_set=input("type int for intersection , sum for union of two sets , diff for difference of two sets  and sym diff for difference of two sets ")
number_set=int(input("enter 2 for operating on a pair of sets and 3 for operating on three sets"))
setAA=set()
setBB=set()     
setCC=set() 
   
def myvenn2():
    
    seta_ele=int(input("enter the number of elements you want in your SET A"))
    setb_ele=int(input("enter the number of elements you want in SET B "))   
    
    for i in range (1,seta_ele+1):
        tempseta=int(input("enter element in set A")) 
        setAA.add(tempseta)
    for i in range(1,setb_ele+1):
        tempsetb=int(input("enter element in set B")) 
        setBB.add(tempsetb) 
    venn.venn2_unweighted([setAA,setBB], set_labels = ('Set A', 'Set B')) 
    #str_main=
    plt.title()
    #print(str_main)
    plt.show()  
    
#myvenn2() 

def myvenn3():
    
    seta_ele=int(input("enter the number of elements you want in your SET A"))
    setb_ele=int(input("enter the number of elements you want in SET B "))
    setc_ele=int(input("enter the number of elements you want in SET C "))
    
    for i in range (1,seta_ele+1):
        tempseta=int(input("enter element in set A"))
        setAA.add(tempseta)
    for i in range(1,setb_ele+1):
        tempsetb=int(input("enter element in set B"))
        setBB.add(tempsetb)
    for i in range(1,setc_ele+1):
        tempsetc=int(input("enter element in set C"))
        setCC.add(tempsetc)    
     
    venn3_unweighted ([setAA,setBB,setCC], set_labels = ('Set A', 'Set B', "Set C"))
    
    plt.show()  
#myvenn3()
#operations start from here
def union():
    if number_set==2:
        str_ok=print("A ∪ B = ", setAA | setBB )
    else:
        str_ok=print("A ∪ B ∪ C = ", setAA | setBB | setCC)
    plt.title("A ∪ B")       
#union()

def inter():
    if number_set==2:
        str_ok=print("A ∩ B = ", setAA & setBB )
    else:
        str_ok=print("A ∩ B ∩ C = ", setAA & setBB & setCC) 
    
#inter()

def diff():
    if number_set==2:
        str_ok=print("A - B = ", setAA - setBB )
    else:
        str_ok=print("A - B - C = ", setAA - setBB - setCC) 
#diff()

def symdiff():
    if number_set==2:
        str_ok=print("A Δ B = ", setAA ^ setBB )
    else:
        str_ok=print("A Δ B Δ C = ", setAA ^ setBB ^ setCC)
#symdiff()



if number_set==2:
    myvenn2()
    if function_set==("int"):
        inter()
        
    elif function_set==("sum"):
        union()
    elif function_set==("diff"):
        diff()
    else:
        symdiff()
elif number_set==3:
    myvenn3()
    if function_set==("int"):
        inter()
    elif function_set==("sum"):
        union()
    elif function_set==("diff"):
        diff()
    else:
        symdiff()
else:
    print ("invalid input error")


