#!/usr/bin/env python3
"""
ED Material Tracker — Elite Dangerous Engineering Material Monitor
Polls journal files every 5 minutes and displays material stock in a dark E:D-themed GUI.
"""

import json
import os
import sys
import glob
import time
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime

_DEBUG_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "debug.log")

# Clear debug log on startup
try:
    open(_DEBUG_LOG, "w").close()
except OSError:
    pass

def _dbg(msg: str):
    """Append debug line to debug.log."""
    try:
        with open(_DEBUG_LOG, "a", encoding="utf-8") as f:
            f.write(msg + "\n")
    except OSError:
        pass


# ── E:D Orange Dark Theme ───────────────────────────────────────────────────

COLORS = {
    "bg":           "#0d0d0d",
    "bg_light":     "#1a1a1a",
    "bg_panel":     "#141414",
    "orange":       "#ff7100",
    "orange_dim":   "#cc5a00",
    "text":         "#e0e0e0",
    "text_dim":     "#888888",
    "text_bright":  "#ffffff",
    "green":        "#00ff7f",
    "row_even":     "#1a1a1a",
    "row_odd":      "#141414",
    "border":       "#2a2a2a",
}

FONT       = ("Consolas", 10)
FONT_BOLD  = ("Consolas", 10, "bold")
FONT_TITLE = ("Consolas", 14, "bold")
FONT_CAT   = ("Consolas", 11, "bold")
FONT_HEAD  = ("Consolas", 9, "bold")

__VERSION__ = "1.0.5"


# ── Material Display Names ──────────────────────────────────────────────────
# Key = journal internal name lowercased with spaces/underscores stripped.
# Value = human-readable display name.
# Based on actual Materials event journal data from ED v4.x+.

