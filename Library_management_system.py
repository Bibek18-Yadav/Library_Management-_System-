import pandas as pd
import random
from datetime import date,timedelta


df=pd.read_excel("staff_details.xlsx")    #reading the excell file of staff
dfs=pd.read_excel("Student_details.xlsx")  #reading the excell file of student

staff_name=input("Enter Staff name:").lower()
staff_id=int(input("Enter Staff ID:"))


if ((df["Name "].str.lower()==staff_name) & (df["ID"]==staff_id)).any():     #comparing the entered data of staff to the stored one 

    print(" WELCOME ", f"{staff_name}",end="\n")
     
    ask=input("Is student there to borrow book or return it?(borrow/returnit)").lower()
     
    if ask=="borrow":
        book_list={
            "computer science":98,
            "physics":97,
            "math":96,
            "chemistry":95,
            "english":94
        }
        print("<<<<    This is the list of books available here   >>>>>",end="\n")
        print(book_list,end="\n\n")

        print("<<<<<   Choose the book you want to borrow   >>>>",end="\n")
        class Student:
           def __init__(self,name,id,mobile,book_id,date):
               self.name=name
               self.id=id
               self.mobile=mobile
               self.book=book_id
               self.date=date

           def __str__(self):      #whenever class will be called this will run and provide output
                return (f"Name:{self.name}\n"
                        f"ID:{self.id}\n"
                        f"Mobile:{self.mobile}\n"
                        f"Book:{self.book}\n"
                        f"Date:{self.date}")

        # Taking inputs from students about their details
        student_name=input("enter the student name:").lower()
        student_id=random.randint(200,400)
        student_mobile=int(input("Enter the mobile no:"))
        student_book=input("enter the borrowed book id:")
        student_date=date.today()
            
        student_data=Student(student_name,student_id,student_mobile,student_book,student_date)
        print(student_data,end="\n\n")
        print(">>>   Remember your student id is", f"{student_id}")     # Telling student about its id to return book latern on 

         # storing student datas in dictionary
        student_data_dict={
            "Name":student_name,
            "ID":student_id,
            "Mobile":student_mobile,
            "Book":student_book,
            "Date":student_date
        }
        new_student_df=pd.DataFrame([student_data_dict])    # Changing dictionary into dataframe
        dfs =pd.concat([dfs, new_student_df],ignore_index=True)    # Concatinating students excell file and enetred data
        dfs.to_excel("Student_details.xlsx",index=False)
        print(">>>>>    Student details saved to Excel!    <<<<<<")

    elif ask=="returnit":
       return_student_id=int(input("<<<<< Please tell me your ID: >>>>>\n"))

    # Check if student exists in the DataFrame
       if return_student_id in dfs["ID"].values:
        # Locate the student row
           student_index=dfs[dfs["ID"]==return_student_id].index[0]

           borrow_date=pd.to_datetime(dfs.loc[student_index,"Date"]).date()
           today_date=date.today()

        # Calculate days difference
           days_diff=(today_date - borrow_date).days

        # Determine fine
           fine_amount=100 if days_diff > 10 else 0


           # --- FIX: Convert columns to compatible types ---
           if "ReturnDate" not in dfs.columns:
                dfs["ReturnDate"]=pd.NaT
           else:
                dfs["ReturnDate"]=pd.to_datetime(dfs["ReturnDate"], errors="coerce")

           if "Fine" not in dfs.columns:
                dfs["Fine"]=pd.Series([0]*len(dfs), dtype='Int64')
           else:
                dfs["Fine"]=dfs["Fine"].astype('Int64')

        # Update return date and fine in DataFrame
           dfs.loc[student_index,"ReturnDate"]=today_date
           dfs.loc[student_index,"Fine"]=fine_amount

        # Save back to Excel
           dfs.to_excel("Student_details.xlsx",index=False)

           print(f"Book returned successfully! Days borrowed:{days_diff}")
           if fine_amount > 0:
            print(f"Late return fine:Rs.{fine_amount}")
           else:
            print("No fine, returned on time.")

       else:
        print("Student ID not found in records!")

            
    else:
        print(">>>>>>      Thank you for logging in     <<<<<<")
        more_details=input("Do you want to access staffs details from excell file?(Yes/no)").lower()
        if more_details=="yes":
            print(df,end="\n\n")    # Printing all the data of staffs stored in excell file

        else:
            print("-----------------------------------------------")

        more_details_student=input("Do you want to access student data from excell file?(yes/no)").lower()
        if more_details_student=="yes":
            print(dfs,end="\n")      # Printing all the data of students stored in excell file


else:
    print("<<<<<  Wrong staff name or ID    >>>>>")


