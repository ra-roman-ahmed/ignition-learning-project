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
print("ModelSpace object found!")