Kazu = int(input("Enter..."))

Ans = 0
Flag = False

if Kazu == 1:
    Ans = 1
    
else:
    while Kazu > 1:
        
        if Flag == False:
            Ans = Kazu * (Kazu-1)
            Flag = True
        else:
            Ans = Ans * (Kazu-1)
        Kazu = Kazu -1

try:
    File = open("Ans.txt", "w")
    File.write(str(Ans))
    #File.write(f"{Ans:,}")
    File.close()
    print("OK!")
except exception as e:
    print("ERROR")