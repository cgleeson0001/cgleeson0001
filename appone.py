import datetime

atm_user = {
    'Chantel':'passwordChantel',
    'Alex':'passwordAlex',
    'Ava':'passwordAva'
}

def login():
    # login function

    name = input("User ID: \n")
    password = input("Password: \n")
    if(name in atm_user and password == atm_user[name]):
        print('\n')
        now = datetime.datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("Hello " + name)
        print('\n')
        return True
    else:
        print('User ID and Password invalid.')
        return False

def atmOperations():

        print('Main Menu')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. Exit')
        print('\n')
        
        selectedOption = int(input('Please select an option:'))

        print(selectedOption == 1)
        
        if(selectedOption == 1):
            print ('You selected %s.' % selectedOption)
            print('\n')
    
            selectedOption = int(input('How much would you like to withdraw?'))

            print('\n')
            print('Take your cash.')
            print('Thank you.')
            print('\n')
            atmOperations()
            
        elif(selectedOption == 2):
            print ('you selected %s' % selectedOption)
              
            selectedOption = int(input('How much would you like to deposit?'))
            
            print('\n')
            print('Current Balance: $1,000,000')
            print('Thank you.')
            print('\n')
            atmOperations()
            
        elif(selectedOption == 3):
            print ('you selected %s' % selectedOption)

            selectedOption = (input('What issue would you like to report?'))
            
            print('\n')
            print('Thank you for contacting us.')
            print('\n')
            atmOperations()

        elif(selectedOption == 4):
            print("Goodbye!")
            
        else:
            print('Invalid Option selected, please try again \n')
            atmOperations()
    
print("Welcome! \n")
print("1. Login")
print("2. First Time User? Register.")
print("3. Exit")
print('\n')

actionSelect = int(input("Please select an option \n"))

if(actionSelect == 1):
    loginSuccessful = False

    while loginSuccessful == False:
        loginSuccessful = login()

    atmOperations()

elif(actionSelect == 2):
    
    selectedOption = (input('Enter your first name:'))
    selectedOption = (input('Enter your password:'))
            
    print('\n')
    print('Generating account number...')
    print('Your account has been created. Your Account Number is 5901301.')
    print('\n')
    atmOperations()
            
    
elif(actionSelect == 3):
    print("Goodbye!")
    
else:
    print('Login failed. User ID and Password invalid.')
            

