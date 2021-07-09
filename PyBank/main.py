# import modules
import csv

# initialize a dictionary to store each key-value
budget_dict = {}
## rowname =  []

# read in the file
budget_file = "./Resources/budget_data.csv"
with open(budget_file) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    # Read in the header
    csvheader = next(csvreader)
    ## print(f"Header: {csvheader}")

    # Read in the rest of the file
    for row in csvreader:
        budget_dict[row[0]] = float(row[1])
    ## budget_dict[rowname[0]] = [row[1] for row in csvreader]


# Count number of months in data set
months_count = len(budget_dict)
# The net total of profit/losses over entire period
# The average of changes over entire period
# Greatest increase in profits (date and amount)
# Greatest decrease in losses (date and amount)
print(budget_dict)
print(months_count)