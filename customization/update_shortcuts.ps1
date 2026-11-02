$appDir = "$env:LOCALAPPDATA\Programs\ArtCraft\DeckCraft"
$icoPath = "$appDir\powerpoint.ico"
$targetExe = "$appDir\deckcraft.exe"

$w = New-Object -ComObject WScript.Shell

# 1. Start Menu Shortcut
$startMenuPath = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs"
Remove-Item -Path "$startMenuPath\PowerPoint*.lnk", "$startMenuPath\DeckCraft.lnk" -Force -ErrorAction SilentlyContinue

$newStartLnk = "$startMenuPath\PowerPoint by ArtCraft.lnk"
$sc = $w.CreateShortcut($newStartLnk)
$sc.TargetPath = $targetExe
$sc.IconLocation = "$icoPath,0"
$sc.Description = "PowerPoint by ArtCraft"
$sc.WorkingDirectory = $appDir
$sc.Save()
Write-Host "Updated Start Menu shortcut: $newStartLnk"

# 2. Desktop Shortcut
$desktopPath = [System.Environment]::GetFolderPath('Desktop')
Remove-Item -Path "$desktopPath\PowerPoint*.lnk", "$desktopPath\DeckCraft.lnk" -Force -ErrorAction SilentlyContinue

$newDeskLnk = "$desktopPath\PowerPoint by ArtCraft.lnk"
$scDesk = $w.CreateShortcut($newDeskLnk)
$scDesk.TargetPath = $targetExe
$scDesk.IconLocation = "$icoPath,0"
$scDesk.Description = "PowerPoint by ArtCraft"
$scDesk.WorkingDirectory = $appDir
$scDesk.Save()
Write-Host "Created Desktop shortcut: $newDeskLnk"

Write-Host "SUCCESS: Shortcuts renamed to 'PowerPoint by ArtCraft' with official PowerPoint icon!"
