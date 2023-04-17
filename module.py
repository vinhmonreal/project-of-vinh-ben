class Parking():
    parkingSpaces =  []
    ticket = [1,2,3,4,5,6,7,8,9,10]
    currentTicket = {}
    '''
    Action = 'show' for Administration
    '''
    def driver(self):
        while True:
            action = input('Would you like to park,pay or leave?').lower()
            if action == 'park':
               self.takeTicket()
            if action == 'pay':
                self.payForParking()
            if action == 'leave':
                self.leaveGarage()
            if action == 'show':
                print(f'parking spaces taken{self.parkingSpaces}\n')
                print(f'payment status {self.currentTicket}\n')
                print(f'ticket number available{self.ticket}\n')
            else:
                print('Please enter a valid action.')
                
    def takeTicket(self):
        if len(self.ticket) > 0:
            new_ticket = self.ticket.pop(0) 
            self.parkingSpaces.append(new_ticket)
            self.currentTicket[new_ticket] = {'paid': False}
            print(f'Your ticket number is {new_ticket}')
            res = input('Would you like to pay now? yes or no?').lower()
            if res == 'yes':
                self.payForParking()
            else:
                self.driver()                
        else:
            print('Sorry! The parking is full.')
            
    def payForParking(self):
        payment = None
        while True:
            try:
                response = int(input('What ticket number would you like to pay?'))
                break
            except:
                print('Please enter a valid ticket number.')
        if response in self.parkingSpaces:
            payment = input('Please pay $5 for 15 minutes. yes or no?').lower()
            if payment == 'yes':
                self.currentTicket[response]['paid'] = True
                print('Thank you! You have 15 minutes to leave.')
            else:
                print('No payment recieved!')
        else:
            print(f'{response} is not a valid ticket number.')
            res = input('Continue to pay or cancel?').lower()
            if res == 'pay':
                self.payForParking()
            elif res == 'cancel':
                self.driver()
                
    def leaveGarage(self):
        while True:
            try:
                response = int(input('Leaving? Enter ticket number:'))
                break
            except:
                print('Please enter a valid ticket number.')
        if response in self.parkingSpaces:
            if self.currentTicket[response]['paid'] == True:
                print('Thank you! Have a good day!')
                self.parkingSpaces.remove(response)
                self.ticket.append(response)
                self.ticket = sorted(self.ticket)
                del self.currentTicket[response]
            else:
                print('Please pay')
                self.payForParking()
                if self.currentTicket[response]['paid'] == True:
                    self.parkingSpaces.remove(response)
                    self.ticket.append(response)
                    self.ticket = sorted(self.ticket)
                    del self.currentTicket[response]
                else:
                    print("Please pay")
        else:
            print('Invalid entry')
                  
car1 = Parking()
car1.driver()
     