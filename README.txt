**Brief**

Your task is to simulate your guild's bank account supporting opening/closing, withdrawals, and deposits of gold. Watch out for concurrent transactions!

In most MMORPGs (Massively Multiplayer Online Role-Playing Game), a player can interact with other players by creating a guild.

Depending on the game, a guild can have various activities, which can be costly. To make it easier to handle this cost, guilds create guild banks.

A guild bank can be accessed in multiple ways. Players can make deposits and withdrawals, and game systems can get money from the guild too. Note: make sure the guild bank can be accessed from multiple threads/processes.

It should be possible to disband the guild. This will cause the guild bank to close; operations against a closed guild bank must fail.

**Exception messages**

For some tests, it might be necessary to raise an exception. When you do this, include a meaningful error message to indicate what the source of the error is.

To raise a message with an exception, just write it as an argument to the exception type. For example, instead of raise Exception, you should write:

raise Exception("Include a meaningful message here")

**Running the tests**

Please use Python 3.7 for this assignment.

To run the tests, run pytest guild_bank_test.py

Alternatively, you can tell Python to run the pytest module: python -m pytest guild_bank_test.py

**Common pytest options**
- -v : enable verbose output
- -x : stop running tests on first failure
- --ff : run failures from previous test before running other test cases
For other options, see python -m pytest -h

**Evaluation Criteria**
- Python best practices
- Show us your work through your commit history
- did you complete the features? Are all the tests running?
- Correctness: does the functionality act in sensible, thought-out ways?
- Maintainability: is it written in a clean, maintainable way?


All the best and happy coding,

The DFIC Quant Group Team