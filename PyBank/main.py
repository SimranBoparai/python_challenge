
import os
import csv

## Define the CSV path
CSV_PATH = os.path.join('Resources', 'budget_data.csv')

## Define indiciese for CSV columns
MONTH_INDEX = 0
PROFIT_INDEX = 1

## Change directory to find specific location of file
os.chdir(os.path.dirname(os.path.realpath(__file__)))
print(__file__)

## Define the constants of the CSV file
def read_csv_count_months(csvpath):
    total_months = 0
    previous_profit = None
    total_profit = 0
    total_change = 0
    greatest_increase = {"value": -99999}
    greatest_decrease = {"value": 99999}

## Read each row in the csv file and calculate the values
    with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        print(header)

        for row in csvreader:
            total_months += 1
            current_date = row[MONTH_INDEX]
            current_profit = int(row[PROFIT_INDEX])
           
           ## Calculate the values 
            total_profit += current_profit
            
            if previous_profit is not None: 
                current_change = current_profit - previous_profit 
                total_change = total_change + current_change
                if current_change > greatest_increase["value"]:
                    greatest_increase = {"month": current_date, "value": current_change} 
                if current_change < greatest_decrease["value"]: 
                    greatest_decrease = {"month" : current_date, "value" : current_change}
                    
            previous_profit = current_profit

    average_change = total_change / (total_months - 1)

    ## Print each calculation
    print(total_months)
    print(total_profit)
    print(average_change)
    print(greatest_increase)
    print(greatest_decrease)


    ## Call the functions to return the values 
    return total_months, total_profit, average_change, greatest_increase, greatest_decrease
            
total_months, total_profit, average_change, greatest_increase, greatest_decrease = read_csv_count_months(CSV_PATH)



## Write a text file for the results
write_file = "Results.txt"
with open(write_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total months: {total_months}\n")
    file.write(f"Total profit: ${total_profit}\n")
    file.write(f"Average change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['value']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['value']})\n")
            
