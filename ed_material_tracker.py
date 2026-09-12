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
import tkinter.messagebox
from tkinter import ttk, filedialog
from datetime import datetime

try:
    from engineering_data import ENGINEERS, ENGINEER_LOCATIONS, ROLLS_PER_GRADE
except ImportError:
    ENGINEERS = {}
    ENGINEER_LOCATIONS = {}
    ROLLS_PER_GRADE = {1: 1, 2: 2, 3: 3, 4: 4, 5: 6}


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
        ttk.Button(btn_frame, text="🔧 Engineering", command=self._open_engineering).pack(side=tk.LEFT, padx=(0, 6))
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

        # Sort controls — right-anchored in tab bar
        self.sort_mode = tk.StringVar(value="qty")
        self.sort_desc = tk.BooleanVar(value=True)
        self.sort_arrow = tk.Label(self.tab_frame, text="▼", font=FONT,
                                   bg=COLORS["bg"], fg=COLORS["orange"])
        self.sort_arrow.pack(side=tk.RIGHT, padx=(0, 4))
        self.sort_buttons = {}
        for mode, label in [("grade", "Grade"), ("qty", "Qty"), ("name", "Name")]:
            btn = tk.Label(self.tab_frame, text=label, font=FONT,
                          bg=COLORS["bg_panel"], fg=COLORS["text_dim"],
                          padx=10, pady=6, cursor="hand2")
            btn.pack(side=tk.RIGHT, padx=(0, 2))
            btn.bind("<Button-1>", lambda e, m=mode: self._set_sort(m))
            self.sort_buttons[mode] = btn
        tk.Label(self.tab_frame, text="Sort:", font=FONT,
                  fg=COLORS["text_dim"], bg=COLORS["bg"]).pack(side=tk.RIGHT, padx=(0, 6))
        tk.Label(self.tab_frame, text="│", font=FONT,
                  fg=COLORS["text_dim"], bg=COLORS["bg"]).pack(side=tk.RIGHT, padx=(0, 6))
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

    def _open_engineering(self):
        if not ENGINEERS:
            tk.messagebox.showerror("Error", "engineering_data.py not found or failed to import.")
            return
        EngineeringCalculator(self.root, self.materials)

    def run(self):
        self.root.mainloop()


# ── Engineering Calculator ─────────────────────────────────────────────────

