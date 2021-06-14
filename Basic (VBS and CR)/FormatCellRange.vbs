'This script will format the given range (A1-B5) with a specific font size, color and fit

Set objExcel = CreateObject("Excel.Application") 'Launches excel
objExcel.Visible = True							 'Makes the newly launched excel window visible
objExcel.Workbooks.Add

objExcel.Cells(1, 1).Value = "Name"				 'Sets the fist column header to 'Name'
objExcel.Cells(1, 2).Value = "Value"			 'Sets the second column header to 'Value'
Set objRange = objExcel.Cells(1, 1).EntireRow    'Selecting the whole header row
objRange.Font.Bold = True			 			 'Setting the header fonts to be bold
objRange.Font.Size = 18							 'Setting header font size to 18
'Assigning data values to the first two columns 
objExcel.Cells(2, 1).Value = "First"
objExcel.Cells(3, 1).Value = "Second"
objExcel.Cells(4, 1).Value = "Third"
objExcel.Cells(5, 1).Value = "Fourth"
objExcel.Cells(2, 2).Value = "1"
objExcel.Cells(3, 2).Value = "2"
objExcel.Cells(4, 2).Value = "3"
objExcel.Cells(5, 2).Value = "4"

'Setting font size for whole range to be 14
Set objRange = objExcel.Range("A2","B5")
objRange.Font.Size = 14

'Setting background color to be purple
Set objRange = objExcel.Range("A2","B5")
objRange.Interior.ColorIndex = 39

'Autofitting the whole value column
Set objRange = objExcel.ActiveCell.EntireColumn
objRange.AutoFit()
