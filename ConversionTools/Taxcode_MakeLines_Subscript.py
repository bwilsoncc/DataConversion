# ---------------------------------------------------------------------------
# test.py
# Created on: Tue Jul 27 2004 02:30:02 PM
#   (generated by ArcGIS/ModelBuilder)
# Usage: test <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, win32com.client

# Create the Geoprocessor object
gp = win32com.client.Dispatch("esriGeoprocessing.GpDispatch.1")

# Script arguments...
Taxcode_SelArcs = sys.argv[1]
Taxcodelines = sys.argv[2]

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(Taxcode_SelArcs, "TaxcodeLines_MakeLayer", "", "", "FNODE_ FNODE_ HIDDEN;TNODE_ TNODE_ HIDDEN;LPOLY_ LPOLY_ HIDDEN;RPOLY_ RPOLY_ HIDDEN;LENGTH LENGTH HIDDEN;TAXMAP_ TAXMAP_ HIDDEN;TAXMAP_ID TAXMAP_ID HIDDEN;ANGLE ANGLE HIDDEN;DISTANCE DISTANCE HIDDEN;RADIUS RADIUS HIDDEN;DELTA DELTA HIDDEN;TANGENT TANGENT HIDDEN;ARCLENGTH ARCLENGTH HIDDEN;SIDE SIDE HIDDEN;RADIUS2 RADIUS2 HIDDEN;TANGENT2 TANGENT2 HIDDEN;TAXMAPSYM TAXMAPSYM HIDDEN;TAXMAPTYPE TAXMAPTYPE HIDDEN;AUTO_METHOD AUTO_METHOD HIDDEN;AUTO_REL AUTO_REL HIDDEN;AUTO_WHO AUTO_WHO HIDDEN;AUTO_DATE AUTO_DATE HIDDEN;GEOTRANSNO GEOTRANSNO HIDDEN")
gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.Append_management("TaxcodeLines_MakeLayer", Taxcodelines, "TEST", )
gp.addmessage("Executed Append")

