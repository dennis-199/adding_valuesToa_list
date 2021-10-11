# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
classes = ["MATH 150", "PSYCH 111", "PSYCH 313", "PSYCH 412", "MATH 300", "MATH 404", "MATH 206", "ENG 100", "ENG 103", "ENG 201", "PSYCH 508", "ENG 220", "ENG 125", "ENG 124"]
upper=[]
lower=[]
for i in classes:
    new=i.split()
    if (new[0]=='MATH') and (int(new[1])>=300):
        upper.append(i)
    elif (new[0]=='ENG') and (int(new[1])>=200):
        upper.append(i)
    elif (new[0]=='PSYCH') and (int(new[1])>=400):
        upper.append(i)
    else:
        lower.append(i)
print("upper=",upper)
print("lower=",lower)
