"""
Engineering blueprint data for ED Material Tracker.
Sourced from EDEngineer (msarilar/EDEngineer) blueprints.json.
Contains all engineers, blueprints per grade with material costs,
and experimental effects.
"""

# Estimated rolls per grade to complete a blueprint
ROLLS_PER_GRADE = {1: 1, 2: 2, 3: 3, 4: 4, 5: 6}

# Engineer locations
ENGINEER_LOCATIONS = {
    "Bill Turner": "Alioth, Turner Metallics Inc.",
    "Broo Tarquin": "Muang, Broo's Legacy",
    "Chloe Sedesi": "Shenve, Sedesi Engineering",
    "Colonel Bris Dekker": "Sol, Dekker's Yard",
    "Didi Vatermann": "Vatermann, Vatermann's Base",
    "Elvira Martuuk": "Khun, Martuuk's Base",
    "Etienne Dorn": "Luchtaine, The Moorings",
    "Felicity Farseer": "Deciat, Farseer Inc.",
    "Hera Tani": "Kuwemaki, The Jet's Hole",
    "Juri Ishmaak": "Giryak, Pater's Memorial",
    "Lei Cheung": "Laksak, Trader's Rest",
    "Liz Ryder": "Eurybia, Demolition Unlimited",
    "Lori Jameson": "Deciat, Jameson Base",
    "Marco Qwent": "Sirius, Qwent Research Base",
    "Marsha Hicks": "Tir, Hicks' Survey",
    "Mel Brandon": "Luchtaine, The Shallows",
    "Oden Geiger": "Dromi, Geiger's Base",
    "Petra Olmanova": "Attenborough's Watch, Olmanova's Base",
    "Professor Palin": "Arque, Abel Laboratory",
    "Ram Tah": "Meene, Phoenix Base",
    "Selene Jean": "Kuk, Prospector's Rest",
    "The Dweller": "Wyrd, The Dweller's Base",
    "The Sarge": "Beta-3 Tucani, The Beach",
    "Tiana Fortune": "Achenar, Fortune's Loss",
    "Tod McQuinn": "Wolf 397, Trophy Camp",
    "Zacariah Nemo": "Yoru, Nemo Cyber Party Base",
}

# Main data structure
# ENGINEERS[engineer_name]["modules"][module_type]["blueprints"][bp_name]["grades"][grade] = [(mat_name, qty), ...]
# ENGINEERS[engineer_name]["modules"][module_type]["experiments"][exp_name] = [(mat_name, qty), ...]

