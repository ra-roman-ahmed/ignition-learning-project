# import win32com.client
# import pandas as pd
# import shutil
# import os
# import time
# import pywintypes

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# acad.Visible = True

# def com_retry(func, retries=15, delay=0.5):
#     last_error = None
#     for attempt in range(retries):
#         try:
#             return func()
#         except pywintypes.com_error as e:
#             if e.args[0] == -2147418111:
#                 last_error = e
#                 time.sleep(delay)
#                 continue
#             else:
#                 raise
#     raise last_error

# BLOCK_A_HANDLE = "4C1B"
# BLOCK_B_HANDLE = "4D79"

# FIELD_DEVICE_HANDLES = {
#     1: "4F0F", 2: "505D", 3: "5098", 4: "50D3",
#     5: "510E", 6: "5149", 7: "5184", 8: "51BF",
#     9: "5205", 10: "5241", 11: "527C", 12: "52B7",
#     13: "52F2", 14: "532D", 15: "5368", 16: "53A3",
# }

# NO_SYMBOL_HANDLE = "5625"
# NC_SYMBOL_HANDLE = "5668"

# # --- Ei value ta tune korার jonno, choto/boro test kore adjust koro ---
# EXTRA_SCALE_MULTIPLIER = 0.3   # <-- shurute 0.3 diye test koro, dorkar hole 0.2/0.4 try koro

# template_path = r"I:\My Drive\ROMAN_AUTOCAD\5069-IB16-DI TEMPLATE_TEST.dwg"
# output_folder = r"I:\My Drive\ROMAN_AUTOCAD\Generated"
# os.makedirs(output_folder, exist_ok=True)

# df = pd.read_excel(r"I:\My Drive\ROMAN_AUTOCAD\DI_IO_LIST.xlsx", sheet_name="Sheet1")
# print(f"Total rows: {len(df)}")

# grouped = df.groupby("Output_File")

# for output_file, group in grouped:
#     output_path = os.path.join(output_folder, output_file)

#     if os.path.exists(output_path):
#         os.remove(output_path)

#     shutil.copy(template_path, output_path)
#     print(f"\n=== Generating {output_file} ({len(group)} points) ===")

#     doc = None
#     try:
#         doc = com_retry(lambda: acad.Documents.Open(output_path))
#         time.sleep(1.5)

#         pspace = com_retry(lambda: doc.PaperSpace)

#         block_a = com_retry(lambda: doc.HandleToObject(BLOCK_A_HANDLE))
#         block_b = com_retry(lambda: doc.HandleToObject(BLOCK_B_HANDLE))

#         no_template = com_retry(lambda: doc.HandleToObject(NO_SYMBOL_HANDLE))
#         nc_template = com_retry(lambda: doc.HandleToObject(NC_SYMBOL_HANDLE))

#         for _, row in group.iterrows():
#             point = int(row["Point"])
#             target_block = block_a if point <= 8 else block_b

#             attribs = target_block.GetAttributes()
#             for attr in attribs:
#                 if attr.TagString == f"TAG{point}":
#                     attr.TextString = str(row["Tag"])
#                 elif attr.TagString == f"DESC{point}":
#                     attr.TextString = str(row["Desc1"])
#                 elif attr.TagString == f"DESC{point}.2":
#                     attr.TextString = str(row["Desc2"]) if pd.notna(row["Desc2"]) else ""

#             fd_handle = FIELD_DEVICE_HANDLES[point]
#             old_circle = doc.HandleToObject(fd_handle)

#             old_pt = old_circle.InsertionPoint
#             old_xscale = old_circle.XScaleFactor
#             old_yscale = old_circle.YScaleFactor
#             old_zscale = old_circle.ZScaleFactor
#             old_rotation = old_circle.Rotation

#             contact_type = str(row["Contact_Type"]).strip().upper()
#             template_symbol = no_template if contact_type == "NO" else nc_template

#             new_symbol = template_symbol.Copy()

#             move_from = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, template_symbol.InsertionPoint)
#             move_to = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, old_pt)
#             new_symbol.Move(move_from, move_to)

#             # --- Scale: old circle-er scale x extra multiplier (choto korার jonno) ---
#             new_symbol.XScaleFactor = old_xscale * EXTRA_SCALE_MULTIPLIER
#             new_symbol.YScaleFactor = old_yscale * EXTRA_SCALE_MULTIPLIER
#             new_symbol.ZScaleFactor = old_zscale
#             new_symbol.Rotation = old_rotation

