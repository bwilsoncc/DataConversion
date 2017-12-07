from __future__ import print_function
import sys
import platform
import arcpy

arch = platform.architecture()
if arch[0] == '64bit': 
    msg = "This script requires 32-bit python."
    arcpy.AddError(msg)
    print(msg)
    exit(-1)

# Copy the coverage polygons to the ORMAP personal geodatabase

#coverage_poly_fc = sys.argv[1]
#mapindex_fc      = sys.argv[2]
#output_fc        = sys.argv[3] # appears to be unused

# Uncomment these lines to test in debugger.
coverage_poly_fc = r"C:\GeoModel\Clatsop\ConvertII\mapindex" # polygons
mapindex_fc      = r"C:\GeoModel\Clatsop\ORMAP-SchemaN_08-21-08.mdb\TaxlotsFD\MapIndex"

# I think this just does field mapping??
layer_name =  "MapIndexPoly_MakeLayer" # Just some random name
arcpy.MakeFeatureLayer_management(coverage_poly_fc, layer_name, "", "", 
                                  "AREA AREA HIDDEN;PERIMETER PERIMETER HIDDEN;MAPINDEX# MAPINDEX# HIDDEN;MAPINDEX-ID MAPINDEX-ID HIDDEN;MAPSCALE MapScale VISIBLE;MAPNUMBER MapNumber VISIBLE;PAGENUMBER PageNumber VISIBLE;ORMAPNUM ORMapNum VISIBLE;CITYNAME CityName VISIBLE;RELIACODE ReliaCode VISIBLE;AUTODATE AutoDate VISIBLE;AUTOMETHOD AutoMethod VISIBLE;AUTOWHO AutoWho VISIBLE"
                                  )

# We're using append to copy features, not really appending.
arcpy.DeleteFeatures_management(mapindex_fc)

# TEST means make sure the schemas match
# so I think the deal here is, if that field mapping fails, this will too.
arcpy.Append_management(layer_name, mapindex_fc, "TEST")

# Convert feet to inches??
arcpy.CalculateField_management(mapindex_polygon, "MapScale", "[MapScale] * 12")
