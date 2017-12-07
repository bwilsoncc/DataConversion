# ---------------------------------------------------------------------------
# TaxlotLines_MakeLines_subscript.py
# Created on: Wednesday Nov 2, 2005
# By: Laura Gordon Polk County
# Usage: TaxlotLines_MakeLines_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.addmessage("1")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
TaxlotLine_Feature2Line = sys.argv[1]
TaxlotLine = sys.argv[2]
gp.addmessage("2")

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(TaxlotLine_Feature2Line, "TaxlotLine_MakeLayer", "", "", "FNODE# FNODE# HIDDEN;TNODE# TNODE# HIDDEN;LPOLY# LPOLY# HIDDEN;RPOLY# RPOLY# HIDDEN;LENGTH LENGTH HIDDEN;TAXLOT# TAXLOT# HIDDEN;TAXLOT-ID TAXLOT-ID HIDDEN;LINETYPE LineType VISIBLE;DIRECTION Direction VISIBLE;DISTANCE Distance VISIBLE;DIRECTION Direction VISIBLE;DELTA Delta VISIBLE;RADIUS Radius VISIBLE;TANGENT Tangent VISIBLE;ARCLENGTH ArcLength VISIBLE;SIDE Side VISIBLE;RADIUS2 Radius2 VISIBLE;TANGENT2 Tangent2 VISIBLE;SOURCE Source VISIBLE;SOURCETYPE SourceType VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE")
gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.addmessage("3")
gp.Append_management("TaxlotLine_MakeLayer", TaxlotLine, "TEST", )
gp.addmessage("Executed Append")

