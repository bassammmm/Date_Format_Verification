def dd_mm_yy(date_list):
    """this function will check the date according to dd-mm-yy format"""
    result_dict = {}
    for date in range(len(date_list)):
        result_dict[date_list[date]] = []
        dash = 0
        if date_list[date].count('-')!=2:
            result_dict[date_list[date]].append("There is an incorrect number of dashes in this date.")
        else:
            dash = 2

        ch_err=0
        for char in date_list[date]:
            if char.isalpha()==True:
                ch_err+=1
        if ch_err>0:
            result_dict[date_list[date]].append("There are alphabet(s) in the date.")

        date_split = date_list[date].split('-')
        if len(date_split)==3:
            if len(date_split[0])>2 or len(date_split[0])<2:
                result_dict[date_list[date]].append("The number of characters in the dd(date) are not correct.")
            if len(date_split[1]) > 2 or len(date_split[1]) < 2:
                result_dict[date_list[date]].append("The number of characters in the mm(month) are not correct.")
            if len(date_split[2]) > 2 or len(date_split[2]) < 2:
                result_dict[date_list[date]].append("The number of characters in the yy(month) are not correct.")
        if ch_err==0 and len(date_split)==3:
            if int(date_split[0])>31 or int(date_split[0])<1:
                result_dict[date_list[date]].append("The day in the date is out of range.")
            if int(date_split[1])>12 or int(date_split[1])<1:
                result_dict[date_list[date]].append("The month in the date is out of range.")
            if int(date_split[0])==31 and (int(date_split[1])==4 or int(date_split[1])==6 or int(date_split[1])==9 or int(date_split[1])==11):
                result_dict[date_list[date]].append("April, June, September and November only have 30 days.")
            if int(date_split[0])>28 and int(date_split[1])==2:
                result_dict[date_list[date]].append("February only has 28 days except for Leap Year only!.")

        if result_dict[date_list[date]]==[]:
            result_dict[date_list[date]].append("This is perfect! No error.")

    for key,val in result_dict.items():
        print("\n",key,":")
        for each in range(len(val)):
            print("{}) {}".format(each+1,val[each]))


def mm_dd_yy(date_list):
    """this function will check the date according to mm-dd-yy format"""
    result_dict = {}
    for date in range(len(date_list)):
        result_dict[date_list[date]] = []
        dash = 0
        if date_list[date].count('-') != 2:
            result_dict[date_list[date]].append("There is an incorrect number of dashes in this date.")
        else:
            dash = 2

        ch_err = 0
        for char in date_list[date]:
            if char.isalpha() == True:
                ch_err += 1
        if ch_err > 0:
            result_dict[date_list[date]].append("There are alphabet(s) in the date.")

        date_split = date_list[date].split('-')
        if len(date_split) == 3:
            if len(date_split[0]) > 2 or len(date_split[0]) < 2:
                result_dict[date_list[date]].append("The number of characters in the dd(date) are not correct.")
            if len(date_split[1]) > 2 or len(date_split[1]) < 2:
                result_dict[date_list[date]].append("The number of characters in the mm(month) are not correct.")
            if len(date_split[2]) > 2 or len(date_split[2]) < 2:
                result_dict[date_list[date]].append("The number of characters in the yy(year) are not correct.")
        if ch_err == 0 and len(date_split) == 3:
            if int(date_split[1])>31 or int(date_split[1])<1:
                result_dict[date_list[date]].append("The day in the date is out of range.")
            if int(date_split[0])>12 or int(date_split[0])<1:
                result_dict[date_list[date]].append("The month in the date is out of range.")
            if int(date_split[1])==31 and (int(date_split[0])==4 or int(date_split[0])==6 or int(date_split[0])==9 or int(date_split[0])==11):
                result_dict[date_list[date]].append("April, June, September and November only have 30 days.")
            if int(date_split[1])>28 and int(date_split[0])==2:
                result_dict[date_list[date]].append("February only has 28 days except for Leap Year only!.")

        if result_dict[date_list[date]] == []:
            result_dict[date_list[date]].append("This is perfect! No error.")

    for key, val in result_dict.items():
        print("\n", key,":")
        for each in range(len(val)):
            print("{}) {}".format(each + 1, val[each]))





date_format = int(input("Which date format would you prefer? :-\n 1)dd-mm-yy \t 2)mm-dd-yy\nPlease choose corresponding(1 or 2):"))
while date_format not in [1,2]:
    print("Please enter only 1 or 2 according to your choice!\n")
    date_format = int(input("Which date format would you prefer? :-\n 1)dd-mm-yy\t2)mm-dd-yy\nPlease choose corresponding(1 or 2):"))


date_list = []
if date_format==1:
    print("Please enter the 10 dates in dd-mm-yy format to check if you entered them correctly:-")
else:
    print("Please enter the 10 dates in mm-dd-yy format to check if you entered them correctly:-")



for x in range(10):
    date = input("Enter Date No.{} :".format(x+1))
    date_list.append(date)

if date_format==1:
    dd_mm_yy(date_list)
elif date_format==2:
    mm_dd_yy(date_list)
else:
    pass
