# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# print(f"Total objects in ModelSpace: {mspace.Count}")
# print("-" * 50)

# block_count = 0

# for entity in mspace:
#     if entity.ObjectName == "AcDbBlockReference":
#         block_count += 1
#         if entity.HasAttributes:
#             attribs = entity.GetAttributes()
#             print(f"\nBlock #{block_count}: {entity.EffectiveName} (Handle: {entity.Handle})")
#             for attr in attribs:
#                 print(f"   {attr.TagString} = '{attr.TextString}'")

# print("-" * 50)
# print(f"Total blocks with attributes: {block_count}")

# import win32com.client
# import shutil

# # Original file-er copy banao (path tomar system onujayi change koro)
# original = r"C:\Users\Yasir iT\My Documents\AcadE 2023\AeData\proj\Demo\demo08.dwg"
# backup = r"C:\Users\Yasir iT\My Documents\AcadE 2023\AeData\proj\Demo\demo08_TEST.dwg"
# shutil.copy(original, backup)
# print("Backup created:", backup)

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# for entity in mspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.HasAttributes:
#         attribs = entity.GetAttributes()
#         for attr in attribs:
#             if attr.TagString == "P_TAG1" and attr.TextString == "PB414A":
#                 attr.TextString = "PB414A_NEW"
#                 print("Tag changed: PB414A -> PB414A_NEW")

# doc.Regen(1)  # screen refresh

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # Handle diye specific ekta block target kora (safest way — 
# # Handle unique, tai bhul block change hobar risk nai)
# target_handle = "137"   # example: PB414A block, age tumar output theke dekhecho

# for entity in mspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.HasAttributes:
#         if entity.Handle == target_handle:
#             attribs = entity.GetAttributes()
#             for attr in attribs:
#                 if attr.TagString == "P_TAG1":
#                     print(f"Tag: {attr.TextString} -> PB414A_TEST")
#                     attr.TextString = "PB414A_TEST"
#                 elif attr.TagString == "DESC1":
#                     print(f"DESC1: {attr.TextString} -> CONVEYOR MOTOR (TEST)")
#                     attr.TextString = "CONVEYOR MOTOR (TEST)"
#                 elif attr.TagString == "DESC2":
#                     print(f"DESC2: {attr.TextString} -> STOP (TEST)")
#                     attr.TextString = "STOP (TEST)"

# doc.Regen(1)
# print("Done! AutoCAD-e giye screen check koro.")

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# target_handle = "159"   # PB422A block

# for entity in mspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.HasAttributes:
#         if entity.Handle == target_handle:
#             attribs = entity.GetAttributes()
#             for attr in attribs:
#                 if attr.TagString == "P_TAG1":
#                     print(f"Tag: {attr.TextString} -> PB422A_ROMAN")
#                     attr.TextString = "PB422A_ROMAN"
#                 elif attr.TagString == "DESC1":
#                     print(f"DESC1: {attr.TextString} -> ROMAN MOTOR")
#                     attr.TextString = "ROMAN MOTOR"
#                 elif attr.TagString == "DESC2":
#                     print(f"DESC2: {attr.TextString} -> STOP MOTOR")
#                     attr.TextString = "STOP MOTOR"

# doc.Regen(1)
# print("Done! AutoCAD-e giye screen check koro.")


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# for entity in mspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.HasAttributes:
#         pt = entity.InsertionPoint
#         print(f"{entity.EffectiveName} (Handle: {entity.Handle}) -> X={pt[0]:.3f}, Y={pt[1]:.3f}")

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # Empty slot - push button row-er next available position
# x, y = 13.375, 10.750

# insertion_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (x, y, 0.0))

# new_block = mspace.InsertBlock(insertion_pt, "NPAB8TA", 1.0, 1.0, 1.0, 0.0)
# print("New block inserted! Handle:", new_block.Handle)

