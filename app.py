import csv
from datetime import datetime

FILE_NAME = 'data.csv'

def createfile():
    try:    
        file = open(FILE_NAME, mode="x", newline = "")
        writer = csv.writer(file)
        writer.writerow([ 'Date','Exprence' , "Amount" , "Notes"])
    except FileExistsError :
        pass   
    
def add_exp():
    time = datetime.now().strftime('%d-%m-%Y')
    expence = str(input('enter food, travel , shoping :'))
    amount = int(input("enter amount :"))
    notes = str(input("enter note :"))
    newfile = open(FILE_NAME, mode="a", newline = "")
    writer = csv.writer(newfile)
    writer.writerow([time, expence, amount, notes])
    
    print('succes')
    
def Show_exp():
    Showexp = open(FILE_NAME, mode='r')
    writer = csv.reader(Showexp)
    
    for row in Showexp:
        print(row)
        
        
def  summary():
    summ={}
    total = 0
    summary_exp = open(FILE_NAME, mode="r")
    reader = csv.reader(summary_exp)
    next(reader)
    for row in reader:
        expence_cat = row[1]
        expence_amount = float(row[2])
       
        if expence_cat in summ:
            summ[expence_cat] += expence_amount
        
        else:
            summ[expence_cat] = expence_amount
            
        total = expence_amount + total
    print(summ)
    print(total)            
         
        
while True:
    createfile()
    print('\n=========Event Expence Managemant=============')
    print('1 for Add Expence')
    print('2 for Show Expence')
    print('3 for Summry Expence')
    print('4 for exit')
    print('Thaks for visit......')
    
    choice = int(input('Enter your Choice : '))
    if choice == 1:
        add_exp()
        
    elif choice == 2:
        Show_exp()
        
        
    elif choice == 3:
        summary()    
        
        
    elif choice == 4:
        print('Thaks for visit')
        break             



