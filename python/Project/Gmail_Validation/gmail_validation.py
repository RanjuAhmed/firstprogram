"""Email dalivadating """
gmail=input("Enter your Email: ")
k,j,d=0,0,0
if len(gmail)>=6:
    if gmail[0].isalpha():
        if ("@" in gmail) and (gmail.count("@")==1):
            if(gmail[-4]==".") ^  (gmail[-3]=="."):
                for i in gmail:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="."or i=="@":
                        continue
                    else:
                        d=1

                if k==1 or k==1:
                    print("place remove space and insure all characture are small latter")
                elif j==1:
                    print("remove upper case")
                
                else:
                    print("Right Email")
            else:
                print("give . before last 4 digit or 3 digit")
        else:
            print("write @ just one time")
    else:
        print("please input first latter is alphabete with small latter")
else:
    print("Pleace write atleast greater then 6 digit")