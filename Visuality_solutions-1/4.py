while True:
    a = int(input("Enter start :"))
    b = int(input("Enter end :"))
    for i in range(a,b+1,1):
        divided = 0
        for j in range(1,i,1):
            if i % j == 0:
                divided +=1
        
        if divided == 1:
            print(i)

    
    