#             if new_symbol.HasAttributes:
#                 for attr in new_symbol.GetAttributes():
#                     if attr.TagString == "P_TAG1":
#                         attr.TextString = str(row["Tag"])

#             old_circle.Delete()

#             print(f"   Point {point}: {row['Tag']} | Contact: {contact_type}")

#         # --- Purono boro template symbol duita (leftover) delete kore dao ---
#         no_template.Delete()
#         nc_template.Delete()
#         print("   Removed leftover oversized template symbols.")

#         doc.Regen(1)
#         doc.Save()
#         doc.Close()
#         print(f"   Saved and closed: {output_file}")

#     except Exception as e:
#         print(f"   ERROR on {output_file}: {e}")
#         if doc is not None:
#             try:
#                 doc.Close(False)
#             except:
#                 pass

# print("\nAll DI card drawings generated!")


# import win32com.client
# import pandas as pd
# import shutil
# import os
# import time
# import pywintypes

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# acad.Visible = True

# def com_retry(func, retries=15, delay=0.5):
#     last_error = None
#     for attempt in range(retries):
#         try:
#             return func()
#         except pywintypes.com_error as e:
#             if e.args[0] == -2147418111:
#                 last_error = e
#                 time.sleep(delay)
#                 continue
#             else:
#                 raise
#     raise last_error

# BLOCK_A_HANDLE = "4C1B"
# BLOCK_B_HANDLE = "4D79"

# FIELD_DEVICE_HANDLES = {
#     1: "4F0F", 2: "505D", 3: "5098", 4: "50D3",
#     5: "510E", 6: "5149", 7: "5184", 8: "51BF",
#     9: "5205", 10: "5241", 11: "527C", 12: "52B7",
#     13: "52F2", 14: "532D", 15: "5368", 16: "53A3",
# }

# NO_SYMBOL_HANDLE = "5625"
# NC_SYMBOL_HANDLE = "5668"

# # --- Ei value ta tune korার jonno, choto/boro test kore adjust koro ---
# EXTRA_SCALE_MULTIPLIER = 0.3   # <-- shurute 0.3 diye test koro, dorkar hole 0.2/0.4 try koro

# # --- NO/NC symbol-ke "3-WIRE FD" (+/-/G) block er pashe boshanor jonno offset ---
# # Negative OFFSET_X = left dike shift, Positive = right dike shift
# # OFFSET_Y = 0 mane same row-e thakবে (up/down shift na hole 0-i rakho)
# # Eি value-o tune korte hobe — ekটা card generate kore visually check koro,
# # tarpor -0.3 / -0.7 / -1.0 etc try kore thik gap khuje নাও।
# OFFSET_X = -0.5
# OFFSET_Y = 0.0

# template_path = r"I:\My Drive\ROMAN_AUTOCAD\5069-IB16-DI TEMPLATE_TEST.dwg"
# output_folder = r"I:\My Drive\ROMAN_AUTOCAD\Generated"
# os.makedirs(output_folder, exist_ok=True)

# df = pd.read_excel(r"I:\My Drive\ROMAN_AUTOCAD\DI_IO_LIST.xlsx", sheet_name="Sheet1")
# print(f"Total rows: {len(df)}")

# grouped = df.groupby("Output_File")

# for output_file, group in grouped:
#     output_path = os.path.join(output_folder, output_file)

#     if os.path.exists(output_path):
#         os.remove(output_path)

#     shutil.copy(template_path, output_path)
#     print(f"\n=== Generating {output_file} ({len(group)} points) ===")

#     doc = None
#     try:
#         doc = com_retry(lambda: acad.Documents.Open(output_path))
#         time.sleep(1.5)

#         pspace = com_retry(lambda: doc.PaperSpace)

#         block_a = com_retry(lambda: doc.HandleToObject(BLOCK_A_HANDLE))
#         block_b = com_retry(lambda: doc.HandleToObject(BLOCK_B_HANDLE))

#         no_template = com_retry(lambda: doc.HandleToObject(NO_SYMBOL_HANDLE))
#         nc_template = com_retry(lambda: doc.HandleToObject(NC_SYMBOL_HANDLE))

#         for _, row in group.iterrows():
#             point = int(row["Point"])
#             target_block = block_a if point <= 8 else block_b

