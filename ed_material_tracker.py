#!/usr/bin/env python3
"""
ED Material Tracker — Elite Dangerous Engineering Material Monitor
Polls journal files every 5 minutes and displays material stock in a dark E:D-themed GUI.
Applies MaterialTrade/MaterialCollected/MaterialDiscarded deltas on top of the last
Materials snapshot so the display stays current between game loads.
"""

import json
import os
import sys
import glob
import tkinter as tk
from tkinter import ttk, filedialog
from datetime import datetime


# ── Theme ───────────────────────────────────────────────────────────────────

COLORS = {
    "bg":          "#0d0d0d",
    "bg_light":    "#1a1a1a",
    "bg_panel":    "#141414",
    "orange":      "#ff7100",
    "orange_dim":  "#cc5a00",
    "text":        "#e0e0e0",
    "text_dim":    "#888888",
    "text_bright": "#ffffff",
}

FONT       = ("Consolas", 10)
FONT_BOLD  = ("Consolas", 10, "bold")
FONT_TITLE = ("Consolas", 14, "bold")
FONT_CAT   = ("Consolas", 11, "bold")
FONT_HEAD  = ("Consolas", 9, "bold")

__VERSION__ = "1.2.0"

_DEBUG_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "debug.log")
try:
    open(_DEBUG_LOG, "w").close()
except OSError:
    pass

