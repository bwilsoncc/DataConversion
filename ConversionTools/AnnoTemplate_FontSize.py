# ---------------------------------------------------------------------------
# StdAnno_FontSize_subscript.py
# Created on: Thursday Nov 3, 2005
# By: Laura Gordon
# Usage: StdAnno_FontSize_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.addmessage("1")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
AnnoFeatureClass = sys.argv[1]
gp.addmessage("2")

# Process: Calculate the field FontSize to equal field MAPSIZE (original sizes)
gp.CalculateField_management(AnnoFeatureClass, "FontSize", "[MAPSIZE]")
gp.addmessage("CALCULATED FontSize to equal Mapsize!!!")
gp.addmessage("3")
