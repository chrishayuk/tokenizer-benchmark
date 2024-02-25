10 PRINT "Welcome to the BASIC Demonstrator Program"
20 PRINT "Select an option:"
30 PRINT "1 - Addition"
40 PRINT "2 - Subtraction"
50 PRINT "3 - Multiplication"
60 PRINT "4 - Division"
70 PRINT "5 - Draw a Square"
80 PRINT "6 - Exit"
90 INPUT "Enter your choice (1-6): ", CHOICE

100 IF CHOICE = 1 THEN GOTO 200
110 IF CHOICE = 2 THEN GOTO 300
120 IF CHOICE = 3 THEN GOTO 400
130 IF CHOICE = 4 THEN GOTO 500
140 IF CHOICE = 5 THEN GOTO 600
150 IF CHOICE = 6 THEN GOTO 700

160 PRINT "Invalid choice, please select 1-6"
170 GOTO 20

' Addition
200 INPUT "Enter first number: ", A
210 INPUT "Enter second number: ", B
220 C = A + B
230 PRINT "Result: "; A; " + "; B; " = "; C
240 GOTO 20

' Subtraction
300 INPUT "Enter first number: ", A
310 INPUT "Enter second number: ", B
320 C = A - B
330 PRINT "Result: "; A; " - "; B; " = "; C
340 GOTO 20

' Multiplication
400 INPUT "Enter first number: ", A
410 INPUT "Enter second number: ", B
420 C = A * B
430 PRINT "Result: "; A; " * "; B; " = "; C
440 GOTO 20

' Division
500 INPUT "Enter first number: ", A
510 INPUT "Enter second number: ", B
520 IF B = 0 THEN PRINT "Cannot divide by zero": GOTO 500
530 C = A / B
540 PRINT "Result: "; A; " / "; B; " = "; C
550 GOTO 20

' Draw a Square
600 CLS ' Clear the screen
610 FOR I = 100 TO 200 STEP 10
620 LINE (I,100)-(I,200)
630 LINE (100,I)-(200,I)
640 NEXT I
650 PRINT "Press any key to return to menu"
660 GETKEY$ ' Wait for a key press
670 CLS ' Clear the screen
680 GOTO 20

' Exit
700 PRINT "Thank you for using the BASIC Demonstrator Program"
710 END