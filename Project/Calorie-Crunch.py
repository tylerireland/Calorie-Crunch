import math
import time
import datetime


# calculate the user's BMR
def CalculateBMR(gender, weight, height, age):
    if gender == 'm':
        #print("\n...using male calc...\n")
        avgBMR = 66 + (6.23 * weight) + (12.7 * height) - (6.8 * age)
    elif gender == 'f':
        #print("\n...using female calc...\n")
        avgBMR = 655 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
    
    else:
        print("Null")
         
    return avgBMR


# saves the userInfo array into the user_info file (used for mulitple users)
def saveDataArray(userInfo):
    user_info = open("user_info", 'a')
    for i in userInfo:
        user_info.write(str(i))
        user_info.write(" ")
    user_info.write("\n")

    
    
# retrieves the line with user's info and puts it into an array
def getDataArray(name):
    user_info = open("user_info", "r")
    for line in user_info:
        if name in line:
            userInfo=line.split()
    return userInfo
    
# saves net calories into a file with name and date (this will save everybody's info and will not be sorted)
def saveCalorieExpend(name, netCals, currentDate):
    calorie_log=open("calorie_log", 'a')
    calorie_log.write(currentDate + " " + name + ": " + str(netCals) + " kcals")
    calorie_log.write("\n")
    
# Function with all the excercise calculations
def CalculateCalExpend(workoutChoice, weight):
            
            # LIFTING WEIGHTS
    if workoutChoice == 1:
        timeLimit=float(input("Enter the total time lifting(minutes): "))
        if weight <= 125:
            totalCals= 3 * timeLimit
        elif weight >=125 and weight <=155:
            totalCals = 3.75 * timeLimit
        elif weight >=155 and weight <=185:
            totalCals = 4.4 * timeLimit
        elif weight > 185:
            totalCals = 5 * timeLimit
            
            
            # WALKING
    elif workoutChoice == 2:
        totalMiles=float(input("Enter the total miles you walked: "))
        if weight <= 120:
            totalCals= 64 * totalMiles
        elif weight >120 and weight <=180:
            totalCals = 85 * totalMiles
        elif weight >180 and weight <=250:
            totalCals =  100 * timeLimit
        elif weight > 250:
            totalCals = 130 * totalMiles
            

            # RUNNING
    elif workoutChoice == 3:
        totalMiles=float(input("Enter the total miles you ran: "))
        timeLimit=float(input("Enter the total time (minutes): "))
        pace=totalMiles/timeLimit

        if pace >= 6:
            if weight <= 130:
                totalCals= 10 * timeLimit
            elif weight >130 and weight <=170:
                totalCals = 12 * timeLimit
            elif weight >170 and weight <=210:
                totalCals =  15 * timeLimit
            elif weight > 210:
                totalCals = 17 * timeLimit

        # use walking formulas
        elif pace < 6:
            if weight <= 120:
                totalCals= 64 * totalMiles
            elif weight >120 and weight <=180:
                totalCals = 85 * totalMiles
            elif weight >180 and weight <=250:
                totalCals =  100 * timeLimit
            elif weight > 250:
                totalCals = 130 * totalMiles


            # BIKING       
    elif workoutChoice == 4:
        totalMiles=float(input("Enter the total miles you biked: "))
        timeLimit=float(input("Enter the total time (minutes): "))
        pace=totalMiles/timeLimit
        if pace >=14:
            if weight <= 140:
                totalCals= 12 * timeLimit
            elif weight >140 and weight <=170:
                totalCals = 14 * timeLimit
            elif weight >170 and weight <=210:
                totalCals =  18 * timeLimit
            elif weight > 210:
                totalCals = 21 * timeLimit
        elif pace < 14:
            if weight <= 130:
                totalCals= 9 * timeLimit
            elif weight >130 and weight <=170:
                totalCals = 10 * timeLimit
            elif weight >170 and weight <=210:
                totalCals = 12 * timeLimit
            elif weight > 210:
                totalCals = 14 * timeLimit


            # ROWING
    elif workoutChoice == 5:
        timeLimit=float(input("Enter the total time rowing(minutes): "))
        if weight <= 125:
            totalCals= 7.5 * timeLimit
        elif weight >=125 and weight <=155:
            totalCals = 9 * timeLimit
        elif weight >=155 and weight <=185:
            totalCals = 10 * timeLimit
        elif weight > 185:
            totalCals = 14 * timeLimit


            # STAIR CLIMBING
    elif workoutChoice == 6:
        timeLimit=float(input("Enter the total time climbing(minutes): "))
        avgSteps=int(input("Enter your average steps per minute: "))
        if avgSteps >= 50:
            if weight <= 125:
                totalCals= 9 * timeLimit
            elif weight >=125 and weight <=155:
                totalCals = 10 * timeLimit
            elif weight >=155 and weight <=185:
                totalCals = 12 * timeLimit
            elif weight > 185 and weight <=215:
                totalCals = 14 * timeLimit
            elif weight > 215:
                totalCals = 16 * timeLimit
        else: # <50 spm
            if weight <= 125:
                totalCals= 3 * timeLimit
            elif weight >=125 and weight <=155:
                totalCals = 4 * timeLimit
            elif weight >=155 and weight <=185:
                totalCals = 5 * timeLimit
            elif weight > 185 and weight <=215:
                totalCals = 6 * timeLimit
            elif weight > 215:
                totalCals = 7 * timeLimit


            # ELLIPTICAL
    elif workoutChoice == 7:
        timeLimit=float(input("Enter the total time excercising(minutes): "))
        if weight <= 125:
            totalCals= 5 * timeLimit
        elif weight >=125 and weight <=155:
            totalCals = 6 * timeLimit
        elif weight >=155 and weight <=185:
            totalCals = 8 * timeLimit
        elif weight > 185 and weight <=215:
            totalCals = 9 * timeLimit
        elif weight > 215:
            totalCals = 10 * timeLimit
   
            
    return totalCals