class EngineeringCalculator:
    """Modal window for planning engineering material requirements."""

    def __init__(self, parent, materials):
        self.parent = parent
        self.materials = materials  # {cat: {name: qty}}
        self.win = tk.Toplevel(parent)
        self.win.title("Engineering Calculator")
        self.win.geometry("900x700")
        self.win.configure(bg=COLORS["bg"])
        self.win.transient(parent)
        self.win.grab_set()

        # Build lookup: all material names -> (category, current_qty)
        self._mat_lookup = {}
        for cat, mats in materials.items():
            for name, qty in mats.items():
                self._mat_lookup[name] = (cat, qty)

        # Gather all engineerable module types
        self._all_modules = sorted(set(
            mod for eng in ENGINEERS.values()
            for mod in eng["modules"]
        ))

        self._build_ui()
        self._update_module_list("")

    # ── Material lookup helper ──

    # EDEngineer name -> MATERIAL_DATA display name aliases
    _MAT_ALIASES = {
        "Abnormal Compact Emission Data": "Abnormal Compact Emissions Data",
        "Atypical Encryption Archives": "Tagged Encryption Codes",
        "Military Grade Alloys": "Phase Alloys",
        "Peculiar Shield Frequency Data": "Decoded Shield Data",
        "Thermic Alloys": "Galvanising Alloys",
        "Unidentified Scan Archives": "Classified Scan Fragment",
        "Untypical Shield Scans": "Distorted Shield Cycle Recordings",
    }

    def _resolve_mat_name(self, name):
        """Resolve EDEngineer material name to MATERIAL_DATA display name."""
        aliased = self._MAT_ALIASES.get(name)
        if aliased:
            return aliased
        key = name.strip().replace(" ", "").replace("_", "").lower()
        from ed_material_tracker import MATERIAL_DATA
        md = MATERIAL_DATA.get(key)
        if md:
            return md[0]
        return name

    def _get_mat_qty(self, name):
        """Return current qty for a material name (display name)."""
        # Direct lookup
        entry = self._mat_lookup.get(name)
        if entry:
            return entry[1]
        # Alias lookup
        aliased = self._MAT_ALIASES.get(name)
        if aliased:
            entry = self._mat_lookup.get(aliased)
            if entry:
                return entry[1]
        # Normalized lookup via MATERIAL_DATA
        key = name.strip().replace(" ", "").replace("_", "").lower()
        from ed_material_tracker import MATERIAL_DATA
        md = MATERIAL_DATA.get(key)
        if md:
            display = md[0]
            entry = self._mat_lookup.get(display)
            if entry:
                return entry[1]
        return 0

    # ── UI Construction ──

    def _build_ui(self):
        # Top: module picker
        top = ttk.Frame(self.win)
        top.pack(fill=tk.X, padx=12, pady=(12, 4))
        ttk.Label(top, text="Module Type:", font=FONT_BOLD,
                  foreground=COLORS["orange"]).pack(side=tk.LEFT)

        self.module_var = tk.StringVar()
        self.module_entry = ttk.Entry(top, textvariable=self.module_var,
                                      font=FONT, width=30)
        self.module_entry.pack(side=tk.LEFT, padx=(8, 0))
        self.module_entry.bind("<KeyRelease>", self._on_module_type)
        self.module_entry.bind("<Return>", self._on_module_select)

        # Module listbox (autocomplete dropdown)
        self.module_list_frame = ttk.Frame(self.win)
        self.module_list_frame.pack(fill=tk.X, padx=12)
        self.module_listbox = tk.Listbox(self.module_list_frame, font=FONT,
                                          bg=COLORS["bg_light"], fg=COLORS["text"],
                                          selectbackground=COLORS["orange_dim"],
                                          height=6, borderwidth=0,
                                          highlightthickness=0)
        self.module_listbox.pack(fill=tk.X)
        self.module_listbox.bind("<<ListboxSelect>>", self._on_module_pick)
        self.module_listbox.bind("<Return>", self._on_module_pick)
        self._module_list_visible = False

        # Middle: engineer info + blueprint/experiment pickers
        mid = ttk.Frame(self.win)
        mid.pack(fill=tk.X, padx=12, pady=(8, 4))

        # Engineers label
        self.eng_label = ttk.Label(mid, text="Engineers: —", font=FONT,
                                    foreground=COLORS["text_dim"])
        self.eng_label.pack(anchor=tk.W)

        # Blueprint picker row
        bp_row = ttk.Frame(mid)
        bp_row.pack(fill=tk.X, pady=(6, 2))
        ttk.Label(bp_row, text="Blueprint:", font=FONT_BOLD,
                  foreground=COLORS["orange"]).pack(side=tk.LEFT)
        self.bp_var = tk.StringVar()
        self.bp_combo = ttk.Combobox(bp_row, textvariable=self.bp_var,
                                      font=FONT, state="readonly", width=30)
        self.bp_combo.pack(side=tk.LEFT, padx=(8, 0))
        self.bp_combo.bind("<<ComboboxSelected>>", self._on_bp_change)

        # Experiment picker row
        exp_row = ttk.Frame(mid)
        exp_row.pack(fill=tk.X, pady=(2, 2))
        ttk.Label(exp_row, text="Experiment:", font=FONT_BOLD,
                  foreground=COLORS["orange"]).pack(side=tk.LEFT)
        self.exp_var = tk.StringVar()
        self.exp_combo = ttk.Combobox(exp_row, textvariable=self.exp_var,
                                       font=FONT, state="readonly", width=30)
        self.exp_combo.pack(side=tk.LEFT, padx=(8, 0))
        self.exp_combo.bind("<<ComboboxSelected>>", self._on_bp_change)

        # Grade slider row
        grade_row = ttk.Frame(mid)
        grade_row.pack(fill=tk.X, pady=(6, 2))
        ttk.Label(grade_row, text="Target Grade:", font=FONT_BOLD,
                  foreground=COLORS["orange"]).pack(side=tk.LEFT)
        self.grade_var = tk.IntVar(value=5)
        self.grade_scale = tk.Scale(grade_row, from_=1, to=5, orient=tk.HORIZONTAL,
                                     variable=self.grade_var, font=FONT_BOLD,
                                     bg=COLORS["bg"], fg=COLORS["orange"],
                                     troughcolor=COLORS["bg_light"],
                                     highlightthickness=0, length=200,
                                     command=lambda _: self._update_requirements())
        self.grade_scale.pack(side=tk.LEFT, padx=(8, 0))
        self.grade_label = ttk.Label(grade_row, text="G5", font=FONT_TITLE,
                                      foreground=COLORS["orange"])
        self.grade_label.pack(side=tk.LEFT, padx=(12, 0))

        # Rolls estimate
        self.rolls_label = ttk.Label(mid, text="", font=FONT,
                                      foreground=COLORS["text_dim"])
        self.rolls_label.pack(anchor=tk.W, pady=(2, 0))

        # Separator
        sep = ttk.Separator(self.win, orient=tk.HORIZONTAL)
        sep.pack(fill=tk.X, padx=12, pady=8)

        # Requirements panel (scrollable)
        req_label = ttk.Label(self.win, text="Material Requirements",
                              font=FONT_CAT, foreground=COLORS["orange"])
        req_label.pack(anchor=tk.W, padx=12)

        req_container = ttk.Frame(self.win)
        req_container.pack(fill=tk.BOTH, expand=True, padx=12, pady=(4, 12))

        self.req_tree = ttk.Treeview(req_container,
                                      columns=("need", "have", "status"),
                                      show="tree headings", selectmode="none")
        self.req_tree.heading("#0", text="Material", anchor=tk.W)
        self.req_tree.heading("need", text="Need", anchor=tk.CENTER)
        self.req_tree.heading("have", text="Have", anchor=tk.CENTER)
        self.req_tree.heading("status", text="Status", anchor=tk.CENTER)
        self.req_tree.column("#0", width=300, minwidth=150)
        self.req_tree.column("need", width=70, minwidth=50, anchor=tk.CENTER)
        self.req_tree.column("have", width=70, minwidth=50, anchor=tk.CENTER)
        self.req_tree.column("status", width=80, minwidth=60, anchor=tk.CENTER)

        vsb = ttk.Scrollbar(req_container, orient=tk.VERTICAL, command=self.req_tree.yview)
        self.req_tree.configure(yscrollcommand=vsb.set)
        self.req_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        self.req_tree.tag_configure("ok", foreground="#00ff88", font=FONT)
        self.req_tree.tag_configure("missing", foreground="#ff4444", font=FONT)
        self.req_tree.tag_configure("grade_header", font=FONT_CAT,
                                     foreground=COLORS["orange"])
        self.req_tree.tag_configure("exp_header", font=FONT_CAT,
                                     foreground="#cc88ff")
        self.req_tree.tag_configure("total", font=FONT_BOLD,
                                     foreground=COLORS["text_bright"])

        # Summary bar at bottom
        self.summary_var = tk.StringVar(value="Select a module to begin.")
        summary = ttk.Label(self.win, textvariable=self.summary_var,
                            font=FONT_BOLD, foreground=COLORS["orange"])
        summary.pack(anchor=tk.W, padx=12, pady=(0, 12))

    # ── Module autocomplete ──

    def _on_module_type(self, event=None):
        query = self.module_var.get().strip().lower()
        self._update_module_list(query)

    def _update_module_list(self, query):
        self.module_listbox.delete(0, tk.END)
        matches = [m for m in self._all_modules if query in m.lower()]
        for m in matches:
            self.module_listbox.insert(tk.END, m)
        if matches and query:
            self.module_list_frame.pack(fill=tk.X, padx=12)
            self._module_list_visible = True
        else:
            self.module_list_frame.pack_forget()
            self._module_list_visible = False

    def _on_module_pick(self, event=None):
        sel = self.module_listbox.curselection()
        if not sel:
            return
        name = self.module_listbox.get(sel[0])
        self.module_var.set(name)
        self.module_list_frame.pack_forget()
        self._module_list_visible = False
        self._select_module(name)

    def _on_module_select(self, event=None):
        query = self.module_var.get().strip()
        # Try exact match first
        if query in self._all_modules:
            self._select_module(query)
            return
        # Try first match
        matches = [m for m in self._all_modules if query.lower() in m.lower()]
        if matches:
            self.module_var.set(matches[0])
            self._select_module(matches[0])

    def _select_module(self, module_name):
        """Populate engineers, blueprints, experiments for the selected module."""
        self._current_module = module_name

        # Find all engineers that work on this module
        engineers = []
        all_bps = set()
        all_exps = set()
        for eng_name, eng_data in ENGINEERS.items():
            mod_data = eng_data["modules"].get(module_name)
            if mod_data:
                loc = eng_data.get("location", "Unknown")
                engineers.append(f"{eng_name} ({loc})")
                all_bps.update(mod_data["blueprints"].keys())
                all_exps.update(mod_data.get("experiments", {}).keys())

        self.eng_label.config(text="Engineers: " + (", ".join(e.split(" (")[0] for e in engineers) if engineers else "None found"))

        # Blueprint combo
        bp_list = sorted(all_bps)
        self.bp_combo["values"] = bp_list
        if bp_list:
            self.bp_var.set(bp_list[0])
        else:
            self.bp_var.set("")

        # Experiment combo
        exp_list = ["(None)"] + sorted(all_exps)
        self.exp_combo["values"] = exp_list
        self.exp_var.set("(None)")

        # Set max grade based on blueprint
        self._update_max_grade()
        self._update_requirements()

    def _on_bp_change(self, event=None):
        self._update_max_grade()
        self._update_requirements()

    def _update_max_grade(self):
        """Update the grade slider max based on selected blueprint."""
        bp_name = self.bp_var.get()
        module = getattr(self, "_current_module", None)
        if not module or not bp_name:
            return
        max_g = 1
        for eng_data in ENGINEERS.values():
            mod_data = eng_data["modules"].get(module)
            if mod_data:
                bp_data = mod_data["blueprints"].get(bp_name)
                if bp_data:
                    grades = bp_data.get("grades", {})
                    if grades:
                        max_g = max(max_g, max(grades.keys()))
        self.grade_scale.config(to=max_g)
        if self.grade_var.get() > max_g:
            self.grade_var.set(max_g)
        self.grade_label.config(text=f"G{self.grade_var.get()}")

    def _update_requirements(self, event=None):
        """Calculate and display material requirements."""
        self.grade_label.config(text=f"G{self.grade_var.get()}")
        self.req_tree.delete(*self.req_tree.get_children())

        module = getattr(self, "_current_module", None)
        bp_name = self.bp_var.get()
        target_grade = self.grade_var.get()
        exp_name = self.exp_var.get()

        if not module or not bp_name:
            self.summary_var.set("Select a module and blueprint.")
            return

        # Collect blueprint materials for grades 1 through target_grade
        # Use the first engineer that has this blueprint to get material data
        bp_grades = None
        for eng_data in ENGINEERS.values():
            mod_data = eng_data["modules"].get(module)
            if mod_data:
                bp_data = mod_data["blueprints"].get(bp_name)
                if bp_data:
                    bp_grades = bp_data.get("grades", {})
                    if bp_grades:
                        break

        if not bp_grades:
            self.summary_var.set("No blueprint data found.")
            return

        # Aggregate materials: each grade needs ROLLS_PER_GRADE[grade] rolls
        # Each roll costs the materials listed for that grade
        total_needed = {}  # material_name -> total_qty_needed
        grade_totals = {}  # grade -> {mat_name: qty}
        for g in range(1, target_grade + 1):
            mats = bp_grades.get(g, [])
            if not mats:
                continue
            rolls = ROLLS_PER_GRADE.get(g, 1)
            g_total = {}
            for mat_name, qty_per_roll in mats:
                total = qty_per_roll * rolls
                total_needed[mat_name] = total_needed.get(mat_name, 0) + total
                g_total[mat_name] = g_total.get(mat_name, 0) + total
            grade_totals[g] = g_total

        # Add experimental effect materials
        exp_mats = {}
        if exp_name and exp_name != "(None)":
            for eng_data in ENGINEERS.values():
                mod_data = eng_data["modules"].get(module)
                if mod_data:
                    exp_data = mod_data.get("experiments", {}).get(exp_name)
                    if exp_data:
                        for mat_name, qty in exp_data:
                            exp_mats[mat_name] = exp_mats.get(mat_name, 0) + qty
                            total_needed[mat_name] = total_needed.get(mat_name, 0) + qty
                        break

        # Populate tree
        total_have = 0
        total_missing = 0

        # Grade-by-grade sections
        for g in range(1, target_grade + 1):
            g_total = grade_totals.get(g, {})
            if not g_total:
                continue
            rolls = ROLLS_PER_GRADE.get(g, 1)
            parent = self.req_tree.insert("", tk.END,
                text=f"Grade {g}  ({rolls} roll{'s' if rolls > 1 else ''})",
                values=("", "", ""), tags=("grade_header",), open=True)
            for mat_name in sorted(g_total.keys()):
                display_name = self._resolve_mat_name(mat_name)
                need = g_total[mat_name]
                have = self._get_mat_qty(mat_name)
                if have >= need:
                    status = "✅"
                    tag = "ok"
                    total_have += need
                else:
                    status = "❌"
                    tag = "missing"
                    total_have += have
                    total_missing += need - have
                self.req_tree.insert(parent, tk.END,
                    text=f"  {display_name}",
                    values=(str(need), str(have), status),
                    tags=(tag,))

        # Experimental effect section
        if exp_mats:
            parent = self.req_tree.insert("", tk.END,
                text=f"Experimental: {exp_name}",
                values=("", "", ""), tags=("exp_header",), open=True)
            for mat_name in sorted(exp_mats.keys()):
                display_name = self._resolve_mat_name(mat_name)
                need = exp_mats[mat_name]
                have = self._get_mat_qty(mat_name)
                if have >= need:
                    status = "✅"
                    tag = "ok"
                    total_have += need
                else:
                    status = "❌"
                    tag = "missing"
                    total_have += have
                    total_missing += need - have
                self.req_tree.insert(parent, tk.END,
                    text=f"  {display_name}",
                    values=(str(need), str(have), status),
                    tags=(tag,))

        # Totals
        all_total = sum(total_needed.values())
        self.req_tree.insert("", tk.END,
            text=f"TOTAL: {all_total} materials needed",
            values=(str(all_total), str(total_have),
                    f"{'✅' if total_missing == 0 else '❌'} {total_missing} missing"),
            tags=("total",))

        # Summary
        if total_missing == 0:
            self.summary_var.set(f"✅ You have all {all_total} materials for {bp_name} G{target_grade}" +
                                 (f" + {exp_name}" if exp_name != "(None)" else "") + "!")
        else:
            self.summary_var.set(f"❌ Missing {total_missing} materials for {bp_name} G{target_grade}" +
                                 (f" + {exp_name}" if exp_name != "(None)" else ""))


if __name__ == "__main__":
    MaterialTracker().run()
