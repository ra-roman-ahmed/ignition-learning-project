import win32com.client

print("Connecting to AutoCAD...")

acad = win32com.client.Dispatch("AutoCAD.Application.24.2")

acad.Visible = True

doc = acad.ActiveDocument

print("Connected to:", doc.Name)
print("Layout:", doc.ActiveLayout.Name)


import win32com.client

print("Connecting to AutoCAD...")

acad = win32com.client.Dispatch("AutoCAD.Application.24.2")

print("AutoCAD connected!")
print("Application:", acad.Name)
print("Version:", acad.Version)
print("Visible:", acad.Visible)

doc = acad.ActiveDocument

print("Active document found!")
print("Active document acquired successfully!")
doc.SendCommand('_.ZOOM _E ')
print("Zoom command sent successfully!")