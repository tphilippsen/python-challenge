# import CSV file
import os
import csv
# identify path to csv file
csvpath = os.path.join('Resources', "budget_data.csv")

 
# open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

# define variables before the loop
    total_months = []
    total = []
    profit_loss_diff = []
    
    print("Financials Analysis")
    print('------------------------------')
    
    # find total number of months in data_set
    csv_header = next(csvreader)
    
    
    for row in csvreader:
        # find total months in csv file
         total_months.append(row[0])
       
        # find total profit/loss in csv file
         total.append(int(row[1]))

    # find the change in profits and losses over the whole period starting with the first period
    for value in range(1, len(total)):
        # change the value of profit_loss_diff by subtracting the next value from the current value
        profit_loss_diff.append(int(total[value])-int(total[value-1]))
   
    # find the average of the changes in profits and losses
    average_profit_loss = sum(profit_loss_diff) / (len(total_months)-1)
   
    # find row with the greatest increase and the row with the greatest decrease
    greatest_increase = max(profit_loss_diff)
    greatest_decrease = min(profit_loss_diff)

    # find the date with the greatest increase and the date with the greatest decrease
    month_maximum = int(profit_loss_diff.index(greatest_increase))
    month_minimum = int(profit_loss_diff.index(greatest_decrease))

# create file to store txt file and txt file
file_to_save = os.path.join("analysis", "profit_loss.txt")
with open (file_to_save, 'w') as txt_file:
    
# print to terminal
    print(f"Total Months: {len(total_months)}")
    print(f"Total : $ {sum(total)}")
    print(f"Average Change : $ {round(average_profit_loss,2)}")
    print(f"Greatest Increase in Profits: {total_months[month_maximum+1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {total_months[month_minimum+1]} (${greatest_decrease})")
    
# Print to txt file
    output = (f"Financial Analysis \n"
              f"------------------------------\n"
              f"Total : $ {sum(total)}\n"
              f"Average Change : $ {round(average_profit_loss,2)}\n"
              f"Greatest Increase in Profits: {total_months[month_maximum+1]} (${greatest_increase})\n"
              f"Greatest Decrease in Profits: {total_months[month_minimum+1]} (${greatest_decrease})")

    txt_file.write(output)

    

  
    