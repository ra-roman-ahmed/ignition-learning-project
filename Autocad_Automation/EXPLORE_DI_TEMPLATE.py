# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument

# print("Active document:", doc.Name)
# print("Total layouts:", doc.Layouts.Count)
# for layout in doc.Layouts:
#     print(" - Layout:", layout.Name)

# print("\nSearching Paper Space...")
# print("-" * 60)

# pspace = doc.PaperSpace

# for entity in pspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.HasAttributes:
#         attribs = entity.GetAttributes()
#         print(f"\nBlock: {entity.EffectiveName} (Handle: {entity.Handle})")
#         for attr in attribs:
#             print(f"   {attr.TagString} = '{attr.TextString}'")

# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# print("Active document:", doc.Name)
# print("Full path:", doc.FullName)


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# pspace = doc.PaperSpace

# for entity in pspace:
#     if entity.ObjectName == "AcDbBlockReference" and entity.HasAttributes:
#         attribs = entity.GetAttributes()
#         for attr in attribs:
#             if attr.TagString == "TAG1":
#                 print(f"BLOCK A (points 1-8) -> Name: {entity.EffectiveName}, Handle: {entity.Handle}")
#             if attr.TagString == "TAG9":
#                 print(f"BLOCK B (points 9-16) -> Name: {entity.EffectiveName}, Handle: {entity.Handle}")


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# pspace = doc.PaperSpace

# print("Newly inserted blocks (Handle > 55E8):")
# print("-" * 60)

# for entity in pspace:
#     if entity.ObjectName == "AcDbBlockReference":
#         try:
#             handle_int = int(entity.Handle, 16)
#             if handle_int > int("55E8", 16):
#                 print(f"\nBlock: {entity.EffectiveName} (Handle: {entity.Handle})")
#                 if entity.HasAttributes:
#                     attribs = entity.GetAttributes()
#                     for attr in attribs:
#                         print(f"   {attr.TagString} = '{attr.TextString}'")
#         except:
#             continue


# import win32com.client

# acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
# doc = acad.ActiveDocument
# pspace = doc.PaperSpace

# # Point 1-er "3-WIRE FD" (Handle 4F0F)-er insertion point ber kori age
# ref = doc.HandleToObject("4F0F")
# target_x, target_y = ref.InsertionPoint[0], ref.InsertionPoint[1]
# tolerance = 0.05

# print(f"Searching entities near ({target_x:.3f}, {target_y:.3f})...")
# print("-" * 60)

# for entity in pspace:
#     try:
#         pt = entity.InsertionPoint
#     except:
#         continue
#     if abs(pt[0] - target_x) < tolerance and abs(pt[1] - target_y) < tolerance:
#         name = entity.EffectiveName if entity.ObjectName == "AcDbBlockReference" else entity.ObjectName
#         has_attr = entity.HasAttributes if entity.ObjectName == "AcDbBlockReference" else "N/A"
#         print(f"ObjectName: {entity.ObjectName} | Name: {name} | Handle: {entity.Handle} | HasAttributes: {has_attr}")



import win32com.client
 
acad = win32com.client.Dispatch("AutoCAD.Application.24.2")
doc = acad.ActiveDocument
pspace = doc.PaperSpace
 
# Point 1-er "3-WIRE FD" (Handle 4F0F)-er insertion point ber kori age (reference)
ref = doc.HandleToObject("4F0F")
target_x, target_y = ref.InsertionPoint[0], ref.InsertionPoint[1]
tolerance = 0.5   # <-- widen kora holo, age 0.05 chilo, tai circle miss hoye gesilo
 
print(f"Reference (3-WIRE FD) at ({target_x:.3f}, {target_y:.3f})")
print("-" * 70)
 
for entity in pspace:
    obj_name = entity.ObjectName
    x = y = None
    try:
        if obj_name == "AcDbCircle":
            # Circle-er InsertionPoint thake na, Center thake -- eta-i age miss hoyechilo
            c = entity.Center
            x, y = c[0], c[1]
        elif hasattr(entity, "InsertionPoint"):
            pt = entity.InsertionPoint
            x, y = pt[0], pt[1]
    except:
        continue
 
    if x is None:
        continue
 
    if abs(x - target_x) < tolerance and abs(y - target_y) < tolerance:
        name = entity.EffectiveName if obj_name == "AcDbBlockReference" else obj_name
        has_attr = entity.HasAttributes if obj_name == "AcDbBlockReference" else "N/A"
        text_val = ""
        if obj_name in ("AcDbText", "AcDbMText"):
            try:
                text_val = entity.TextString
            except:
                pass
        print(f"ObjectName: {obj_name} | Name: {name} | Handle: {entity.Handle} | "
              f"HasAttributes: {has_attr} | Pos: ({x:.3f},{y:.3f}) | Text: '{text_val}'")
 
print("-" * 70)
print("Done.")