MATERIAL_NAMES: dict[str, str] = {
    # ── Raw ──
    "carbon": "Carbon", "iron": "Iron", "nickel": "Nickel",
    "phosphorus": "Phosphorus", "sulphur": "Sulphur", "lead": "Lead",
    "rhenium": "Rhenium", "chromium": "Chromium", "manganese": "Manganese",
    "zinc": "Zinc", "germanium": "Germanium", "vanadium": "Vanadium",
    "selenium": "Selenium", "cadmium": "Cadmium", "molybdenum": "Molybdenum",
    "ruthenium": "Ruthenium", "tin": "Tin", "tungsten": "Tungsten",
    "mercury": "Mercury", "niobium": "Niobium", "zirconium": "Zirconium",
    "tellurium": "Tellurium", "arsenic": "Arsenic", "antimony": "Antimony",
    # ── Encoded — Wake ──
    "disruptedwakeechoes": "Atypical Disrupted Wake Echoes",
    "fsdtelemetry": "Anomalous FSD Telemetry",
    "wakesolutions": "Strange Wake Solutions",
    "hyperspacetrajectories": "Eccentric Hyperspace Trajectories",
    "dataminedwake": "Datamined Wake Exceptions",
    # ── Encoded — Shield ──
    "shieldcyclerecordings": "Distorted Shield Cycle Recordings",
    "shieldpatternanalysis": "Aberrant Shield Pattern Analysis",
    "shielddensityreports": "Unexpected Shield Data",
    "shieldsoakanalysis": "Inconsistent Shield Soak Analysis",
    "shieldfrequencydata": "Decoded Shield Data",
    # ── Encoded — Scan ──
    "modifiedconsumerfirmware": "Modified Consumer Firmware",
    "compactscandata": "Compact Scan Data",
    "bulkscandata": "Anomalous Bulk Scan Data",
    "scandatabanks": "Classified Scan Databanks",
    "encodedscandata": "Detailed Scan Data",
    "scanarchives": "Classified Scan Fragment",
    "legacyfirmware": "Legacy Firmware",
    "specialisedlegacyfirmware": "Specialised Legacy Firmware",
    "taggedencryptioncodes": "Tagged Encryption Codes",
    "unusualencryptedfiles": "Unusual Encrypted Files",
    # ── Encoded — Emission ──
    "scrambledemissiondata": "Exceptional Scrambled Emission Data",
    "archivedemissiondata": "Irregular Emission Data",
    "emissiondata": "Unexpected Emission Data",
    "decodedemissiondata": "Decoded Emission Data",
    "compactemissionsdata": "Abnormal Compact Emissions Data",
    "securityfirmware": "Security Firmware Patch",
    # ── Encoded — Firmware ──
    "crackedindustrialfirmware": "Cracked Industrial Firmware",
    "modifiedembeddedfirmware": "Modified Embedded Firmware",
    "consumerfirmware": "Consumer Firmware",
    "industrialfirmware": "Industrial Firmware",
    "embeddedfirmware": "Embedded Firmware",
    "adaptiveencryptors": "Adaptive Encryptors Capture",
    "encryptionarchives": "Tagged Encryption Codes",
    # ── Encoded — Guardian Ancient ──
    "ancienthistoricaldata": "Guardian Historical Data",
    "ancientbiologicaldata": "Guardian Biological Data",
    "ancienttechnologicaldata": "Guardian Technological Data",
    "ancientlanguagedata": "Guardian Language Data",
    "ancientculturaldata": "Guardian Cultural Data",
    # ── Manufactured — Chemical ──
    "chemicalstorageunits": "Chemical Storage Units",
    "chemicalprocessors": "Chemical Processors",
    "chemicaldistillery": "Chemical Distillery",
    "chemicalmanipulators": "Chemical Manipulators",
    "chemicalworkshop": "Chemical Workshop",
    # ── Manufactured — Thermic ──
    "heatconductionwiring": "Heat Conduction Wiring",
    "heatdispersionplate": "Heat Dispersion Plate",
    "heatexchangers": "Heat Exchangers",
    "heatvanes": "Heat Vanes",
    "protoheatradiators": "Proto Heat Radiators",
    # ── Manufactured — Alloys ──
    "temperedalloys": "Tempered Alloys",
    "precipitatedalloys": "Precipitated Alloys",
    "salvagedalloys": "Salvaged Alloys",
    "galvanisingalloys": "Galvanising Alloys",
    "phasealloys": "Phase Alloys",
    # ── Manufactured — Focus Crystals ──
    "refinedfocuscrystals": "Refined Focus Crystals",
    "exquisitefocuscrystals": "Exquisite Focus Crystals",
    "dazzlingfocuscrystals": "Dazzling Focus Crystals",
    "focuscrystals": "Focus Crystals",
    "uncutfocuscrystals": "Flawed Focus Crystals",
    "crystalshards": "Crystal Shards",
    # ── Manufactured — Conductive ──
    "basicconductors": "Basic Conductors",
    "conductivecomponents": "Conductive Components",
    "conductiveceramics": "Conductive Ceramics",
    "conductivepolymers": "Conductive Polymers",
    # ── Manufactured — Mechanical ──
    "mechanicalscrap": "Mechanical Scrap",
    "mechanicalequipment": "Mechanical Equipment",
    "mechanicalcomponents": "Mechanical Components",
    "configurablecomponents": "Configurable Components",
    # ── Manufactured — Shielding ──
    "wornshieldemitters": "Worn Shield Emitters",
    "shieldemitters": "Shield Emitters",
    "shieldingsensors": "Shielding Sensors",
    "compoundshielding": "Compound Shielding",
    # ── Manufactured — High Tech ──
    "gridresistors": "Grid Resistors",
    "hybridcapacitors": "Hybrid Capacitors",
    "electrochemicalarrays": "Electrochemical Arrays",
    "polymercapacitors": "Polymer Capacitors",
    "militarysupercapacitors": "Military Supercapacitors",
    # ── Manufactured — Composites ──
    "highdensitycomposites": "High Density Composites",
    "proprietorycomposites": "Proprietary Composites",
    "proprietarycomposites": "Proprietary Composites",
    "imperialshielding": "Imperial Shielding",
    "coredynamicscomposites": "Core Dynamics Composites",
    "fedcorecomposites": "Core Dynamics Composites",
    # ── Manufactured — Proto ──
    "protoradiolicalloys": "Proto Radiolic Alloys",
    "protolightalloys": "Proto Light Alloys",
    # ── Manufactured — Bio ──
    "biotechconductors": "Biotech Conductors",
    "pharmaceuticalisolators": "Pharmaceutical Isolators",
    # ── Manufactured — Guardian ──
    "guardianpowerconduit": "Guardian Power Conduit",
    "guardiantechnologycomponent": "Guardian Technology Component",
    "guardianpowercell": "Guardian Power Cell",
    "guardianwreckagecomponents": "Guardian Wreckage Components",
    "guardiansentinelweaponparts": "Guardian Sentinel Weapon Parts",
    "guardian_powerconduit": "Guardian Power Conduit",
    "guardian_techcomponent": "Guardian Technology Component",
    "guardian_powercell": "Guardian Power Cell",
    "guardian_sentinel_wreckagecomponents": "Guardian Wreckage Components",
    "guardian_sentinel_weaponparts": "Guardian Sentinel Weapon Parts",
    # ── Manufactured — Thargoid / Misc ──
    "sensorfragment": "Sensor Fragment",
    "unknowntechnology": "Unknown Technology",
    "unknowncarapace": "Unknown Carapace",
    "unknownorganiccircuitry": "Unknown Organic Circuitry",
    "unknownenergysource": "Unknown Energy Source",
    "unknownfragment": "Unknown Fragment",
}


# ── Journal Parser ───────────────────────────────────────────────────────────

