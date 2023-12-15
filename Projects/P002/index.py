import os

directory=input("Enter your directory: ")

def showallfiles():#https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
    count=0
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                print(os.path.join(root, file))
                count+=1
    print("-----",count,"files were found-----")
def readfile():#https://www.google.com/search?q=how+to+read+line+all+lines+in+a+file+python&rlz=1C1CHBD_en-GBIR1022IR1022&oq=how+to+read+line+all+lines+in+&gs_lcrp=EgZjaHJvbWUqCggFECEYFhgdGB4yBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigATIKCAUQIRgWGB0YHjIKCAYQIRgWGB0YHjIKCAcQIRgWGB0YHjIKCAgQIRgWGB0YHjIKCAkQIRgWGB0YHtIBCTIxMjQxajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
    filename=input("enter filename: ")
    with open(directory+"/"+filename+".txt") as file_in:
        lines = []
        for line in file_in:
            print(line)
def rebrand():#https://www.google.com/search?q=how+to+rename+file+in+python&rlz=1C1CHBD_en-GBIR1022IR1022&oq=how+to+rename+file+&gs_lcrp=EgZjaHJvbWUqBwgCEAAYgAQyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDU3NDdqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8
    file1=input("which file do you wish to rename: ")+".txt"
    file2=input("what do you wish to name it: ")+".txt"
    os.rename(directory+"/"+file1,directory+"/"+file2) 
def changedir():
    directory=input("Enter your directory: ")
def getentery():
    print("1. see all files within this directory.")
    print("2. read a file.")
    print("3. change name.")
    print("4. change directory.")
    print("-1. Exit")
    return(int(input("Enter a command number:")))


def main(num:int):
    while(num!=-1):
        if(num==1):
            showallfiles()
        elif(num==2):
            readfile()
        elif(num==3):
            rebrand()
        elif(num==4):
            changedir()
        else:
            print("command not found!")
            print("please try again!")
        
        num=getentery()

    print("it was a pleasure helping you.")

main(getentery())