# dictionary to print out excercises with respective numbers
workoutList=['1. Lifting Weights','2. Walking','3. Running','4. Biking','5. Rowing','6. Stair Climbing','7. Elliptical']

#used to store user's data
userInfo=[]

# sets current date
currentDate = datetime.datetime.now()

# setting application states before running
isOpen=True
alreadyOpen=False

while(isOpen):
    if(alreadyOpen == False):
        #prints current date
        print("\t\t\t\t "+currentDate.strftime("%m")+"/"+currentDate.strftime("%d")+"/"+currentDate.strftime("%y"))
        time.sleep(1.0)
        print("    Welcome to Calorie Crunch! ")
        time.sleep(1.0)

    # prompt user if 'new' or 'returning' 
    userStatus = ""

    while (userStatus != "r" and userStatus != "n"):
        userStatus=input("Are you a returning user, or a new user? (r/n): ")
        userStatus=userStatus.lower()

    time.sleep(0.5)

    # if user is new, this will get user's info, and append it to userInfo array

    if userStatus == 'n':
        netCals = 0

        name=input("Enter your name: ")

        time.sleep(1.0)

        print("\n  Hello " + name + "!")
        name=name.lower()
        userInfo.append(name)

        time.sleep(1.0)

        gender = ""
        while(gender != "m" and gender != "f"):
            gender=str(input("\nEnter your gender (m/f): "))

            if gender =='m' or gender == 'f':

                userInfo.append(gender)
                
                time.sleep(1.0)

                weight=int(input("\nEnter your weight(pounds): "))
                userInfo.append(weight)
                
                time.sleep(1.0)

                height=int(input("\nEnter your height(inches): "))
                userInfo.append(height)
                
                time.sleep(1.0)

                age=int(input("\nEnter your age: "))
                userInfo.append(age)
                
                time.sleep(1.0)

            else:
                time.sleep(1.0)
                print(" Invalid input, must be 'm' or 'f'.")


        # calcs user's BMR
        userBMR=CalculateBMR(gender,weight,height,age)
        
        # appends it to the userInfo array
        userInfo.append(userBMR)

        # writes the array into a new file called "user_info"
        saveDataArray(userInfo)


        # displays BMR
        print("\n We use this information to calculate your average BMR, or Basal Metabolic Rate.")
        time.sleep(2.0)
        print("Your BMR is the total calories your body needs to perform basic, life-sustaining functions.")
        time.sleep(2.0)
        print("This is just an estimate.")
        time.sleep(1.0)
        print("\n Your average BMR is %.2f" % userBMR)
        time.sleep(1.0)


    # if user is returning, prompts for name
    elif userStatus == 'r':
        name = input("Enter your name: ")
        name=name.lower()
        #searches the file for line containing name, getDataArray() returns an array of the user's info
        userInfo=getDataArray(name)
        #stores the user's info into respective variable names for excercise calculations
        name=str(userInfo[0])
        gender=str(userInfo[1])
        weight=int(userInfo[2])
        userBMR=float(userInfo[5])
        time.sleep(0.5)
        print("\nWelcome back, " + name + "!")
        time.sleep(1.0)


    # sets state for adding new workouts
    newWorkout = True
    
    # sets net calories to BMR before adding excercise calories
    netCals=userBMR

    
    while(newWorkout):
        # prompt for new workout workout
        addWorkout=input("\nDo you want to add a workout? (y/n): ")
        # if user wants to add a workout, this will use the CalcCalExpend function to find total calories
        if addWorkout == 'y':
            print("\n")
            
            # prints the dictionary of workouts to choose from
            for item in workoutList:
                print(item)
            
            workoutChoice=int(input("\nChoose a workout to add: "))
            time.sleep(0.5)
            
            # CalculateCalExpend returns the total calories burned from chosen workout
            totalCals=CalculateCalExpend(workoutChoice, weight)
            
            # displays the total calories for this workout
            print("This workout burned around %.1f calories!" % totalCals)
            
            # adds workout calories to net calories
            netCals+=totalCals

        # if user does not want to add a workout, this will display total cals and prompt for log out or close
        elif addWorkout == 'n':
            newWorkout = False
            time.sleep(1.0)
            
            # displays total calories at the end of the day
            print("By the end of the day, you burned around " + str(netCals) + " calories!" )
            time.sleep(1.0)
            print(" Great Job!")
            time.sleep(1.5)
            
            # prompts user to log out or close program
            status=int(input("Would you like to Log out(1) or Close this application(2)? (1 / 2): "))
            if status == 1:
                alreadyOpen=True
            elif status == 2:
                isOpen = False