def find_latest_materials_event(journal_path: str) -> dict | None:
    """Scan journal files for the most recent Materials event."""
    pattern = os.path.join(journal_path, "Journal.*.log")
    files = sorted(glob.glob(pattern))
    if not files:
        return None

    latest = None
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
                        latest = entry
            if latest:
                return latest
        except OSError:
            continue
    return latest


def pretty_name(raw: str) -> str:
    """Convert journal internal name to human-readable display name.
    Strips spaces and underscores, lowercases, then looks up in table.
    Falls back to title case if not found.
    """
    key = raw.strip().replace(" ", "").replace("_", "").lower()
    result = MATERIAL_NAMES.get(key, None)
    if result is None:
        result = raw.strip().replace("_", " ").title()
        _dbg(f"MISS: {raw!r} -> key={key!r} -> fallback={result!r}")
    return result


def parse_materials(entry: dict) -> dict:
    """Parse a Materials event into {category: {name: count}}."""
    result = {"Raw": {}, "Encoded": {}, "Manufactured": {}}

    for item in entry.get("Raw", []):
        raw_name = item.get("Name", "Unknown")
        name = pretty_name(raw_name)
        count = item.get("Count", 0)
        result["Raw"][name] = count

    for item in entry.get("Encoded", []):
        raw_name = item.get("Name", "Unknown")
        name = pretty_name(raw_name)
        count = item.get("Count", 0)
        result["Encoded"][name] = count

    for item in entry.get("Manufactured", []):
        raw_name = item.get("Name", "Unknown")
        name = pretty_name(raw_name)
        count = item.get("Count", 0)
        result["Manufactured"][name] = count

    return result


# ── GUI ─────────────────────────────────────────────────────────────────────

