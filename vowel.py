def vowel(string):
    
    vowel = ['a','i','u','e','o']
    
    string = string.lower()
    print(string)
    arr = list(string)
    counter = len(arr)
    mark = 0 
    
    for i in range(counter):
        if arr[i] in vowel:
            mark += 1

    print(mark)
    
string = input("Masukkan string")
vowel(string)