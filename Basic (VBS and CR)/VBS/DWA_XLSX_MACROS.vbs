Sub Clear3Rows()
' This Macro will clear the current row, along with the next three rows in the selected column.
' Useful for 15 Sec polling intervals
    Selection.ClearContents
    ActiveCell.Offset(1).Select
    Selection.ClearContents
    ActiveCell.Offset(1).Select
    Selection.ClearContents
    ActiveCell.Offset(1).Select
    ActiveCell.Offset(1).Select
End Sub
