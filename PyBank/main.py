# import modules
import csv, pathlib

# initialize list to store dictionary rows and profit/loss changes
budget_list = []

# initialize counter variables to zero
profit_loss_total   = 0
profit_change_total = 0
greatest_decrease   = 0
greatest_increase   = 0
profit_loss_change  = 0
prior_profit_loss   = 0

# Define input and output files
budget_csv      = pathlib.Path("./Resources/budget_data.csv")
budget_analysis = pathlib.Path("./analysis/budget_analysis.csv")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Read in the header
    csvheader = next(csvreader)

    # Read in the rest of the file
    # Gather stats per line, save into a list of dictionaries
    for index, row in enumerate(csvreader):
        profit_loss = float(row[1])
        profit_loss_date = row[0]

        # Calculate change in profit/loss for current row
        # First entry has no profit/loss change
        if index == 0:
            profit_loss_change = 0
        else:
            profit_loss_change = profit_loss - prior_profit_loss

        # Update greatest increase if current profit is greater than previous
        if profit_loss_change > greatest_increase:
            greatest_increase = profit_loss_change
            greatest_increase_date = profit_loss_date
        # Update greatest decrease if current loss is greater than previous
        if profit_loss_change < greatest_decrease:
            greatest_decrease = profit_loss_change
            greatest_decrease_date = profit_loss_date

        # Store rows in list of dictionaries. Include change in profit/loss
        budget_list.append({profit_loss_date : [profit_loss, profit_loss_change]})
        
        # Update counters for next iteration
        prior_profit_loss    = profit_loss
        profit_change_total += profit_loss_change
        profit_loss_total   += profit_loss

# Count number of months in data set
months_count = len(budget_list)

# for irow in budget_list:
#     print(f"{irow}")

# The net total of profit/losses over entire period
## already calculated in profit_loss_total

# The average of changes over entire period (exclude first row)
avg_change = profit_change_total / (months_count - 1)

# Print out findings to screen
print("---------------------------------------------------------")
print(f"Financial Analysis for file {budget_csv}")
print("---------------------------------------------------------")
print(f"Total Months:                       {months_count}")
print(f"Total Profit/Loss:                  ${profit_loss_total:.0f}")
print(f"Average Change:                     ${avg_change:.2f}")
print(f"Greatest Profits Increase: {greatest_increase_date} ${greatest_increase:.0f}")
print(f"Greatest Profits Decrease: {greatest_decrease_date} ${greatest_decrease:.0f}\n")

# Print findings to analysis folder