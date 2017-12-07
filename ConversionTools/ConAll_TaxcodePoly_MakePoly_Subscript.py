# ---------------------------------------------------------------------------
# TaxcodePoly_MakePoly_subscript.py
# Created on: Wednesday Nov 2, 2005
# By: Laura Gordon
# Usage: TaxcodePoly_MakePoly_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.addmessage("1")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
TaxcodePoly_Feature2Poly = sys.argv[1]
TaxcodePoly = sys.argv[2]
gp.addmessage("2")

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(TaxcodePoly_Feature2Poly, "TaxcodePoly_MakeLayer", "", "", "AREA AREA HIDDEN;PERIMETER PERIMETER HIDDEN;TAXCODE# TAXCODE# HIDDEN;TAXCODE-ID TAXCODE-ID HIDDEN;COUNTY County VISIBLE;TAXCODE TaxCode VISIBLE;SOURCE Source VISIBLE;YEARCREATED YearCreated VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE")
gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.addmessage("3")
gp.Append_management("TaxcodePoly_MakeLayer", TaxcodePoly, "TEST", )
gp.addmessage("Executed Append")

