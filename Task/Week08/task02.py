# Listin eleməntlərini ekrana çap edin


myList=[1,34,56,100,-12,87,987,1,3,5,56,67]

def element(list):
    nothing=" "
    for i in list:
        nothing+=str(i)+" "
    print("Elemetlerin sira ile duzulmesi:",nothing)

element(myList)

