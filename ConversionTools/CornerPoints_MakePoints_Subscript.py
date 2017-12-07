# ---------------------------------------------------------------------------
# CornerPoints_MakePoints_subscript.py
# Created on: Monday October 24, 2005
#   (generated by ArcGIS/ModelBuilder)
# Usage: CornerPoints_MakePoints_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()
gp.addmessage("1")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
CornerPoint_Feature2Point = sys.argv[1]
CornerPoint = sys.argv[2]
gp.addmessage("2")

# Process: Make Feature Layer...
#gp.MakeFeatureLayer_management(CornerPoint_Feature2Point, "CornerPoint_MakeLayer")
#gp.MakeFeatureLayer_management(CornerPoint_Feature2Point, "CornerPoint_MakeLayer", "", "", "CORNER# CORNER# HIDDEN;CORNER-ID CORNER-ID HIDDEN;CORNPT1# CORNPT1# HIDDEN;CORNPT1-ID CORNPT1-ID HIDDEN;IGDS-GGNO IGDS-GGNO HIDDEN;MAPNUM MAPNUM HIDDEN;TOWN TOWN HIDDEN;RANGE RANGE HIDDEN;SECTION SECTION HIDDEN;QTR QTR HIDDEN;TAXLOT TAXLOT HIDDEN;REFOREST REFOREST HIDDEN;TAXCODE TAXCODE HIDDEN;CLOSEMETHOD CLOSEMETHOD HIDDEN;CLOSERROR CLOSERROR HIDDEN;LEGACRES1 LEGACRES1 HIDDEN;LEGACRES2 LEGACRES2 HIDDEN;MAPACRES MAPACRES HIDDEN;AUTO-METHOD AUTO-METHOD HIDDEN;AUTO-REL AUTO-REL HIDDEN;AUTO-WHO AUTO-WHO HIDDEN;AUTO-DATE AUTO-DATE HIDDEN;GEOTRANSNO GEOTRANSNO HIDDEN;TAXMAPTYPE TAXMAPTYPE HIDDEN;TAXMAPSYM TAXMAPSYM HIDDEN;POINTNAME POINTNAME HIDDEN;TAXBOUND# TAXBOUND# HIDDEN;TAXBOUND-ID TAXBOUND-ID HIDDEN;CORNERSYMBOL CornerSymbol VISIBLE;CORNERDESC CornerDesc VISIBLE;CONTROLTYPE ControlType VISIBLE;COMMONNAME CommonName VISIBLE;GCDB GCDB VISIBLE;EASTING Easting VISIBLE;NORTHING Northing VISIBLE;LATITUDE Latitude VISIBLE;LONGITUDE Longitude VISIBLE;MAPSCALE MapScale VISIBLE;MAPNUMBER MapNumber VISIBLE;PAGENUMBER PAGENUMBER HIDDEN;ORMAPNUMB ORMAPNUM HIDDEN;MAPSUFTYPE MAPSUFTYPE HIDDEN;CITYNAME CITYNAME HIDDEN;TAXLOTC TAXLOTC HIDDEN;MQ MQ HIDDEN; MQQ MQQ HIDDEN;SOURCE Source VISIBLE;SOURCETYPE SourceType VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE;$POLYGONID $POLYGONID HIDDEN;$SCALE $SCALE HIDDEN; $ANGLE $ANGLE HIDDEN")
gp.MakeFeatureLayer_management(CornerPoint_Feature2Point, "CornerPoint_MakeLayer", "", "", "CORNER# CORNER# HIDDEN;CORNER-ID CORNER-ID HIDDEN;CORNERSYMBOL CornerSymbol VISIBLE;CORNERDESC CornerDesc VISIBLE;CONTROLTYPE ControlType VISIBLE;COMMONNAME CommonName VISIBLE;GCDB GCDB VISIBLE;EASTING Easting VISIBLE;NORTHING Northing VISIBLE;LATITUDE Latitude VISIBLE;LONGITUDE Longitude VISIBLE;MAPSCALE MapScale VISIBLE;MAPNUMBER MapNumber VISIBLE;SOURCE Source VISIBLE;SOURCETYPE SourceType VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE;$POLYGONID $POLYGONID HIDDEN;$SCALE $SCALE HIDDEN; $ANGLE $ANGLE HIDDEN")

gp.addmessage("Executed MakeFeatureLayer")

# Process: Append...
gp.addmessage("3")
gp.Append_management("CornerPoint_MakeLayer", CornerPoint, "TEST", )
gp.addmessage("Executed Append")

