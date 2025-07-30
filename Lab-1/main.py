def read():
  with open ("data.txt","r") as f:
      data=f.read()
      print(data)
  print("Enter the details of student in the format (Roll no.,Name,Age,Department)=")
  with open ("data.txt","a") as f:
        a=[input() for i in range (0,4)]
        # f.write(",".join(a))
        if a[0] in data:
            print("Roll no. already exists")
            c=int(input("Do you want to enter student (0(No)/1(Yes))="))
            if(c==1):
                read()
            else:
                exit()
        else:
            f.write("\n")
            f.write(",".join(a))
            f.flush()
            d=int(input("Do you want to enter student (0(No)/1(Yes))="))
            if(d==1):
                read()
            else:
                exit()
        print(a)
read()