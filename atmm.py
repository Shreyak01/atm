print("Welcome to Techie Programmer Bank Atm")                                                                                      
restart="Y"                                                                                                                         
chances=3                                                                                                                           
balance=10000                                                                                                                       
while chances>=0:                                                                                                                   
 pin=int(input('Please enter your 4 Digit Pin:'))                                                                                       
 if pin==1234:                                                                                                                       
  print('You Entered pin correctly\n')                                                                                               
  while restart not in('n','NO','no','N'):                                                                                           
   print('Please Press 1 for Balance\n')                                                                                             
   print('Please Press 2 for Withdrawal\n')                                                                                          
   print('Please Press 3 to Pay\n')                                                                                                  
   print('Please Press 4 to Return Card\n')                                                                                          
   option=int(input('What would you like to choose?'))                                                                               
   if option==1:                                                                                                                     
    print('Your balance is Rs',balance,'\n')                                                                                         
    restart=input('Would you like to go back?')                                                                                      
    if restart in('n','NO','no','N'):                                                                                                
     print('Thank You')                                                                                                              
     break                                                                                                                           
   elif option==2:                                                                                                                   
    option2='y'                                                                                                                      
    withdrawl=float(input('How much would you like to withdraw?\nRs10\nRs50\nRs100\nRs200\nRs500\nRs2000\n for other enter 1:'))      
    if withdrawl in [10,50,100,200,500,2000]:                                                                                       
     balance=balance-withdrawl                                                                                                      
    print('\n Your balance is now Rs',balance)                                                                                      
    restart=input(('Would you like to go back?'))                                                                                   
    if restart in('n','NO','no','N'):                                                                                                
      print('Thank You')                                                                                                         
                                                                                                                                    
   elif withdrawl!= [10,50,100,200,500,2000]:                                                                                          
     print('Invalid Amount,Please Re-try\n')                                                                                 
     restart='y'
   elif withdrawl==1:
    restart=input(('Would you like to go back?'))                                                                                   
    if restart in('n','NO','no','N'):
      print('Choose their option')
      break
                                                                                                                                                                        
    elif option==3:                                                                                                                
     Pay_in=float(input('How much would you like to Pay in?'))                                                                   
     balance=balance+Pay_in
     print('\n Your balance is now Rs',balance)
     restart=input(('Would you like to go back?'))                                                                                   
    if restart in('n','NO','no','N'):                                                                                                
     print('Thank You')
     break                       
   elif option==4:
   	print('PLease wait whilst your card is Returned...\n')
   	print('Thank you for your service')
   else:
    print('Enter a correct no')
    restart='y'

 elif pin!='1234':
  print('Incorrect Password')
 chances=chances-1
 if chances==0:
      print('\n No more tries')
      break


    