class MaterialTracker:
    """Main application window."""

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

        # Auto-detect journal directory, only prompt if not found
        default = os.path.expandvars(r"%USERPROFILE%\Saved Games\Frontier Developments\Elite Dangerous")
        if os.path.isdir(default):
            self.journal_path = default
            self.path_var.set(default if len(default) < 60 else "…" + default[-57:])
            self.root.after(100, self._poll_once)
            self._start_polling()
        else:
            self.root.after(100, self._pick_directory)

    # ── Styles ──────────────────────────────────────────────────────────────

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(".", background=COLORS["bg"], foreground=COLORS["text"], font=FONT)
        style.configure("TFrame", background=COLORS["bg"])
        style.configure("TLabel", background=COLORS["bg"], foreground=COLORS["text"], font=FONT)
        style.configure("Title.TLabel", font=FONT_TITLE, foreground=COLORS["orange"])
        style.configure("Status.TLabel", font=FONT, foreground=COLORS["text_dim"])
        style.configure("Path.TLabel", font=("Consolas", 9), foreground=COLORS["text_dim"])

        style.configure("TButton",
                         background=COLORS["orange"],
                         foreground=COLORS["text_bright"],
                         font=FONT_BOLD,
                         borderwidth=0,
                         padding=(12, 6))
        style.map("TButton",
                  background=[("active", COLORS["orange_dim"])],
                  foreground=[("active", COLORS["text_bright"])])

        style.configure("Treeview",
                         background=COLORS["bg_light"],
                         foreground=COLORS["text"],
                         fieldbackground=COLORS["bg_light"],
                         font=FONT,
                         rowheight=22,
                         borderwidth=0)
        style.configure("Treeview.Heading",
                         background=COLORS["bg_panel"],
                         foreground=COLORS["orange"],
                         font=FONT_HEAD,
                         borderwidth=0)
        style.map("Treeview",
                  background=[("selected", COLORS["orange_dim"])],
                  foreground=[("selected", COLORS["text_bright"])])

    # ── Toolbar ─────────────────────────────────────────────────────────────

    def _build_toolbar(self):
        tb = ttk.Frame(self.root)
        tb.pack(fill=tk.X, padx=10, pady=(10, 0))

        ttk.Label(tb, text="◆ ED Material Tracker", style="Title.TLabel").pack(side=tk.LEFT)

        btn_frame = ttk.Frame(tb)
        btn_frame.pack(side=tk.RIGHT)

        self.refresh_btn = ttk.Button(btn_frame, text="⟳ Refresh", command=self._manual_refresh)
        self.refresh_btn.pack(side=tk.LEFT, padx=(0, 6))

        self.export_btn = ttk.Button(btn_frame, text="📋 Copy JSON", command=self._export_json)
        self.export_btn.pack(side=tk.LEFT, padx=(0, 6))

        self.dir_btn = ttk.Button(btn_frame, text="📁 Change Dir", command=self._pick_directory)
        self.dir_btn.pack(side=tk.LEFT)

    # ── Tree ────────────────────────────────────────────────────────────────

    def _build_tree(self):
        container = ttk.Frame(self.root)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(container, columns=("qty", "bar"), show="tree headings", selectmode="none")
        self.tree.heading("#0", text="Material", anchor=tk.W)
        self.tree.heading("qty", text="Qty", anchor=tk.E)
        self.tree.heading("bar", text="", anchor=tk.W)
        self.tree.column("#0", width=350, minwidth=200)
        self.tree.column("qty", width=50, minwidth=50, anchor=tk.E)
        self.tree.column("bar", width=200, minwidth=100)

        vsb = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)

        # Tags
        self.tree.tag_configure("cat_raw",         font=FONT_CAT, foreground="#ff9e3d")
        self.tree.tag_configure("cat_encoded",     font=FONT_CAT, foreground="#ff7100")
        self.tree.tag_configure("cat_manufactured", font=FONT_CAT, foreground="#cc5a00")
        self.tree.tag_configure("item",            font=FONT,     foreground=COLORS["text"])
        self.tree.tag_configure("item_alt",        font=FONT,     foreground=COLORS["text_dim"])

    # ── Status Bar ──────────────────────────────────────────────────────────

    def _build_status(self):
        sf = ttk.Frame(self.root)
        sf.pack(fill=tk.X, padx=10, pady=(0, 8))

        self.status_var = tk.StringVar(value="No journal loaded")
        self.path_var   = tk.StringVar(value="")
        self.timer_var  = tk.StringVar(value="")

        ttk.Label(sf, textvariable=self.status_var, style="Status.TLabel").pack(side=tk.LEFT)
        ttk.Label(sf, textvariable=self.timer_var,  style="Status.TLabel").pack(side=tk.RIGHT)
        ttk.Label(sf, textvariable=self.path_var,    style="Path.TLabel").pack(side=tk.LEFT, padx=(12, 0))

    # ── Directory Picker ────────────────────────────────────────────────────

    def _pick_directory(self):
        default = os.path.expandvars(r"%USERPROFILE%\Saved Games\Frontier Developments\Elite Dangerous")
        if not os.path.isdir(default):
            default = os.path.expanduser("~")

        path = filedialog.askdirectory(
            title="Select Elite Dangerous Journal Directory",
            initialdir=default,
        )
        if path:
            self.journal_path = path
            short = path if len(path) < 60 else "…" + path[-57:]
            self.path_var.set(short)
            self._poll_once()
            self._start_polling()

    # ── Polling ─────────────────────────────────────────────────────────────

    def _poll_once(self):
        if not self.journal_path:
            return
        entry = find_latest_materials_event(self.journal_path)
        if entry:
            self.materials = parse_materials(entry)
            ts = entry.get("timestamp", "")
            try:
                dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                ts = dt.strftime("%Y-%m-%d %H:%M:%S")
            except (ValueError, AttributeError):
                pass
            total = sum(sum(v.values()) for v in self.materials.values())
            self.status_var.set(f"✔ {total} materials loaded  |  Last journal: {ts}")
        else:
            self.status_var.set("⚠ No Materials event found — play ED and collect some mats!")
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
        self.root.after(300_000, self._schedule_poll)  # 5 min

    def _manual_refresh(self):
        self._poll_once()

    def _export_json(self):
        """Fresh poll, then copy all materials as JSON to clipboard."""
        self._poll_once()
        export = {
            "timestamp": datetime.now().isoformat(),
            "journal_path": self.journal_path,
            "materials": self.materials,
            "totals": {
                cat: sum(mats.values()) for cat, mats in self.materials.items()
            },
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

    # ── Tree Refresh ────────────────────────────────────────────────────────

    def _refresh_tree(self):
        self.tree.delete(*self.tree.get_children())

        cat_tags = {
            "Raw":          "cat_raw",
            "Encoded":      "cat_encoded",
            "Manufactured": "cat_manufactured",
        }

        for cat in ("Raw", "Encoded", "Manufactured"):
            mats = self.materials.get(cat, {})
            if not mats:
                continue
            total = sum(mats.values())
            parent = self.tree.insert(
                "", tk.END,
                text=f"  {cat.upper()}  ({total})",
                values=("", ""),
                tags=(cat_tags[cat],),
                open=True,
            )
            for i, (name, qty) in enumerate(sorted(mats.items())):
                tag = "item_alt" if i % 2 else "item"
                bar_len = min(qty, 100)
                bar = "█" * (bar_len // 5) + "░" * (20 - bar_len // 5)
                self.tree.insert(
                    parent, tk.END,
                    text=f"    {name}",
                    values=(qty, bar),
                    tags=(tag,),
                )

    # ── Run ─────────────────────────────────────────────────────────────────

    def run(self):
        self.root.mainloop()


# ── Entry Point ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    app = MaterialTracker()
    app.run()
