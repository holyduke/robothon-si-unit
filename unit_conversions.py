# length [mm]
units_length_pattern = r"km|m|cm|dm|mm|\"|inch|inches"
units_length_conversions = {
    "km": 1000000,
    "m": 1000,
    "dm": 100,
    "cm": 10,
    "mm": 1,
    "inch": 25.4,
}

# weight [g]
units_weight_pattern = r"kg|g|t"
units_weight_conversions = {
    "t": 1_000_000,
    "kg": 1_000,
    "g": 1,
}

# power [W]
units_power_pattern = r"kW|W|MW"
units_power_conversions = {
    "MW": 1_000_000,
    "kW": 1_000,
    "W": 1,
}

# frequency [Hz]
units_freq_pattern = r"Hz|kHz"
units_freq_conversions = {
    "kHz": 1_000,
    "Hz": 1,
}

# time [s]
units_time_pattern = r"h|dnů|dnu|d|min|ms|ns"
units_time_conversions = {
    "dnů": 86_400,
    "dnu": 86_400,
    "d": 86_400,
    "h": 3_600,
    "min": 60,
    "s": 1,
    "ms": 0.001,
    "ns": 0.000001,
}

# storage [MB]
units_storage_pattern = r"TB|GB|MB|KB"
units_storage_conversions = {
    "TB": 1_000_000 ,
    "GB": 1_000,
    "MB": 1,
    "KB": 0.001,
}