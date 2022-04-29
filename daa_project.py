from tkinter import *

r = Tk()
r.title('DAA PROJECT')
r.config(bg='grey')
r.geometry("444x434")
Label(r, pady=4, bd=2, font=('calibre', 12), background="light pink", text='ENTER FIRST STRING').grid(row=0, column=3)
Label(r, pady=4, bd=2, font=('calibre', 12), background="light pink", text='ENTER SECOND STRING').grid(row=1, column=3)
Label(r, pady=4, bd=2, font=("calibre", 12), background="light blue", text='LCS = ').grid(row=2, column=3)
Label(r, bd=2, font=("calibre", 10), background="light blue", text='LCS Length = ').grid(row=4, column=3)
s1 = StringVar()
s2 = StringVar()
e1 = Entry(r, bd=2, textvariable=s1)
e2 = Entry(r, bd=2, textvariable=s2)
e1.grid(pady=4, column=7, row=0)
e2.grid(pady=4, column=7, row=1)

ans=""
def lcs(X, Y):
    m=len(X)
    n=len(Y)
    L = [[0 for i in range(n+1)] for j in range(m+1)]

    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

        # Create a string variable to store the lcs string
    lcs = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:

        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i -= 1
            j -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i -= 1

        else:
            j -= 1

    # We traversed the table in reverse order
    # LCS is the reverse of what we got
    ans = lcs[::-1]
    return ans


e4 = Label(r, bd=2, width=20, font=('calibre', 12), text="")
e4.config(bg='light green')
e4.grid( column=7, row=2)
e5 = Label(r, bd=2, width=20, font=('calibre', 12), text="")
e5.config(bg='light green')
e5.grid( column=7, row=4)
Label(r,font=('calibre', 12), bd=2, background="pink",width=30, text='LONGEST COMMON SUBSEQUENCE').grid(row=6)


def f():
    ans=lcs(e1.get(),e2.get())
    e4.config(text=ans, font=('Ariel', 12))
    e5.config(text=len(ans), font=('Ariel', 12))


b = Button(r, bg='light blue', text='CALCULATE', width=25, font=('calibre', 10, 'bold'), command=f)
b.grid(column=7, row=6)
print("hello")
r.mainloop()
