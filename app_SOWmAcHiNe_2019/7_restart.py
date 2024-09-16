
import os

#### ATTENTION: this deletes the test SOW file (no bid deal just fyi) ####

# delete a file in directory named book_01.xlsx
os.remove("/Users/sudz4/Desktop/BOOK-II/servicenow-interview-proj/app_SOWmAcHiNe_2019/book01.xlsx")

if os.path.exists("/Users/sudz4/Desktop/BOOK-II/servicenow-interview-proj/app_SOWmAcHiNe_2019/book01.xlsx"):
    print("The file was not deleted.")  
else:
    print("The file was deleted.")