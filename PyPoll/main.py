import csv, pathlib

poll_csv_input = pathlib.Path('./Resources/election_data.csv')
poll_analysis_output = pathlib.Path('./analysis/poll_analysis.csv')
# poll_list = []
poll_dict = {}
total_voters = 0

with open(poll_csv_input) as poll_file:
    pollreader = csv.reader(poll_file, delimiter = ",")
    pollheader = next(pollreader)

    for row in pollreader:
        # voter_id = row[0]
        # voter_county = row[1]
        voter_candidate = row[2]
        # poll_list.append({voter_id : [voter_county, voter_candidate]})
        # Tally votes with polling dictionary
        if voter_candidate in poll_dict:
            poll_dict[voter_candidate] = poll_dict[voter_candidate] + 1
        else:
            poll_dict[voter_candidate] = 1
        total_voters += 1
# print(poll_dict)

# Print out the results
# The total number of votes cast
print(f"Total voter records: {total_voters}")

# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
votes_to_beat = 0
for candidate in poll_dict:
    pct_votes = poll_dict[candidate] * 100 / total_voters
    print(f"{candidate:10}:  {pct_votes:8.3f}% ({poll_dict[candidate]} votes)")
    if poll_dict[candidate] > votes_to_beat:
        winner        = candidate
        votes_to_beat = poll_dict[candidate]

# The winner of the election based on popular vote.
print(f"WINNER       : {winner}")