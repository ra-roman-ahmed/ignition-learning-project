# import win32com.client
# import pandas as pd
# import shutil
# import os
# import time
# import pywintypes

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# acad.Visible = True

# def com_retry(func, retries=15, delay=0.5):
#     """COM call busy thakle retry kore, AutoCAD-ke shomoy dey."""
#     last_error = None
#     for attempt in range(retries):
#         try:
#             return func()
#         except pywintypes.com_error as e:
#             if e.args[0] == -2147418111:  # Call was rejected by callee
#                 last_error = e
#                 time.sleep(delay)
#                 continue
#             else:
#                 raise
#     raise last_error

# # --- Excel read koro ---
# df = pd.read_excel(r"C:\user c folder\Downloads\IO_List.xlsx", sheet_name="Sheet1")
# print(f"Total rows: {len(df)}")

# template_folder = r"C:\Users\Yasir iT\My Documents\AcadE 2023\AeData\proj\Demo"
# output_folder = r"C:\Users\Yasir iT\My Documents\AcadE 2023\AeData\proj\Demo\Generated"

# os.makedirs(output_folder, exist_ok=True)

# target_handle = "137"   # PB414A_TEST block - amader test target

# for index, row in df.iterrows():
#     template_path = os.path.join(template_folder, "demo08_TEST.dwg")
#     output_path = os.path.join(output_folder, row["Output_File"])

#     # Purono output file thakle age delete koro (fresh copy nishchit korার jonno)
#     if os.path.exists(output_path):
#         os.remove(output_path)

#     # Step 1: template copy koro notun file hishebe
#     shutil.copy(template_path, output_path)
#     print(f"\n[{index+1}/{len(df)}] Copied template -> {row['Output_File']}")

#     doc = None
#     try:
#         # Step 2: notun file open koro (retry shoho)
#         doc = com_retry(lambda: acad.Documents.Open(output_path))
#         time.sleep(1)  # AutoCAD-ke drawing pura load korার shomoy dao

#         mspace = com_retry(lambda: doc.ModelSpace)

#         # Step 3: target block khuje tag/desc update koro
#         target = com_retry(lambda: doc.HandleToObject(target_handle))
#         if target.HasAttributes:
#             attribs = target.GetAttributes()
#             for attr in attribs:
#                 if attr.TagString == "P_TAG1":
#                     attr.TextString = row["Tag"]
#                 elif attr.TagString == "DESC1":
#                     attr.TextString = row["Description"]

#         doc.Regen(1)

#         # Step 4: save kore close koro
#         doc.Save()
#         doc.Close()
#         print(f"   Saved and closed: {row['Output_File']}")

#     except Exception as e:
#         print(f"   ERROR on {row['Output_File']}: {e}")
#         if doc is not None:
#             try:
#                 doc.Close(False)  # save na kore forcefully close
#             except:
#                 pass

# print("\nAll drawings generated!")


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

# --- Symbol naam -> existing block Handle mapping ---
symbol_map = {
    "PushButton": "137",   # NPAB8TA - PB414A_TEST position
    "PilotLight": "1A1",   # NPAB8TSR - POWER ON position
}

# --- Excel read koro ---
df = pd.read_excel(r"C:\user c folder\Downloads\IO_List.xlsx", sheet_name="Sheet1")
print(f"Total rows: {len(df)}")

template_folder = r"C:\Users\Yasir iT\My Documents\AcadE 2023\AeData\proj\Demo"
output_folder = r"C:\Users\Yasir iT\My Documents\AcadE 2023\AeData\proj\Demo\Generated"

os.makedirs(output_folder, exist_ok=True)

for index, row in df.iterrows():
    template_path = os.path.join(template_folder, "demo08_TEST.dwg")
    output_path = os.path.join(output_folder, row["Output_File"])

    if os.path.exists(output_path):
        os.remove(output_path)

    shutil.copy(template_path, output_path)
    print(f"\n[{index+1}/{len(df)}] Copied template -> {row['Output_File']} (Symbol: {row['Symbol']})")

    doc = None
    try:
        doc = com_retry(lambda: acad.Documents.Open(output_path))
        time.sleep(1)

        mspace = com_retry(lambda: doc.ModelSpace)

        # --- Symbol column dekhe target handle decide koro ---
        symbol_name = row["Symbol"]
        if symbol_name not in symbol_map:
            print(f"   WARNING: Unknown symbol '{symbol_name}', skipping row.")
            doc.Close(False)
            continue

        target_handle = symbol_map[symbol_name]
        target = com_retry(lambda: doc.HandleToObject(target_handle))

        if target.HasAttributes:
            attribs = target.GetAttributes()
            for attr in attribs:
                if attr.TagString == "P_TAG1":
                    attr.TextString = row["Tag"]
                elif attr.TagString == "DESC1":
                    attr.TextString = row["Description"]

        doc.Regen(1)
        doc.Save()
        doc.Close()
        print(f"   Saved and closed: {row['Output_File']} (used {symbol_name} block)")

    except Exception as e:
        print(f"   ERROR on {row['Output_File']}: {e}")
        if doc is not None:
            try:
                doc.Close(False)
            except:
                pass

print("\nAll drawings generated!")