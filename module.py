class Parking():
    parkingSpaces =  []
    ticketNumber = [1,2,3,4,5,6,7,8,9,10]
    paymentStatus_dict = {}
    
    '''
        currentTicket_dict: {
        'ticketNumber': {'paid': True }
        '1' : {'paid': True }
        }
    '''
    
    def driver(self):
        parking = True
        while parking:
            action = input('Would you like to park,pay or leave?').lower()
            if action == 'park':
               self.takeTicket()
            if action == 'pay':
                self.payForParking()
            if action == 'leave':
                self.leaveGarage()
            if action == 'show':
                print(self.parkingSpaces)
                print(self.paymentStatus_dict)
                print(self.ticketNumber)
    def takeTicket(self):
        if len(self.ticketNumber) > 0:
            new_ticket = self.ticketNumber.pop(0) 
            self.parkingSpaces.append(new_ticket)
            print(f'Your ticket number is {new_ticket}, please park in designated space.')
            print(f'There are now {len(self.ticketNumber)} spaces left.')
            self.paymentStatus_dict[new_ticket] = {'paid': False}
            print(self.paymentStatus_dict)
        else:
            print('There are no spaces left.')
    def payForParking(self):
        response = int(input('What ticket number would you like to pay?').lower())
        if response in self.parkingSpaces:
            self.paymentStatus_dict[response]['paid'] = True
            print(f'Paid ticket {response} succesfully!')
            self.leaveGarage()
        else:
            print(f'{response} is not a valid ticket number.')
    def leaveGarage(self):
        response = int(input('Are you ready to leave? Enter ticket number:').lower())
        if response in self.parkingSpaces:
            if self.paymentStatus_dict[response]['paid'] == True:
                print('Park here again any time!')
                self.parkingSpaces.remove(response)
                self.ticketNumber.append(response)
                self.ticketNumber = sorted(self.ticketNumber)
                del self.paymentStatus_dict[response]
                # print(self.ticketNumber)
                # print(self.paymentStatus_dict)
                # print(self.parkingSpaces)
            else:
                self.payForParking()
                if self.paymentStatus_dict[response]['paid'] == True:
                    print(f'Ticket {response} has been paid, you are free to go!.')
                    self.parkingSpaces.remove(response)
                    self.ticketNumber.append(response)
                    self.ticketNumber = sorted(self.ticketNumber)
                    del self.paymentStatus_dict[response]
                else:
                    print("You have to pay")
        else:
            print('Invalid entry')
            
        
car1 = Parking()

car1.driver()
     