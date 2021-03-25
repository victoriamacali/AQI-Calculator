print("Air Quality Index Calculator")
numlocation = int(input("How many locations for this report?"))
locations = []

for i in range (1, numlocation + 1 ):
    numL = "What is the name of Location " + str(i)+ "?"
    location1 = input(numL)
    locations.append (location1)
    emp2_5 = float(input("Enter PM-2.5 concentration: ")) 


    Cp = emp2_5

    if emp2_5 >= 0 and emp2_5 <= 12.0:
        C_low = 0.0
        C_high = 12.0
        I_low = 0.0
        I_high = 50.0
        AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
        aqiP =("Good")
        print("PM-2.5 concentration of", (emp2_5)," is index level", + (AQI))
        print(f"{AQI:0.1f}")

    elif emp2_5 >= 12.1 and emp2_5 <= 35.4:
        C_low = 12.1
        C_high = 35.4
        I_low = 51.0
        I_high = 100.0
        AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
        aqiP =("Moderate")
        print("PM-2.5 concentration of", (emp2_5)," is index level", + (AQI))
        print(f"{emp2_5:0.1f}")

    elif emp2_5 >= 35.5 and emp2_5 <= 55.4:
        C_low = 35.5
        C_high = 55.4
        I_low = 101.0
        I_high = 150.0
        AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
        aqiP =("Unhealthy for Sensitive Groups")
        print("PM-2.5 concentration of", (emp2_5)," is index level", + (AQI))

    elif emp2_5 >= 55.5 and emp2_5 <= 150.4:
        C_low = 55.5
        C_high = 150.4
        I_low = 151.0
        I_high = 200.0
        AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )        
        aqiP =("Unhealthy")
        print("PM-2.5 concentration of", (emp2_5)," is index level", + (AQI))

    elif emp2_5 >= 150.5 and emp2_5 <= 250.4:
        C_low = 150.5
        C_high = 250.4
        I_low = 201.1
        I_high = 300.0
        AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
        aqiP =("Very Unhealthy")
        print("PM-2.5 concentration of", (emp2_5)," is index level", + (AQI))

    elif emp2_5 >= 250.0 and emp2_5 <= 500.4:
        C_low = 250.0
        C_high = 500.4
        I_low = 301.0
        I_high = 500.0
        AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
        aqiP =("Hazardous")
        print("PM-2.5 concentration of", (emp2_5)," is index level", + (AQI))

    emp10 = float(input("Enter PM-10 concentration: "))


    if emp10 >= 0 and emp10 <= 54.0:
            C_low = 0.0
            C_high = 54.0
            I_low = 0.0
            I_high = 50.0
            AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
            print("PM-10 concentration of", (emp10)," is index level", + (AQI))

    elif emp10 >= 55 and emp10 <= 154.0:
            C_low = 55
            C_high = 154.0
            I_low = 51
            I_high = 100
            AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
            print("PM-10 concentration of", (emp10)," is index level", + (AQI))
        
    elif emp10 >= 155 and emp10 <= 254.0:
            C_low = 155
            C_high = 254.0
            I_low = 101
            I_high = 150
            AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
            print("PM-10 concentration of", (emp10)," is index level", + (AQI))

    elif emp10 >= 255 and emp10 <= 354.0:
            C_low = 255
            C_high = 354.0
            I_low = 151
            I_high = 200
            AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
            print("PM-10 concentration of", (emp10)," is index level", + (AQI))
        
    elif emp10 >= 355 and emp10 <= 424.0:
            C_low = 355
            C_high = 424.0
            I_low = 201
            I_high = 300
            AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
            print("PM-10 concentration of", (emp10)," is index level", + (AQI))

    elif emp10 >= 425 and emp10 <= 604.0:
            C_low = 425
            C_high = 604.0
            I_low = 301
            I_high = 500
            AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
            print("PM-10 concentration of", (emp10)," is index level", + (AQI))

    no2 = float(input("Enter NO-2 concentration:"))

    if no2 >= 0 and no2 <= 53.0:
                C_low = 0.0
                C_high = 53.0
                I_low = 0.0
                I_high = 50.0
                AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
                print("NO-2 concentration of", (no2)," is index level", + (AQI))

    elif no2 >= 54.0 and no2 <= 100.0:
                C_low = 54.0
                C_high = 100.0
                I_low = 51.0
                I_high = 100.0
                AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
                print("NO-2 concentration of", (no2)," is index level", + (AQI))

    elif no2 >= 101.0 and no2 <= 360.0:
                C_low = 101.0
                C_high = 360.0
                I_low = 101.0
                I_high = 150.0
                AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
                print("NO-2 concentration of", (no2)," is index level", + (AQI))

    elif no2 >= 361.0 and no2 <= 649.0:
                C_low = 361.0
                C_high = 649.0
                I_low = 151.0
                I_high = 200.0
                AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
                print("NO-2 concentration of", (no2)," is index level", + (AQI))

    elif no2 >= 650.0 and no2 <= 1249.0:
                C_low = 650.0
                C_high = 1249.0
                I_low = 201.1
                I_high = 300.0
                AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
                print("NO-2 concentration of", (no2)," is index level", + (AQI))

    elif no2 >= 1250.0 and no2 <= 2049.0:
                C_low = 1250.0
                C_high = 2049.0
                I_low = 301.0
                I_high = 500.0
                AQI = ((((I_high - I_low)/(C_high - C_low) ) * (Cp - C_low)) + (I_low) )
                print("NO-2 concentration of", (no2)," is index level", + (AQI))

    print("AQI for", (location1), "is", (AQI))
    print("Air Quality: ", (aqiP))

