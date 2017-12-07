# ---------------------------------------------------------------------------
# ConAll_WaterPoly_MakePoly_subscript.py
# Created on: Wednesday Nov 2, 2005
# By: Laura Gordon
# Usage: ConAll_WaterPoly_MakePoly_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.addmessage("1")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
WaterPoly_Feature2Poly = sys.argv[1]
WaterPoly = sys.argv[2]
gp.addmessage("2")

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(WaterPoly_Feature2Poly, "WaterPoly_MakeLayer", "", "", "AREA AREA HIDDEN;PERIMETER PERIMETER HIDDEN;WATER# WATER# HIDDEN;WATER-ID WATER-ID HIDDEN;WATERNAME WaterName VISIBLE;WATERTYPE WaterType VISIBLE;SOURCE Source VISIBLE;SOURCETYPE SourceType VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE")
gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.addmessage("3")
gp.Append_management("WaterPoly_MakeLayer", WaterPoly, "TEST", )
gp.addmessage("Executed Append")

