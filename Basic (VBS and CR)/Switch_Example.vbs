Sub Generate_Path    
	'This switch statement converts the current month and year into a file path for the corresponding file location. 
    pathString = ""
    monthString = Month(Now)
    yearString = Year(Now)
    Select Case monthString
        Case 1
            pathString = (pathString & ("0" & monthString)) & ("-January " & yearString)
        Case 2
            pathString = (pathString & ("0" & monthString)) & ("-February " & yearString)
        Case 3
            pathString = (pathString & ("0" & monthString)) & ("-March " & yearString)
        Case 4
            pathString = (pathString & ("0" & monthString)) & ("-April " & yearString)
        Case 5
            pathString = (pathString & ("0" & monthString)) & ("-May " & yearString)
        Case 6
            pathString = (pathString & ("0" & monthString)) & ("-June " & yearString)
        Case 7
            pathString = (pathString & ("0" & monthString)) & ("-July " & yearString)
        Case 8
            pathString = (pathString & ("0" & monthString)) & ("-August " & yearString)
        Case 9
            pathString = (pathString & ("0" & monthString)) & ("-September " & yearString)
        Case 10
            pathString = (pathString & monthString) & ("-October " & yearString)
        Case 11
            pathString = (pathString & monthString) & ("-November " & yearString)
        Case 12
            pathString = (pathString & monthString) & ("-December " & yearString)
    End Select

    'Adding the server path to the determined Checkbook location.
	pathString = (("\\<path>\<to>\<file>\" & yearString) & ("\" & pathString)) & ".<file extension>"
EndSub
