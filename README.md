Assumptions
---------------
- User input is not constrained to be uppercase
- User input is can include whitespace; my app removes and whitespace and capitalises instruction before proceeding to next steps
- Wherever user provides invalid instruction, my app ignores it
- Board is considered to be square and dimension is set to 5 but this is configurable in config file


Improvements
-----------------
- fuzzy matching commands - we could provide user with suggestion if they are "close" to correct command eg. someone enters "MOEV", we could suggest "Did you mean MOVE?"
- Could separate static validate methods in command handler to CommandValidator class. In this case, it is small simple method, hence manageable
-