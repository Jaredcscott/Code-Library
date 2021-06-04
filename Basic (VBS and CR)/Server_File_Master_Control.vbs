Option Explicit 
Const DEST_FILE = "C:\<path>\<to>\<file>\<filename of local file>"  'Adjust the path here to point to the desired location of your output file. 
Dim objWSHShell, sLaunchFile,FSO 								 	'Declaring variables 														
Set FSO = CreateObject("Scripting.FileSystemObject") 				'Instantiating a File System Object 
FSO.CopyFile "C:\<path>\<filename of server copy>", DEST_FILE, True	'Alter this path to point to the server copy of the document you want to protect
Set objWSHShell = CreateObject("Wscript.Shell")						'Creating a shell to execute the copy command 
objWSHShell.run chr(34) & DEST_FILE & chr(34), 0, True				'Running the command within the shell created in the previous instruction 