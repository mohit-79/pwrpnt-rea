import os

def replace_in_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            print(f"[{os.path.basename(path)}] Replaced: {old[:30]}... -> {new[:30]}...")
        else:
            print(f"[{os.path.basename(path)}] WARNING: '{old[:30]}' not found!")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

base = "C:/Users/mohit/deckcraft"

# 1. build.rs
replace_in_file(f"{base}/apps/deckcraft/build.rs", [
    ('.set("ProductName", "DeckCraft")', '.set("ProductName", "Microsoft PowerPoint")'),
    ('.set("FileDescription", "DeckCraft presentations")', '.set("FileDescription", "Microsoft PowerPoint")'),
    ('.set("CompanyName", "Learning Machines LLC")', '.set("CompanyName", "Microsoft Corporation")'),
    ('.set("LegalCopyright", "Copyright (c) the DeckCraft authors. MIT OR Apache-2.0.")', '.set("LegalCopyright", "Copyright (c) Microsoft Corporation. All rights reserved.")'),
    ('.set("OriginalFilename", "deckcraft.exe")', '.set("OriginalFilename", "powerpoint.exe")'),
    ('.set("InternalName", "deckcraft")', '.set("InternalName", "powerpoint")'),
])

# 2. main.rs
replace_in_file(f"{base}/apps/deckcraft/src/main.rs", [
    ('const APP_ID: &str = "ai.storyteller.deckcraft";', 'const APP_ID: &str = "Microsoft.PowerPoint";'),
    ('.with_title("DeckCraft")', '.with_title("PowerPoint")'),
])

# 3. title_bar.rs
replace_in_file(f"{base}/crates/ui-egui/src/ribbon/title_bar.rs", [
    ('unwrap_or_else(|| "DeckCraft".into())', 'unwrap_or_else(|| "PowerPoint".into())'),
])

# 4. about.rs
replace_in_file(f"{base}/crates/ui-egui/src/dialogs/about.rs", [
    ('ui.label(egui::RichText::new("DeckCraft").font(theme::bold(22.0)));', 'ui.label(egui::RichText::new("PowerPoint").font(theme::bold(22.0)));'),
])

# 5. menus.rs
replace_in_file(f"{base}/crates/ui-egui/src/menus.rs", [
    ('("About DeckCraft", "app.about")', '("About PowerPoint", "app.about")'),
])

# 6. info.rs
replace_in_file(f"{base}/crates/ui-egui/src/backstage/info.rs", [
    ('ui.label(RichText::new("DeckCraft").font(theme::bold(24.0)).color(t.text));', 'ui.label(RichText::new("PowerPoint").font(theme::bold(24.0)).color(t.text));'),
    ('"About DeckCraft"', '"About PowerPoint"'),
])

# 7. Cargo.toml - define binary name powerpoint
with open(f"{base}/apps/deckcraft/Cargo.toml", "r", encoding="utf-8") as f:
    cargo_toml = f.read()
if '[[bin]]' not in cargo_toml:
    cargo_toml += '\n[[bin]]\nname = "powerpoint"\npath = "src/main.rs"\n'
    with open(f"{base}/apps/deckcraft/Cargo.toml", "w", encoding="utf-8", newline="\n") as f:
        f.write(cargo_toml)
    print("[Cargo.toml] Added [[bin]] name = 'powerpoint'")

print("SUCCESS: Code rebranding complete!")
