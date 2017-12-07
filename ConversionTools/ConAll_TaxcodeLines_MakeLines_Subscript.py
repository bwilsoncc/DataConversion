# ---------------------------------------------------------------------------
# TaxcodeLines_MakeLines_subscript.py
# Created on: Wednesday Nov 2, 2005
# By: Laura Gordon
# Usage: TaxcodeLines_MakeLines_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.addmessage("1")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
TaxcodeLine_Feature2Line = sys.argv[1]
TaxcodeLine = sys.argv[2]
gp.addmessage("2")

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(TaxcodeLine_Feature2Line, "TaxcodeLine_MakeLayer", "", "", "FNODE# FNODE# HIDDEN;TNODE# TNODE# HIDDEN;LPOLY# LPOLY# HIDDEN;RPOLY# RPOLY# HIDDEN;LENGTH LENGTH HIDDEN;TAXCODE# TAXCODE# HIDDEN;TAXCODE-ID TAXCODE-ID HIDDEN;CURRENTLINE CurrentLine VISIBLE")
gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.addmessage("3")
gp.Append_management("TaxcodeLine_MakeLayer", TaxcodeLine, "TEST", )
gp.addmessage("Executed Append")

