"""
The scared-of-risk agent.

It chooses to always bluff if it is impossible to bet something that it does not possess itself. meaning:
If it has dices:
2x Four
3x Five
it will only bet 2x Four or 3x Five at MAXIMUM, otherwise it will call bluff.
"""