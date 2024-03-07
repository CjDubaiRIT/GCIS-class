def CurrencyConverter():
    AED_to_EUR = 0.249
    EUR_to_AED = 3.982557
    AED_to_GBP = 0.214498
    GBP_to_AED = 4.66
    AED_to_USD = 0.272264
    USD_to_AED = 3.6725
    

def AED_Options(amount, from_currency, to_currency):
    if from_currency == "AED" and to_currency == "USD":
       return amount * 0.272264
    elif from_currency == "AED" and to_currency == "GBP":
         return amount * 0.214498
    elif from_currency == "AED" and to_currency == "EUR":
         return amount * 0.249
    else:
         return ("")
def Other_toAED(amount, from_currency, to_currency):
    if from_currency == "USD" and to_currency == "AED":
        return amount * 3.6725
        #testing if this works on python first befor writing the code
    elif from_currency == "GBP" and to_currency == "AED":
        return amount * 4.66
    elif from_currency == "EUR" and to_currency == "AED":
            return amount * 3.982557

    else:
        return ("")


def main():
    # use split funtion to make the main menu organaized imo
    mainmenu = "Menu//Welcome to our Currency converter/-----------------------------------/"
    token = mainmenu.split("/")
    for i in token:
        print(i)
    # using split funtion to make the code print each option on a different line
    lisoption = "1.) AED to other currencies/2.) Other currencies to AED/3.) Exit"
    token = lisoption.split("/")
    for i in token:
        print(i)
    # amount given from user
    amount = float(input("Enter the amount you would like to be converted today"))
    # our user option is gonna be called option
    option = int(input("What would you like to convert: "))
    while True:
        if option == 1:
            submenu="1.). AED to Euro (EUR)/2.) AED to British Pound (GBP)/3.) AED to US Dollar/4.)Exit"
            token=submenu.split("/")
            for i in token:
                print(i)
            from_currency='AED'
            AED_opt = int(input("pick your option"))
            if AED_opt == "1":
                to_currency='EUR'
                return to_currency
                return amount * 0.249
            elif AED_opt == "2":
                to_currency='GBP'
                return to_currency
                return amount * 0.214498
            elif AED_opt == "3":
                to_currency='USD'
                return to_currency
                return amount * 0.272264
            elif AED_opt == "4":
                return ("program is out")

            # the function AED_Options will have the options for the user
            # to pick from and the amount to be converted then
            # have three functions for each conversion type
            AED_Options(amount, from_currency, to_currency)
        elif option == 2:
            submenu="1.) Euro (EUR) to AED/2.) British Pound (GBP) to AED/3.) Dollar to AED/4.) Exit"
            token=submenu.split("/")
            for i in token:
                print(i)
            to_currency='AED'
            AED_opt = int(input("pick your option"))
            if AED_opt == "1":
                from_currency='EUR'
                return to_currency
                return amount * 3.982557
            elif AED_opt == "2":
                from_currency='GPB'
                return to_currency
                return amount * 4.66
            elif AED_opt == "3":
                from_currency='USD'
                return to_currency
                return amount * 3.6725
            elif AED_opt == "4":
                return ("program is out")

            # the function Other_toAED will have the options for the user
            # to pick from and the amount to be converted then
            # have three functions for each conversion type
            Other_toAED(amount, from_currency, to_currency)
        elif option == 3:
            print("Thank you for working with us today")
        else:
            print("Error")


main()