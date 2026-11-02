import os

def replace_in_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"[{os.path.basename(path)}] Replaced: {old[:30]}... -> {new[:30]}...")
        else:
            print(f"[{os.path.basename(path)}] Skipping / not found: '{old[:30]}'")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

base = "C:/Users/mohit/deckcraft"

# 1. build.rs
replace_in_file(f"{base}/apps/deckcraft/build.rs", [
    ('.set("ProductName", "PowerPoint by rea-harjani")', '.set("ProductName", "PowerPoint by ArtCraft")'),
    ('.set("FileDescription", "PowerPoint by rea-harjani")', '.set("FileDescription", "PowerPoint by ArtCraft")'),
    ('.set("CompanyName", "rea-harjani")', '.set("CompanyName", "ArtCraft")'),
    ('.set("LegalCopyright", "Copyright (c) rea-harjani. All rights reserved.")', '.set("LegalCopyright", "Copyright (c) ArtCraft Team. MIT OR Apache-2.0.")'),
])

# 2. main.rs
replace_in_file(f"{base}/apps/deckcraft/src/main.rs", [
    ('.with_title("PowerPoint by rea-harjani")', '.with_title("PowerPoint by ArtCraft")'),
])

# 3. title_bar.rs
replace_in_file(f"{base}/crates/ui-egui/src/ribbon/title_bar.rs", [
    ('unwrap_or_else(|| "PowerPoint by rea-harjani".into())', 'unwrap_or_else(|| "PowerPoint by ArtCraft".into())'),
])

# 4. about.rs
replace_in_file(f"{base}/crates/ui-egui/src/dialogs/about.rs", [
    ('RichText::new("PowerPoint by rea-harjani")', 'RichText::new("PowerPoint by ArtCraft")'),
])

# 5. menus.rs
replace_in_file(f"{base}/crates/ui-egui/src/menus.rs", [
    ('About PowerPoint by rea-harjani', 'About PowerPoint by ArtCraft'),
])

# 6. info.rs
replace_in_file(f"{base}/crates/ui-egui/src/backstage/info.rs", [
    ('RichText::new("PowerPoint by rea-harjani")', 'RichText::new("PowerPoint by ArtCraft")'),
    ('"About PowerPoint by rea-harjani"', '"About PowerPoint by ArtCraft"'),
])

# 7. deckcraft.wxs
replace_in_file(f"{base}/packaging/windows/deckcraft.wxs", [
    ('Name="PowerPoint by rea-harjani" Manufacturer="rea-harjani"', 'Name="PowerPoint by ArtCraft" Manufacturer="ArtCraft"'),
    ('Description="PowerPoint by rea-harjani" Manufacturer="rea-harjani"', 'Description="PowerPoint by ArtCraft" Manufacturer="ArtCraft"'),
    ('Title="PowerPoint by rea-harjani"', 'Title="PowerPoint by ArtCraft"'),
])

# 8. README.md
replace_in_file(f"{base}/README.md", [
    ('# PowerPoint by rea-harjani', '# PowerPoint by ArtCraft'),
])

# 9. build-and-release.yml
replace_in_file(f"{base}/.github/workflows/build-and-release.yml", [
    ('PowerPoint-by-rea-harjani', 'PowerPoint-by-ArtCraft'),
])

print("SUCCESS: Code rebranded to 'PowerPoint by ArtCraft'!")
