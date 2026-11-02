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
    ('.set("ProductName", "Microsoft PowerPoint")', '.set("ProductName", "PowerPoint by rea-harjani")'),
    ('.set("ProductName", "DeckCraft")', '.set("ProductName", "PowerPoint by rea-harjani")'),
    ('.set("FileDescription", "Microsoft PowerPoint")', '.set("FileDescription", "PowerPoint by rea-harjani")'),
    ('.set("FileDescription", "DeckCraft presentations")', '.set("FileDescription", "PowerPoint by rea-harjani")'),
    ('.set("CompanyName", "Microsoft Corporation")', '.set("CompanyName", "rea-harjani")'),
    ('.set("CompanyName", "Learning Machines LLC")', '.set("CompanyName", "rea-harjani")'),
    ('.set("LegalCopyright", "Copyright (c) Microsoft Corporation. All rights reserved.")', '.set("LegalCopyright", "Copyright (c) rea-harjani. All rights reserved.")'),
    ('.set("LegalCopyright", "Copyright (c) the DeckCraft authors. MIT OR Apache-2.0.")', '.set("LegalCopyright", "Copyright (c) rea-harjani. All rights reserved.")'),
    ('.set("OriginalFilename", "deckcraft.exe")', '.set("OriginalFilename", "powerpoint.exe")'),
    ('.set("InternalName", "deckcraft")', '.set("InternalName", "powerpoint")'),
])

# 2. main.rs
replace_in_file(f"{base}/apps/deckcraft/src/main.rs", [
    ('.with_title("PowerPoint")', '.with_title("PowerPoint by rea-harjani")'),
    ('.with_title("DeckCraft")', '.with_title("PowerPoint by rea-harjani")'),
])

# 3. title_bar.rs
replace_in_file(f"{base}/crates/ui-egui/src/ribbon/title_bar.rs", [
    ('unwrap_or_else(|| "PowerPoint".into())', 'unwrap_or_else(|| "PowerPoint by rea-harjani".into())'),
    ('unwrap_or_else(|| "DeckCraft".into())', 'unwrap_or_else(|| "PowerPoint by rea-harjani".into())'),
])

# 4. about.rs
replace_in_file(f"{base}/crates/ui-egui/src/dialogs/about.rs", [
    ('RichText::new("PowerPoint")', 'RichText::new("PowerPoint by rea-harjani")'),
    ('RichText::new("DeckCraft")', 'RichText::new("PowerPoint by rea-harjani")'),
])

# 5. menus.rs
replace_in_file(f"{base}/crates/ui-egui/src/menus.rs", [
    ('About PowerPoint', 'About PowerPoint by rea-harjani'),
    ('About DeckCraft', 'About PowerPoint by rea-harjani'),
])

# 6. info.rs
replace_in_file(f"{base}/crates/ui-egui/src/backstage/info.rs", [
    ('RichText::new("PowerPoint")', 'RichText::new("PowerPoint by rea-harjani")'),
    ('RichText::new("DeckCraft")', 'RichText::new("PowerPoint by rea-harjani")'),
    ('"About PowerPoint"', '"About PowerPoint by rea-harjani"'),
    ('"About DeckCraft"', '"About PowerPoint by rea-harjani"'),
])

print("SUCCESS: Code rebranding to 'PowerPoint by rea-harjani' complete!")