def _dbg(msg: str):
    try:
        with open(_DEBUG_LOG, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except OSError:
        pass


# ── Material Names ──────────────────────────────────────────────────────────
# ALL keys are lowercased with spaces AND underscores stripped.
# The pretty_name function normalizes the same way before lookup.

# ── Material Grades & Max Capacities ─────────────────────────────────────────
# Grade 1 (Very Common): 300 | G2 (Common): 250 | G3 (Standard): 200
# G4 (Rare): 150 | G5 (Very Rare): 100
# Raw materials only have 4 grades (max 150).

def _max_cap(grade: int, category: str) -> int:
    """Return max storage capacity for a material grade."""
    if category == "Raw":
        return {1: 300, 2: 250, 3: 200, 4: 150}.get(grade, 300)
    return {1: 300, 2: 250, 3: 200, 4: 150, 5: 100}.get(grade, 300)

# key = normalized name (lowercase, no spaces/underscores), value = (display_name, grade)
MATERIAL_DATA: dict[str, tuple[str, int, str]] = {
    # ── Raw (4 grades, max 150 at G4) ──
    "carbon":    ("Carbon", 1, "Raw"),    "iron":      ("Iron", 1, "Raw"),
    "nickel":    ("Nickel", 1, "Raw"),    "phosphorus": ("Phosphorus", 1, "Raw"),
    "sulphur":   ("Sulphur", 1, "Raw"),   "lead":      ("Lead", 1, "Raw"),
    "rhenium":   ("Rhenium", 2, "Raw"),   "chromium":  ("Chromium", 2, "Raw"),
    "manganese": ("Manganese", 2, "Raw"), "zinc":      ("Zinc", 2, "Raw"),
    "germanium": ("Germanium", 2, "Raw"), "vanadium":  ("Vanadium", 2, "Raw"),
    "selenium":  ("Selenium", 3, "Raw"),  "cadmium":   ("Cadmium", 3, "Raw"),
    "molybdenum":("Molybdenum",3, "Raw"), "ruthenium": ("Ruthenium", 3, "Raw"),
    "tin":       ("Tin", 3, "Raw"),       "tungsten":  ("Tungsten", 3, "Raw"),
    "mercury":   ("Mercury", 3, "Raw"),   "niobium":   ("Niobium", 3, "Raw"),
    "zirconium": ("Zirconium", 3, "Raw"), "boron":     ("Boron", 3, "Raw"),
    "tellurium": ("Tellurium", 4, "Raw"), "arsenic":   ("Arsenic", 4, "Raw"),
    "antimony":  ("Antimony", 4, "Raw"),  "polonium":  ("Polonium", 4, "Raw"),
    "yttrium":   ("Yttrium", 4, "Raw"),   "technetium":("Technetium", 4, "Raw"),

    # ── Encoded (5 grades) ──
    "disruptedwakeechoes":    ("Atypical Disrupted Wake Echoes", 1, "Encoded"),
    "fsdtelemetry":           ("Anomalous FSD Telemetry", 2, "Encoded"),
    "wakesolutions":          ("Strange Wake Solutions", 3, "Encoded"),
    "hyperspacetrajectories": ("Eccentric Hyperspace Trajectories", 4, "Encoded"),
    "dataminedwake":          ("Datamined Wake Exceptions", 5, "Encoded"),
    "shieldcyclerecordings":  ("Distorted Shield Cycle Recordings", 1, "Encoded"),
    "shieldpatternanalysis":  ("Aberrant Shield Pattern Analysis", 2, "Encoded"),
    "shielddensityreports":   ("Unexpected Shield Data", 3, "Encoded"),
    "shieldsoakanalysis":     ("Inconsistent Shield Soak Analysis", 4, "Encoded"),
    "shieldfrequencydata":    ("Decoded Shield Data", 5, "Encoded"),
    "modifiedconsumerfirmware": ("Modified Consumer Firmware", 1, "Encoded"),
    "compactscandata":         ("Compact Scan Data", 2, "Encoded"),
    "bulkscandata":            ("Anomalous Bulk Scan Data", 3, "Encoded"),
    "scandatabanks":           ("Classified Scan Databanks", 4, "Encoded"),
    "encodedscandata":         ("Detailed Scan Data", 5, "Encoded"),
    "scanarchives":            ("Classified Scan Fragment", 5, "Encoded"),
    "divergentscandata":       ("Divergent Scan Data", 3, "Encoded"),
    "legacyfirmware":           ("Legacy Firmware", 1, "Encoded"),
    "specialisedlegacyfirmware": ("Specialised Legacy Firmware", 2, "Encoded"),
    "scrambledemissiondata":   ("Exceptional Scrambled Emission Data", 1, "Encoded"),
    "archivedemissiondata":    ("Irregular Emission Data", 2, "Encoded"),
    "emissiondata":            ("Unexpected Emission Data", 3, "Encoded"),
    "decodedemissiondata":     ("Decoded Emission Data", 4, "Encoded"),
    "compactemissionsdata":    ("Abnormal Compact Emissions Data", 5, "Encoded"),
    "securityfirmware":        ("Security Firmware Patch", 5, "Encoded"),
    "taggedencryptioncodes":   ("Tagged Encryption Codes", 3, "Encoded"),
    "unusualencryptedfiles":   ("Unusual Encrypted Files", 4, "Encoded"),
    "crackedindustrialfirmware": ("Cracked Industrial Firmware", 3, "Encoded"),
    "modifiedembeddedfirmware":  ("Modified Embedded Firmware", 5, "Encoded"),
    "consumerfirmware":          ("Consumer Firmware", 2, "Encoded"),
    "industrialfirmware":        ("Industrial Firmware", 3, "Encoded"),
    "embeddedfirmware":          ("Embedded Firmware", 4, "Encoded"),
    "adaptiveencryptors":        ("Adaptive Encryptors Capture", 5, "Encoded"),
    "encryptionarchives":        ("Tagged Encryption Codes", 3, "Encoded"),
    "ancienthistoricaldata":    ("Guardian Historical Data", 3, "Encoded"),
    "ancientbiologicaldata":    ("Guardian Biological Data", 3, "Encoded"),
    "ancienttechnologicaldata": ("Guardian Technological Data", 3, "Encoded"),
    "ancientlanguagedata":      ("Guardian Language Data", 3, "Encoded"),
    "ancientculturaldata":      ("Guardian Cultural Data", 3, "Encoded"),
    "guardianmoduleblueprintfragment": ("Guardian Module Blueprint Fragment", 5, "Encoded"),
    "guardianvesselblueprintfragment": ("Guardian Vessel Blueprint Fragment", 5, "Encoded"),
    "symmetrickeys":               ("Open Symmetric Keys", 3, "Encoded"),
    "encryptedfiles":              ("Unusual Encrypted Files", 4, "Encoded"),
    "encryptioncodes":             ("Tagged Encryption Codes", 3, "Encoded"),
    "classifiedscandata":          ("Classified Scan Fragment", 5, "Encoded"),

    # ── Manufactured (5 grades) ──
    "chemicalstorageunits":    ("Chemical Storage Units", 1, "Manufactured"),
    "chemicalprocessors":      ("Chemical Processors", 2, "Manufactured"),
    "chemicaldistillery":      ("Chemical Distillery", 3, "Manufactured"),
    "chemicalmanipulators":    ("Chemical Manipulators", 4, "Manufactured"),
    "chemicalworkshop":        ("Chemical Workshop", 4, "Manufactured"),
    "heatconductionwiring":    ("Heat Conduction Wiring", 1, "Manufactured"),
    "heatdispersionplate":     ("Heat Dispersion Plate", 2, "Manufactured"),
    "heatexchangers":          ("Heat Exchangers", 3, "Manufactured"),
    "heatvanes":               ("Heat Vanes", 4, "Manufactured"),
    "protoheatradiators":      ("Proto Heat Radiators", 5, "Manufactured"),
    "temperedalloys":          ("Tempered Alloys", 1, "Manufactured"),
    "precipitatedalloys":      ("Precipitated Alloys", 2, "Manufactured"),
    "salvagedalloys":          ("Salvaged Alloys", 3, "Manufactured"),
    "galvanisingalloys":       ("Galvanising Alloys", 4, "Manufactured"),
    "phasealloys":             ("Phase Alloys", 5, "Manufactured"),
    "crystalshards":           ("Crystal Shards", 1, "Manufactured"),
    "uncutfocuscrystals":      ("Flawed Focus Crystals", 2, "Manufactured"),
    "focuscrystals":           ("Focus Crystals", 3, "Manufactured"),
    "refinedfocuscrystals":    ("Refined Focus Crystals", 4, "Manufactured"),
    "dazzlingfocuscrystals":   ("Dazzling Focus Crystals", 4, "Manufactured"),
    "exquisitefocuscrystals":  ("Exquisite Focus Crystals", 5, "Manufactured"),
    "basicconductors":         ("Basic Conductors", 1, "Manufactured"),
    "conductivecomponents":    ("Conductive Components", 2, "Manufactured"),
    "conductiveceramics":      ("Conductive Ceramics", 3, "Manufactured"),
    "conductivepolymers":      ("Conductive Polymers", 4, "Manufactured"),
    "mechanicalscrap":         ("Mechanical Scrap", 1, "Manufactured"),
    "mechanicalequipment":     ("Mechanical Equipment", 2, "Manufactured"),
    "mechanicalcomponents":    ("Mechanical Components", 3, "Manufactured"),
    "configurablecomponents":  ("Configurable Components", 4, "Manufactured"),
    "wornshieldemitters":      ("Worn Shield Emitters", 1, "Manufactured"),
    "shieldemitters":          ("Shield Emitters", 2, "Manufactured"),
    "shieldingsensors":        ("Shielding Sensors", 3, "Manufactured"),
    "compoundshielding":       ("Compound Shielding", 4, "Manufactured"),
    "gridresistors":           ("Grid Resistors", 1, "Manufactured"),
    "hybridcapacitors":        ("Hybrid Capacitors", 2, "Manufactured"),
    "electrochemicalarrays":   ("Electrochemical Arrays", 3, "Manufactured"),
    "polymercapacitors":       ("Polymer Capacitors", 4, "Manufactured"),
    "militarysupercapacitors": ("Military Supercapacitors", 5, "Manufactured"),
    "highdensitycomposites":   ("High Density Composites", 4, "Manufactured"),
    "proprietorycomposites":   ("Proprietary Composites", 4, "Manufactured"),
    "proprietarycomposites":   ("Proprietary Composites", 4, "Manufactured"),
    "fedproprietarycomposites":("Proprietary Composites", 4, "Manufactured"),
    "imperialshielding":       ("Imperial Shielding", 5, "Manufactured"),
    "coredynamicscomposites":  ("Core Dynamics Composites", 5, "Manufactured"),
    "fedcorecomposites":       ("Core Dynamics Composites", 5, "Manufactured"),
    "protoradiolicalloys":     ("Proto Radiolic Alloys", 4, "Manufactured"),
    "protolightalloys":        ("Proto Light Alloys", 4, "Manufactured"),
    "biotechconductors":       ("Biotech Conductors", 4, "Manufactured"),
    "pharmaceuticalisolators": ("Pharmaceutical Isolators", 5, "Manufactured"),
    "guardianpowerconduit":               ("Guardian Power Conduit", 3, "Manufactured"),
    "guardiantechnologycomponent":        ("Guardian Technology Component", 3, "Manufactured"),
    "guardiantechcomponent":              ("Guardian Technology Component", 3, "Manufactured"),
    "guardianpowercell":                  ("Guardian Power Cell", 3, "Manufactured"),
    "guardianwreckagecomponents":         ("Guardian Wreckage Components", 3, "Manufactured"),
    "guardiansentinelwreckagecomponents": ("Guardian Wreckage Components", 3, "Manufactured"),
    "guardiansentinelweaponparts":        ("Guardian Sentinel Weapon Parts", 3, "Manufactured"),
    "propulsionelements":                 ("Propulsion Elements", 3, "Manufactured"),
    "sensorfragment":           ("Sensor Fragment", 3, "Manufactured"),
    "unknowntechnology":        ("Unknown Technology", 3, "Manufactured"),
    "unknowncarapace":          ("Unknown Carapace", 3, "Manufactured"),
    "unknownorganiccircuitry":  ("Unknown Organic Circuitry", 3, "Manufactured"),
    "unknownenergysource":      ("Unknown Energy Source", 3, "Manufactured"),
    "unknownfragment":          ("Unknown Fragment", 3, "Manufactured"),
    "heatresistantceramics":       ("Heat Resistant Ceramics", 3, "Manufactured"),
    "compactcomposites":           ("Compact Composites", 2, "Manufactured"),
    "filamentcomposites":          ("Filament Composites", 3, "Manufactured"),
    "improvisedcomponents":        ("Improvised Components", 4, "Manufactured"),
}

# Back-compat: MATERIAL_NAMES derived from MATERIAL_DATA
MATERIAL_NAMES: dict[str, str] = {k: v[0] for k, v in MATERIAL_DATA.items()}

GRADE_COLORS = {1: "#ffffff", 2: "#00ff88", 3: "#00ddff", 4: "#cc88ff", 5: "#ff7100"}

# Category detection for MaterialTrade events (maps Category field → our bucket)
_CAT_MAP = {
    "$MICRORESOURCE_category_raw;": "Raw",
    "$MICRORESOURCE_category_encoded;": "Encoded",
    "$MICRORESOURCE_category_manufactured;": "Manufactured",
}


# ── Helpers ─────────────────────────────────────────────────────────────────

def pretty_name(raw: str) -> str:
    key = raw.strip().replace(" ", "").replace("_", "").lower()
    entry = MATERIAL_DATA.get(key)
    if entry is not None:
        return entry[0]
    result = raw.strip().replace("_", " ").title()
    _dbg(f"MISS: {raw!r} -> key={key!r} -> fallback={result!r}")
    return result

def material_grade(raw: str) -> int | None:
    """Return grade (1-5) for a material, or None if unknown."""
    key = raw.strip().replace(" ", "").replace("_", "").lower()
    entry = MATERIAL_DATA.get(key)
    return entry[1] if entry else None

def material_max_cap(raw: str, category: str) -> int:
    """Return max storage capacity for a material."""
    g = material_grade(raw)
    if g is None:
        return 300
    return _max_cap(g, category)


def _classify(item: dict) -> str | None:
    """Return 'Raw'/'Encoded'/'Manufactured' from a journal item's Category field."""
    cat = item.get("Category", "")
    return _CAT_MAP.get(cat)


# ── Journal Scan ────────────────────────────────────────────────────────────

def scan_journal(journal_path: str) -> dict[str, dict[str, int]]:
    """Return current material stock by applying deltas on top of the latest
    Materials snapshot, scanning all journal files chronologically."""
    pattern = os.path.join(journal_path, "Journal.*.log")
    files = sorted(glob.glob(pattern))
    if not files:
        return {"Raw": {}, "Encoded": {}, "Manufactured": {}}

    # Phase 1: find the LATEST Materials snapshot across all files
    snapshot: dict | None = None
    snapshot_file: str | None = None
    for fpath in reversed(files):
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if entry.get("event") == "Materials":
                        snapshot = entry
                        snapshot_file = fpath
                        break
            if snapshot:
                break
        except OSError:
            continue

    if not snapshot:
        return {"Raw": {}, "Encoded": {}, "Manufactured": {}}

    # Parse snapshot into mutable stock dict  {display_name: (category, count)}
    stock: dict[str, tuple[str, int]] = {}
    for cat in ("Raw", "Encoded", "Manufactured"):
        for item in snapshot.get(cat, []):
            name = pretty_name(item.get("Name", "Unknown"))
            count = item.get("Count", 0)
            stock[name] = (cat, count)

    # Phase 2: scan forward from snapshot for delta events
    snapshot_ts = snapshot.get("timestamp", "")
    # Files to scan: snapshot file onward
    files_to_scan = files[files.index(snapshot_file):] if snapshot_file in files else files

    for fpath in files_to_scan:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        entry = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    event = entry.get("event", "")
                    ts = entry.get("timestamp", "")

                    # Only process events AFTER the snapshot
                    if fpath == snapshot_file and ts <= snapshot_ts:
                        continue

                    if event == "Materials":
                        # New snapshot — reset stock
                        stock.clear()
                        for cat in ("Raw", "Encoded", "Manufactured"):
                            for item in entry.get(cat, []):
                                name = pretty_name(item.get("Name", "Unknown"))
                                count = item.get("Count", 0)
                                stock[name] = (cat, count)

                    elif event == "MaterialCollected":
                        name = pretty_name(entry.get("Name", "Unknown"))
                        cat = _classify(entry) or "Manufactured"
                        qty = entry.get("Count", 1)
                        if name in stock:
                            old_cat, old_qty = stock[name]
                            stock[name] = (old_cat, old_qty + qty)
                        else:
                            stock[name] = (cat, qty)

                    elif event == "MaterialDiscarded":
                        name = pretty_name(entry.get("Name", "Unknown"))
                        cat = _classify(entry) or "Manufactured"
                        qty = entry.get("Count", 1)
                        if name in stock:
                            old_cat, old_qty = stock[name]
                            stock[name] = (old_cat, max(0, old_qty - qty))

                    elif event == "MaterialTrade":
                        paid = entry.get("Paid", {})
                        received = entry.get("Received", {})
                        if paid:
                            pname = pretty_name(paid.get("Material", ""))
                            pqty = paid.get("Quantity", 0)
                            if pname in stock:
                                old_cat, old_qty = stock[pname]
                                stock[pname] = (old_cat, max(0, old_qty - pqty))
                        if received:
                            rname = pretty_name(received.get("Material", ""))
                            rqty = received.get("Quantity", 0)
                            rcat = _classify(received) or "Manufactured"
                            if rname in stock:
                                old_cat, old_qty = stock[rname]
                                stock[rname] = (old_cat, old_qty + rqty)
                            else:
                                stock[rname] = (rcat, rqty)
        except OSError:
            continue

    # Convert to {category: {name: count}}
    result: dict[str, dict[str, int]] = {"Raw": {}, "Encoded": {}, "Manufactured": {}}
    for name, (cat, count) in stock.items():
        if count > 0:
            result[cat][name] = count
    # Add all known materials at 0 so nothing is hidden
    for _key, (_display, _grade, _cat) in MATERIAL_DATA.items():
        if _display not in result.get(_cat, {}):
            result[_cat][_display] = 0
    return result


# ── GUI ─────────────────────────────────────────────────────────────────────

class MaterialTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(f"ED Material Tracker v{__VERSION__}")
        self.root.geometry("700x850")
        self.root.configure(bg=COLORS["bg"])
        self.root.resizable(True, True)

        self.materials = {"Raw": {}, "Encoded": {}, "Manufactured": {}}
        self.journal_path = None
        self.polling = False

        self._configure_styles()
        self._build_toolbar()
        self._build_tree()
        self._build_status()

        # Auto-detect or prompt
        default = os.path.expandvars(r"%USERPROFILE%\Saved Games\Frontier Developments\Elite Dangerous")
        if os.path.isdir(default):
            self.journal_path = default
            self.path_var.set(default if len(default) < 60 else "…" + default[-57:])
            self.root.after(100, self._poll_once)
            self._start_polling()
        else:
            self.root.after(100, self._pick_directory)

    # ── Styles ──

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(".", background=COLORS["bg"], foreground=COLORS["text"], font=FONT)
        style.configure("TFrame", background=COLORS["bg"])
        style.configure("TLabel", background=COLORS["bg"], foreground=COLORS["text"], font=FONT)
        style.configure("Title.TLabel", font=FONT_TITLE, foreground=COLORS["orange"])
        style.configure("Status.TLabel", font=FONT, foreground=COLORS["text_dim"])
        style.configure("Path.TLabel", font=("Consolas", 9, "Manufactured"), foreground=COLORS["text_dim"])
        style.configure("TButton", background=COLORS["orange"], foreground=COLORS["text_bright"],
                         font=FONT_BOLD, borderwidth=0, padding=(12, 6))
        style.map("TButton", background=[("active", COLORS["orange_dim"])],
                  foreground=[("active", COLORS["text_bright"])])
        style.configure("Treeview", background=COLORS["bg_light"], foreground=COLORS["text"],
                         fieldbackground=COLORS["bg_light"], font=FONT, rowheight=22, borderwidth=0)
        style.configure("Treeview.Heading", background=COLORS["bg_panel"],
                         foreground=COLORS["orange"], font=FONT_HEAD, borderwidth=0)
        style.map("Treeview", background=[("selected", COLORS["orange_dim"])],
                  foreground=[("selected", COLORS["text_bright"])])

    # ── Toolbar ──

    def _build_toolbar(self):
        tb = ttk.Frame(self.root)
        tb.pack(fill=tk.X, padx=10, pady=(10, 0))
        ttk.Label(tb, text="◆ ED Material Tracker", style="Title.TLabel").pack(side=tk.LEFT)
        btn_frame = ttk.Frame(tb)
        btn_frame.pack(side=tk.RIGHT)
        ttk.Button(btn_frame, text="⟳ Refresh", command=self._manual_refresh).pack(side=tk.LEFT, padx=(0, 6))
        ttk.Button(btn_frame, text="📋 Copy JSON", command=self._export_json).pack(side=tk.LEFT, padx=(0, 6))
        ttk.Button(btn_frame, text="📁 Change Dir", command=self._pick_directory).pack(side=tk.LEFT)

    # ── Tree ──

    def _build_tree(self):
        # Tab bar for category switching
        self.tab_frame = ttk.Frame(self.root)
        self.tab_frame.pack(fill=tk.X, padx=10, pady=(10, 0))
        self.active_tab = tk.StringVar(value="ALL")
        self.tab_buttons = {}
        for cat in ("ALL", "RAW", "ENCODED", "MANUFACTURED"):
            btn = tk.Label(self.tab_frame, text=cat, font=FONT_BOLD,
                          bg=COLORS["bg_panel"], fg=COLORS["text_dim"],
                          padx=16, pady=6, cursor="hand2")
            btn.pack(side=tk.LEFT, padx=(0, 2))
            btn.bind("<Button-1>", lambda e, c=cat: self._switch_tab(c))
            self.tab_buttons[cat] = btn
        self._highlight_tab("ALL")

        # Sort controls — right side of tab bar
        self.sort_mode = tk.StringVar(value="qty")  # name, qty, grade
        self.sort_desc = tk.BooleanVar(value=True)
        tk.Label(self.tab_frame, text="│", font=FONT,
                  fg=COLORS["text_dim"], bg=COLORS["bg"]).pack(side=tk.LEFT, padx=(8, 4))
        tk.Label(self.tab_frame, text="Sort:", font=FONT,
                  fg=COLORS["text_dim"], bg=COLORS["bg"]).pack(side=tk.LEFT)
        self.sort_buttons = {}
        for mode, label in [("name", "Name"), ("qty", "Qty"), ("grade", "Grade")]:
            btn = tk.Label(self.tab_frame, text=label, font=FONT,
                          bg=COLORS["bg_panel"], fg=COLORS["text_dim"],
                          padx=10, pady=6, cursor="hand2")
            btn.pack(side=tk.LEFT, padx=(6, 0))
            btn.bind("<Button-1>", lambda e, m=mode: self._set_sort(m))
            self.sort_buttons[mode] = btn
        self.sort_arrow = tk.Label(self.tab_frame, text="▼", font=FONT,
                                   bg=COLORS["bg"], fg=COLORS["orange"])
        self.sort_arrow.pack(side=tk.LEFT, padx=(4, 0))
        self._highlight_sort("qty")

        # Tree container
        container = ttk.Frame(self.root)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=(4, 10))
        self.tree = ttk.Treeview(container, columns=("info",), show="tree headings", selectmode="none")
        self.tree.heading("#0", text="Qty  Material", anchor=tk.W)
        self.tree.heading("info", text="Grade / Capacity", anchor=tk.W)
        self.tree.column("#0", width=350, minwidth=200)
        self.tree.column("info", width=300, minwidth=150)
        vsb = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        for g, c in GRADE_COLORS.items():
            self.tree.tag_configure(f"grade_{g}", foreground=c, font=FONT)
        self.tree.tag_configure("grade_0", foreground=COLORS["text"], font=FONT)
        self.tree.tag_configure("cat_header", font=FONT_CAT, foreground=COLORS["orange"])

    def _highlight_tab(self, active):
        for cat, btn in self.tab_buttons.items():
            if cat == active:
                btn.configure(bg=COLORS["orange"], fg=COLORS["text_bright"])
            else:
                btn.configure(bg=COLORS["bg_panel"], fg=COLORS["text_dim"])

    def _switch_tab(self, cat):
        self.active_tab.set(cat)
        self._highlight_tab(cat)
        self._refresh_tree()

    def _highlight_sort(self, active):
        for mode, btn in self.sort_buttons.items():
            if mode == active:
                btn.configure(bg=COLORS["orange"], fg=COLORS["text_bright"])
            else:
                btn.configure(bg=COLORS["bg_panel"], fg=COLORS["text_dim"])

    def _set_sort(self, mode):
        if self.sort_mode.get() == mode:
            # Toggle direction
            self.sort_desc.set(not self.sort_desc.get())
        else:
            self.sort_mode.set(mode)
            self.sort_desc.set(True)
        self._highlight_sort(mode)
        self.sort_arrow.configure(text="▼" if self.sort_desc.get() else "▲")
        self._refresh_tree()

    # ── Status ──

    def _build_status(self):
        sf = ttk.Frame(self.root)
        sf.pack(fill=tk.X, padx=10, pady=(0, 8))
        self.status_var = tk.StringVar(value="No journal loaded")
        self.path_var   = tk.StringVar(value="")
        self.timer_var  = tk.StringVar(value="")
        ttk.Label(sf, textvariable=self.status_var, style="Status.TLabel").pack(side=tk.LEFT)
        ttk.Label(sf, textvariable=self.timer_var,  style="Status.TLabel").pack(side=tk.RIGHT)
        ttk.Label(sf, textvariable=self.path_var,   style="Path.TLabel").pack(side=tk.LEFT, padx=(12, 0))

    # ── Directory ──

    def _pick_directory(self):
        default = os.path.expandvars(r"%USERPROFILE%\Saved Games\Frontier Developments\Elite Dangerous")
        if not os.path.isdir(default):
            default = os.path.expanduser("~")
        path = filedialog.askdirectory(title="Select ED Journal Directory", initialdir=default)
        if path:
            self.journal_path = path
            self.path_var.set(path if len(path) < 60 else "…" + path[-57:])
            self._poll_once()
            self._start_polling()

    # ── Polling ──

    def _poll_once(self):
        if not self.journal_path:
            return
        self.materials = scan_journal(self.journal_path)
        total = sum(sum(v.values()) for v in self.materials.values())
        self.status_var.set(f"✔ {total} materials tracked  |  Last scan: {datetime.now().strftime('%H:%M:%S')}")
        self._refresh_tree()
        self._update_countdown()

    def _start_polling(self):
        if self.polling:
            return
        self.polling = True
        self._schedule_poll()

    def _schedule_poll(self):
        if not self.polling:
            return
        self._poll_once()
        self.root.after(300_000, self._schedule_poll)

    def _manual_refresh(self):
        self._poll_once()

    def _export_json(self):
        self._poll_once()
        export = {
            "timestamp": datetime.now().isoformat(),
            "journal_path": self.journal_path,
            "materials": self.materials,
            "totals": {cat: sum(mats.values()) for cat, mats in self.materials.items()},
        }
        blob = json.dumps(export, indent=2, ensure_ascii=False)
        self.root.clipboard_clear()
        self.root.clipboard_append(blob)
        self.status_var.set("📋 JSON copied to clipboard!")

    def _update_countdown(self):
        self.timer_var.set("⟳ Next poll: 5:00")
        self._tick_countdown(300)

    def _tick_countdown(self, secs):
        if secs <= 0:
            return
        m, s = divmod(secs, 60)
        self.timer_var.set(f"⟳ Next poll: {m}:{s:02d}")
        self.root.after(1000, self._tick_countdown, secs - 1)

    # ── Tree Refresh ──

    def _refresh_tree(self):
        self.tree.delete(*self.tree.get_children())
        tab = self.active_tab.get()
        cat_map = {"RAW": "Raw", "ENCODED": "Encoded", "MANUFACTURED": "Manufactured"}
        cats = [cat_map[tab]] if tab != "ALL" else ["Raw", "Encoded", "Manufactured"]
        for cat in cats:
            mats = self.materials.get(cat, {})
            if not mats:
                continue
            total = sum(max(0, v) for v in mats.values())
            # Category header
            parent = self.tree.insert("", tk.END, text=f"{cat.upper()}  ({total})",
                                       values=("",), tags=("cat_header",), open=True)
            # Build items with grade info for sorting
            items_with_grade = []
            for name, qty in mats.items():
                entry = None
                for k, v in MATERIAL_DATA.items():
                    if v[0] == name:
                        entry = v
                        break
                grade = entry[1] if entry else 0
                items_with_grade.append((name, qty, grade))

            # Sort based on current mode
            mode = self.sort_mode.get()
            desc = self.sort_desc.get()
            if mode == "name":
                items_with_grade.sort(key=lambda x: x[0].lower(), reverse=desc)
            elif mode == "qty":
                items_with_grade.sort(key=lambda x: x[1], reverse=desc)
            elif mode == "grade":
                items_with_grade.sort(key=lambda x: x[2], reverse=desc)

            for i, (name, qty, grade) in enumerate(items_with_grade):
                max_cap = _max_cap(grade, cat) if grade else 300
                # Bar relative to max capacity
                pct = min(qty / max_cap, 1.0) if max_cap else 0
                filled = int(pct * 20)
                bar = "█" * filled + "░" * (20 - filled)
                grade_label = f"G{grade}" if grade else ""
                item_id = self.tree.insert(parent, tk.END,
                    text=f"{qty:>5}  {name}",
                    values=(f"{grade_label}  {bar}  {qty}/{max_cap}",),
                    tags=(f"grade_{grade}",))

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    MaterialTracker().run()
