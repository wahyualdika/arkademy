def triangle(t):
    if t < 3 :
        print("Input harus lebih besar dari 2")
        exit()
    
    row = t
    column = row + (row-1)
    r=0
    for r in range(row):
        # print(r)
        for c in range(column):
            if r == 0 or c == r or c == (column) - r -1:
                if r != row-1:
                    print(" * ",end='')
                else:
                    print("  *",end='')
                    break
            else:
                print("  ",end='')
        print('\n')

number = int(input("Masukka angka(minimal angka 3):"))
triangle(number)