# if new_block.HasAttributes:
#     attribs = new_block.GetAttributes()
#     for attr in attribs:
#         if attr.TagString == "P_TAG1":
#             attr.TextString = "MOTOR1"
#         elif attr.TagString == "DESC1":
#             attr.TextString = "RAM MOTOR"
#         elif attr.TagString == "DESC2":
#             attr.TextString = "STOP"

# doc.Regen(1)
# print("Done! AutoCAD screen check koro.")


#########################

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # --- Step 0: Purono broken insert (D5B) delete kore dao ---
# for entity in mspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.Handle == "D5B":
#         entity.Delete()
#         print("Old broken block deleted.")
#         break

# # --- Step 1: Template hishebe existing shothik push button (PB414A_TEST, Handle 137) use korbo ---
# template_handle = "137"
# template = None
# for entity in mspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.Handle == template_handle:
#         template = entity
#         break

# if template is None:
#     print("Template block not found!")
# else:
#     # --- Step 2: Notun 2-ta push button banabo, right side-e (empty slot: X=13.375, 15.375) ---
#     new_components = [
#         {"x": 13.375, "y": 10.750, "tag": "MOTOR1", "desc1": "RAM MOTOR", "desc2": "STOP"},
#         {"x": 15.375, "y": 10.750, "tag": "MOTOR2", "desc1": "WEB MOTOR", "desc2": "STOP"},
#     ]

#     tpt = template.InsertionPoint

#     for comp in new_components:
#         new_obj = template.Copy()  # clone kore full graphic+attribute+dynamic state
        
#         from_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (tpt[0], tpt[1], 0.0))
#         to_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (comp["x"], comp["y"], 0.0))
#         new_obj.Move(from_pt, to_pt)

#         if new_obj.HasAttributes:
#             attribs = new_obj.GetAttributes()
#             for attr in attribs:
#                 if attr.TagString == "P_TAG1":
#                     attr.TextString = comp["tag"]
#                 elif attr.TagString == "DESC1":
#                     attr.TextString = comp["desc1"]
#                 elif attr.TagString == "DESC2":
#                     attr.TextString = comp["desc2"]

#         print(f"Inserted {comp['tag']} at ({comp['x']}, {comp['y']}) -> Handle: {new_obj.Handle}")

# doc.Regen(1)
# print("Done! AutoCAD screen check koro.")



# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# target_x, target_y = 5.875, 10.750
# tolerance = 0.01

# print(f"Searching entities near ({target_x}, {target_y})...")
# print("-" * 60)

# for entity in mspace:
#     try:
#         pt = entity.InsertionPoint
#     except:
#         continue
#     if abs(pt[0] - target_x) < tolerance and abs(pt[1] - target_y) < tolerance:
#         name = entity.EffectiveName if entity.ObjectName == "AcDbBlockReference" else entity.ObjectName
#         has_attr = entity.HasAttributes if entity.ObjectName == "AcDbBlockReference" else "N/A"
#         print(f"ObjectName: {entity.ObjectName} | Name: {name} | Handle: {entity.Handle} | HasAttributes: {has_attr}")


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # --- Step 0: D65 (jodi ekhono exist kore) delete koro, HandleToObject diye ---
# try:
#     obj = doc.HandleToObject("D65")
#     obj.Delete()
#     print("Deleted broken block: D65")
# except Exception as e:
#     print("D65 already deleted or not found, skipping.")

# # --- Step 1: Duita template direct HandleToObject diye niye nao (loop lagbe na) ---
# template_graphic = doc.HandleToObject("55")    # ABPB3M - circle
# template_attrib = doc.HandleToObject("137")    # NPAB8TA - tag/desc box

# tpt = template_attrib.InsertionPoint

# new_components = [
#     {"x": 13.375, "y": 10.750, "tag": "MOTOR1", "desc1": "RAM MOTOR", "desc2": "STOP"},
#     {"x": 15.375, "y": 10.750, "tag": "MOTOR2", "desc1": "WEB MOTOR", "desc2": "STOP"},
# ]

