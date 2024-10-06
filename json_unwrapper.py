#!/usr/bin/python3

import json

inp = input()
data = json.loads(inp)
new_data = {}
new_data["include"] = []
for el in data.get("include"):
    names = el.get("name")
    boards = el.get("board")
    shields = el.get("shield")
    flags = el.get("flags")
    if type(names) != list:
        names = [names]
    if type(boards) != list:
        boards = [boards]
    if type(shields) != list:
        shields = [shields]
    if flags is not None and type(flags) != list:
        flags = [flags]
    for name in names:
        for board in boards:
            for shield in shields:
                new_el = {}
                if name is not None:
                    new_el["name"] = name.replace(" ", "\ ")
                    new_el["file_name_suffix"] = "-" + name.replace(" ", "-").lower()
                else:
                    new_el["file_name_suffix"] = ""
                new_el["board"] = board
                if shield is not None:
                    new_el["shield"] = shield
                if flags:
                    new_el["flags"] = ""
                    if "no_crystal" in flags:
                        new_el["flags"] += (
                            "-DCONFIG_CLOCK_CONTROL_NRF=y "
                            "-DCONFIG_CLOCK_CONTROL_NRF_K32SRC_RC=y "
                            "-DCONFIG_CLOCK_CONTROL_NRF_K32SRC_500PPM=y "
                        )
                    if "screen" in flags:
                        new_el["flags"] += r"-DCONFIG_ZMK_DISPLAY=y "
                    if "no_mono" in flags:
                        new_el["flags"] += r"-DCONFIG_LV_USE_THEME_MONO=n "
                    if "studio" in flags:
                        new_el["flags"] += r"-DCONFIG_ZMK_STUDIO=y "
                        new_el["snippets"] += r"studio-rpc-usb-uart "
                new_data["include"].append(new_el)
print(json.dumps(new_data))
