import csv
import os
# Define variables and file paths
budget_data=os.path.join(".","Resources","budget_data.csv")
output_file = os.path.join(".","Analysis","budget_data.txt")
months = {}
totalmonths = 0
# Lists to store months and Profits/Losses in order
profits = []
profitchanges = []

# Define function to analyse budget
def budgetanalysis():
    # Opening the CSV file and creating a dictionary
    with open(budget_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        # Skipping header rows
        next(csvreader, None)
        for rows in csvreader:
            months[rows[0]] = int(rows[1])
            profits.append(int(rows[1]))
            profitchanges.append(rows[0])
            
    # Find total months 
    totalmonths = len(months)
    
    # Net total of Profit/Losses
    profitlosses = sum(months.values())
    
    # Average Changes in Profit/Losses 
    Changes = []
    Previousprofit = 1088983
    for i in profits:
        Changes.append(i-Previousprofit)
        Previousprofit = i
    averagechanges = sum(Changes)/(len(Changes)-1)
    
    # Greatest Increase in Profits
    greatestincrease = 0
    greatestmonth = ""
    for Change_index in range(len(Changes)):
        if Changes[Change_index] > greatestincrease:
            greatestincrease = Changes[Change_index]
            greatestmonth = profitchanges[Change_index]
            
    # Greatest Decrease in Profits
    greatestdecrease = 0
    leastmonth = ""
    for Change_index in range(len(Changes)):
        if Changes[Change_index] < greatestdecrease:
            greatestdecrease = Changes[Change_index]
            leastmonth = profitchanges[Change_index]
            
    # Print results in terminal
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(totalmonths))
    print("Total: $" + str(profitlosses))
    print("Average Change: $" + str(round(averagechanges,2)))
    print("Greatest Increase in Profits: " + str(greatestmonth) + " ($" + str(greatestincrease)+")")
    print("Greatest Decrease in Profits: " + str(leastmonth) + " ($" + str(greatestdecrease)+")")
    # Print results in file
    with open(output_file, "w", newline='') as datafile:
        datafile.write("Financial Analysis\n\n")
        datafile.write("----------------------------\n\n")
        datafile.write("Total Months: " + str(totalmonths) + "\n")
        datafile.write("Total: $" + str(profitlosses) + "\n")
        datafile.write("Average Change: $" + str(round(averagechanges,2)) + "\n")
        datafile.write("Greatest Increase in Profits: " + str(greatestmonth) + " ($" + str(greatestincrease)+")\n")
        datafile.write("Greatest Decrease in Profits: " + str(leastmonth) + " ($" + str(greatestdecrease)+")\n")
        
    return
    
budgetanalysis()