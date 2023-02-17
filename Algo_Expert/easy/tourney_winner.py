def tournamentWinner(competitions, results):
    # Write your code here.
    score = {}
    for num in range(0, len(competitions)):
        if results[num] == 1:
            score[competitions[num][0]] = score.get(
                competitions[num][0], 0) + 3
            score[competitions[num][1]] = score.get(competitions[num][1], 0)
        else:
            score[competitions[num][0]] = score.get(competitions[num][0], 0)
            score[competitions[num][1]] = score.get(
                competitions[num][1], 0) + 3

    winning_team = max(score, key=score.get)
    return winning_team
