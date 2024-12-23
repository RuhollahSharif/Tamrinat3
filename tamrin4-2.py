class Footbalist:

    def __init__(self, first_name, last_name, weight ,  height , number ):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.height = height
        self.weight = weight

    def player_first_number(self):
        return('The player first name: '+ self.first_name)
   
class Goalkeeper(Footbalist):
    pass

class Defenders(Footbalist):
    pass

player1 = Footbalist('Ruhollah' , 'Sharif' , 82 , 180 , 17)
player2 = Goalkeeper('Alireza' , 'Biranvand' , 70 , 190 , 1)
player3 = Defenders('Alireza' , 'Nikouei' , 80 , 170 , 3)
player4 = Defenders('Mehdi' , 'Norozi' , 75 , 160 , 4)
print(player1.player_first_number())