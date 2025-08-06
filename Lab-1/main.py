def add_student():
    print("Enter the details of student in the format (Roll no.,Name,Age,Department)=")
    with open("data.txt","r") as f:
        data=f.read()
    with open ("data.txt","a") as f:
        a=[input() for i in range (0,4)]
        if a[0] in data:
            print("Roll no. already exists")
            c=int(input("Do you want to enter student (0(No)/1(Yes))="))
            if(c==1):
                add_student()
            else:
                return 0
        else:
            f.write("\n")
            f.write(",".join(a))
            f.flush()
            d=int(input("Do you want to enter student (0(No)/1(Yes))="))
            if(d==1):
                add_student()
            else:
                return 0

def read():
    print("Roll no.    Name      Age     Department")
    with open("data.txt", "r") as f:
        while True:
            q = f.readline()
            if q == "":
                break
            r = q.strip().split(",")
            for i in r:
                print(i, end="   ")
            print()


def search():
    b2=input("Enter the roll no. that you want to search=")
    with open("data.txt","r") as f:
        while(1):
            a2=f.readline()
            if (b2 in a2):
               r2=a2.replace(",","  ")
               print(f"Yes the record exits = {r2}")
               return 0


def update():
    b=input("Enter the roll no. whose data you want to update=")
    b2=input("Enter the details of student again in format(Roll no,Name,Age,Department) seperating it with (,)")
    with open("data.txt","r") as f:
        lines=f.readlines()

    for i in range(len(lines)):
        if b in lines[i]:
            lines[i]=lines[i].replace(lines[i],b2)

    with open("data.txt","w") as f:
       f.writelines(lines)

def delete():
    b=input("Enter the roll no. whose details you want to delete=")
    with open("data.txt","r") as f:
        lines=f.readlines()

    for i in range(len(lines)):
       if b in lines[i]:
          del lines[i]

    with open("data.txt","w") as f:
       f.writelines(lines)

while(1):
  print("Enter for number given choice: \n 1.Add a student record  \n 2.View all records \n 3.Search a record by roll no. \n 4.Update a record \n 5.Delete a record \n 6.Exit")
  b=int(input())
  match b:
    case 1:
      add_student()
    case 2:
      read()
    case 3:
      search()
    case 4:
      update()
    case 5:
      delete()
    case 6:
      exit()