# for comp in new_components:
#     from_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (tpt[0], tpt[1], 0.0))
#     to_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (comp["x"], comp["y"], 0.0))

#     new_graphic = template_graphic.Copy()
#     new_graphic.Move(from_pt, to_pt)

#     new_attrib = template_attrib.Copy()
#     new_attrib.Move(from_pt, to_pt)

#     if new_attrib.HasAttributes:
#         attribs = new_attrib.GetAttributes()
#         for attr in attribs:
#             if attr.TagString == "P_TAG1":
#                 attr.TextString = comp["tag"]
#             elif attr.TagString == "DESC1":
#                 attr.TextString = comp["desc1"]
#             elif attr.TagString == "DESC2":
#                 attr.TextString = comp["desc2"]

#     print(f"Inserted {comp['tag']} -> Graphic: {new_graphic.Handle}, Attrib: {new_attrib.Handle}")

# doc.Regen(1)
# print("Done! AutoCAD screen check koro.")

#############


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# target_x, target_y = 2.375, 19.250
# tolerance = 0.01

# print(f"Searching entities near ({target_x}, {target_y})...")
# print("-" * 60)

# for entity in mspace:
#     try:
#         pt = entity.InsertionPoint
#     except:
#         continue
#     if abs(pt[0] - target_x) < tolerance and abs(pt[1] - target_y) < tolerance:
#         name = entity.EffectiveName if entity.ObjectName == "AcDbBlockReference" else entity.ObjectName
#         has_attr = entity.HasAttributes if entity.ObjectName == "AcDbBlockReference" else "N/A"
#         print(f"ObjectName: {entity.ObjectName} | Name: {name} | Handle: {entity.Handle} | HasAttributes: {has_attr}")


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # --- Template blocks direct HandleToObject diye niye nao ---
# template_graphic = doc.HandleToObject("84")     # ABLT3R - circle+R letter
# template_attrib = doc.HandleToObject("1A1")     # NPAB8TSR - tag/desc box

# tpt = template_attrib.InsertionPoint

# # Notun position - bottom row-e empty slot (X=2.375, Y=10.750)
# x, y = 2.375, 10.750
# tag_name = "POWER2"
# desc1 = "POWER"
# desc2 = "ON"

# from_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (tpt[0], tpt[1], 0.0))
# to_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (x, y, 0.0))

# new_graphic = template_graphic.Copy()
# new_graphic.Move(from_pt, to_pt)

# new_attrib = template_attrib.Copy()
# new_attrib.Move(from_pt, to_pt)

# if new_attrib.HasAttributes:
#     attribs = new_attrib.GetAttributes()
#     for attr in attribs:
#         if attr.TagString == "P_TAG1":
#             attr.TextString = tag_name
#         elif attr.TagString == "DESC1":
#             attr.TextString = desc1
#         elif attr.TagString == "DESC2":
#             attr.TextString = desc2

# print(f"Inserted {tag_name} at ({x}, {y}) -> Graphic: {new_graphic.Handle}, Attrib: {new_attrib.Handle}")

# doc.Regen(1)
# print("Done! AutoCAD screen check koro.")



####################

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # --- Step 1: Ekta simple wire (line) banao + ekta sensor (existing block copy) ---
# p1 = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (0.0, 0.0, 0.0))
# p2 = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (2.0, 0.0, 0.0))
# wire = mspace.AddLine(p1, p2)

# sensor_template = doc.HandleToObject("84")   # ABLT3R - existing sensor/pilot symbol
# sensor = sensor_template.Copy()

# sensor_from_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, sensor_template.InsertionPoint)
# sensor.Move(sensor_from_pt, p1)

# # --- Step 2: Notun empty block definition banao ---
# basept = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (0.0, 0.0, 0.0))
# new_block_def = doc.Blocks.Add(basept, "SensorGroup1")