#             attribs = target_block.GetAttributes()
#             for attr in attribs:
#                 if attr.TagString == f"TAG{point}":
#                     attr.TextString = str(row["Tag"])
#                 elif attr.TagString == f"DESC{point}":
#                     attr.TextString = str(row["Desc1"])
#                 elif attr.TagString == f"DESC{point}.2":
#                     attr.TextString = str(row["Desc2"]) if pd.notna(row["Desc2"]) else ""

#             fd_handle = FIELD_DEVICE_HANDLES[point]
#             # NOTE: eta-i "3-WIRE FD" block (+/-/G) — ETA DELETE HOBE NA,
#             # shudhu reference position/scale/rotation nite use hocche.
#             old_circle = doc.HandleToObject(fd_handle)

#             old_pt = old_circle.InsertionPoint
#             old_xscale = old_circle.XScaleFactor
#             old_yscale = old_circle.YScaleFactor
#             old_zscale = old_circle.ZScaleFactor
#             old_rotation = old_circle.Rotation

#             contact_type = str(row["Contact_Type"]).strip().upper()
#             template_symbol = no_template if contact_type == "NO" else nc_template

#             new_symbol = template_symbol.Copy()

#             # --- Target position = FD block-er position + offset (pashe boshanor jonno) ---
#             target_pt = (old_pt[0] + OFFSET_X, old_pt[1] + OFFSET_Y, old_pt[2])

#             move_from = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, template_symbol.InsertionPoint)
#             move_to = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, target_pt)
#             new_symbol.Move(move_from, move_to)

#             # --- Scale: old circle-er scale x extra multiplier (choto korার jonno) ---
#             new_symbol.XScaleFactor = old_xscale * EXTRA_SCALE_MULTIPLIER
#             new_symbol.YScaleFactor = old_yscale * EXTRA_SCALE_MULTIPLIER
#             new_symbol.ZScaleFactor = old_zscale
#             new_symbol.Rotation = old_rotation

#             if new_symbol.HasAttributes:
#                 for attr in new_symbol.GetAttributes():
#                     if attr.TagString == "P_TAG1":
#                         attr.TextString = str(row["Tag"])

#             # old_circle.Delete()  <-- REMOVED: "3-WIRE FD" (+/-/G) block ekhon r delete hobe na, thakবে।

#             print(f"   Point {point}: {row['Tag']} | Contact: {contact_type}")

#         # --- Master template symbol duita (staging copies, single instance) delete kore dao ---
#         no_template.Delete()
#         nc_template.Delete()
#         print("   Removed leftover master template symbols.")

#         doc.Regen(1)
#         doc.Save()
#         doc.Close()
#         print(f"   Saved and closed: {output_file}")

#     except Exception as e:
#         print(f"   ERROR on {output_file}: {e}")
#         if doc is not None:
#             try:
#                 doc.Close(False)
#             except:
#                 pass

# print("\nAll DI card drawings generated!")


import win32com.client
import pandas as pd
import shutil
import os
import time
import pywintypes

acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
acad.Visible = True

def com_retry(func, retries=15, delay=0.5):
    last_error = None
    for attempt in range(retries):
        try:
            return func()
        except pywintypes.com_error as e:
            if e.args[0] == -2147418111:
                last_error = e
                time.sleep(delay)
                continue
            else:
                raise
    raise last_error

# --- Main DI block handles (16-point card, split into 2 blocks) ---
BLOCK_A_HANDLE = "4C1B"   # 5069-IB16-DI1 -> Point 1-8
BLOCK_B_HANDLE = "4D79"   # 5069-IB16-DI2 -> Point 9-16

# --- Field-device (3-WIRE FD) handles, per point - reference point for NO/NC placement ---
FIELD_DEVICE_HANDLES = {
    1: "4F0F", 2: "505D", 3: "5098", 4: "50D3",
    5: "510E", 6: "5149", 7: "5184", 8: "51BF",
    9: "5205", 10: "5241", 11: "527C", 12: "52B7",
    13: "52F2", 14: "532D", 15: "5368", 16: "53A3",
}

# --- NO/NC template symbol handles (in template file, oversized originals) ---
NO_SYMBOL_HANDLE = "5625"   # ABSS3LM
NC_SYMBOL_HANDLE = "5668"   # ABPPB010R

