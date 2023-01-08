try:
    x = float(input("Enter the amount you wish to withdraw: "))
except:
    print("Error!!! You must enter only numbers!!!")
    quit()  
if x%50 == 0:
    y = x/50
    print("You'll be given %d notes of 50ghc" %(y))
elif x%50 != 0:
    if x < 50:
        if x%20 == 0:
            y = x/20
            print("You'll be given %d notes of 20ghc" %(y))
        elif x%20 != 0:
            if x > 20:
                y = x//20
                print("You'll be given %d notes of 20ghc" %(y))
                k = x%20
                if k%10 == 0:
                    y = k/10
                    print("You'll be given %d notes of 10ghc" %(y))
                elif k%10 != 0:
                    if k > 10:
                        ff = k//10
                        print("You'll be given %d notes of 10ghc" %(ff))
                        rem = k%10
                        if rem%5 == 0:
                            y = rem/5
                            print("You'll be given %d notes of 5ghc" %(y))
                        elif rem%5 != 0:
                            if rem>5:
                                intpart = rem//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = rem%5
                                if rem2%2 == 0:
                                    y = rem/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif rem<5:
                                if rem%2 == 0:
                                    y = rem/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem%2 != 0:
                                    if rem > 2:
                                        new = rem//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem))
                    elif k < 10:
                        if k%5 == 0:
                            y = k/5
                            print("You'll receive %d notes of 5ghc" %(y))
                        elif k%5 != 0:
                            if k>5:
                                intpart = k//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = k%5
                                if rem2%2 == 0:
                                    y = rem2/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif k<5:
                                if k%2 == 0:
                                    y = k/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif k%2 != 0:
                                    if k > 2:
                                        new = k//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = k%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif k < 2:
                                        print("You'll receive %d notes of 1ghc" %(k))
            elif x < 20:
                if x%10 == 0:
                    y = x/10
                    print("You'll receive %d notes of 10ghc" %(y))
                elif x%10 != 0:
                    if x > 10:
                        ff = x//10
                        print("You'll be given %d notes of 10ghc" %(ff))
                        rem = x%10
                        if rem%5 == 0:
                            y = rem/5
                            print("You'll be given %d notes of 5ghc" %(y))
                        elif rem%5 != 0:
                            if rem>5:
                                intpart = rem//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = rem%5
                                if rem2%2 == 0:
                                    y = rem2/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif rem<5:
                                if rem%2 == 0:
                                    y = rem/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem%2 != 0:
                                    if rem > 2:
                                        new = rem//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem))
                    elif x < 10:
                        if x%5 == 0:
                            y = x/5
                            print("You'll receive %d notes of 5ghc" %(y))
                        elif x%5 != 0:
                            if x>5:
                                intpart = x//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = x%5
                                if rem2%2 == 0:
                                    y = rem2/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif x<5:
                                if x%2 == 0:
                                    y = x/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif x%2 != 0:
                                    if x > 2:
                                        new = x//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = x%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif x < 2:
                                        print("You'll receive %d notes of 1ghc" %(x))
    if x > 50:
        kk = x//50
        print("You'll receive %d notes of 50ghc" %(kk))
        rm = x%50
        if rm%20 == 0:
            y = rm/20
            print("You'll be given %d notes of 20ghc" %(y))
        elif rm%20 != 0:
            if rm > 20:
                y = rm//20
                print("You'll be given %d notes of 20ghc" %(y))
                k = rm%20
                if k%10 == 0:
                    y = k/10
                    print("You'll be given %d notes of 10ghc" %(y))
                elif k%10 != 0:
                    if k > 10:
                        ff = k//10
                        print("You'll be given %d notes of 10ghc" %(ff))
                        rem = k%10
                        if rem%5 == 0:
                            y = rem/5
                            print("You'll be given %d notes of 5ghc" %(y))
                        elif rem%5 != 0:
                            if rem>5:
                                intpart = rem//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = rem%5
                                if rem2%2 == 0:
                                    y = rem/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif rem<5:
                                if rem%2 == 0:
                                    y = rem/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem%2 != 0:
                                    if rem > 2:
                                        new = rem//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem))
                    elif k < 10:
                        if k%5 == 0:
                            y = k/5
                            print("You'll receive %d notes of 5ghc" %(y))
                        elif k%5 != 0:
                            if k>5:
                                intpart = k//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = k%5
                                if rem2%2 == 0:
                                    y = rem2/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif k<5:
                                if k%2 == 0:
                                    y = k/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif k%2 != 0:
                                    if k > 2:
                                        new = k//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = k%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif k < 2:
                                        print("You'll receive %d notes of 1ghc" %(k))
            elif rm < 20:
                if rm%10 == 0:
                    y = rm/10
                    print("You'll receive %d notes of 10ghc" %(y))
                elif rm%10 != 0:
                    if rm > 10:
                        ff = rm//10
                        print("You'll be given %d notes of 10ghc" %(ff))
                        rem = rm%10
                        if rem%5 == 0:
                            y = rem/5
                            print("You'll be given %d notes of 5ghc" %(y))
                        elif rem%5 != 0:
                            if rem>5:
                                intpart = rem//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = rem%5
                                if rem2%2 == 0:
                                    y = rem2/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif rem<5:
                                if rem%2 == 0:
                                    y = rem/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem%2 != 0:
                                    if rem > 2:
                                        new = rem//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem))
                    elif rm < 10:
                        if rm%5 == 0:
                            y = rm/5
                            print("You'll receive %d notes of 5ghc" %(y))
                        elif rm%5 != 0:
                            if rm>5:
                                intpart = rm//5
                                print("You'll be given %d notes of 5ghc" %(intpart))
                                rem2 = rm%5
                                if rem2%2 == 0:
                                    y = rem2/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rem2%2 != 0:
                                    if rem2 > 2:
                                        new = rem2//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rem2%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rem2 < 2:
                                        print("You'll receive %d notes of 1ghc" %(rem2))
                            elif rm<5:
                                if rm%2 == 0:
                                    y = rm/2
                                    print("You'll be given %d notes of 2ghc" %(y))
                                elif rm%2 != 0:
                                    if rm > 2:
                                        new = rm//2
                                        print("You'll be given %d notes of 2ghc" %(new))
                                        rem3 = rm%2
                                        print("You'll receive %d notes of 1ghc" %(rem3))
                                    elif rm < 2:
                                        print("You'll receive %d notes of 1ghc" %(rm))
