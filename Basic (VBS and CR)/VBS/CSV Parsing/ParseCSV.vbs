'Create object that will be used to read a file
Set fso = CreateObject("Scripting.FileSystemObject")

'Open the file for reading text. This script is expecting a csv file with this format: 
'<name>,<age>,<Favorite color>
Set file = fso.OpenTextFile ("C:\Users\jscott\Desktop\Code-Library\Basic (VBS and CR)\VBS\CSV Parsing\inputFile.csv", 1)	'Adjust path here the 1 means for reading 

Dim outString 'This dim will be used to store the results

Do Until file.AtEndOfStream 
	'Read next line
	line = file.ReadLine
	'Split the line into an array
	arrValues = Split(line, ",")	
	outString = outString & "Name: " & arrValues(0) & " Age: " & arrValues(1) & " Favorite Color: " & arrValues(2) & vbcrlf
Loop

file.Close 			'Closing the file 
MsgBox  outString	'Printing the results to a message box window