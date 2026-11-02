import os
from PIL import Image

raw_path = "C:/Users/mohit/deckcraft/powerpoint_raw.png"
ico_path = "C:/Users/mohit/deckcraft/powerpoint.ico"
target_ico = "C:/Users/mohit/deckcraft/assets/app-icon/deckcraft.ico"
target_1024 = "C:/Users/mohit/deckcraft/assets/app-icon/deckcraft-1024.png"

print("Loading downloaded PowerPoint icon...")
img = Image.open(raw_path).convert("RGBA")
img.save(target_1024, "PNG")

print("Generating multi-resolution .ico...")
ico_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
img.save(ico_path, format="ICO", sizes=ico_sizes)
img.save(target_ico, format="ICO", sizes=ico_sizes)

print("Generating hicolor PNG sizes...")
sizes = [16, 24, 32, 48, 64, 128, 256, 512]
for s in sizes:
    resized = img.resize((s, s), Image.Resampling.LANCZOS)
    dest = f"C:/Users/mohit/deckcraft/assets/app-icon/hicolor/{s}x{s}/apps/ai.storyteller.deckcraft.png"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    resized.save(dest, "PNG")

print("SUCCESS: All PowerPoint icons generated successfully!")
