#
#Emily Gavrilenko
#015218875
#4/2/2019
#
#Lab 0
#Section 12
#Purpose: This function will return the weight of a person on Mars and Jupiter after inputing their weight on Earth

def weight_on_planets():
   #weight is a person's weight on earth, in pounds
   weight_ = input('What do you weigh on earth? ')
   #converts weight from a String to float variable
   weight = float(weight_)
   print("\nOn Mars you would weigh",0.38*weight,"pounds.\nOn Jupiter you would weigh", 2.34*weight, "pounds.")


if __name__ == '__main__':
     weight_on_planets()
