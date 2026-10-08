total_charge=0
print(sum())
def spms():
    print("choose vehicle type\n1.bus\n2.car\n3.bike")
    bus=80
    car=40
    bike=20 
    choice=int(input("enter vehicle "))
    print("Enter No Of hours parked \n")
    no_of_hours=int(input("Hours="))
    no_of_hours-=1
    if no_of_hours<0:
        print("negative time\n")
    if choice==1:
        charge=no_of_hours*bus
        bus=no_of_hours*bus
        if no_of_hours>5:
            charge=bus-bus*10/100
        
    elif choice==2:
        charge=no_of_hours*car
        car=no_of_hours*car
        if no_of_hours>5:
            charge=car-car*10/100
    elif choice==3:
        charge=no_of_hours*bike
        bike=no_of_hours*bike
        if no_of_hours>5:
            charge=bike-bike*10/100
    else:
        print("invalid vehicle input")
        return
    print(f"successfully charged amount of ={charge}")
    return charge

def display():
    print(f"Total earnings:{total_charge}\n")


while True:
    print("*"*50)
    print("Smart park Management system\n")
    print("1.ADD Parking\n")
    print("2.Display total amount EArned\n")
    print("3.EXIT\n")
    print("*"*50)
    choice=int(input("enter the choice\n"))
    print("*"*50)
    match choice:
        case 1:
            total_charge+=spms()
        case 2:
            display()
        case 3:
            break