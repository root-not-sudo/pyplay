def electionsWinners(votes, k):

    current_leader = max(votes)
    possible_winners = 0
    num_current_leaders = 0
    for i in votes:
        if i == current_leader:
            num_current_leaders += 1
        if i + k > current_leader:
            possible_winners += 1
    if num_current_leaders == 1 and possible_winners == 0:
        return 1
    return possible_winners
