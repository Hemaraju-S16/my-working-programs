def payment_checher(amount):

    print("""hi welcome to XYZ payment gateway
    
            000000000
            
            begin transcation
            """)
    total_amount = 97500
    paid_amount  = amount
    #cheching for outstanding amount

    balance_amount = total_amount  -paid_amount

    if balance_amount == 0:
        print("👍")

    else:
        print(f'pay your {balance_amount} balance amount')

payment_checher(97500)

payment_checher(50000)


def fees_checker():
    if payment_checher:
        print("done")



def Some_function(name = 'hem', age = 19):
    print(name, age)

Some_function('raj', 22)



dict = {
    'student_name'  : ['hemaraju', 'harsha','keeri raj', 'josh'],
    'student_marks' : {78,45, 56,89}

        }



for x in dict.keys:
    print(x)
    

