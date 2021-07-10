# import modules
import csv

# initialize a dictionary to store each key-value
budget_dict = {}
budget_list = []
profit_loss_total = 0
profit_change_total = 0

# read in the file
budget_file = "./Resources/budget_data.csv"
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Read in the header
    csvheader = next(csvreader)

    # Read in the rest of the file
    # Save into a list of dictionaries
    #    records  =  [ 0, {"Jan-2010": 867884}]
    for index, row in enumerate(csvreader):
        profit_loss = float(row[1])
        profit_loss_date = row[0]
        profit_loss_total += profit_loss
        if index == 0:
            prior_profit_loss = 0
            greatest_decrease = 0
            greatest_decrease_date = ""
            greatest_increase = 0
            greatest_increase_date = ""
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

        budget_list.append({profit_loss_date : [profit_loss, profit_loss_change]})
        budget_dict[profit_loss_date] = profit_loss

        prior_profit_loss = profit_loss
        profit_change_total += profit_loss_change

# print(budget_list)
# print(budget_dict)
# Count number of months in data set
months_count = len(budget_dict)
# months_count = len(budget_list)

# The net total of profit/losses over entire period
## already calculated in final profit_losses

# The average of changes over entire period
avg_change = profit_change_total / (months_count - 1)

# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)
## print(budget_dict)
print(f"Total months: {months_count}")
print(f"Total profit/loss: ${profit_loss_total}")
print(f"Average change: ${avg_change}")
print(f"Greatest increase in profits: {greatest_increase_date} ${greatest_increase}")
print(f"Greatest decrease in profits: {greatest_decrease_date} ${greatest_decrease}")