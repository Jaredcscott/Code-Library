::An example batch script which can be used to run various automated processes 
@echo off
:: Starting the server with the role of Primary  
cd C:\Program Files (x86)\SmartBear\TestExecute 14\x64\Bin
:: This is where Test Execute would start
start .\TestExecute.exe "C:\Users\jscott\Desktop\Test_Complete_Projects\Campbell_Aero\Campbell_Aero_Test_Suite.pjs" /r /p:Test_Automation_Demo /ExportLogToXMLAlso /ExportSummary:"C:\Users\jscott\Desktop\CA_ATS_LISTENER\junit.xml"
timeout 1