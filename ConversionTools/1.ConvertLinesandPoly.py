# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 2ConvertLinesandPoly.py
# Created on: 2017-05-24 14:31:05.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy,os,time,datetime,traceback

# logfile

arcpy.Delete_management ("1ConvertLinesandPolyLog.txt")
logfile = open("1ConvertLinesandPolyLog.txt", "w")
logfile.write ("1ConvertLinesandPolyLog.txt"+ '\n')
starttime =  str(datetime.datetime.now())
logfile.write ('\n' + '\n' + "StartTime:" + starttime + '\n' + '\n')
               

# Local variables:
try:

    CornerPoint = "..\\corner\\point"
    TaxlotArc = "..\\taxlot\\arc"
    TaxlotPoint = "..\\taxlotpt\\point"
    TaxcodeArc = "..\\taxcode\\arc" 
    TaxcodePoint = "..\\taxcode\\label" 
    TaxboundArc = "..\\taxbound\\arc" 
    Taxboundpoint = "..\\taxbound\\label"

    WaterLineArc = "..\\waterlin\\arc" 
    CartolineArc = "..\\cartolin\\arc" 
    RefLineArc = "..\\refline\\arc" 
    PLSSLineArc ="..\\plssline\\arc" 

    Corner = "..\\townedgeo.gdb\\corner"

    TaxlotLines = "..\\townedgeo.gdb\\TaxlotsFD\\TaxlotLines" 
    TaxlotPoints = "..\\townedgeo.gdb\\TaxlotsFD\\TaxlotPoints"
    Taxlot = "..\\townedgeo.gdb\\TaxlotsFD\\Taxlot"

    MapIndexLines = "..\\townedgeo.gdb\\TaxlotsFD\\MapIndexLines" 
    MapIndexPoints = "..\\townedgeo.gdb\\TaxlotsFD\\MapIndexPoints"
    MapIndex = "..\\townedgeo.gdb\\TaxlotsFD\\MapIndex"

    TaxcodeLines = "..\\townedgeo.gdb\\TaxlotsFD\\TaxcodeLines" 
    TaxcodePoints = "..\\townedgeo.gdb\\TaxlotsFD\\TaxcodePoints"
    Taxcode = "..\\townedgeo.gdb\\TaxlotsFD\\Taxcode"

    PLSSLines = "..\\townedgeo.gdb\\PLSSLines"
    WaterLines = "..\\townedgeo.gdb\\WaterLines"
    CartographicLines = "..\\townedgeo.gdb\\CartographicLines"
    ReferenceLines = "..\\townedgeo.gdb\\ReferenceLines"

    print "Variables made"

# Process: Append
    arcpy.DeleteFeatures_management(Corner)
    arcpy.Append_management(CornerPoint,Corner, "NO_TEST", "", "")
    print "Control Done"
    logfile.write ("Control Done" + '\n')
    
    arcpy.DeleteFeatures_management(TaxlotLines)
    arcpy.Append_management(TaxlotArc,TaxlotLines, "NO_TEST", "", "")
    print "TaxlotLines Done"
    logfile.write ("TaxlotLines Done" + '\n')
    
    arcpy.DeleteFeatures_management(TaxlotPoints)
    arcpy.Append_management(TaxlotPoint,TaxlotPoints, "NO_TEST", "", "")
    print "TaxlotPoint Done"
    logfile.write ("TaxlotPoint Done" + '\n')
    
    arcpy.DeleteFeatures_management(TaxcodePoints)
    arcpy.Append_management(TaxcodePoint,TaxcodePoints, "NO_TEST", "", "")
    print "TaxcodePoints Done"
    logfile.write ("TaxcodePoints Don" + '\n')
    
    arcpy.DeleteFeatures_management(TaxcodeLines)
    arcpy.Append_management(TaxcodeArc,TaxcodeLines, "NO_TEST", "", "")
    print "TaxcodeLines Done"
    logfile.write ("TaxcodeLines Done" + '\n')
    
    arcpy.DeleteFeatures_management(MapIndexPoints)
    arcpy.Append_management(Taxboundpoint,MapIndexPoints, "NO_TEST", "", "")
    print "MapindexPoints Done"
    logfile.write ("MapindexPoints Done" + '\n')
    
    arcpy.DeleteFeatures_management(MapIndexLines)
    arcpy.Append_management(TaxboundArc,MapIndexLines, "NO_TEST", "", "")
    print "MapIndexLines Done"
    logfile.write ("MapIndexLines Done" + '\n')
    
    arcpy.DeleteFeatures_management(WaterLines)
    arcpy.Append_management(WaterLineArc,WaterLines, "NO_TEST", "", "")
    print "WaterLines Done"
    logfile.write ("WaterLines Done" + '\n')
    
    arcpy.DeleteFeatures_management(CartographicLines)
    arcpy.Append_management(CartolineArc,CartographicLines, "NO_TEST", "", "")
    print "CartographicLines Done"
    logfile.write ("CartographicLines Done" + '\n')
    
    arcpy.DeleteFeatures_management(ReferenceLines)
    arcpy.Append_management(RefLineArc,ReferenceLines, "NO_TEST", "", "")
    print "ReferenceLines Done"
    logfile.write ("ReferenceLines Done" + '\n')
    
    arcpy.DeleteFeatures_management(PLSSLines)
    arcpy.Append_management(PLSSLineArc,PLSSLines, "NO_TEST", "", "")
    print "PLSSLines Done"
    logfile.write ("PLSSLines Done" + '\n')

    arcpy.Delete_management(MapIndex)
    arcpy.Delete_management(Taxcode)
    arcpy.Delete_management(Taxlot)

    arcpy.FeatureToPolygon_management(MapIndexLines, MapIndex, "", "ATTRIBUTES", MapIndexPoints)
    arcpy.FeatureToPolygon_management(TaxcodeLines, Taxcode, "", "ATTRIBUTES", TaxcodePoints)
    arcpy.FeatureToPolygon_management(TaxlotLines, Taxlot, "", "ATTRIBUTES", TaxlotPoints)
    print "Polygons Made - last stop"
    logfile.write ("Polygons Made - last stop" + '\n')
    
#End
      
    endtime =  str(datetime.datetime.now())
    logfile.write ('\n' + '\n' + "Succesful!!  EndTime:" + endtime + '\n')

    logfile.close()

except:
    badness = traceback.format_exc()
    print ('\n' + '\n' + "*** BADNESS ****" + '\n' + '\n')
    print (badness)
    
    logfile.write ('\n' + '\n' + "**** BADNESS *****" + '\n' + '\n')
    logfile.write (badness)
    
    logfile.close()  


