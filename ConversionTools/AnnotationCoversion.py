# ---------------------------------------------------------------------------
# AnnotationCoversion.py
# Updated on: Tue Dec 21
#   (generated by ArcGIS/ModelBuilder)
# Usage: AnnotationCoversion <Anno1200scale> <AnnoClass 0> ... <AnnoClass 15> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, win32com.client

# Create the Geoprocessor object
gp = win32com.client.Dispatch("esriGeoprocessing.GpDispatch.1")

# Script arguments...
AnnoFC = sys.argv[1]
AnnoClass0 = int(sys.argv[2])
AnnoClass1 = int(sys.argv[3])
AnnoClass2 = int(sys.argv[4])
AnnoClass3 = int(sys.argv[5])
AnnoClass4 = int(sys.argv[6])
AnnoClass5 = int(sys.argv[7])
AnnoClass6 = int(sys.argv[8])
AnnoClass7 = int(sys.argv[9])
AnnoClass8 = int(sys.argv[10])
AnnoClass9 = int(sys.argv[11])
AnnoClass10 = int(sys.argv[12])
AnnoClass11 = int(sys.argv[13])
AnnoClass12 = int(sys.argv[14])
AnnoClass13 = int(sys.argv[15])
AnnoClass14 = int(sys.argv[16])
AnnoClass15 = int(sys.argv[17])
gp.addmessage("Set argument values")


# Process: Add Fields To PreServe Current Settings...
gp.AddField_management(AnnoFC, "FontSize2", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "", )
gp.AddField_management(AnnoFC, "VertAlign2", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "", )
gp.AddField_management(AnnoFC, "HorzAlign2", "SHORT", "", "", "", "", "NULLABLE", "NON_REQUIRED", "", )
gp.AddField_management(AnnoFC, "XOffset2", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "", )
gp.AddField_management(AnnoFC, "YOffset2", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "", )
gp.AddField_management(AnnoFC, "Angle2", "DOUBLE", "", "", "", "", "NULLABLE", "NON_REQUIRED", "", )
gp.addmessage("Added fields: Fontsize2, VertAlign2, HorzAlign2, XOffset2, YOffset2, Angle2...")


# Process: Calculate Fields To Preserve Current Settings...
gp.CalculateField_management(AnnoFC, "FontSize2", "[FontSize]", )
gp.addmessage("Calculated Fontsize2...")
gp.CalculateField_management(AnnoFC, "VertAlign2", "[VerticalAlignment]", )
gp.addmessage("Calculated VertAlign2...")
gp.CalculateField_management(AnnoFC, "HorzAlign2", "[HorizontalAlignment]",)
gp.addmessage("Calculated HorzAlign2...")
gp.CalculateField_management(AnnoFC, "XOffset2", "[XOffset]", )
gp.addmessage("Calculated XOffset2...")
gp.CalculateField_management(AnnoFC, "YOffset2", "[YOffset]", )
gp.addmessage("Calculated YOffset2...")
gp.CalculateField_management(AnnoFC, "Angle2", "[Angle]", )
gp.addmessage("Calculated Angle2...")
    
    
# Process: Select Each AnnotationClassID And Calculate the new SymbolID
if AnnoClass0 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 0", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass0, )
    gp.addmessage("Calculated SymbolID for AnnoClass0")
    
if AnnoClass1 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 1", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass1, )
    gp.addmessage("Calculated SymbolID for AnnoClass1")

if AnnoClass2 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 2", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass2, )
    gp.addmessage("Calculated SymbolID for AnnoClass2")
        
if AnnoClass3 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 3", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass3, )
    gp.addmessage("Calculated SymbolID for AnnoClass3")
        
if AnnoClass4 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 4", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass4, )
    gp.addmessage("Calculated SymbolID for AnnoClass4")
        
if AnnoClass5 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 5", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass5, )
    gp.addmessage("Calculated SymbolID for AnnoClass5")
        
if AnnoClass6 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 6", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass6, )
    gp.addmessage("Calculated SymbolID for AnnoClass6")
        
if AnnoClass7 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 7", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass7, )
    gp.addmessage("Calculated SymbolID for AnnoClass7")
        
if AnnoClass8 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 8", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass8, )
    gp.addmessage("Calculated SymbolID for AnnoClass8")
        
if AnnoClass9 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 9", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass9, )
    gp.addmessage("Calculated SymbolID for AnnoClass9")
        
if AnnoClass10 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 10", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass10, )
    gp.addmessage("Calculated SymbolID for AnnoClass10")
        
if AnnoClass11 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 11", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass11, )
    gp.addmessage("Calculated SymbolID for AnnoClass11")
        
if AnnoClass12 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 12", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass12, )
    gp.addmessage("Calculated SymbolID for AnnoClass12")
        
if AnnoClass13 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 13", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass13, )
    gp.addmessage("Calculated SymbolID for AnnoClass13")

if AnnoClass14 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 14", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass14, )
    gp.addmessage("Calculated SymbolID for AnnoClass14")
        
if AnnoClass15 < 999:
    gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[AnnotationClassID] = 15", )
    gp.CalculateField_management(AnnoFC, "SymbolID", AnnoClass15, )
    gp.addmessage("Calculated SymbolID for AnnoClass15")
    
    
# Process: Select All Features for following calculations
gp.SelectLayerByAttribute_management(AnnoFC, "NEW_SELECTION", "[OBJECTID] >= 0", )
gp.addmessage("Select all features")
    
    
# Process: Calculate Fields TO Retrieve Preserved Characteristics
gp.CalculateField_management(AnnoFC, "FontSize", "[FontSize2]", )
gp.addmessage("Calculated Fontsize...")
gp.CalculateField_management(AnnoFC, "VerticalAlignment", "[VertAlign2]", )
gp.addmessage("Calculated VerticalAlignment...")
gp.CalculateField_management(AnnoFC, "HorizontalAlignment", "[HorzAlign2]", )
gp.addmessage("Calculated HorizontalAlignment...")
gp.CalculateField_management(AnnoFC, "XOffset", "[XOffset2]", )
gp.addmessage("Calculated XOffset...")
gp.CalculateField_management(AnnoFC, "YOffset", "[YOffset2]", )
gp.addmessage("Calculated YOffset...")
gp.CalculateField_management(AnnoFC, "Angle", "[Angle2]", )
gp.addmessage("Calculated Angle...")

# Process: Delete Fields...
#gp.DeleteField_management(AnnoFC, "FontSize2;VertAlign2;HorzAlign2,XOffset2,YOffset2,Angle2")
gp.DeleteField_management(AnnoFC, "FontSize2;VertAlign2;HorzAlign2;XOffset2;YOffset2;Angle2")
gp.addmessage("Deleted fields: Fontsize2, VertAlign2, HorzAlign2, XOffset2, YOffset2, Angle2...")
