"""Minimal test: do Treeview images show on Windows?"""
import tkinter as tk
from tkinter import ttk
import os, sys

root = tk.Tk()
root.title("Treeview Icon Debug")
root.geometry("700x500")
root.configure(bg="#1a1a2e")

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", background="#16162a", foreground="#e0e0e0",
                fieldbackground="#16162a", font=("Consolas", 10), rowheight=22, borderwidth=0)

# Load icons same way as the app
_ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
_icon_cache = {}

def load_icon(path, size=16):
    cache_key = f"{path}_{size}"
    if cache_key in _icon_cache:
        return _icon_cache[cache_key]
    if not os.path.exists(path):
        print(f"  NOT FOUND: {path}")
        return None
    try:
        try:
            from PIL import Image, ImageTk
            img = Image.open(path).convert("RGBA")
            img = img.resize((size, size), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            print(f"  PIL loaded: {path} -> {photo}")
        except ImportError:
            photo = tk.PhotoImage(file=path)
            w, h = photo.width(), photo.height()
            if w > size or h > size:
                fx = max(1, w // size)
                fy = max(1, h // size)
                photo = photo.subsample(fx, fy)
            print(f"  tk.PhotoImage loaded: {path} -> {photo}")
        _icon_cache[cache_key] = photo
        return photo
    except Exception as e:
        print(f"  FAILED: {path}: {e}")
        return None

grade_icons = {}
for g in range(1, 6):
    path = os.path.join(_ASSETS_DIR, f"grade-{g}.png")
    print(f"Grade {g}:")
    icon = load_icon(path, 16)
    grade_icons[g] = icon
    print(f"  Result: {icon}")

# ── TEST 1: Flat tree (no nesting) with image= on insert ──
print("\n=== TEST 1: Flat tree ===")
tree1 = ttk.Treeview(root, columns=("info",), show="tree headings", selectmode="none", height=5)
tree1.heading("#0", text="Material", anchor=tk.W)
tree1.heading("info", text="Grade", anchor=tk.W)
tree1.column("#0", width=300)
tree1.column("info", width=200)
tree1.pack(fill=tk.X, padx=10, pady=(10, 5))

items = [("Sulphur", 298, 1), ("Iron", 183, 1), ("Tungsten", 30, 4), ("Antimony", 5, 5)]
for name, qty, grade in items:
    icon = grade_icons.get(grade)
    tree1.insert("", tk.END, text=f"{qty:>5}  {name}",
                 values=(f"{'●'*grade}",), image=icon if icon else "")

# ── TEST 2: Nested tree (parent + children) with image= on insert ──
print("\n=== TEST 2: Nested tree ===")
tree2 = ttk.Treeview(root, columns=("info",), show="tree headings", selectmode="none", height=8)
tree2.heading("#0", text="Material", anchor=tk.W)
tree2.heading("info", text="Grade", anchor=tk.W)
tree2.column("#0", width=300)
tree2.column("info", width=200)
tree2.pack(fill=tk.X, padx=10, pady=5)

cat = tree2.insert("", tk.END, text="RAW  (500)", values=("",), tags=("cat",), open=True)
for name, qty, grade in items:
    icon = grade_icons.get(grade)
    tree2.insert(cat, tk.END, text=f"{qty:>5}  {name}",
                 values=(f"{'●'*grade}",), image=icon if icon else "")

# ── TEST 3: Nested tree with tag_configure image ──
print("\n=== TEST 3: Nested tree + tag_configure image ===")
tree3 = ttk.Treeview(root, columns=("info",), show="tree headings", selectmode="none", height=8)
tree3.heading("#0", text="Material", anchor=tk.W)
tree3.heading("info", text="Grade", anchor=tk.W)
tree3.column("#0", width=300)
tree3.column("info", width=200)
tree3.pack(fill=tk.X, padx=10, pady=5)

for g in range(1, 6):
    if grade_icons.get(g):
        tree3.tag_configure(f"grade_{g}", image=grade_icons[g])

cat3 = tree3.insert("", tk.END, text="RAW  (500)", values=("",), tags=("cat",), open=True)
for name, qty, grade in items:
    tree3.insert(cat3, tk.END, text=f"{qty:>5}  {name}",
                 values=(f"{'●'*grade}",), tags=(f"grade_{grade}",))

# Labels to identify tests
tk.Label(root, text="Test 1: Flat (image=)", fg="#ff7100", bg="#1a1a2e", font=("Consolas", 10)).pack(anchor=tk.W, padx=10)
tk.Label(root, text="Test 2: Nested (image=)", fg="#ff7100", bg="#1a1a2e", font=("Consolas", 10)).pack(anchor=tk.W, padx=10)
tk.Label(root, text="Test 3: Nested (tag_configure image)", fg="#ff7100", bg="#1a1a2e", font=("Consolas", 10)).pack(anchor=tk.W, padx=10)

root.mainloop()
