def number(string):
    string = string.replace(" ", "")
    string = string.replace("-","")
    
    arr = list(string)
    counter = 0
    mark = 0
    
    while counter < len(arr):
        mark+=1
        if mark == 3:
            arr.insert(counter+1,"-")
            mark = 0 
            counter+=1
        counter+=1
    
    if arr[len(arr)-1] != '-' and arr[len(arr)-2] == '-':
        temp = arr[len(arr)-2]
        arr[len(arr)-2] = arr[len(arr)-3]
        arr[len(arr)-3] = temp
    
    if arr[len(arr)-1] == '-':
        arr[len(arr)-1] = ''
     
    for i in arr: 
        print(i, end="") 


inputan = input("Masukkan nomor")
number(inputan)