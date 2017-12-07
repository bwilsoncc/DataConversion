# ---------------------------------------------------------------------------
# TaxcodeLines_MakeLines_subscript.py
# Created on: Wednesday Nov 2, 2005
# By: Laura Gordon
# Usage: TaxcodeLines_MakeLines_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, win32com.client

# Create the Geoprocessor object
gp = win32com.client.Dispatch("esriGeoprocessing.GpDispatch.1")
gp.addmessage("1")

# Script arguments...
TaxcodeLine_Feature2Line = sys.argv[1]
TaxcodeLine = sys.argv[2]
gp.addmessage("2")

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(TaxcodeLine_Feature2Line, "TaxcodeLine_MakeLayer", "", "", "FNODE# FNODE# HIDDEN;TNODE# TNODE# HIDDEN;LPOLY# LPOLY# HIDDEN;RPOLY# RPOLY# HIDDEN;LENGTH LENGTH HIDDEN;REFLIN# REFLIN# HIDDEN;REFLIN-ID REFLIN-ID HIDDEN;IGDS-STYLE IGDS-STYLE HIDDEN;DIRECTION Direction VISIBLE;DISTANCE Distance VISIBLE;RADIUS Radius VISIBLE;DELTA Delta VISIBLE;TANGENT Tangent VISIBLE;ARCLENGTH ArcLength VISIBLE;SIDE Side VISIBLE;RADIUS2 Radius2 VISIBLE;TANGENT2 Tangent2 VISIBLE;DETAILSCALE DETAILSCALE HIDDEN;SVYNUM SVYNUM HIDDEN;TAXLOTKEY TAXLOTKEY HIDDEN;LINETYPE LineType VISIBLE;MAPSCALE MapScale VISIBLE;MAPNUMBER MapNumber VISIBLE;SOURCE Source VISIBLE;SOURCETYPE SourceType VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE;LOSTATION LoStation VISIBLE;HISTATION HiStation VISIBLE")
gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.addmessage("3")
gp.Append_management("TaxcodeLine_MakeLayer", TaxcodeLine, "TEST", )
gp.addmessage("Executed Append")

