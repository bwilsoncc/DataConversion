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
Taxlot_Feature2Poly = sys.argv[1]
Taxlot = sys.argv[2]

# Process: Make Feature Layer...
gp.MakeFeatureLayer_management(Taxlot_Feature2Poly, "Taxlot_MakeLayer", "", "", "AREA AREA HIDDEN;PERIMETER PERIMETER HIDDEN;TAXMAP_ TAXMAP_ HIDDEN;TAXMAP_ID TAXMAP_ID HIDDEN;IGDS_GGNO IGDS_GGNO HIDDEN;MAPNUM MapNumber VISIBLE;TOWN Town VISIBLE;RANGE Range VISIBLE;SECTION_ SecNumber VISIBLE;QTR QTR HIDDEN;TAXLOT Taxlot VISIBLE;REFOREST REFOREST HIDDEN;TAXCODE TAXCODE HIDDEN;DETAILSCALE DETAILSCALE HIDDEN;CLOSEMETHOD CLOSEMETHOD HIDDEN;CLOSERROR CLOSERROR HIDDEN;LEGACRES1 TaxlotAcre VISIBLE;LEGACRES2 LEGACRES2 HIDDEN;MAPACRES MapAcres VISIBLE;AUTO_METHOD AutoMethod VISIBLE;AUTO_REL AUTO_REL HIDDEN;AUTO_WHO AutoWho VISIBLE;AUTO_DATE AutoDate VISIBLE;GEOTRANSNO GEOTRANSNO HIDDEN;TAXMAPTYPE TAXMAPTYPE HIDDEN;TAXMAPSYM TAXMAPSYM HIDDEN;POINTNAME POINTNAME HIDDEN;SVYNUM SVYNUM HIDDEN;TAXLOTKEY TAXLOTKEY HIDDEN;MAPSCALE MAPSCALE HIDDEN;ORMAPNUM ORMapNum VISIBLE;PAGENUM PAGENUM HIDDEN;MAPSUFTYPE MapSufType VISIBLE;MAPSUFNUM MapSufNum VISIBLE;OQTR Qtr VISIBLE;OQTRQTR QtrQtr VISIBLE;TAXLOTC TAXLOTC HIDDEN;TAXNUM TAXNUM HIDDEN;POLYGONID POLYGONID HIDDEN;SCALE SCALE HIDDEN;ANGLE ANGLE HIDDEN;Shape_Length Shape_Length HIDDEN;Shape_Area Shape_Area HIDDEN")
#gp.MakeFeatureLayer_management(Taxlot_Feature2Poly, "Taxlot_MakeLayer", "", "", "MAPNUM MapNumber VISIBLE;TOWN Town VISIBLE;RANGE Range VISIBLE;SECTION_ SecNumber VISIBLE;TAXLOT Taxlot VISIBLE;LEGACRES1 TaxlotAcre VISIBLE;MAPACRES MapAcres VISIBLE;AUTO_METHOD AutoMethod VISIBLE;AUTO_WHO AutoWho VISIBLE;AUTO_DATE AutoDate VISIBLE;ORMAPNUM ORMapNum VISIBLE;MAPSUFTYPE MapSufType VISIBLE;MAPSUFNUM MapSufNum VISIBLE")
gp.addmessage("Executed MakeFeatureLayer")

gp.Append_management("Taxlot_MakeLayer", Taxlot, "TEST", )
gp.addmessage("Executed Append")


