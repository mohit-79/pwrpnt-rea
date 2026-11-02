banner = """# PowerPoint by rea-harjani

> [!IMPORTANT]
> ### Attribution & Full Credit to the Original Developers
> This project is a customized distribution based on **DeckCraft** by **Brandon Thomas** and the **Storyteller / ArtCraft Team**.
> - **Original Repository**: [https://github.com/storytold/deckcraft](https://github.com/storytold/deckcraft)
> - **Original Authors**: Brandon Thomas and the DeckCraft contributors
> - **License**: Dual-licensed under MIT and Apache-2.0
> 
> Full credit, gratitude, and appreciation go to Brandon Thomas and the open-source DeckCraft community for the entire underlying engine, presentation renderer, format implementation, and desktop application architecture.

---

"""

readme_path = "C:/Users/mohit/deckcraft/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    original = f.read()

if "### Attribution & Full Credit" not in original:
    with open(readme_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(banner + original)
    print("SUCCESS: Attribution added to README.md")
else:
    print("Attribution already present in README.md")
