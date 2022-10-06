import pandas as pd
import pyrankvote
from pyrankvote import Ballot
from pyrankvote import Candidate

candidates = [Candidate(str(i)) for i in range(1, 10)]
candidate_map = dict(zip(range(1, 10), candidates))

votes = pd.read_csv("cultivatordao_cleaned.csv")

ballots = []
for _, vote in votes.iterrows():
    ballots += [
        Ballot(
            ranked_candidates=[
                candidate_map[candidate] for candidate in eval(vote["choice"])
            ]
        )
        for _ in range(int(vote["vp"]))
    ]

election_result = pyrankvote.single_transferable_vote(
    candidates, ballots, number_of_seats=5
)
print(election_result)
