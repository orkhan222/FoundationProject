# Listin içindən tək yerdə duran elementləri silərək əldə olunan listi ekrana çap edin


myList=[1,34,56,100,-12,87,987,1,3,5,56,67]


def element(list):
    nothing=" "
    myList.sort()
    for i in list:
        if i%2==1:
            nothing+=str(i)+" "
    print("Elemetlerin tek sirasi ile duzulmesi:",nothing)

element(myList)