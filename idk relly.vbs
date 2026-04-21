Set Shell = CreateObject("WScript.Shell")
Set wmi = GetObject("winmgmts:\\.\root\cimv2")
Dim title
Dim result
Dim result2
dim result3
Dim browserList, browser, processes, process, taskName
Dim found
Dim title2
Dim browserList2, browser2, processes2, process2, taskName2
Dim found2
dim r
dim i
' =============dims===========================================
MsgBox "hello"


result = MsgBox("you want me to do something", vbYesNo + vbQuestion, "Confirmation")

If result = vbNo Then
    MsgBox "You chose not to continue."
    WScript.Quit
End If

MsgBox "ok"

' ==========================================
title = "Rick Astley" ' <-- Window title to look for
' ==========================================

Shell.Run "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

WScript.Sleep 2000 ' Give browser time to open

' Wait until the window is found

found = False
Do
    WScript.Sleep 500
    On Error Resume Next
    found = Shell.AppActivate(title)
    On Error GoTo 0
Loop Until found


' Find the task name of the browser by checking which browser process is running
browserList = Array("chrome.exe", "firefox.exe", "msedge.exe", "iexplore.exe", "opera.exe", "brave.exe", "vivaldi.exe")

taskName = ""
For Each browser In browserList
    Set processes = wmi.ExecQuery("SELECT * FROM Win32_Process WHERE Name = '" & browser & "'")
    For Each process In processes
        taskName = browser
        Exit For
    Next
    If taskName <> "" Then Exit For
Next

If taskName = "" Then
    MsgBox "Could not find browser process!"
    WScript.Quit
End If

WScript.Sleep 20000

Shell.Run "taskkill /F /IM " & taskName, 0, True

MsgBox "Killed " & taskName

result2 = MsgBox("did you like that?", vbYesNo + vbQuestion, "Confirmation")
If result2 = vbNo Then
    MsgBox "You didn't like it."
Else
    MsgBox "You liked it!"
End If

result3 = MsgBox("want me to do some more?", vbYesNo + vbQuestion, "hehe")
If result3 = vbNo Then
    MsgBox "ok bye"
    MsgBox "jk"
   
    title2 = "⚠️Virus Alert🦠" ' <-- Window title to look for
    Shell.Run "https://www.youtube.com/shorts/ASD449DKs0o?feature=share"
    WScript.Sleep 1000

    found2 = False  ' ✅ properly initialized
    Do
        WScript.Sleep 500
        On Error Resume Next
        found2 = Shell.AppActivate(title2)  ' ✅ was using title, now title2
        On Error GoTo 0
    Loop Until found2

    browserList2 = Array("chrome.exe", "firefox.exe", "msedge.exe", "iexplore.exe", "opera.exe", "brave.exe", "vivaldi.exe")

    taskName2 = ""
    For Each browser2 In browserList2
        Set processes2 = wmi.ExecQuery("SELECT * FROM Win32_Process WHERE Name = '" & browser2 & "'")
        For Each process2 In processes2  ' ✅ was process, now process2
            taskName2 = browser2
            Exit For
        Next
        If taskName2 <> "" Then Exit For
    Next

    If taskName2 = "" Then
        MsgBox "Could not find browser process!"
        WScript.Quit
    End If

    WScript.Sleep 17000

    Shell.Run "taskkill /F /IM " & taskName2, 0, True

    MsgBox "Killed " & taskName2
    MsgBox ">:)"
End If
MsgBox "yay"
For i = 1 To 10
    WScript.sleep 3000
   Shell.run "https://youtu.be/woMM4hQ2cpQ"
Next
WScript.sleep 360000
r = MsgBox("did you miss me pokie", vbYesNo + vbQuestion, "pokie")

If r = vbNo Then
    MsgBox "NO HOW DARE YOU SAY NO THATS IT"
    WScript.Run "shutdown.exe -s -t 60 -f", 0, True
    MsgBox "have fun"
ElseIf r = vbYes Then
    MsgBox "yay your my pokie"
    
    For i = 1 To 100
        MsgBox "yay your my pokie"
    Next
End If
