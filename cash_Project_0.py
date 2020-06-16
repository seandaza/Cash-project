
n = float(input("Your total change in cents is: "))

if n <= 0:
    print("The change should be positive")
    

else: 

        if n < 25 and n >= 10:
            print("I give you", int(n/10),"coin(s) of 10c")
            resto = n - int(n/10)*10
            if resto < 10 and resto >= 5:
                    print("I give you",int(resto/5), "coin(s) of 5c")
                    resto = n - int(n/5)*5
            if resto < 5:
                    print("I give you", int(resto), "coin(s) of 1c")
        
        
        if n < 10 and n >= 5:
            print("I give you",int(n/5),"coin(s) of 5c")
            resto = n - int(n/5)*5
            print("I give you", int(resto), "coin(s) of 1c")

        if n < 5:
            print("I give you", int(n), "coin(s) of 1c")

        if n >= 25: 
            print("I give you", int(n/25),"coin(s) of 25c")
            resto = n - int(n/25)*25
            
            if resto >= 5 and resto < 10:
                print("I give you", int(resto/5),"coin(s) of 5c")
                resto1 = resto - (int(resto/5))*5
                if resto1 < 5:
                    print("I give you", int(resto1),"coin(s) of 1c" )
            if resto < 5:
                print("I give you", int(resto),"coin(s) of 1c")       

            if resto < 25 and resto >= 10:
                print("I give you", int(resto/10),"coin(s) of 10c")
                resto1 = resto - (int(resto/10))*10
                if resto1 < 5:
                       print("I give you", int(resto1),"coin(s) of 1c")
                if resto1 < 10 and resto1 >= 5:
                       print("I give you", int(resto1/5),"coin(s) of 5c")
                       resto2 = resto1 - (int(resto1/5))*5
                       print("I give you", int(resto2),"coin(s) of 1c" )