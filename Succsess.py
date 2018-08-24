from tkinter import *
import requests 

root = Tk()

def apiCall():
    ethValue = "https://api.nanopool.org/v1/eth/user/0xb015db50c47bde61d70c79725135f07cfe171502" 
    ethUsd = "https://api.nanopool.org/v1/eth/prices"
    hashRate = "https://api.nanopool.org/v1/eth/reportedhashrate/0xb015db50c47bde61d70c79725135f07cfe171502"
    poolHash = "https://api.nanopool.org/v1/eth/pool/hashrate"


    main_json = requests.get(ethValue).json()
    usdToEthJson = requests.get(ethUsd).json()
    hashRateJson = requests.get(hashRate).json()
    poolHashJson = requests.get(poolHash).json()


    json_status = main_json ['status']
    print("Is the API running?")
    print(json_status)




    ethBalance = main_json ['data']['balance']
    print("Amount of Ethereum in your account:")
    print(ethBalance)
    ethBalanceText = Text(root, height=2, width = 75, fg="red")
    ethBalanceText.grid(row=4, column=1)
    ethBalanceText.insert(END, "Amount of Ether: " + str (ethBalance))




    ethToUsd = usdToEthJson ['data']['price_usd']
    print("USD value of ETH:")
    print(ethToUsd)
    ethUsdText = Text(root, height=2, width = 75, fg="red")
    ethUsdText.grid(row=3, column=1)
    ethUsdText.insert(END, "USD value of ETH: " + str (ethToUsd))



    userValue = float(ethToUsd) * float(ethBalance)
    print("Total USD value of ETH in your account:")
    print(int(userValue))
    userValueText = Text(root, height=2, width = 75, fg="red")
    userValueText.grid(row=2, column=1)
    userValueText.insert(END, "Total USD value of ETH in your account: " + str (userValue))


    userHash = hashRateJson['data']
    print ("Current hashRate:")
    print(userHash)
    userHashText = Text (root, height=2, width=75, fg="red")
    userHashText.grid(row=5, column=1)
    userHashText.insert(END, "Is the Rig up?(MH/S): " + str (userHash))



    totalPoolHash = poolHashJson['data']
    print("Total Pool Hash: ")
    print(totalPoolHash)
    poolHashText = Text (root, height =2, width=75, fg="red")
    poolHashText.grid(row=5, column=1)
    poolHashText.insert(END, "Total Pool Hash: " + str (totalPoolHash))


button1 = Button(root, text= "Refresh The Data", command = apiCall)
button1.grid(row=1, column=1)





root.mainloop()

                       
