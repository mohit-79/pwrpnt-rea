wxs_path = "C:/Users/mohit/deckcraft/packaging/windows/deckcraft.wxs"
with open(wxs_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('Name="DeckCraft" Manufacturer="Learning Machines LLC"', 'Name="PowerPoint by rea-harjani" Manufacturer="rea-harjani"')
content = content.replace('Description="DeckCraft presentations and slide shows" Manufacturer="Learning Machines LLC"', 'Description="PowerPoint by rea-harjani" Manufacturer="rea-harjani"')
content = content.replace('Title="DeckCraft"', 'Title="PowerPoint by rea-harjani"')

with open(wxs_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)
print("Updated deckcraft.wxs branding successfully")