ENGINEERS = {
    "Bill Turner": {
        "location": "Alioth, Turner Metallics Inc.",
        "modules": {
            "Auto Field-Maintenance Unit": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Fuel Scoop": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Kill Warrant Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Life Support": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Radiolic Alloys", 1), ("Proto Light Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Manifest Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Plasma Accelerator": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Dazzle Shell": [("Mechanical Scrap", 5), ("Manganese", 4), ("Hybrid Capacitors", 5), ("Mechanical Components", 5)],
                    "Dispersal Field": [("Conductive Components", 5), ("Hybrid Capacitors", 5), ("Irregular Emission Data", 5), ("Worn Shield Emitters", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Plasma Slug": [("Heat Exchangers", 3), ("Modified Embedded Firmware", 2), ("Refined Focus Crystals", 2), ("Mercury", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Target Lock Breaker": [("Selenium", 5), ("Security Firmware Patch", 3), ("Adaptive Encryptors Capture", 1)],
                    "Thermal Conduit": [("Heat Dispersion Plate", 5), ("Sulphur", 5), ("Tempered Alloys", 5)],
                },
            },
            "Refinery": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Wake Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Broo Tarquin": {
        "location": "Muang, Broo's Legacy",
        "modules": {
            "Beam Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1), ("Biotech Conductors", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Regeneration Sequence": [("Refined Focus Crystals", 3), ("Shielding Sensors", 4), ("Peculiar Shield Frequency Data", 1)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Conduit": [("Heat Dispersion Plate", 5), ("Sulphur", 5), ("Tempered Alloys", 5)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                    "Thermal Vent": [("Flawed Focus Crystals", 5), ("Conductive Polymers", 3), ("Precipitated Alloys", 3)],
                },
            },
            "Burst Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Thermic Alloys", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Precipitated Alloys", 1), ("Configurable Components", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Inertial Impact": [("Flawed Focus Crystals", 5), ("Distorted Shield Cycle Recordings", 5), ("Atypical Disrupted Wake Echoes", 5)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Scramble Spectrum": [("Crystal Shards", 5), ("Untypical Shield Scans", 3), ("Exceptional Scrambled Emission Data", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
            "Pulse Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Scramble Spectrum": [("Crystal Shards", 5), ("Untypical Shield Scans", 3), ("Exceptional Scrambled Emission Data", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
        }
    },
    "Chloe Sedesi": {
        "location": "Shenve, Sedesi Engineering",
        "modules": {
            "Frame Shift Drive": {
                "blueprints": {
                    "Faster FSD Boot Sequence": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Grid Resistors", 1), ("Heat Dispersion Plate", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Heat Exchangers", 1), ("Hybrid Capacitors", 1)],
                            5: [("Electrochemical Arrays", 1), ("Heat Vanes", 1), ("Tellurium", 1)],
                        }
                    },
                    "Increased FSD Range": {
                        "grades": {
                            1: [("Atypical Disrupted Wake Echoes", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Chemical Processors", 1)],
                            3: [("Chemical Processors", 1), ("Phosphorus", 1), ("Strange Wake Solutions", 1)],
                            4: [("Chemical Distillery", 1), ("Eccentric Hyperspace Trajectories", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Chemical Manipulators", 1), ("Datamined Wake Exceptions", 1)],
                        }
                    },
                    "Shielded FSD": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("Shielding Sensors", 1), ("Zinc", 1)],
                            4: [("Compound Shielding", 1), ("High Density Composites", 1), ("Vanadium", 1)],
                            5: [("Imperial Shielding", 1), ("Proprietary Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Deep Charge": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Double Braced": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Configurable Components", 1)],
                    "Mass Manager": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Stripped Down": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Heat Vanes", 1), ("Grid Resistors", 3)],
                },
            },
            "Thrusters": {
                "blueprints": {
                    "Clean Drive Tuning": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1), ("Unexpected Emission Data", 1)],
                            4: [("Conductive Ceramics", 1), ("Decoded Emission Data", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Abnormal Compact Emission Data", 1), ("Conductive Ceramics", 1), ("Tin", 1)],
                        }
                    },
                    "Dirty Drive Tuning": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Mechanical Equipment", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("Mechanical Components", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Configurable Components", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Cracked Industrial Firmware", 1), ("Pharmaceutical Isolators", 1)],
                        }
                    },
                    "Drive Strengthening": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Heat Conduction Wiring", 1), ("Vanadium", 1)],
                            3: [("Heat Conduction Wiring", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            4: [("Compound Shielding", 1), ("Heat Dispersion Plate", 1), ("High Density Composites", 1)],
                            5: [("Heat Exchangers", 1), ("Imperial Shielding", 1), ("Proprietary Composites", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proprietary Composites", 1)],
                    "Drag Drives": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Drive Distributors": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Stripped Down": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Iron", 5), ("Hybrid Capacitors", 3), ("Heat Vanes", 1)],
                },
            },
        }
    },
    "Colonel Bris Dekker": {
        "location": "Sol, Dekker's Yard",
        "modules": {
            "Frame Shift Drive": {
                "blueprints": {
                    "Faster FSD Boot Sequence": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Grid Resistors", 1), ("Heat Dispersion Plate", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Heat Exchangers", 1), ("Hybrid Capacitors", 1)],
                            5: [("Electrochemical Arrays", 1), ("Heat Vanes", 1), ("Tellurium", 1)],
                        }
                    },
                    "Increased FSD Range": {
                        "grades": {
                            1: [("Atypical Disrupted Wake Echoes", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Chemical Processors", 1)],
                            3: [("Chemical Processors", 1), ("Phosphorus", 1), ("Strange Wake Solutions", 1)],
                            4: [("Chemical Distillery", 1), ("Eccentric Hyperspace Trajectories", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Chemical Manipulators", 1), ("Datamined Wake Exceptions", 1)],
                        }
                    },
                    "Shielded FSD": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("Shielding Sensors", 1), ("Zinc", 1)],
                            4: [("Compound Shielding", 1), ("High Density Composites", 1), ("Vanadium", 1)],
                            5: [("Imperial Shielding", 1), ("Proprietary Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Deep Charge": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Double Braced": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Configurable Components", 1)],
                    "Mass Manager": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Stripped Down": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Heat Vanes", 1), ("Grid Resistors", 3)],
                },
            },
            "Frame Shift Drive Interdictor": {
                "blueprints": {
                    "Expanded FSD Interdictor Capture Arc": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Equipment", 1), ("Unusual Encrypted Files", 1)],
                            3: [("Grid Resistors", 1), ("Mechanical Components", 1), ("Tagged Encryption Codes", 1)],
                            4: [("Divergent Scan Data", 1), ("Mechanical Equipment", 1), ("Strange Wake Solutions", 1)],
                            5: [("Classified Scan Fragment", 1), ("Eccentric Hyperspace Trajectories", 1), ("Mechanical Components", 1)],
                        }
                    },
                    "Long Range FSD Interdictor": {
                        "grades": {
                            1: [("Unusual Encrypted Files", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Tagged Encryption Codes", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Anomalous FSD Telemetry", 1), ("Open Symmetric Keys", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Strange Wake Solutions", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Classified Scan Databanks", 1), ("Eccentric Hyperspace Trajectories", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Didi Vatermann": {
        "location": "Vatermann, Vatermann's Base",
        "modules": {
            "Shield Booster": {
                "blueprints": {
                    "Blast Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Iron", 1)],
                            4: [("Germanium", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Niobium", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Heavy Duty": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1), ("Niobium", 1)],
                            4: [("Electrochemical Arrays", 1), ("Inconsistent Shield Soak Analysis", 1), ("Tin", 1)],
                            5: [("Antimony", 1), ("Polymer Capacitors", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Grid Resistors", 1)],
                            3: [("Focus Crystals", 1), ("Hybrid Capacitors", 1), ("Salvaged Alloys", 1)],
                            4: [("Galvanising Alloys", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Phase Alloys", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Resistance Augmented": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Manganese", 1), ("Refined Focus Crystals", 1)],
                            5: [("Conductive Ceramics", 1), ("Imperial Shielding", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Thermal Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Focus Crystals", 1), ("Heat Conduction Wiring", 1), ("Heat Dispersion Plate", 1)],
                            4: [("Heat Dispersion Plate", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Heat Exchangers", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                },
                "experiments": {
                    "Blast Block": [("Inconsistent Shield Soak Analysis", 5), ("Heat Resistant Ceramics", 3), ("Heat Dispersion Plate", 3), ("Selenium", 2)],
                    "Double Braced": [("Distorted Shield Cycle Recordings", 5), ("Galvanising Alloys", 3), ("Shield Emitters", 3)],
                    "Flow Control": [("Inconsistent Shield Soak Analysis", 5), ("Security Firmware Patch", 3), ("Focus Crystals", 3), ("Niobium", 3)],
                    "Force Block": [("Unidentified Scan Archives", 5), ("Shielding Sensors", 3), ("Aberrant Shield Pattern Analysis", 2)],
                    "Super Capacitor": [("Untypical Shield Scans", 3), ("Compact Composites", 5), ("Cadmium", 2)],
                    "Thermo Block": [("Anomalous Bulk Scan Data", 5), ("Conductive Ceramics", 3), ("Heat Vanes", 3)],
                },
            },
            "Shield Generator": {
                "blueprints": {
                    "Enhanced, Low Power Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Precipitated Alloys", 1)],
                            4: [("Inconsistent Shield Soak Analysis", 1), ("Niobium", 1), ("Thermic Alloys", 1)],
                            5: [("Military Grade Alloys", 1), ("Tin", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Reinforced Shields": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Mechanical Components", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Configurable Components", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Conductive Polymers", 1), ("Improvised Components", 1)],
                        }
                    },
                    "Thermal Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Configurable Components", 1)],
                    "Fast Charge": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Compound Shielding", 1)],
                    "Force Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Decoded Emission Data", 1)],
                    "Hi-cap": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Lo-draw": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Multi-weave": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Aberrant Shield Pattern Analysis", 1)],
                    "Stripped Down": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Proto Light Alloys", 1)],
                    "Thermo Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Heat Vanes", 1)],
                },
            },
        }
    },
    "Elvira Martuuk": {
        "location": "Khun, Martuuk's Base",
        "modules": {
            "Frame Shift Drive": {
                "blueprints": {
                    "Faster FSD Boot Sequence": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Grid Resistors", 1), ("Heat Dispersion Plate", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Heat Exchangers", 1), ("Hybrid Capacitors", 1)],
                            5: [("Electrochemical Arrays", 1), ("Heat Vanes", 1), ("Tellurium", 1)],
                        }
                    },
                    "Increased FSD Range": {
                        "grades": {
                            1: [("Atypical Disrupted Wake Echoes", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Chemical Processors", 1)],
                            3: [("Chemical Processors", 1), ("Phosphorus", 1), ("Strange Wake Solutions", 1)],
                            4: [("Chemical Distillery", 1), ("Eccentric Hyperspace Trajectories", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Chemical Manipulators", 1), ("Datamined Wake Exceptions", 1)],
                        }
                    },
                    "Shielded FSD": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("Shielding Sensors", 1), ("Zinc", 1)],
                            4: [("Compound Shielding", 1), ("High Density Composites", 1), ("Vanadium", 1)],
                            5: [("Imperial Shielding", 1), ("Proprietary Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Deep Charge": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Double Braced": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Configurable Components", 1)],
                    "Mass Manager": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Stripped Down": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Heat Vanes", 1), ("Grid Resistors", 3)],
                },
            },
            "Shield Cell Bank": {
                "blueprints": {
                    "Rapid Charge": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Hybrid Capacitors", 1), ("Precipitated Alloys", 1), ("Sulphur", 1)],
                            4: [("Chromium", 1), ("Electrochemical Arrays", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Specialised": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Cracked Industrial Firmware", 1), ("Exceptional Scrambled Emission Data", 1)],
                            4: [("Conductive Components", 1), ("Cracked Industrial Firmware", 1), ("Yttrium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Boss Cells": [("Chemical Storage Units", 5), ("Chromium", 3), ("Polymer Capacitors", 1)],
                    "Double Braced": [("Chemical Storage Units", 5), ("Chromium", 3), ("Yttrium", 1)],
                    "Flow Control": [("Chemical Storage Units", 5), ("Chromium", 3), ("Conductive Polymers", 1)],
                    "Recycling Cells": [("Chemical Storage Units", 5), ("Chromium", 3), ("Configurable Components", 1)],
                    "Stripped Down": [("Chemical Storage Units", 5), ("Chromium", 3), ("Proto Light Alloys", 1)],
                },
            },
            "Shield Generator": {
                "blueprints": {
                    "Enhanced, Low Power Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Precipitated Alloys", 1)],
                            4: [("Inconsistent Shield Soak Analysis", 1), ("Niobium", 1), ("Thermic Alloys", 1)],
                            5: [("Military Grade Alloys", 1), ("Tin", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Reinforced Shields": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Mechanical Components", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Configurable Components", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Conductive Polymers", 1), ("Improvised Components", 1)],
                        }
                    },
                    "Thermal Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Configurable Components", 1)],
                    "Fast Charge": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Compound Shielding", 1)],
                    "Force Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Decoded Emission Data", 1)],
                    "Hi-cap": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Lo-draw": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Multi-weave": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Aberrant Shield Pattern Analysis", 1)],
                    "Stripped Down": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Proto Light Alloys", 1)],
                    "Thermo Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Heat Vanes", 1)],
                },
            },
            "Thrusters": {
                "blueprints": {
                    "Clean Drive Tuning": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1), ("Unexpected Emission Data", 1)],
                            4: [("Conductive Ceramics", 1), ("Decoded Emission Data", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Abnormal Compact Emission Data", 1), ("Conductive Ceramics", 1), ("Tin", 1)],
                        }
                    },
                    "Dirty Drive Tuning": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Mechanical Equipment", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("Mechanical Components", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Configurable Components", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Cracked Industrial Firmware", 1), ("Pharmaceutical Isolators", 1)],
                        }
                    },
                    "Drive Strengthening": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Heat Conduction Wiring", 1), ("Vanadium", 1)],
                            3: [("Heat Conduction Wiring", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            4: [("Compound Shielding", 1), ("Heat Dispersion Plate", 1), ("High Density Composites", 1)],
                            5: [("Heat Exchangers", 1), ("Imperial Shielding", 1), ("Proprietary Composites", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proprietary Composites", 1)],
                    "Drag Drives": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Drive Distributors": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Stripped Down": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Iron", 5), ("Hybrid Capacitors", 3), ("Heat Vanes", 1)],
                },
            },
        }
    },
    "Etienne Dorn": {
        "location": "Luchtaine, The Moorings",
        "modules": {
            "Kill Warrant Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Life Support": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Radiolic Alloys", 1), ("Proto Light Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Manifest Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Plasma Accelerator": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Dazzle Shell": [("Mechanical Scrap", 5), ("Manganese", 4), ("Hybrid Capacitors", 5), ("Mechanical Components", 5)],
                    "Dispersal Field": [("Conductive Components", 5), ("Hybrid Capacitors", 5), ("Irregular Emission Data", 5), ("Worn Shield Emitters", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Plasma Slug": [("Heat Exchangers", 3), ("Modified Embedded Firmware", 2), ("Refined Focus Crystals", 2), ("Mercury", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Target Lock Breaker": [("Selenium", 5), ("Security Firmware Patch", 3), ("Adaptive Encryptors Capture", 1)],
                    "Thermal Conduit": [("Heat Dispersion Plate", 5), ("Sulphur", 5), ("Tempered Alloys", 5)],
                },
            },
            "Power Distributor": {
                "blueprints": {
                    "Charge Enhanced": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Chemical Processors", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chemical Distillery", 1), ("Grid Resistors", 1), ("Modified Consumer Firmware", 1)],
                            4: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Hybrid Capacitors", 1)],
                            5: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Engine Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "High Charge Capacity": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Chromium", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("High Density Composites", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Modified Consumer Firmware", 1), ("Proprietary Composites", 1), ("Selenium", 1)],
                            5: [("Cracked Industrial Firmware", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "System Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "Weapon Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Hybrid Capacitors", 1), ("Selenium", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Electrochemical Arrays", 1), ("Cadmium", 1)],
                            5: [("Classified Scan Databanks", 1), ("Polymer Capacitors", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Cluster Capacitor": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Cadmium", 1)],
                    "Double Braced": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proprietary Composites", 1)],
                    "Flow Control": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Conductive Polymers", 1)],
                    "Stripped Down": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proto Light Alloys", 1)],
                    "Super Conduits": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Security Firmware Patch", 1)],
                },
            },
            "Power Plant": {
                "blueprints": {
                    "Armoured": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Low Emissions": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Irregular Emission Data", 1)],
                            3: [("Heat Exchangers", 1), ("Iron", 1), ("Irregular Emission Data", 1)],
                            4: [("Germanium", 1), ("Unexpected Emission Data", 1), ("Heat Vanes", 1)],
                            5: [("Niobium", 1), ("Decoded Emission Data", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                    "Overcharged": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Conductive Components", 1), ("Heat Conduction Wiring", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Conductive Ceramics", 1), ("Heat Dispersion Plate", 1)],
                            5: [("Chemical Manipulators", 1), ("Conductive Ceramics", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Grid Resistors", 5), ("Vanadium", 3), ("Proprietary Composites", 1)],
                    "Monstered": [("Grid Resistors", 5), ("Vanadium", 3), ("Polymer Capacitors", 1)],
                    "Stripped Down": [("Grid Resistors", 5), ("Vanadium", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Grid Resistors", 5), ("Vanadium", 3), ("Heat Vanes", 1)],
                },
            },
            "Rail Gun": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Thermic Alloys", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Feedback Cascade": [("Open Symmetric Keys", 5), ("Shield Emitters", 5), ("Filament Composites", 5)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Plasma Slug": [("Heat Exchangers", 3), ("Modified Embedded Firmware", 2), ("Refined Focus Crystals", 2), ("Mercury", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Super Penetrator": [("Proto Light Alloys", 3), ("Refined Focus Crystals", 3), ("Zirconium", 3), ("Untypical Shield Scans", 5)],
                },
            },
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Wake Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Felicity Farseer": {
        "location": "Deciat, Farseer Inc.",
        "modules": {
            "Frame Shift Drive": {
                "blueprints": {
                    "Faster FSD Boot Sequence": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Grid Resistors", 1), ("Heat Dispersion Plate", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Heat Exchangers", 1), ("Hybrid Capacitors", 1)],
                            5: [("Electrochemical Arrays", 1), ("Heat Vanes", 1), ("Tellurium", 1)],
                        }
                    },
                    "Increased FSD Range": {
                        "grades": {
                            1: [("Atypical Disrupted Wake Echoes", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Chemical Processors", 1)],
                            3: [("Chemical Processors", 1), ("Phosphorus", 1), ("Strange Wake Solutions", 1)],
                            4: [("Chemical Distillery", 1), ("Eccentric Hyperspace Trajectories", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Chemical Manipulators", 1), ("Datamined Wake Exceptions", 1)],
                        }
                    },
                    "Shielded FSD": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("Shielding Sensors", 1), ("Zinc", 1)],
                            4: [("Compound Shielding", 1), ("High Density Composites", 1), ("Vanadium", 1)],
                            5: [("Imperial Shielding", 1), ("Proprietary Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Deep Charge": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Double Braced": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Configurable Components", 1)],
                    "Mass Manager": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Stripped Down": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Heat Vanes", 1), ("Grid Resistors", 3)],
                },
            },
            "Frame Shift Drive Interdictor": {
                "blueprints": {
                    "Expanded FSD Interdictor Capture Arc": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Equipment", 1), ("Unusual Encrypted Files", 1)],
                            3: [("Grid Resistors", 1), ("Mechanical Components", 1), ("Tagged Encryption Codes", 1)],
                            4: [("Divergent Scan Data", 1), ("Mechanical Equipment", 1), ("Strange Wake Solutions", 1)],
                            5: [("Classified Scan Fragment", 1), ("Eccentric Hyperspace Trajectories", 1), ("Mechanical Components", 1)],
                        }
                    },
                    "Long Range FSD Interdictor": {
                        "grades": {
                            1: [("Unusual Encrypted Files", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Tagged Encryption Codes", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Anomalous FSD Telemetry", 1), ("Open Symmetric Keys", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Strange Wake Solutions", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Classified Scan Databanks", 1), ("Eccentric Hyperspace Trajectories", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Power Plant": {
                "blueprints": {
                    "Armoured": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Low Emissions": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Irregular Emission Data", 1)],
                            3: [("Heat Exchangers", 1), ("Iron", 1), ("Irregular Emission Data", 1)],
                            4: [("Germanium", 1), ("Unexpected Emission Data", 1), ("Heat Vanes", 1)],
                            5: [("Niobium", 1), ("Decoded Emission Data", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                    "Overcharged": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Conductive Components", 1), ("Heat Conduction Wiring", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Conductive Ceramics", 1), ("Heat Dispersion Plate", 1)],
                            5: [("Chemical Manipulators", 1), ("Conductive Ceramics", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Grid Resistors", 5), ("Vanadium", 3), ("Proprietary Composites", 1)],
                    "Monstered": [("Grid Resistors", 5), ("Vanadium", 3), ("Polymer Capacitors", 1)],
                    "Stripped Down": [("Grid Resistors", 5), ("Vanadium", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Grid Resistors", 5), ("Vanadium", 3), ("Heat Vanes", 1)],
                },
            },
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Shield Booster": {
                "blueprints": {
                    "Blast Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Iron", 1)],
                            4: [("Germanium", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Niobium", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Heavy Duty": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1), ("Niobium", 1)],
                            4: [("Electrochemical Arrays", 1), ("Inconsistent Shield Soak Analysis", 1), ("Tin", 1)],
                            5: [("Antimony", 1), ("Polymer Capacitors", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Grid Resistors", 1)],
                            3: [("Focus Crystals", 1), ("Hybrid Capacitors", 1), ("Salvaged Alloys", 1)],
                            4: [("Galvanising Alloys", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Phase Alloys", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Resistance Augmented": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Manganese", 1), ("Refined Focus Crystals", 1)],
                            5: [("Conductive Ceramics", 1), ("Imperial Shielding", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Thermal Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Focus Crystals", 1), ("Heat Conduction Wiring", 1), ("Heat Dispersion Plate", 1)],
                            4: [("Heat Dispersion Plate", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Heat Exchangers", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                },
                "experiments": {
                    "Blast Block": [("Inconsistent Shield Soak Analysis", 5), ("Heat Resistant Ceramics", 3), ("Heat Dispersion Plate", 3), ("Selenium", 2)],
                    "Double Braced": [("Distorted Shield Cycle Recordings", 5), ("Galvanising Alloys", 3), ("Shield Emitters", 3)],
                    "Flow Control": [("Inconsistent Shield Soak Analysis", 5), ("Security Firmware Patch", 3), ("Focus Crystals", 3), ("Niobium", 3)],
                    "Force Block": [("Unidentified Scan Archives", 5), ("Shielding Sensors", 3), ("Aberrant Shield Pattern Analysis", 2)],
                    "Super Capacitor": [("Untypical Shield Scans", 3), ("Compact Composites", 5), ("Cadmium", 2)],
                    "Thermo Block": [("Anomalous Bulk Scan Data", 5), ("Conductive Ceramics", 3), ("Heat Vanes", 3)],
                },
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Thrusters": {
                "blueprints": {
                    "Clean Drive Tuning": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1), ("Unexpected Emission Data", 1)],
                            4: [("Conductive Ceramics", 1), ("Decoded Emission Data", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Abnormal Compact Emission Data", 1), ("Conductive Ceramics", 1), ("Tin", 1)],
                        }
                    },
                    "Dirty Drive Tuning": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Mechanical Equipment", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("Mechanical Components", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Configurable Components", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Cracked Industrial Firmware", 1), ("Pharmaceutical Isolators", 1)],
                        }
                    },
                    "Drive Strengthening": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Heat Conduction Wiring", 1), ("Vanadium", 1)],
                            3: [("Heat Conduction Wiring", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            4: [("Compound Shielding", 1), ("Heat Dispersion Plate", 1), ("High Density Composites", 1)],
                            5: [("Heat Exchangers", 1), ("Imperial Shielding", 1), ("Proprietary Composites", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proprietary Composites", 1)],
                    "Drag Drives": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Drive Distributors": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Stripped Down": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Iron", 5), ("Hybrid Capacitors", 3), ("Heat Vanes", 1)],
                },
            },
        }
    },
    "Hera Tani": {
        "location": "Kuwemaki, The Jet's Hole",
        "modules": {
            "Power Distributor": {
                "blueprints": {
                    "Charge Enhanced": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Chemical Processors", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chemical Distillery", 1), ("Grid Resistors", 1), ("Modified Consumer Firmware", 1)],
                            4: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Hybrid Capacitors", 1)],
                            5: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Engine Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "High Charge Capacity": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Chromium", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("High Density Composites", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Modified Consumer Firmware", 1), ("Proprietary Composites", 1), ("Selenium", 1)],
                            5: [("Cracked Industrial Firmware", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "System Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "Weapon Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Hybrid Capacitors", 1), ("Selenium", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Electrochemical Arrays", 1), ("Cadmium", 1)],
                            5: [("Classified Scan Databanks", 1), ("Polymer Capacitors", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Cluster Capacitor": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Cadmium", 1)],
                    "Double Braced": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proprietary Composites", 1)],
                    "Flow Control": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Conductive Polymers", 1)],
                    "Stripped Down": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proto Light Alloys", 1)],
                    "Super Conduits": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Security Firmware Patch", 1)],
                },
            },
            "Power Plant": {
                "blueprints": {
                    "Armoured": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Low Emissions": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Irregular Emission Data", 1)],
                            3: [("Heat Exchangers", 1), ("Iron", 1), ("Irregular Emission Data", 1)],
                            4: [("Germanium", 1), ("Unexpected Emission Data", 1), ("Heat Vanes", 1)],
                            5: [("Niobium", 1), ("Decoded Emission Data", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                    "Overcharged": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Conductive Components", 1), ("Heat Conduction Wiring", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Conductive Ceramics", 1), ("Heat Dispersion Plate", 1)],
                            5: [("Chemical Manipulators", 1), ("Conductive Ceramics", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Grid Resistors", 5), ("Vanadium", 3), ("Proprietary Composites", 1)],
                    "Monstered": [("Grid Resistors", 5), ("Vanadium", 3), ("Polymer Capacitors", 1)],
                    "Stripped Down": [("Grid Resistors", 5), ("Vanadium", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Grid Resistors", 5), ("Vanadium", 3), ("Heat Vanes", 1)],
                },
            },
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Juri Ishmaak": {
        "location": "Giryak, Pater's Memorial",
        "modules": {
            "Mine Launcher": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Radiolic Alloys", 1), ("Proto Light Alloys", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Technetium", 1), ("Precipitated Alloys", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Ion Disruptor": [("Sulphur", 5), ("Phosphorus", 5), ("Chemical Distillery", 3), ("Electrochemical Arrays", 3)],
                    "Overload Munitions": [("Filament Composites", 5), ("Tagged Encryption Codes", 4), ("Aberrant Shield Pattern Analysis", 2), ("Germanium", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Radiant Canister": [("Polonium", 1), ("Phase Alloys", 3), ("Heat Dispersion Plate", 4)],
                    "Reverberating Cascade": [("Configurable Components", 2), ("Classified Scan Databanks", 3), ("Filament Composites", 4), ("Chromium", 4)],
                    "Shift-Lock Canister": [("Tempered Alloys", 5), ("Strange Wake Solutions", 3), ("Salvaged Alloys", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
            "Missile Rack": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Precipitated Alloys", 1), ("Configurable Components", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Drag Munition (Seeker only)": [("Carbon", 5), ("Grid Resistors", 5), ("Molybdenum", 2)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "FSD Interrupt (Dumbfire only)": [("Strange Wake Solutions", 3), ("Anomalous FSD Telemetry", 5), ("Mechanical Equipment", 5), ("Configurable Components", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Overload Munitions": [("Filament Composites", 5), ("Tagged Encryption Codes", 4), ("Aberrant Shield Pattern Analysis", 2), ("Germanium", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Penetrator Munitions (Dumbfire only)": [("Galvanising Alloys", 5), ("Electrochemical Arrays", 3), ("Zirconium", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Cascade": [("Heat Conduction Wiring", 5), ("Hybrid Capacitors", 4), ("High Density Composites", 3), ("Phosphorus", 5)],
                },
            },
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Torpedo Pylon": {
                "blueprints": {
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Mass Lock Munition": [("Mechanical Equipment", 5), ("High Density Composites", 3), ("Aberrant Shield Pattern Analysis", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Penetrator Payload": [("Mechanical Components", 3), ("Tungsten", 3), ("Anomalous Bulk Scan Data", 5), ("Selenium", 3)],
                    "Reverberating Cascade": [("Configurable Components", 2), ("Classified Scan Databanks", 3), ("Filament Composites", 4), ("Chromium", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
        }
    },
    "Lei Cheung": {
        "location": "Laksak, Trader's Rest",
        "modules": {
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Shield Booster": {
                "blueprints": {
                    "Blast Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Iron", 1)],
                            4: [("Germanium", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Niobium", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Heavy Duty": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1), ("Niobium", 1)],
                            4: [("Electrochemical Arrays", 1), ("Inconsistent Shield Soak Analysis", 1), ("Tin", 1)],
                            5: [("Antimony", 1), ("Polymer Capacitors", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Grid Resistors", 1)],
                            3: [("Focus Crystals", 1), ("Hybrid Capacitors", 1), ("Salvaged Alloys", 1)],
                            4: [("Galvanising Alloys", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Phase Alloys", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Resistance Augmented": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Manganese", 1), ("Refined Focus Crystals", 1)],
                            5: [("Conductive Ceramics", 1), ("Imperial Shielding", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Thermal Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Focus Crystals", 1), ("Heat Conduction Wiring", 1), ("Heat Dispersion Plate", 1)],
                            4: [("Heat Dispersion Plate", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Heat Exchangers", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                },
                "experiments": {
                    "Blast Block": [("Inconsistent Shield Soak Analysis", 5), ("Heat Resistant Ceramics", 3), ("Heat Dispersion Plate", 3), ("Selenium", 2)],
                    "Double Braced": [("Distorted Shield Cycle Recordings", 5), ("Galvanising Alloys", 3), ("Shield Emitters", 3)],
                    "Flow Control": [("Inconsistent Shield Soak Analysis", 5), ("Security Firmware Patch", 3), ("Focus Crystals", 3), ("Niobium", 3)],
                    "Force Block": [("Unidentified Scan Archives", 5), ("Shielding Sensors", 3), ("Aberrant Shield Pattern Analysis", 2)],
                    "Super Capacitor": [("Untypical Shield Scans", 3), ("Compact Composites", 5), ("Cadmium", 2)],
                    "Thermo Block": [("Anomalous Bulk Scan Data", 5), ("Conductive Ceramics", 3), ("Heat Vanes", 3)],
                },
            },
            "Shield Generator": {
                "blueprints": {
                    "Enhanced, Low Power Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Precipitated Alloys", 1)],
                            4: [("Inconsistent Shield Soak Analysis", 1), ("Niobium", 1), ("Thermic Alloys", 1)],
                            5: [("Military Grade Alloys", 1), ("Tin", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Reinforced Shields": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Mechanical Components", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Configurable Components", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Conductive Polymers", 1), ("Improvised Components", 1)],
                        }
                    },
                    "Thermal Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Configurable Components", 1)],
                    "Fast Charge": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Compound Shielding", 1)],
                    "Force Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Decoded Emission Data", 1)],
                    "Hi-cap": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Lo-draw": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Multi-weave": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Aberrant Shield Pattern Analysis", 1)],
                    "Stripped Down": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Proto Light Alloys", 1)],
                    "Thermo Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Heat Vanes", 1)],
                },
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Liz Ryder": {
        "location": "Eurybia, Demolition Unlimited",
        "modules": {
            "Armour": {
                "blueprints": {
                    "Blast Resistant": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Zinc", 1)],
                            3: [("Salvaged Alloys", 1), ("Vanadium", 1), ("Zirconium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Mercury", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Ruthenium", 1)],
                        }
                    },
                    "Heavy Duty": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Kinetic Resistant": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Vanadium", 1)],
                            3: [("High Density Composites", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Proprietary Composites", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Core Dynamics Composites", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("High Density Composites", 1), ("Iron", 1)],
                            4: [("Germanium", 1), ("Conductive Ceramics", 1), ("Proprietary Composites", 1)],
                            5: [("Conductive Ceramics", 1), ("Tin", 1), ("Military Grade Alloys", 1)],
                        }
                    },
                    "Thermal Resistant": {
                        "grades": {
                            1: [("Heat Conduction Wiring", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Nickel", 1)],
                            3: [("Heat Exchangers", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Heat Vanes", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                },
                "experiments": {
                    "Angled Plating": [("Compact Composites", 5), ("High Density Composites", 3), ("Zirconium", 3)],
                    "Deep Plating": [("Compact Composites", 5), ("Mechanical Equipment", 3), ("Molybdenum", 2)],
                    "Layered Plating": [("Heat Conduction Wiring", 5), ("High Density Composites", 3), ("Niobium", 1)],
                    "Reflective Plating": [("Compact Composites", 5), ("Heat Dispersion Plate", 3), ("Thermic Alloys", 2)],
                },
            },
            "Hull Reinforcement Package": {
                "blueprints": {
                    "Blast Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Zinc", 1)],
                            3: [("Salvaged Alloys", 1), ("Vanadium", 1), ("Zirconium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Mercury", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Ruthenium", 1)],
                        }
                    },
                    "Heavy Duty Hull Reinforcement": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Kinetic Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Vanadium", 1)],
                            3: [("High Density Composites", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Proprietary Composites", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Core Dynamics Composites", 1)],
                        }
                    },
                    "Lightweight Hull Reinforcement": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("High Density Composites", 1), ("Iron", 1)],
                            4: [("Conductive Ceramics", 1), ("Germanium", 1), ("Proprietary Composites", 1)],
                            5: [("Conductive Ceramics", 1), ("Military Grade Alloys", 1), ("Tin", 1)],
                        }
                    },
                    "Thermal Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Heat Conduction Wiring", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Nickel", 1)],
                            3: [("Heat Exchangers", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Heat Vanes", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                },
                "experiments": {
                    "Angled Plating": [("Tempered Alloys", 5), ("Zirconium", 3), ("Carbon", 5), ("High Density Composites", 3)],
                    "Deep Plating": [("Compact Composites", 5), ("Molybdenum", 3), ("Ruthenium", 2)],
                    "Layered Plating": [("Heat Conduction Wiring", 5), ("Shielding Sensors", 3), ("Tungsten", 3)],
                    "Reflective Plating": [("Heat Conduction Wiring", 5), ("Heat Dispersion Plate", 3), ("Proto Light Alloys", 1), ("Zinc", 4)],
                },
            },
            "Mine Launcher": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Radiolic Alloys", 1), ("Proto Light Alloys", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Technetium", 1), ("Precipitated Alloys", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Ion Disruptor": [("Sulphur", 5), ("Phosphorus", 5), ("Chemical Distillery", 3), ("Electrochemical Arrays", 3)],
                    "Overload Munitions": [("Filament Composites", 5), ("Tagged Encryption Codes", 4), ("Aberrant Shield Pattern Analysis", 2), ("Germanium", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Radiant Canister": [("Polonium", 1), ("Phase Alloys", 3), ("Heat Dispersion Plate", 4)],
                    "Reverberating Cascade": [("Configurable Components", 2), ("Classified Scan Databanks", 3), ("Filament Composites", 4), ("Chromium", 4)],
                    "Shift-Lock Canister": [("Tempered Alloys", 5), ("Strange Wake Solutions", 3), ("Salvaged Alloys", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
            "Missile Rack": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Precipitated Alloys", 1), ("Configurable Components", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Drag Munition (Seeker only)": [("Carbon", 5), ("Grid Resistors", 5), ("Molybdenum", 2)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "FSD Interrupt (Dumbfire only)": [("Strange Wake Solutions", 3), ("Anomalous FSD Telemetry", 5), ("Mechanical Equipment", 5), ("Configurable Components", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Overload Munitions": [("Filament Composites", 5), ("Tagged Encryption Codes", 4), ("Aberrant Shield Pattern Analysis", 2), ("Germanium", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Penetrator Munitions (Dumbfire only)": [("Galvanising Alloys", 5), ("Electrochemical Arrays", 3), ("Zirconium", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Cascade": [("Heat Conduction Wiring", 5), ("Hybrid Capacitors", 4), ("High Density Composites", 3), ("Phosphorus", 5)],
                },
            },
            "Torpedo Pylon": {
                "blueprints": {
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Mass Lock Munition": [("Mechanical Equipment", 5), ("High Density Composites", 3), ("Aberrant Shield Pattern Analysis", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Penetrator Payload": [("Mechanical Components", 3), ("Tungsten", 3), ("Anomalous Bulk Scan Data", 5), ("Selenium", 3)],
                    "Reverberating Cascade": [("Configurable Components", 2), ("Classified Scan Databanks", 3), ("Filament Composites", 4), ("Chromium", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
        }
    },
    "Lori Jameson": {
        "location": "Deciat, Jameson Base",
        "modules": {
            "Auto Field-Maintenance Unit": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Fuel Scoop": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Kill Warrant Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Life Support": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Radiolic Alloys", 1), ("Proto Light Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Manifest Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Refinery": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Shield Cell Bank": {
                "blueprints": {
                    "Rapid Charge": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Hybrid Capacitors", 1), ("Precipitated Alloys", 1), ("Sulphur", 1)],
                            4: [("Chromium", 1), ("Electrochemical Arrays", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Specialised": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Cracked Industrial Firmware", 1), ("Exceptional Scrambled Emission Data", 1)],
                            4: [("Conductive Components", 1), ("Cracked Industrial Firmware", 1), ("Yttrium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Boss Cells": [("Chemical Storage Units", 5), ("Chromium", 3), ("Polymer Capacitors", 1)],
                    "Double Braced": [("Chemical Storage Units", 5), ("Chromium", 3), ("Yttrium", 1)],
                    "Flow Control": [("Chemical Storage Units", 5), ("Chromium", 3), ("Conductive Polymers", 1)],
                    "Recycling Cells": [("Chemical Storage Units", 5), ("Chromium", 3), ("Configurable Components", 1)],
                    "Stripped Down": [("Chemical Storage Units", 5), ("Chromium", 3), ("Proto Light Alloys", 1)],
                },
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Wake Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Marco Qwent": {
        "location": "Sirius, Qwent Research Base",
        "modules": {
            "Power Distributor": {
                "blueprints": {
                    "Charge Enhanced": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Chemical Processors", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chemical Distillery", 1), ("Grid Resistors", 1), ("Modified Consumer Firmware", 1)],
                            4: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Hybrid Capacitors", 1)],
                            5: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Engine Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "High Charge Capacity": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Chromium", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("High Density Composites", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Modified Consumer Firmware", 1), ("Proprietary Composites", 1), ("Selenium", 1)],
                            5: [("Cracked Industrial Firmware", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "System Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "Weapon Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Hybrid Capacitors", 1), ("Selenium", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Electrochemical Arrays", 1), ("Cadmium", 1)],
                            5: [("Classified Scan Databanks", 1), ("Polymer Capacitors", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Cluster Capacitor": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Cadmium", 1)],
                    "Double Braced": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proprietary Composites", 1)],
                    "Flow Control": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Conductive Polymers", 1)],
                    "Stripped Down": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proto Light Alloys", 1)],
                    "Super Conduits": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Security Firmware Patch", 1)],
                },
            },
            "Power Plant": {
                "blueprints": {
                    "Armoured": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Low Emissions": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Irregular Emission Data", 1)],
                            3: [("Heat Exchangers", 1), ("Iron", 1), ("Irregular Emission Data", 1)],
                            4: [("Germanium", 1), ("Unexpected Emission Data", 1), ("Heat Vanes", 1)],
                            5: [("Niobium", 1), ("Decoded Emission Data", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                    "Overcharged": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Conductive Components", 1), ("Heat Conduction Wiring", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Conductive Ceramics", 1), ("Heat Dispersion Plate", 1)],
                            5: [("Chemical Manipulators", 1), ("Conductive Ceramics", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Grid Resistors", 5), ("Vanadium", 3), ("Proprietary Composites", 1)],
                    "Monstered": [("Grid Resistors", 5), ("Vanadium", 3), ("Polymer Capacitors", 1)],
                    "Stripped Down": [("Grid Resistors", 5), ("Vanadium", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Grid Resistors", 5), ("Vanadium", 3), ("Heat Vanes", 1)],
                },
            },
        }
    },
    "Marsha Hicks": {
        "location": "Tir, Hicks' Survey",
        "modules": {
            "Cannon": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Auto Loader": [("Mechanical Equipment", 4), ("Mechanical Components", 3), ("High Density Composites", 3)],
                    "Dispersal Field": [("Conductive Components", 5), ("Hybrid Capacitors", 5), ("Irregular Emission Data", 5), ("Worn Shield Emitters", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Force Shell": [("Mechanical Scrap", 5), ("Zinc", 5), ("Phase Alloys", 3), ("Heat Conduction Wiring", 3)],
                    "High Yield Shell": [("Mechanical Scrap", 5), ("Proto Light Alloys", 3), ("Chemical Manipulators", 3), ("Nickel", 5)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Smart Rounds": [("Mechanical Scrap", 5), ("Security Firmware Patch", 3), ("Decoded Emission Data", 3), ("Classified Scan Databanks", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Cascade": [("Heat Conduction Wiring", 5), ("Hybrid Capacitors", 4), ("High Density Composites", 3), ("Phosphorus", 5)],
                },
            },
            "Collector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Fragment Cannon": {
                "blueprints": {
                    "Double Shot": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Mechanical Equipment", 1)],
                            3: [("Carbon", 1), ("Cracked Industrial Firmware", 1), ("Mechanical Equipment", 1)],
                            4: [("Mechanical Components", 1), ("Security Firmware Patch", 1), ("Vanadium", 1)],
                            5: [("High Density Composites", 1), ("Configurable Components", 1), ("Modified Embedded Firmware", 1)],
                        }
                    },
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Corrosive Shell": [("Chemical Storage Units", 5), ("Precipitated Alloys", 4), ("Arsenic", 3)],
                    "Dazzle Shell": [("Mechanical Scrap", 5), ("Manganese", 4), ("Hybrid Capacitors", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Drag Munition": [("Carbon", 5), ("Grid Resistors", 5), ("Molybdenum", 2)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Incendiary Rounds": [("Heat Conduction Wiring", 5), ("Phosphorus", 5), ("Sulphur", 5), ("Phase Alloys", 3)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Screening Shell": [("Mechanical Scrap", 5), ("Distorted Shield Cycle Recordings", 5), ("Modified Consumer Firmware", 5), ("Niobium", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
            "Fuel Scoop": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Fuel Transfer Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Hatch Breaker Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Multi-cannon": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Auto Loader": [("Mechanical Equipment", 4), ("Mechanical Components", 3), ("High Density Composites", 3)],
                    "Corrosive Shell": [("Chemical Storage Units", 5), ("Precipitated Alloys", 4), ("Arsenic", 3)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Incendiary Rounds": [("Heat Conduction Wiring", 5), ("Phosphorus", 5), ("Sulphur", 5), ("Phase Alloys", 3)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Smart Rounds": [("Mechanical Scrap", 5), ("Security Firmware Patch", 3), ("Decoded Emission Data", 3), ("Classified Scan Databanks", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
            "Prospector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Refinery": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Mel Brandon": {
        "location": "Luchtaine, The Shallows",
        "modules": {
            "Beam Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1), ("Biotech Conductors", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Regeneration Sequence": [("Refined Focus Crystals", 3), ("Shielding Sensors", 4), ("Peculiar Shield Frequency Data", 1)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Conduit": [("Heat Dispersion Plate", 5), ("Sulphur", 5), ("Tempered Alloys", 5)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                    "Thermal Vent": [("Flawed Focus Crystals", 5), ("Conductive Polymers", 3), ("Precipitated Alloys", 3)],
                },
            },
            "Burst Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Thermic Alloys", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Precipitated Alloys", 1), ("Configurable Components", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Inertial Impact": [("Flawed Focus Crystals", 5), ("Distorted Shield Cycle Recordings", 5), ("Atypical Disrupted Wake Echoes", 5)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Scramble Spectrum": [("Crystal Shards", 5), ("Untypical Shield Scans", 3), ("Exceptional Scrambled Emission Data", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
            "Frame Shift Drive": {
                "blueprints": {
                    "Faster FSD Boot Sequence": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Grid Resistors", 1), ("Heat Dispersion Plate", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Heat Exchangers", 1), ("Hybrid Capacitors", 1)],
                            5: [("Electrochemical Arrays", 1), ("Heat Vanes", 1), ("Tellurium", 1)],
                        }
                    },
                    "Increased FSD Range": {
                        "grades": {
                            1: [("Atypical Disrupted Wake Echoes", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Chemical Processors", 1)],
                            3: [("Chemical Processors", 1), ("Phosphorus", 1), ("Strange Wake Solutions", 1)],
                            4: [("Chemical Distillery", 1), ("Eccentric Hyperspace Trajectories", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Chemical Manipulators", 1), ("Datamined Wake Exceptions", 1)],
                        }
                    },
                    "Shielded FSD": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("Shielding Sensors", 1), ("Zinc", 1)],
                            4: [("Compound Shielding", 1), ("High Density Composites", 1), ("Vanadium", 1)],
                            5: [("Imperial Shielding", 1), ("Proprietary Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Deep Charge": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Double Braced": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Configurable Components", 1)],
                    "Mass Manager": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Stripped Down": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Heat Vanes", 1), ("Grid Resistors", 3)],
                },
            },
            "Frame Shift Drive Interdictor": {
                "blueprints": {
                    "Expanded FSD Interdictor Capture Arc": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Equipment", 1), ("Unusual Encrypted Files", 1)],
                            3: [("Grid Resistors", 1), ("Mechanical Components", 1), ("Tagged Encryption Codes", 1)],
                            4: [("Divergent Scan Data", 1), ("Mechanical Equipment", 1), ("Strange Wake Solutions", 1)],
                            5: [("Classified Scan Fragment", 1), ("Eccentric Hyperspace Trajectories", 1), ("Mechanical Components", 1)],
                        }
                    },
                    "Long Range FSD Interdictor": {
                        "grades": {
                            1: [("Unusual Encrypted Files", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Tagged Encryption Codes", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Anomalous FSD Telemetry", 1), ("Open Symmetric Keys", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Strange Wake Solutions", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Classified Scan Databanks", 1), ("Eccentric Hyperspace Trajectories", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Pulse Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Scramble Spectrum": [("Crystal Shards", 5), ("Untypical Shield Scans", 3), ("Exceptional Scrambled Emission Data", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
            "Shield Booster": {
                "blueprints": {
                    "Blast Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Iron", 1)],
                            4: [("Germanium", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Niobium", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Heavy Duty": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Hybrid Capacitors", 1), ("Niobium", 1)],
                            4: [("Electrochemical Arrays", 1), ("Inconsistent Shield Soak Analysis", 1), ("Tin", 1)],
                            5: [("Antimony", 1), ("Polymer Capacitors", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Grid Resistors", 1)],
                            3: [("Focus Crystals", 1), ("Hybrid Capacitors", 1), ("Salvaged Alloys", 1)],
                            4: [("Galvanising Alloys", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Phase Alloys", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Resistance Augmented": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Focus Crystals", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Manganese", 1), ("Refined Focus Crystals", 1)],
                            5: [("Conductive Ceramics", 1), ("Imperial Shielding", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Thermal Resistant": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Germanium", 1), ("Heat Conduction Wiring", 1)],
                            3: [("Focus Crystals", 1), ("Heat Conduction Wiring", 1), ("Heat Dispersion Plate", 1)],
                            4: [("Heat Dispersion Plate", 1), ("Untypical Shield Scans", 1), ("Refined Focus Crystals", 1)],
                            5: [("Heat Exchangers", 1), ("Aberrant Shield Pattern Analysis", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                },
                "experiments": {
                    "Blast Block": [("Inconsistent Shield Soak Analysis", 5), ("Heat Resistant Ceramics", 3), ("Heat Dispersion Plate", 3), ("Selenium", 2)],
                    "Double Braced": [("Distorted Shield Cycle Recordings", 5), ("Galvanising Alloys", 3), ("Shield Emitters", 3)],
                    "Flow Control": [("Inconsistent Shield Soak Analysis", 5), ("Security Firmware Patch", 3), ("Focus Crystals", 3), ("Niobium", 3)],
                    "Force Block": [("Unidentified Scan Archives", 5), ("Shielding Sensors", 3), ("Aberrant Shield Pattern Analysis", 2)],
                    "Super Capacitor": [("Untypical Shield Scans", 3), ("Compact Composites", 5), ("Cadmium", 2)],
                    "Thermo Block": [("Anomalous Bulk Scan Data", 5), ("Conductive Ceramics", 3), ("Heat Vanes", 3)],
                },
            },
            "Shield Cell Bank": {
                "blueprints": {
                    "Rapid Charge": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Hybrid Capacitors", 1), ("Precipitated Alloys", 1), ("Sulphur", 1)],
                            4: [("Chromium", 1), ("Electrochemical Arrays", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Specialised": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Cracked Industrial Firmware", 1), ("Exceptional Scrambled Emission Data", 1)],
                            4: [("Conductive Components", 1), ("Cracked Industrial Firmware", 1), ("Yttrium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Boss Cells": [("Chemical Storage Units", 5), ("Chromium", 3), ("Polymer Capacitors", 1)],
                    "Double Braced": [("Chemical Storage Units", 5), ("Chromium", 3), ("Yttrium", 1)],
                    "Flow Control": [("Chemical Storage Units", 5), ("Chromium", 3), ("Conductive Polymers", 1)],
                    "Recycling Cells": [("Chemical Storage Units", 5), ("Chromium", 3), ("Configurable Components", 1)],
                    "Stripped Down": [("Chemical Storage Units", 5), ("Chromium", 3), ("Proto Light Alloys", 1)],
                },
            },
            "Shield Generator": {
                "blueprints": {
                    "Enhanced, Low Power Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Precipitated Alloys", 1)],
                            4: [("Inconsistent Shield Soak Analysis", 1), ("Niobium", 1), ("Thermic Alloys", 1)],
                            5: [("Military Grade Alloys", 1), ("Tin", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Kinetic Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                    "Reinforced Shields": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Conductive Components", 1), ("Phosphorus", 1)],
                            3: [("Conductive Components", 1), ("Mechanical Components", 1), ("Phosphorus", 1)],
                            4: [("Conductive Ceramics", 1), ("Configurable Components", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Conductive Polymers", 1), ("Improvised Components", 1)],
                        }
                    },
                    "Thermal Resistant Shields": {
                        "grades": {
                            1: [("Distorted Shield Cycle Recordings", 1)],
                            2: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1)],
                            3: [("Distorted Shield Cycle Recordings", 1), ("Germanium", 1), ("Selenium", 1)],
                            4: [("Focus Crystals", 1), ("Inconsistent Shield Soak Analysis", 1), ("Mercury", 1)],
                            5: [("Refined Focus Crystals", 1), ("Ruthenium", 1), ("Untypical Shield Scans", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Configurable Components", 1)],
                    "Fast Charge": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Compound Shielding", 1)],
                    "Force Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Decoded Emission Data", 1)],
                    "Hi-cap": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Lo-draw": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Conductive Polymers", 1)],
                    "Multi-weave": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Aberrant Shield Pattern Analysis", 1)],
                    "Stripped Down": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Proto Light Alloys", 1)],
                    "Thermo Block": [("Worn Shield Emitters", 5), ("Flawed Focus Crystals", 3), ("Heat Vanes", 1)],
                },
            },
            "Thrusters": {
                "blueprints": {
                    "Clean Drive Tuning": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1), ("Unexpected Emission Data", 1)],
                            4: [("Conductive Ceramics", 1), ("Decoded Emission Data", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Abnormal Compact Emission Data", 1), ("Conductive Ceramics", 1), ("Tin", 1)],
                        }
                    },
                    "Dirty Drive Tuning": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Mechanical Equipment", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("Mechanical Components", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Configurable Components", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Cracked Industrial Firmware", 1), ("Pharmaceutical Isolators", 1)],
                        }
                    },
                    "Drive Strengthening": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Heat Conduction Wiring", 1), ("Vanadium", 1)],
                            3: [("Heat Conduction Wiring", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            4: [("Compound Shielding", 1), ("Heat Dispersion Plate", 1), ("High Density Composites", 1)],
                            5: [("Heat Exchangers", 1), ("Imperial Shielding", 1), ("Proprietary Composites", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proprietary Composites", 1)],
                    "Drag Drives": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Drive Distributors": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Stripped Down": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Iron", 5), ("Hybrid Capacitors", 3), ("Heat Vanes", 1)],
                },
            },
        }
    },
    "Petra Olmanova": {
        "location": "Attenborough's Watch, Olmanova's Base",
        "modules": {
            "Armour": {
                "blueprints": {
                    "Blast Resistant": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Zinc", 1)],
                            3: [("Salvaged Alloys", 1), ("Vanadium", 1), ("Zirconium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Mercury", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Ruthenium", 1)],
                        }
                    },
                    "Heavy Duty": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Kinetic Resistant": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Vanadium", 1)],
                            3: [("High Density Composites", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Proprietary Composites", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Core Dynamics Composites", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("High Density Composites", 1), ("Iron", 1)],
                            4: [("Germanium", 1), ("Conductive Ceramics", 1), ("Proprietary Composites", 1)],
                            5: [("Conductive Ceramics", 1), ("Tin", 1), ("Military Grade Alloys", 1)],
                        }
                    },
                    "Thermal Resistant": {
                        "grades": {
                            1: [("Heat Conduction Wiring", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Nickel", 1)],
                            3: [("Heat Exchangers", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Heat Vanes", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                },
                "experiments": {
                    "Angled Plating": [("Compact Composites", 5), ("High Density Composites", 3), ("Zirconium", 3)],
                    "Deep Plating": [("Compact Composites", 5), ("Mechanical Equipment", 3), ("Molybdenum", 2)],
                    "Layered Plating": [("Heat Conduction Wiring", 5), ("High Density Composites", 3), ("Niobium", 1)],
                    "Reflective Plating": [("Compact Composites", 5), ("Heat Dispersion Plate", 3), ("Thermic Alloys", 2)],
                },
            },
            "Auto Field-Maintenance Unit": {
                "blueprints": {
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Core Dynamics Composites", 1), ("Compound Shielding", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Chaff Launcher": {
                "blueprints": {
                    "Ammo Capacity": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Electronic Countermeasure": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Heat Sink Launcher": {
                "blueprints": {
                    "Ammo Capacity": {
                        "grades": {
                            1: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Modified Heat Sink Launcher": [("Mechanical Scrap", 8), ("Niobium", 6), ("Vanadium", 6), ("Mechanical Components", 4)],
                },
            },
            "Hull Reinforcement Package": {
                "blueprints": {
                    "Blast Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Zinc", 1)],
                            3: [("Salvaged Alloys", 1), ("Vanadium", 1), ("Zirconium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Mercury", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Ruthenium", 1)],
                        }
                    },
                    "Heavy Duty Hull Reinforcement": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Kinetic Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Vanadium", 1)],
                            3: [("High Density Composites", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Proprietary Composites", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Core Dynamics Composites", 1)],
                        }
                    },
                    "Lightweight Hull Reinforcement": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("High Density Composites", 1), ("Iron", 1)],
                            4: [("Conductive Ceramics", 1), ("Germanium", 1), ("Proprietary Composites", 1)],
                            5: [("Conductive Ceramics", 1), ("Military Grade Alloys", 1), ("Tin", 1)],
                        }
                    },
                    "Thermal Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Heat Conduction Wiring", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Nickel", 1)],
                            3: [("Heat Exchangers", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Heat Vanes", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                },
                "experiments": {
                    "Angled Plating": [("Tempered Alloys", 5), ("Zirconium", 3), ("Carbon", 5), ("High Density Composites", 3)],
                    "Deep Plating": [("Compact Composites", 5), ("Molybdenum", 3), ("Ruthenium", 2)],
                    "Layered Plating": [("Heat Conduction Wiring", 5), ("Shielding Sensors", 3), ("Tungsten", 3)],
                    "Reflective Plating": [("Heat Conduction Wiring", 5), ("Heat Dispersion Plate", 3), ("Proto Light Alloys", 1), ("Zinc", 4)],
                },
            },
            "Mine Launcher": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Radiolic Alloys", 1), ("Proto Light Alloys", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Technetium", 1), ("Precipitated Alloys", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Ion Disruptor": [("Sulphur", 5), ("Phosphorus", 5), ("Chemical Distillery", 3), ("Electrochemical Arrays", 3)],
                    "Overload Munitions": [("Filament Composites", 5), ("Tagged Encryption Codes", 4), ("Aberrant Shield Pattern Analysis", 2), ("Germanium", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Radiant Canister": [("Polonium", 1), ("Phase Alloys", 3), ("Heat Dispersion Plate", 4)],
                    "Reverberating Cascade": [("Configurable Components", 2), ("Classified Scan Databanks", 3), ("Filament Composites", 4), ("Chromium", 4)],
                    "Shift-Lock Canister": [("Tempered Alloys", 5), ("Strange Wake Solutions", 3), ("Salvaged Alloys", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
            "Missile Rack": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Precipitated Alloys", 1), ("Configurable Components", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Drag Munition (Seeker only)": [("Carbon", 5), ("Grid Resistors", 5), ("Molybdenum", 2)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "FSD Interrupt (Dumbfire only)": [("Strange Wake Solutions", 3), ("Anomalous FSD Telemetry", 5), ("Mechanical Equipment", 5), ("Configurable Components", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Overload Munitions": [("Filament Composites", 5), ("Tagged Encryption Codes", 4), ("Aberrant Shield Pattern Analysis", 2), ("Germanium", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Penetrator Munitions (Dumbfire only)": [("Galvanising Alloys", 5), ("Electrochemical Arrays", 3), ("Zirconium", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Cascade": [("Heat Conduction Wiring", 5), ("Hybrid Capacitors", 4), ("High Density Composites", 3), ("Phosphorus", 5)],
                },
            },
            "Point Defence": {
                "blueprints": {
                    "Ammo Capacity": {
                        "grades": {
                            1: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Torpedo Pylon": {
                "blueprints": {
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Mass Lock Munition": [("Mechanical Equipment", 5), ("High Density Composites", 3), ("Aberrant Shield Pattern Analysis", 3)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Penetrator Payload": [("Mechanical Components", 3), ("Tungsten", 3), ("Anomalous Bulk Scan Data", 5), ("Selenium", 3)],
                    "Reverberating Cascade": [("Configurable Components", 2), ("Classified Scan Databanks", 3), ("Filament Composites", 4), ("Chromium", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
        }
    },
    "Professor Palin": {
        "location": "Arque, Abel Laboratory",
        "modules": {
            "Frame Shift Drive": {
                "blueprints": {
                    "Faster FSD Boot Sequence": {
                        "grades": {
                            1: [("Grid Resistors", 1)],
                            2: [("Chromium", 1), ("Grid Resistors", 1)],
                            3: [("Grid Resistors", 1), ("Heat Dispersion Plate", 1), ("Selenium", 1)],
                            4: [("Cadmium", 1), ("Heat Exchangers", 1), ("Hybrid Capacitors", 1)],
                            5: [("Electrochemical Arrays", 1), ("Heat Vanes", 1), ("Tellurium", 1)],
                        }
                    },
                    "Increased FSD Range": {
                        "grades": {
                            1: [("Atypical Disrupted Wake Echoes", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Chemical Processors", 1)],
                            3: [("Chemical Processors", 1), ("Phosphorus", 1), ("Strange Wake Solutions", 1)],
                            4: [("Chemical Distillery", 1), ("Eccentric Hyperspace Trajectories", 1), ("Manganese", 1)],
                            5: [("Arsenic", 1), ("Chemical Manipulators", 1), ("Datamined Wake Exceptions", 1)],
                        }
                    },
                    "Shielded FSD": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("Shielding Sensors", 1), ("Zinc", 1)],
                            4: [("Compound Shielding", 1), ("High Density Composites", 1), ("Vanadium", 1)],
                            5: [("Imperial Shielding", 1), ("Proprietary Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Deep Charge": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Double Braced": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Configurable Components", 1)],
                    "Mass Manager": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Eccentric Hyperspace Trajectories", 1)],
                    "Stripped Down": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Atypical Disrupted Wake Echoes", 5), ("Galvanising Alloys", 3), ("Heat Vanes", 1), ("Grid Resistors", 3)],
                },
            },
            "Thrusters": {
                "blueprints": {
                    "Clean Drive Tuning": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Conductive Components", 1), ("Specialised Legacy Firmware", 1), ("Unexpected Emission Data", 1)],
                            4: [("Conductive Ceramics", 1), ("Decoded Emission Data", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Abnormal Compact Emission Data", 1), ("Conductive Ceramics", 1), ("Tin", 1)],
                        }
                    },
                    "Dirty Drive Tuning": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Mechanical Equipment", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("Mechanical Components", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Configurable Components", 1), ("Modified Consumer Firmware", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Cracked Industrial Firmware", 1), ("Pharmaceutical Isolators", 1)],
                        }
                    },
                    "Drive Strengthening": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Heat Conduction Wiring", 1), ("Vanadium", 1)],
                            3: [("Heat Conduction Wiring", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            4: [("Compound Shielding", 1), ("Heat Dispersion Plate", 1), ("High Density Composites", 1)],
                            5: [("Heat Exchangers", 1), ("Imperial Shielding", 1), ("Proprietary Composites", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proprietary Composites", 1)],
                    "Drag Drives": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Drive Distributors": [("Iron", 5), ("Hybrid Capacitors", 3), ("Security Firmware Patch", 1)],
                    "Stripped Down": [("Iron", 5), ("Hybrid Capacitors", 3), ("Proto Light Alloys", 1)],
                    "Thermal Spread": [("Iron", 5), ("Hybrid Capacitors", 3), ("Heat Vanes", 1)],
                },
            },
        }
    },
    "Ram Tah": {
        "location": "Meene, Phoenix Base",
        "modules": {
            "Chaff Launcher": {
                "blueprints": {
                    "Ammo Capacity": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Collector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Electronic Countermeasure": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Fuel Transfer Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Hatch Breaker Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Heat Sink Launcher": {
                "blueprints": {
                    "Ammo Capacity": {
                        "grades": {
                            1: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {
                    "Modified Heat Sink Launcher": [("Mechanical Scrap", 8), ("Niobium", 6), ("Vanadium", 6), ("Mechanical Components", 4)],
                },
            },
            "Point Defence": {
                "blueprints": {
                    "Ammo Capacity": {
                        "grades": {
                            1: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Prospector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Selene Jean": {
        "location": "Kuk, Prospector's Rest",
        "modules": {
            "Armour": {
                "blueprints": {
                    "Blast Resistant": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Zinc", 1)],
                            3: [("Salvaged Alloys", 1), ("Vanadium", 1), ("Zirconium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Mercury", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Ruthenium", 1)],
                        }
                    },
                    "Heavy Duty": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Kinetic Resistant": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Vanadium", 1)],
                            3: [("High Density Composites", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Proprietary Composites", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Core Dynamics Composites", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("High Density Composites", 1), ("Iron", 1)],
                            4: [("Germanium", 1), ("Conductive Ceramics", 1), ("Proprietary Composites", 1)],
                            5: [("Conductive Ceramics", 1), ("Tin", 1), ("Military Grade Alloys", 1)],
                        }
                    },
                    "Thermal Resistant": {
                        "grades": {
                            1: [("Heat Conduction Wiring", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Nickel", 1)],
                            3: [("Heat Exchangers", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Heat Vanes", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                },
                "experiments": {
                    "Angled Plating": [("Compact Composites", 5), ("High Density Composites", 3), ("Zirconium", 3)],
                    "Deep Plating": [("Compact Composites", 5), ("Mechanical Equipment", 3), ("Molybdenum", 2)],
                    "Layered Plating": [("Heat Conduction Wiring", 5), ("High Density Composites", 3), ("Niobium", 1)],
                    "Reflective Plating": [("Compact Composites", 5), ("Heat Dispersion Plate", 3), ("Thermic Alloys", 2)],
                },
            },
            "Hull Reinforcement Package": {
                "blueprints": {
                    "Blast Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Carbon", 1), ("Zinc", 1)],
                            3: [("Salvaged Alloys", 1), ("Vanadium", 1), ("Zirconium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Mercury", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Ruthenium", 1)],
                        }
                    },
                    "Heavy Duty Hull Reinforcement": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Kinetic Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Vanadium", 1)],
                            3: [("High Density Composites", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Proprietary Composites", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Core Dynamics Composites", 1)],
                        }
                    },
                    "Lightweight Hull Reinforcement": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Conductive Components", 1), ("High Density Composites", 1), ("Iron", 1)],
                            4: [("Conductive Ceramics", 1), ("Germanium", 1), ("Proprietary Composites", 1)],
                            5: [("Conductive Ceramics", 1), ("Military Grade Alloys", 1), ("Tin", 1)],
                        }
                    },
                    "Thermal Resistant Hull Reinforcement": {
                        "grades": {
                            1: [("Heat Conduction Wiring", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Nickel", 1)],
                            3: [("Heat Exchangers", 1), ("Salvaged Alloys", 1), ("Vanadium", 1)],
                            4: [("Galvanising Alloys", 1), ("Tungsten", 1), ("Heat Vanes", 1)],
                            5: [("Phase Alloys", 1), ("Molybdenum", 1), ("Proto Heat Radiators", 1)],
                        }
                    },
                },
                "experiments": {
                    "Angled Plating": [("Tempered Alloys", 5), ("Zirconium", 3), ("Carbon", 5), ("High Density Composites", 3)],
                    "Deep Plating": [("Compact Composites", 5), ("Molybdenum", 3), ("Ruthenium", 2)],
                    "Layered Plating": [("Heat Conduction Wiring", 5), ("Shielding Sensors", 3), ("Tungsten", 3)],
                    "Reflective Plating": [("Heat Conduction Wiring", 5), ("Heat Dispersion Plate", 3), ("Proto Light Alloys", 1), ("Zinc", 4)],
                },
            },
        }
    },
    "The Dweller": {
        "location": "Wyrd, The Dweller's Base",
        "modules": {
            "Beam Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1), ("Biotech Conductors", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Regeneration Sequence": [("Refined Focus Crystals", 3), ("Shielding Sensors", 4), ("Peculiar Shield Frequency Data", 1)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Conduit": [("Heat Dispersion Plate", 5), ("Sulphur", 5), ("Tempered Alloys", 5)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                    "Thermal Vent": [("Flawed Focus Crystals", 5), ("Conductive Polymers", 3), ("Precipitated Alloys", 3)],
                },
            },
            "Burst Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Thermic Alloys", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Precipitated Alloys", 1), ("Configurable Components", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Inertial Impact": [("Flawed Focus Crystals", 5), ("Distorted Shield Cycle Recordings", 5), ("Atypical Disrupted Wake Echoes", 5)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Scramble Spectrum": [("Crystal Shards", 5), ("Untypical Shield Scans", 3), ("Exceptional Scrambled Emission Data", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
            "Power Distributor": {
                "blueprints": {
                    "Charge Enhanced": {
                        "grades": {
                            1: [("Specialised Legacy Firmware", 1)],
                            2: [("Chemical Processors", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chemical Distillery", 1), ("Grid Resistors", 1), ("Modified Consumer Firmware", 1)],
                            4: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Hybrid Capacitors", 1)],
                            5: [("Chemical Manipulators", 1), ("Cracked Industrial Firmware", 1), ("Exquisite Focus Crystals", 1)],
                        }
                    },
                    "Engine Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "High Charge Capacity": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Chromium", 1), ("Specialised Legacy Firmware", 1)],
                            3: [("Chromium", 1), ("High Density Composites", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Modified Consumer Firmware", 1), ("Proprietary Composites", 1), ("Selenium", 1)],
                            5: [("Cracked Industrial Firmware", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "System Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Chromium", 1), ("Electrochemical Arrays", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Selenium", 1), ("Polymer Capacitors", 1)],
                            5: [("Classified Scan Databanks", 1), ("Cadmium", 1), ("Military Supercapacitors", 1)],
                        }
                    },
                    "Weapon Focused": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Conductive Components", 1), ("Sulphur", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Hybrid Capacitors", 1), ("Selenium", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Electrochemical Arrays", 1), ("Cadmium", 1)],
                            5: [("Classified Scan Databanks", 1), ("Polymer Capacitors", 1), ("Tellurium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Cluster Capacitor": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Cadmium", 1)],
                    "Double Braced": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proprietary Composites", 1)],
                    "Flow Control": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Conductive Polymers", 1)],
                    "Stripped Down": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Proto Light Alloys", 1)],
                    "Super Conduits": [("Phosphorus", 5), ("Heat Resistant Ceramics", 3), ("Security Firmware Patch", 1)],
                },
            },
            "Pulse Laser": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Concordant Sequence": [("Focus Crystals", 5), ("Modified Embedded Firmware", 3), ("Zirconium", 1)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Scramble Spectrum": [("Crystal Shards", 5), ("Untypical Shield Scans", 3), ("Exceptional Scrambled Emission Data", 5)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
        }
    },
    "The Sarge": {
        "location": "Beta-3 Tucani, The Beach",
        "modules": {
            "Cannon": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Auto Loader": [("Mechanical Equipment", 4), ("Mechanical Components", 3), ("High Density Composites", 3)],
                    "Dispersal Field": [("Conductive Components", 5), ("Hybrid Capacitors", 5), ("Irregular Emission Data", 5), ("Worn Shield Emitters", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Force Shell": [("Mechanical Scrap", 5), ("Zinc", 5), ("Phase Alloys", 3), ("Heat Conduction Wiring", 3)],
                    "High Yield Shell": [("Mechanical Scrap", 5), ("Proto Light Alloys", 3), ("Chemical Manipulators", 3), ("Nickel", 5)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Smart Rounds": [("Mechanical Scrap", 5), ("Security Firmware Patch", 3), ("Decoded Emission Data", 3), ("Classified Scan Databanks", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Cascade": [("Heat Conduction Wiring", 5), ("Hybrid Capacitors", 4), ("High Density Composites", 3), ("Phosphorus", 5)],
                },
            },
            "Collector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Fuel Transfer Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Hatch Breaker Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Prospector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Rail Gun": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Thermic Alloys", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Feedback Cascade": [("Open Symmetric Keys", 5), ("Shield Emitters", 5), ("Filament Composites", 5)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Plasma Slug": [("Heat Exchangers", 3), ("Modified Embedded Firmware", 2), ("Refined Focus Crystals", 2), ("Mercury", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Super Penetrator": [("Proto Light Alloys", 3), ("Refined Focus Crystals", 3), ("Zirconium", 3), ("Untypical Shield Scans", 5)],
                },
            },
        }
    },
    "Tiana Fortune": {
        "location": "Achenar, Fortune's Loss",
        "modules": {
            "Collector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Frame Shift Drive Interdictor": {
                "blueprints": {
                    "Expanded FSD Interdictor Capture Arc": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Equipment", 1), ("Unusual Encrypted Files", 1)],
                            3: [("Grid Resistors", 1), ("Mechanical Components", 1), ("Tagged Encryption Codes", 1)],
                            4: [("Divergent Scan Data", 1), ("Mechanical Equipment", 1), ("Strange Wake Solutions", 1)],
                            5: [("Classified Scan Fragment", 1), ("Eccentric Hyperspace Trajectories", 1), ("Mechanical Components", 1)],
                        }
                    },
                    "Long Range FSD Interdictor": {
                        "grades": {
                            1: [("Unusual Encrypted Files", 1)],
                            2: [("Atypical Disrupted Wake Echoes", 1), ("Tagged Encryption Codes", 1)],
                            3: [("Anomalous Bulk Scan Data", 1), ("Anomalous FSD Telemetry", 1), ("Open Symmetric Keys", 1)],
                            4: [("Unidentified Scan Archives", 1), ("Strange Wake Solutions", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Classified Scan Databanks", 1), ("Eccentric Hyperspace Trajectories", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Fuel Transfer Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Hatch Breaker Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Kill Warrant Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Manifest Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Prospector Limpet Controller": {
                "blueprints": {
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Sensors": {
                "blueprints": {
                    "Light Weight Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Salvaged Alloys", 1), ("Manganese", 1)],
                            3: [("Salvaged Alloys", 1), ("Manganese", 1), ("Conductive Ceramics", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Germanium", 1), ("Mechanical Scrap", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Surface Scanner": {
                "blueprints": {
                    "Expanded Probe Scanning Radius": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Phase Alloys", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Proto Light Alloys", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                },
                "experiments": {},
            },
            "Wake Scanner": {
                "blueprints": {
                    "Fast Scanner": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Phosphorus", 1), ("Flawed Focus Crystals", 1)],
                            3: [("Phosphorus", 1), ("Flawed Focus Crystals", 1), ("Open Symmetric Keys", 1)],
                            4: [("Manganese", 1), ("Focus Crystals", 1), ("Atypical Encryption Archives", 1)],
                            5: [("Arsenic", 1), ("Refined Focus Crystals", 1), ("Adaptive Encryptors Capture", 1)],
                        }
                    },
                    "Lightweight": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Scanner": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Iron", 1), ("Hybrid Capacitors", 1)],
                            3: [("Iron", 1), ("Hybrid Capacitors", 1), ("Unexpected Emission Data", 1)],
                            4: [("Germanium", 1), ("Electrochemical Arrays", 1), ("Decoded Emission Data", 1)],
                            5: [("Niobium", 1), ("Polymer Capacitors", 1), ("Abnormal Compact Emission Data", 1)],
                        }
                    },
                    "Reinforced": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                    "Shielded": {
                        "grades": {
                            1: [("Worn Shield Emitters", 1)],
                            2: [("Carbon", 1), ("Shield Emitters", 1)],
                            3: [("Carbon", 1), ("High Density Composites", 1), ("Shield Emitters", 1)],
                            4: [("Proprietary Composites", 1), ("Shielding Sensors", 1), ("Vanadium", 1)],
                            5: [("Compound Shielding", 1), ("Core Dynamics Composites", 1), ("Tungsten", 1)],
                        }
                    },
                    "Wide Angle Scanner": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Germanium", 1)],
                            3: [("Mechanical Scrap", 1), ("Germanium", 1), ("Classified Scan Databanks", 1)],
                            4: [("Mechanical Equipment", 1), ("Niobium", 1), ("Divergent Scan Data", 1)],
                            5: [("Mechanical Components", 1), ("Tin", 1), ("Classified Scan Fragment", 1)],
                        }
                    },
                },
                "experiments": {},
            },
        }
    },
    "Tod McQuinn": {
        "location": "Wolf 397, Trophy Camp",
        "modules": {
            "Cannon": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Auto Loader": [("Mechanical Equipment", 4), ("Mechanical Components", 3), ("High Density Composites", 3)],
                    "Dispersal Field": [("Conductive Components", 5), ("Hybrid Capacitors", 5), ("Irregular Emission Data", 5), ("Worn Shield Emitters", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Force Shell": [("Mechanical Scrap", 5), ("Zinc", 5), ("Phase Alloys", 3), ("Heat Conduction Wiring", 3)],
                    "High Yield Shell": [("Mechanical Scrap", 5), ("Proto Light Alloys", 3), ("Chemical Manipulators", 3), ("Nickel", 5)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Smart Rounds": [("Mechanical Scrap", 5), ("Security Firmware Patch", 3), ("Decoded Emission Data", 3), ("Classified Scan Databanks", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Cascade": [("Heat Conduction Wiring", 5), ("Hybrid Capacitors", 4), ("High Density Composites", 3), ("Phosphorus", 5)],
                },
            },
            "Fragment Cannon": {
                "blueprints": {
                    "Double Shot": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Mechanical Equipment", 1)],
                            3: [("Carbon", 1), ("Cracked Industrial Firmware", 1), ("Mechanical Equipment", 1)],
                            4: [("Mechanical Components", 1), ("Security Firmware Patch", 1), ("Vanadium", 1)],
                            5: [("High Density Composites", 1), ("Configurable Components", 1), ("Modified Embedded Firmware", 1)],
                        }
                    },
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Corrosive Shell": [("Chemical Storage Units", 5), ("Precipitated Alloys", 4), ("Arsenic", 3)],
                    "Dazzle Shell": [("Mechanical Scrap", 5), ("Manganese", 4), ("Hybrid Capacitors", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Drag Munition": [("Carbon", 5), ("Grid Resistors", 5), ("Molybdenum", 2)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Incendiary Rounds": [("Heat Conduction Wiring", 5), ("Phosphorus", 5), ("Sulphur", 5), ("Phase Alloys", 3)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Screening Shell": [("Mechanical Scrap", 5), ("Distorted Shield Cycle Recordings", 5), ("Modified Consumer Firmware", 5), ("Niobium", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
            "Multi-cannon": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Auto Loader": [("Mechanical Equipment", 4), ("Mechanical Components", 3), ("High Density Composites", 3)],
                    "Corrosive Shell": [("Chemical Storage Units", 5), ("Precipitated Alloys", 4), ("Arsenic", 3)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Incendiary Rounds": [("Heat Conduction Wiring", 5), ("Phosphorus", 5), ("Sulphur", 5), ("Phase Alloys", 3)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Smart Rounds": [("Mechanical Scrap", 5), ("Security Firmware Patch", 3), ("Decoded Emission Data", 3), ("Classified Scan Databanks", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
            "Rail Gun": {
                "blueprints": {
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Thermic Alloys", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Feedback Cascade": [("Open Symmetric Keys", 5), ("Shield Emitters", 5), ("Filament Composites", 5)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Plasma Slug": [("Heat Exchangers", 3), ("Modified Embedded Firmware", 2), ("Refined Focus Crystals", 2), ("Mercury", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Super Penetrator": [("Proto Light Alloys", 3), ("Refined Focus Crystals", 3), ("Zirconium", 3), ("Untypical Shield Scans", 5)],
                },
            },
        }
    },
    "Zacariah Nemo": {
        "location": "Yoru, Nemo Cyber Party Base",
        "modules": {
            "Fragment Cannon": {
                "blueprints": {
                    "Double Shot": {
                        "grades": {
                            1: [("Carbon", 1)],
                            2: [("Carbon", 1), ("Mechanical Equipment", 1)],
                            3: [("Carbon", 1), ("Cracked Industrial Firmware", 1), ("Mechanical Equipment", 1)],
                            4: [("Mechanical Components", 1), ("Security Firmware Patch", 1), ("Vanadium", 1)],
                            5: [("High Density Composites", 1), ("Configurable Components", 1), ("Modified Embedded Firmware", 1)],
                        }
                    },
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Corrosive Shell": [("Chemical Storage Units", 5), ("Precipitated Alloys", 4), ("Arsenic", 3)],
                    "Dazzle Shell": [("Mechanical Scrap", 5), ("Manganese", 4), ("Hybrid Capacitors", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Drag Munition": [("Carbon", 5), ("Grid Resistors", 5), ("Molybdenum", 2)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Incendiary Rounds": [("Heat Conduction Wiring", 5), ("Phosphorus", 5), ("Sulphur", 5), ("Phase Alloys", 3)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Screening Shell": [("Mechanical Scrap", 5), ("Distorted Shield Cycle Recordings", 5), ("Modified Consumer Firmware", 5), ("Niobium", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                },
            },
            "Multi-cannon": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "High Capacity Magazine": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Mechanical Scrap", 1), ("Vanadium", 1)],
                            3: [("Mechanical Scrap", 1), ("Niobium", 1), ("Vanadium", 1)],
                            4: [("High Density Composites", 1), ("Mechanical Equipment", 1), ("Tin", 1)],
                            5: [("Mechanical Components", 1), ("Military Supercapacitors", 1), ("Proprietary Composites", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Auto Loader": [("Mechanical Equipment", 4), ("Mechanical Components", 3), ("High Density Composites", 3)],
                    "Corrosive Shell": [("Chemical Storage Units", 5), ("Precipitated Alloys", 4), ("Arsenic", 3)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Emissive Munitions": [("Mechanical Equipment", 4), ("Unexpected Emission Data", 3), ("Heat Exchangers", 3), ("Manganese", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Incendiary Rounds": [("Heat Conduction Wiring", 5), ("Phosphorus", 5), ("Sulphur", 5), ("Phase Alloys", 3)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Smart Rounds": [("Mechanical Scrap", 5), ("Security Firmware Patch", 3), ("Decoded Emission Data", 3), ("Classified Scan Databanks", 3)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Thermal Shock": [("Flawed Focus Crystals", 5), ("Heat Resistant Ceramics", 3), ("Conductive Components", 3), ("Tungsten", 3)],
                },
            },
            "Plasma Accelerator": {
                "blueprints": {
                    "Efficient Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Sulphur", 1)],
                            3: [("Chromium", 1), ("Exceptional Scrambled Emission Data", 1), ("Heat Exchangers", 1)],
                            4: [("Heat Vanes", 1), ("Irregular Emission Data", 1), ("Selenium", 1)],
                            5: [("Cadmium", 1), ("Proto Heat Radiators", 1), ("Unexpected Emission Data", 1)],
                        }
                    },
                    "Focused Weapon": {
                        "grades": {
                            1: [("Iron", 1)],
                            2: [("Conductive Components", 1), ("Iron", 1)],
                            3: [("Chromium", 1), ("Conductive Ceramics", 1), ("Iron", 1)],
                            4: [("Focus Crystals", 1), ("Germanium", 1), ("Polymer Capacitors", 1)],
                            5: [("Military Supercapacitors", 1), ("Niobium", 1), ("Refined Focus Crystals", 1)],
                        }
                    },
                    "Lightweight Mount": {
                        "grades": {
                            1: [("Phosphorus", 1)],
                            2: [("Manganese", 1), ("Salvaged Alloys", 1)],
                            3: [("Conductive Ceramics", 1), ("Manganese", 1), ("Salvaged Alloys", 1)],
                            4: [("Conductive Components", 1), ("Phase Alloys", 1), ("Proto Light Alloys", 1)],
                            5: [("Conductive Ceramics", 1), ("Proto Light Alloys", 1), ("Proto Radiolic Alloys", 1)],
                        }
                    },
                    "Long Range Weapon": {
                        "grades": {
                            1: [("Sulphur", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            3: [("Focus Crystals", 1), ("Modified Consumer Firmware", 1), ("Sulphur", 1)],
                            4: [("Conductive Polymers", 1), ("Focus Crystals", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Cracked Industrial Firmware", 1), ("Thermic Alloys", 1)],
                        }
                    },
                    "Overcharged Weapon": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Conductive Components", 1), ("Nickel", 1)],
                            3: [("Conductive Components", 1), ("Electrochemical Arrays", 1), ("Nickel", 1)],
                            4: [("Conductive Ceramics", 1), ("Polymer Capacitors", 1), ("Zinc", 1)],
                            5: [("Conductive Polymers", 1), ("Modified Embedded Firmware", 1), ("Zirconium", 1)],
                        }
                    },
                    "Rapid Fire Modification": {
                        "grades": {
                            1: [("Mechanical Scrap", 1)],
                            2: [("Heat Dispersion Plate", 1), ("Mechanical Scrap", 1)],
                            3: [("Mechanical Equipment", 1), ("Precipitated Alloys", 1), ("Specialised Legacy Firmware", 1)],
                            4: [("Mechanical Components", 1), ("Modified Consumer Firmware", 1), ("Thermic Alloys", 1)],
                            5: [("Configurable Components", 1), ("Precipitated Alloys", 1), ("Technetium", 1)],
                        }
                    },
                    "Short Range Blaster": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            3: [("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1), ("Nickel", 1)],
                            4: [("Conductive Polymers", 1), ("Electrochemical Arrays", 1), ("Modified Consumer Firmware", 1)],
                            5: [("Biotech Conductors", 1), ("Configurable Components", 1), ("Cracked Industrial Firmware", 1)],
                        }
                    },
                    "Sturdy Mount": {
                        "grades": {
                            1: [("Nickel", 1)],
                            2: [("Nickel", 1), ("Shield Emitters", 1)],
                            3: [("Nickel", 1), ("Shield Emitters", 1), ("Tungsten", 1)],
                            4: [("Molybdenum", 1), ("Tungsten", 1), ("Zinc", 1)],
                            5: [("High Density Composites", 1), ("Molybdenum", 1), ("Technetium", 1)],
                        }
                    },
                },
                "experiments": {
                    "Dazzle Shell": [("Mechanical Scrap", 5), ("Manganese", 4), ("Hybrid Capacitors", 5), ("Mechanical Components", 5)],
                    "Dispersal Field": [("Conductive Components", 5), ("Hybrid Capacitors", 5), ("Irregular Emission Data", 5), ("Worn Shield Emitters", 5)],
                    "Double Braced": [("Mechanical Scrap", 5), ("Compact Composites", 5), ("Vanadium", 3)],
                    "Flow Control": [("Mechanical Scrap", 5), ("Hybrid Capacitors", 3), ("Modified Embedded Firmware", 1)],
                    "Multi-Servos": [("Mechanical Scrap", 5), ("Focus Crystals", 4), ("Conductive Polymers", 2), ("Configurable Components", 2)],
                    "Oversized": [("Mechanical Scrap", 5), ("Mechanical Components", 3), ("Ruthenium", 1)],
                    "Phasing Sequence": [("Focus Crystals", 5), ("Aberrant Shield Pattern Analysis", 3), ("Niobium", 3), ("Configurable Components", 3)],
                    "Plasma Slug": [("Heat Exchangers", 3), ("Modified Embedded Firmware", 2), ("Refined Focus Crystals", 2), ("Mercury", 4)],
                    "Stripped Down": [("Salvaged Alloys", 5), ("Carbon", 5), ("Tin", 1)],
                    "Target Lock Breaker": [("Selenium", 5), ("Security Firmware Patch", 3), ("Adaptive Encryptors Capture", 1)],
                    "Thermal Conduit": [("Heat Dispersion Plate", 5), ("Sulphur", 5), ("Tempered Alloys", 5)],
                },
            },
        }
    },
}
