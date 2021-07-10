import csv

poll_file = './Resources/election_data.csv'
poll_list = []
poll_dict = {}
with open(poll_file) as p:
    pollreader = csv.reader(p, delimiter = ",")
    pollheader = next(pollreader)

    for index, row in enumerate(pollreader):
        voter_id = row[0]
        voter_county = row[1]
        voter_candidate = row[2]
        poll_list.append({voter_id : [voter_county, voter_candidate]})
        if voter_candidate in poll_dict:
            poll_dict[voter_candidate] = poll_dict[voter_candidate] + 1
        else:
            poll_dict[voter_candidate] = 1

# The total number of votes cast
total_voters = len(poll_list)
print(f"Total voter records: {total_voters}")

# A complete list of candidates who received votes
# print(poll_dict)
for candidate in poll_dict:
    print(f"{candidate}:  {poll_dict[candidate]}")

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.
