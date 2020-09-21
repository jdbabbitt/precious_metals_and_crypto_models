from chart_display_functions import *

# displays single price chart
def display_single_chart():
    chart = input("Which chart would you like to see? b = bitcoin, e = ethereum, g = gold, s = silver\n").lower()
    
    if chart == "b":
        supply = input("Would you like to see the bitcoin current supply chart as well? y for yes, n for no").lower()
        if supply == "n":
            btc_price_chart()
        elif supply == "y":
            btc_price_chart()
            btc_supply_chart()
        else:
            print("Invalid Response.")
            display_single_chart()

    elif chart == "e":
        eth_price_chart()
    
    elif chart == "g":
        gold_price_chart()
    
    elif chart == "s":
        silver_price_chart()
    
    else:
        print("Invalid input try again\n")
        display_single_chart()

# displays multiple price charts
def display_price_charts():
    charts = input("Which charts would you like to see? enter a comma separated list. Ex) bitcoin,ethereum,gold,silver\n").lower()
    # removes whitespace
    charts = charts.replace(" ", "")
    # splits the string into a list
    charts = charts.split(",")
    num_of_charts = len(charts) # number of charts is equal to the length of the list
    # loops through and builds the plot 
    print(charts)
    for chart_num in range(0, len(charts)):
        if charts[chart_num]== "bitcoin":
            btc_price_chart(chart_num+1,num_of_charts)    
        
        elif charts[chart_num] == "ethereum":
            eth_price_chart(chart_num+1,num_of_charts)
        
        elif charts[chart_num] == "gold":
            gold_price_chart(chart_num+1, num_of_charts)
        
        elif charts[chart_num] == "silver":
            silver_price_chart(chart_num+1, num_of_charts)
        
        else:
            print("Invalid input try again\n")
            display_price_charts()


if __name__ == "__main__":
    display_choice = input("Would you like to see a single price chart or multiple price charts? s = single price chart, m = multiple price charts\n").lower()
    if display_choice == "s":
        display_single_chart()
    elif display_choice == "m":
        display_price_charts()
    else:
        print("Invalid Response")
    plt.show()