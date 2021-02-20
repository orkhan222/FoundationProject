# Listin içində cüt yerdə duran elementləri ekrana çap edin

myList=[1,34,56,100,-12,87,987,1,3,5,56,67]


def element(list):
    nothing=" "
    for i in list:
        if i%2==0:
            nothing+=str(i)+" "
    print("Elemetlerin cut sirasi ile duzulmesi:",nothing)

element(myList)
