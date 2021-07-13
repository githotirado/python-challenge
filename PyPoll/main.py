import csv, pathlib

poll_csv_input = pathlib.Path('./Resources/election_data.csv')
poll_analysis_output = pathlib.Path('./analysis/poll_analysis.txt')
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

# Print out the results to screen and to output file
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
votes_to_beat = 0

with open(poll_analysis_output, "w") as output_txt:
    total_voter_records=f"\nTotal voter records: {total_voters}\n"
    print(total_voter_records)
    output_txt.write(total_voter_records + "\n")
    for candidate, total_votes in poll_dict.items():
        pct_votes = total_votes * 100 / total_voters
        candidate_counts=f"{candidate:10}:  {pct_votes:8.3f}% ({total_votes} votes)"
        print(candidate_counts)
        output_txt.write(candidate_counts + "\n")
        if total_votes > votes_to_beat:
            winner        = candidate
            votes_to_beat = total_votes

    # The winner of the election based on popular vote.
    winner=f"\nWINNER    : {winner}"
    print(winner)
    output_txt.write(winner)