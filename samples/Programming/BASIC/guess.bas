10 PRINT "Guess the Number Game"
20 PRINT "I'm thinking of a number between 1 and 100."

30 RANDOMIZE TIMER
40 SECRET = INT(RND * 100) + 1

50 PRINT "Enter your guess:"
60 INPUT GUESS

70 IF GUESS < SECRET THEN PRINT "Too low, try again.": GOTO 50
80 IF GUESS > SECRET THEN PRINT "Too high, try again.": GOTO 50
90 IF GUESS = SECRET THEN PRINT "Congratulations! You guessed it!": END

100 PRINT "Do you want to play again (Y/N)?"
110 INPUT ANSWER$
120 IF UPPER$(ANSWER$) = "Y" THEN GOTO 20
130 PRINT "Thank you for playing!"
140 END