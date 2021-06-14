'
' Capture the results of a command line execution and
' return them to the caller.
'
Function getCommandOutput(theCommand)

    Dim objShell, objCmdExec
    Set objShell = CreateObject("WScript.Shell")
    Set objCmdExec = objshell.exec(thecommand)
    getCommandOutput = objCmdExec.StdOut.ReadAll

end Function