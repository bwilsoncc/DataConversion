# ---------------------------------------------------------------------------
# TaxlotPoly_MakePoly_subscript.py
# Created on: Wednesday Nov 2, 2005
# By: Laura Gordon
# Usage: TaxlotPoly_MakePoly_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.addmessage("1")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
TaxlotPoly_Feature2Poly = sys.argv[1]
TaxlotPoly = sys.argv[2]
gp.addmessage("2")

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(TaxlotPoly_Feature2Poly, "TaxlotPoly_MakeLayer", "", "", "AREA AREA HIDDEN;PERIMETER PERIMETER HIDDEN;TAXLOT# TAXLOT# HIDDEN;TAXLOT-ID TAXLOT-ID HIDDEN;COUNTY County VISIBLE;TOWN Town VISIBLE;TOWNPART TownPart VISIBLE;TOWNDIR TownDir VISIBLE;RANGE Range VISIBLE;RANGEPART RangePart VISIBLE;RANGEDIR RangeDir VISIBLE;SECNUMBER SecNumber VISIBLE;QTR Qtr VISIBLE;QTRQTR QtrQtr VISIBLE;ANOMALY Anomaly VISIBLE;MAPSUFTYPE MapSufType VISIBLE;MAPSUFNUM MapSufNum VISIBLE;MAPNUMBER MapNumber VISIBLE;ORMAPNUM ORMapNum VISIBLE;TAXLOT Taxlot VISIBLE;SPECIALINT SpecialInt VISIBLE;MAPTAXLOT MapTaxlot VISIBLE;ORTAXLOT ORTaxlot VISIBLE;TAXLOTFEET TaxlotFeet VISIBLE;TAXLOTACRE TaxlotAcre VISIBLE;MAPACRES MapAcres VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE")
gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.addmessage("3")
gp.Append_management("TaxlotPoly_MakeLayer", TaxlotPoly, "NO_TEST", )
gp.addmessage("Executed Append")

