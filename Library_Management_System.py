import pandas as pd
import matplotlib.pyplot as plt


print("*********WELCOME-TO-LIBRARY-MANAGEMENT*********")
df = pd.read_csv('Library_Management_System.csv')
print("*********LIBRARY--DATA*************")
print(df)
print("--------Data Manipulation---------")
print("Enter 1 to add new Book Record")
print("Enter 2 to remove Book Record")
print("Enter 3 to search Book Detail BY Book Name")
print("Enter 4 to update Book Record")

task = int(input("Enter Your Task: "))


if task == 1:
    print("NOTE: BOOK ID should be a unique number........")
    bookid = input("Enter BookID: ")
    patronName = input("Enter Patron Name")
    bookname = input("Enter Book Name: ")
    authorname = input("Enter Author Name: ")
    print("NOTE: Date should be in dd/mm/yyyy format.....")
    issuedate = input("Enter Issue Date: ")
    returningdate = input("Enter Returning Date: ")
    newbook = pd.DataFrame({
        'BookID': [bookid],
        'Patron' : [patronName],
        'BookName': [bookname],
        'AuthorName': [authorname],
        'IssueDate': [issuedate],
        'ReturningDate': [returningdate]
    })
    df = pd.concat([df, newbook], ignore_index=True)
    df.to_csv('codecsv.csv', index=False)
    print(df)


elif task == 2:
    bookid = (input("Enter BookID to remove: "))
    df = df[df['BookID'] != bookid]
    df.to_csv('codecsv.csv', index=False)
    print(df)


elif task == 3:
    Bookname = input("Enter Book Name: ")
    bookname = df[df['BookName'] == Bookname]
    if not bookname.empty:
        print(bookname)
    else:
        print("No Book found with that name.")

elif task == 4:
    print("***********Update-MENU**********")
    print("Enter 1 for Patron Name")
    print("Enter 2 for Enter the New book & Author Name")
    print("Enter 3 for Change the Returning Date ")

    update = int(input("Enter the Number: "))
    bookid = (input("Enter BOOK ID: "))

    if bookid in df['BookID'].values:
        if update == 1:
            patronname = input("Enter the new Patron name: ")
            df.loc[df['BookID'] == bookid, 'PatronName'] = patronname
        elif update == 2:
            BookName = input("Enter the new Book Name: ")
            AuthorName = input("Enter the new Author Name: ")
            df.loc[df['BookID'] == bookid, 'BookName'] = BookName
            df.loc[df['BookID'] == bookid, 'AuthorName'] = AuthorName
        elif update == 3:
            ReturningDate = input("Enter the new position: ")
            df.loc[df['BookID'] == bookid, 'ReturningDate'] = ReturningDate
        df.to_csv('codecsv.csv', index=False)
        print(df)
    else:
        print("BOOk ID not found.")
