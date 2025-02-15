# Color_Schemes_GUI.py

import tkinter as tk
import json
from typing import Dict, List


def main() -> None:
    root: tk.Tk = tk.Tk()
    with open("myCode/color_schemes.json", "r") as f:
        data: Dict[str, List[Dict[str, str | Dict[str, str]]]] = json.load(f)

    frames: List[tk.Frame] = []

    for i, scheme in enumerate(data["schemes"]):
        name: str = scheme["name"]
        colors: Dict[str, str] = scheme["colors"]

        frames.append(tk.Frame(root, width=300, height=200, bg="#F0F0F0"))
        label: tk.Label = tk.Label(frames[i], text=name)
        label.grid(row=0, column=0)

        color1: tk.Label = tk.Label(frames[i], text=colors["light"], bg=colors["light"], fg=colors["dark"], padx=10, pady=10)
        color1.grid(row=1, column=0, padx=10, pady=10)

        color2: tk.Label = tk.Label(frames[i], text=colors["medium"], bg=colors["medium"], fg=colors["light"], padx=10, pady=10)
        color2.grid(row=1, column=1, padx=10, pady=10)

        color3: tk.Label = tk.Label(frames[i], text=colors["dark"], bg=colors["dark"], fg=colors["light"], padx=10, pady=10)
        color3.grid(row=1, column=2, padx=10, pady=10)

        print(name)
        print(colors["light"])
        print(colors["medium"])
        print(colors["dark"])

    for i, frame in enumerate(frames):
        frame.grid(row=i, column=0, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()