# # --- Step 3: Wire + sensor-ke notun block definition-er bhitore copy koro ---
# source_objects = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_DISPATCH, (wire, sensor))
# doc.CopyObjects(source_objects, new_block_def)

# # --- Step 4: Original wire+sensor (modelspace-e boshano copy) delete kore dao, template-i thakuk ---
# wire.Delete()
# sensor.Delete()

# print("SensorGroup1 block definition created!")

# # --- Step 5: Ekhon eta jekono jaigay 'place' koro ---
# place_pt1 = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (20.0, 5.0, 0.0))
# mspace.InsertBlock(place_pt1, "SensorGroup1", 1.0, 1.0, 1.0, 0.0)

# place_pt2 = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (25.0, 5.0, 0.0))
# mspace.InsertBlock(place_pt2, "SensorGroup1", 1.0, 1.0, 1.0, 0.0)

# doc.Regen(1)
# print("Placed SensorGroup1 at 2 locations!")

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # Notun kono jaigay, shudhu name diye call — kono wire/sensor notun kore banate hocche na
# place_pt3 = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (30.0, 5.0, 0.0))
# mspace.InsertBlock(place_pt3, "SensorGroup1", 1.0, 1.0, 1.0, 0.0)

# place_pt4 = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (35.0, 8.0, 0.0))
# mspace.InsertBlock(place_pt4, "SensorGroup1", 1.0, 1.0, 1.0, 0.0)

# doc.Regen(1)
# print("SensorGroup1 placed at 2 more locations!")



#####################
# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # --- Step 1: Duita wire + 1 sensor banao ---
# p_origin = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (0.0, 0.0, 0.0))
# p_mid    = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (2.0, 0.0, 0.0))
# p_up     = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (2.0, 1.5, 0.0))

# wire1 = mspace.AddLine(p_origin, p_mid)   # horizontal wire
# wire2 = mspace.AddLine(p_mid, p_up)       # vertical wire

# sensor_template = doc.HandleToObject("84")   # ABLT3R - same sensor symbol
# sensor = sensor_template.Copy()

# sensor_from_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, sensor_template.InsertionPoint)
# sensor.Move(sensor_from_pt, p_up)   # sensor-ta wire-er sheshe boshabe

# # --- Step 2: Notun empty block definition banao ---
# basept = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (0.0, 0.0, 0.0))
# new_block_def = doc.Blocks.Add(basept, "SensorGroup2")

# # --- Step 3: Duita wire + sensor-ke notun block definition-er bhitore copy koro ---
# source_objects = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_DISPATCH, (wire1, wire2, sensor))
# doc.CopyObjects(source_objects, new_block_def)

# # --- Step 4: Original wire+sensor delete kore dao (template-i thakuk) ---
# wire1.Delete()
# wire2.Delete()
# sensor.Delete()

# print("SensorGroup2 block definition created! (1 sensor + 2 wires)")

# doc.Regen(1)


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# mspace = doc.ModelSpace

# # --- Age-er creation code (comment out, ar dorkar nai — block already ache) ---
# # p_origin = win32com.client.VARIANT(...)
# # ... (pura creation part comment kore rakho ba delete kore dao)

# # --- Notun: SensorGroup2 place koro ---
# place_pt = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (40.0, 5.0, 0.0))
# mspace.InsertBlock(place_pt, "SensorGroup2", 1.0, 1.0, 1.0, 0.0)

# place_pt2 = win32com.client.VARIANT(win32com.client.pythoncom.VT_ARRAY | win32com.client.pythoncom.VT_R8, (45.0, 8.0, 0.0))
# mspace.InsertBlock(place_pt2, "SensorGroup2", 1.0, 1.0, 1.0, 0.0)

# doc.Regen(1)
# print("SensorGroup2 placed at 2 locations!")