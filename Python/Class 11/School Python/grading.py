mark = int(input("Tell Your Marks?:"))


if mark>0:
    if mark>33:
        if mark>41:
            if mark>51:
                if mark>61:
                    if mark>71:
                        if mark>81:
                            if mark>91:
                                if mark>101:
                                    print("Marks Not Valid")
                                else:
                                    print("Congrats You Got 'A1' Grade")
                            else:
                                print("Congrats You Got 'A2' Grade")
                        else:
                            print("Congrats You Got 'B1' Grade")
                    else:
                        print("Congrats You Got 'B2' Grade")
                else:
                    print("Congrats You Got 'C1' Grade")
            else:
                print("Congrats You Got 'C2' Grade")
        else:
            print("Congrats, You Got 'D' Grade")
    else:
        print("Sorry you Got 'E' and Failed")
else:
    print("Marks not Valid")