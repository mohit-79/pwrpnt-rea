$appDir = "$env:LOCALAPPDATA\Programs\ArtCraft\DeckCraft"
$icoPath = "$appDir\powerpoint.ico"
$targetExe = "$appDir\deckcraft.exe"

$w = New-Object -ComObject WScript.Shell

# 1. Start Menu Shortcut
$startMenuPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs"
$oldStartLnk = "$startMenuPath\DeckCraft.lnk"
$newStartLnk = "$startMenuPath\PowerPoint.lnk"

if (Test-Path $oldStartLnk) {
    Remove-Item -Path $oldStartLnk -Force -ErrorAction SilentlyContinue
}

$sc = $w.CreateShortcut($newStartLnk)
$sc.TargetPath = $targetExe
$sc.IconLocation = "$icoPath,0"
$sc.Description = "Microsoft PowerPoint"
$sc.WorkingDirectory = $appDir
$sc.Save()
Write-Host "Updated Start Menu shortcut: $newStartLnk"

# 2. Desktop Shortcut
$desktopPath = [System.Environment]::GetFolderPath('Desktop')
$oldDeskLnk = "$desktopPath\DeckCraft.lnk"
$newDeskLnk = "$desktopPath\PowerPoint.lnk"

if (Test-Path $oldDeskLnk) {
    Remove-Item -Path $oldDeskLnk -Force -ErrorAction SilentlyContinue
}

$scDesk = $w.CreateShortcut($newDeskLnk)
$scDesk.TargetPath = $targetExe
$scDesk.IconLocation = "$icoPath,0"
$scDesk.Description = "Microsoft PowerPoint"
$scDesk.WorkingDirectory = $appDir
$scDesk.Save()
Write-Host "Created Desktop shortcut: $newDeskLnk"

# 3. Refresh Windows icon cache notification
[void][System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
Write-Host "SUCCESS: Shortcuts renamed to PowerPoint with official PowerPoint icon!"
