Sub FillInTestData()
    Dim InLine As String
    Dim Line As String
    Dim FSO As New FileSystemObject
    Dim TSO As Object
    Dim StrLineElements As Variant
    Dim DataVals As Variant
    Dim Rows As String
    Dim Row As Long
    Dim Col As Long
    Dim i As Long
    Dim Comma As String
    Comma = ","
    Dim Colon As String
    Colon = ":"
    Dim cType As String
    Dim Data As String
    Dim Msg As String
    Set FSO = CreateObject("Scripting.FileSystemObject")
    Set TSO = FSO.OpenTextFile("C:\Users\jscott\Desktop\Campbell_Aero_NOAA\outData.dat")
    Row = 1
    Do While TSO.AtEndOfStream = False
       InLine = TSO.ReadLine
       StrLineElements = Split(InLine, Colon)
       cType = StrLineElements(0)
       Data = StrLineElements(1)
       If cType = "Var" Then
        DataVals = Split(Data, Comma)
        Col = Range(DataVals(1) & 1).Column
        Row = CLng(DataVals(0))
        Cells(Row, Col).Value = DataVals(2)
        Cells(Row, Col + 1).Value = DataVals(3)
       Row = Row + 1
       ElseIf cType = "DEBUG" Then
        DataVals = Split(Data, Comma)
        Row = CLng(Right(DataVals(0), Len(DataVals(0)) - 1))
        Col = Range("U" & 1).Column
        Msg = DataVals(1)
        Msg = Right(Msg, Len(Msg) - 1)
        Msg = Left(Msg, Len(Msg) - 1)
        Cells(Row, Col).Value = Msg
       End If
    Loop
TSO.Close
End Sub