# --- Tuning values - test kore adjust koro ---
EXTRA_SCALE_MULTIPLIER = 0.3   # NO/NC symbol koto choto hobe
X_OFFSET = 0.8                # field device theke koto bame boshbe
Y_OFFSET = 0.2

# --- Paths ---
template_path = r"I:\My Drive\ROMAN_AUTOCAD\5069-IB16-DI TEMPLATE_TEST.dwg"
output_folder = r"I:\My Drive\ROMAN_AUTOCAD\Generated"
os.makedirs(output_folder, exist_ok=True)

# --- Excel read koro ---
df = pd.read_excel(r"I:\My Drive\ROMAN_AUTOCAD\DI_IO_LIST.xlsx", sheet_name="Sheet1")
print(f"Total rows: {len(df)}")

grouped = df.groupby("Output_File")

for output_file, group in grouped:
    output_path = os.path.join(output_folder, output_file)

    if os.path.exists(output_path):
        os.remove(output_path)

    shutil.copy(template_path, output_path)
    print(f"\n=== Generating {output_file} ({len(group)} points) ===")

    doc = None
    try:
        doc = com_retry(lambda: acad.Documents.Open(output_path))
        time.sleep(1.5)

        pspace = com_retry(lambda: doc.PaperSpace)

        block_a = com_retry(lambda: doc.HandleToObject(BLOCK_A_HANDLE))
        block_b = com_retry(lambda: doc.HandleToObject(BLOCK_B_HANDLE))

        no_template = com_retry(lambda: doc.HandleToObject(NO_SYMBOL_HANDLE))
        nc_template = com_retry(lambda: doc.HandleToObject(NC_SYMBOL_HANDLE))

        for _, row in group.iterrows():
            point = int(row["Point"])
            target_block = block_a if point <= 8 else block_b

            # --- 1. TAG/DESC attribute update ---
            attribs = target_block.GetAttributes()
            for attr in attribs:
                if attr.TagString == f"TAG{point}":
                    attr.TextString = str(row["Tag"])
                elif attr.TagString == f"DESC{point}":
                    attr.TextString = str(row["Desc1"])
                elif attr.TagString == f"DESC{point}.2":
                    attr.TextString = str(row["Desc2"]) if pd.notna(row["Desc2"]) else ""

            # --- 2. Field-device (3-WIRE FD) - UNCHANGED, shudhu reference point hisebe use kori ---
            fd_handle = FIELD_DEVICE_HANDLES[point]
            fd_block = doc.HandleToObject(fd_handle)

            fd_pt = fd_block.InsertionPoint
            fd_xscale = fd_block.XScaleFactor
            fd_yscale = fd_block.YScaleFactor
            fd_zscale = fd_block.ZScaleFactor
            fd_rotation = fd_block.Rotation

            # --- 3. NO/NC symbol - field device-er bame boshabe ---
            contact_type = str(row["Contact_Type"]).strip().upper()
            template_symbol = no_template if contact_type == "NO" else nc_template

            new_symbol = template_symbol.Copy()

            target_x = fd_pt[0] - X_OFFSET
            target_y = fd_pt[1] - Y_OFFSET

            move_from = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, template_symbol.InsertionPoint)
            move_to = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (target_x, target_y, 0.0))
            new_symbol.Move(move_from, move_to)

            new_symbol.XScaleFactor = fd_xscale * EXTRA_SCALE_MULTIPLIER
            new_symbol.YScaleFactor = fd_yscale * EXTRA_SCALE_MULTIPLIER
            new_symbol.ZScaleFactor = fd_zscale
            new_symbol.Rotation = fd_rotation

            if new_symbol.HasAttributes:
                for attr in new_symbol.GetAttributes():
                    if attr.TagString == "P_TAG1":
                        attr.TextString = str(row["Tag"])

            print(f"   Point {point}: {row['Tag']} | {row['Desc1']} | Contact: {contact_type}")

        # --- Purono boro template symbol duita (leftover) delete kore dao ---
        no_template.Delete()
        nc_template.Delete()
        print("   Removed leftover oversized template symbols.")

        doc.Regen(1)
        doc.Save()
        doc.Close()
        print(f"   Saved and closed: {output_file}")

    except Exception as e:
        print(f"   ERROR on {output_file}: {e}")
        if doc is not None:
            try:
                doc.Close(False)
            except:
                pass

print("\nAll DI card drawings generated!")