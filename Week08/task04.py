# Listin elementlərini azalan sıra ilə sıralayaraq ekrana çap edin



myList=[1,34,56,100,-12,87,987,1,3,5,56,67]


def element(list):
    nothing=" "
    list.sort()
    list.reverse()
    for i in list:
            nothing+=str(i)+" "
    print("Elemetlerin azalan sira ile duzulmesi:",nothing)

element(myList)

