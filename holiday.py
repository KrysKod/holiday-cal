''' creating simple holliday calculator here i give user 3 options to chose from the output will depend on his chosen options
i will create functions for the future, i will use if loop to determine the price of  flight and room in chosen city
all wll be displayed in nice way '''
print("Welcome to my Holiday calculator")
print()
city_flight = input("Please choose your destination from options provided" "\n" "Rome" "\n" "Lisbon" "\n" "Krakow" "\n"  ).title()
#creating variable hotel_room and fligh of which the value dipendes of user selection
if city_flight == "Krakow":
    hotel_room = 75 
    flight = int(156)
if city_flight == "Rome":
    hotel_room = 65
    flight = int(125)
if city_flight == "Lisbon":
    hotel_room = 85
    flight = int(162)

    

print("Pleae enter how many nights you are planing to go for : ")

num_nights = int(input())



print("Please enter for how man days would you like to hire a car: ")

rental_days = int(input())



def plane_cost(city_flight):
    
    
    plane_cost = flight
    print (f"The flight cost to {city_flight} is : £{flight}")#display chosen destination and ticket cost
    return plane_cost
  

plane_cost(city_flight)
plane_cost = flight
def hotel_cost(num_nights,hotel_room):
    
    hotel_cost = num_nights * hotel_room
    print(f"Your hotel room in {city_flight} for {num_nights} night's will cost you : £{hotel_cost}")
    return hotel_cost
   

hotel_cost(num_nights,hotel_room)
hotel_cost = num_nights * hotel_room

def car_rental(rental_days,day_rate = 65):
    car_rental = rental_days * day_rate
    print(f"Car rental for {rental_days} day's will cost you: £{car_rental}") #display rental cost dippend on user input
    return car_rental
    

car_rental(rental_days,day_rate = 65)
car_rental=rental_days * 65
def holliday_cost(hotel_cost,car_rental,plane_cost):
    holliday_cost = int(hotel_cost)+int(car_rental)+int(plane_cost)
    print ("Total cost for your holliday including \n Flight \n Car rental \n Hotel \n is....\n£", holliday_cost)
    return holliday_cost
holliday_cost(hotel_cost,car_rental,plane_cost)

  
