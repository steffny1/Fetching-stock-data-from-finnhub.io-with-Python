import requests
import json
import csv
#pretty print data in readable format
from pprintpp import pprint as pp


"""input your API key"""
api_key = ''


url = "https://finnhub.io/api/v1/quote?"

symbols = ["AAPL","AMZN","GOOGL","FB","NFLX"]


#function to fetch data from API
def fetch_data():
    
    temp_dict = []
    
    #iterate over the symbols list to get data for each stock
    for symbol in symbols:
        response = requests.get(url,params={'symbol':symbol,'token':api_key})
        
        #convert to python object
        stock_data = response.json()
        
        #store in temp dict in reference to the stock names as keys and the stock data as values
        temp_dict.append({symbol:stock_data})
    #pretty print data
    pp(temp_dict)
    
    #return values otherwise it will return None which will throw error in for loop    
    return temp_dict
    

# function to find the maximum value of percentage change
# C = Current price
# dp = percentage change
# pc = last price
def find_max_per_change():
    
    #get the stock data
    stock_data = fetch_data()
    percentage_change = "dp"
    
    #temp list to store max values of percentage change
    dp_list = []
    
    #list to store dict with the max % change
    most_volatile_stock = []

    #iterate through list of nested dict to find the max value of percentage change
    for i in stock_data:
        for j in i.values():
            dp = j[percentage_change]
            dp_list.append(dp)
            

    # find the max value in the temp list        
    mv = max(dp_list)

    #iterate through list of nested dic to find the stock(dict) that has the max value in percentage change
    for i in stock_data:
        for j,k in i.items():
            if k['dp'] == mv:     
                stock_symbol = j
                percentage_change = k['dp']
                current_price = k['c']
                last_price = k['pc']
                
                # add all required variables/data to write to CSV to list   
                flist = [stock_symbol,percentage_change,current_price,last_price]
                
                #add the values of the stock with max value to most_volatile_stock list
                most_volatile_stock.extend(flist)
                    
                print(most_volatile_stock)
                                          
    return most_volatile_stock             


#function to write data to CSV file
def write_data_to_csv():
    headers = ["stock_symbol","percentage_change","current_price","last_close_price"]
    data = find_max_per_change()

    #name of CSV file
    file_name = "Most_Volatile_Stock.csv"

    #open the file in write mode
    f = open(f"C:\\Users\\User\\Desktop\\{file_name}", 'w', newline='')

    #create the CSV writer
    writer = csv.writer(f)

    #write the headers to the CSV file
    writer.writerow(headers)

    #write the data to the CSV file
    writer.writerow(data)

    #close the file
    f.close()

    print("Data successfully written")

#call the function    
write_data_to_csv()
    
    


    
