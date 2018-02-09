# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# 2.ConvertGenAnno.py
# Created on: November 2017 - Dean 
#
# Description: Converts annotation Prepped with AML to correct ORCMAP Anno Classes
#
# 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Functions ------------------------------------------------------------------------

#calcfield Functions - field calc sizes for annotation features

def CalcFields(Anno):
    # Process: Calculate Field
    arcpy.CalculateField_management(Anno, "FontName", "[STDFONT]", "VB", "")

    # Process: Calculate Field (2)
    arcpy.CalculateField_management(Anno, "FontSize", "[STDSIZE]", "VB", "")

    # Process: Calculate Field (3)
    arcpy.CalculateField_management(Anno, "Bold", "[STDBOLD]", "VB", "")

    # Process: Calculate Field (13)
    arcpy.CalculateField_management(Anno, "Italic", "[STDITALIC]", "VB", "")

    # Process: Calculate Field (17)
    arcpy.CalculateField_management(Anno, "TextString", "Replace( [TextString],\"^\",\"°\"  )", "VB", "")
    print ("Done with Calc- " + Anno)

    return;

# ImportAnno - Deletes anno feature and then converts the anno

def ImportAnno(AnnoCov,AnnoF):
    # Delete 
    arcpy.Delete_management(AnnoF)

    # Process: Import Coverage Annotation
    arcpy.ImportCoverageAnnotation_conversion(AnnoCov, AnnoF, "1200", "CLASSES_FROM_LEVELS", "NO_MATCH", "NO_SYMBOL_REQUIRED", "STANDARD", "", "AUTO_CREATE", "AUTO_UPDATE")

    print ("Done with import- " + AnnoF)
    
    return;

#--------------------------------------------------------------------------------------


# Local variables:

AnnoIGDS = "..\\taxmap\\annotation.igds" 
scales = ["0100","0200","0400","2000"] 


for scale in scales:
    AnnoScaleIGDS = "Anno" + scale + "IGDS"
    AnnoScale = "..\\townedgeo.gdb\\Anno" + scale + "Scale" 
    print AnnoScale
    
    #AnnoScale = "..\\townedgeo.gdb\\Anno0100Scale"  
    print AnnoScaleIGDS +  "---" + AnnoScale

    mapscale =  "mapscale = " + str(int(scale)) 
    print mapscale
                                         
    # Delete 
    arcpy.Delete_management(AnnoScale)

    # Process: Make Feature Layer
    arcpy.MakeFeatureLayer_management(AnnoIGDS, AnnoScaleIGDS, mapscale , "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;IGDS# IGDS# VISIBLE NONE;IGDS-ID IGDS-ID VISIBLE NONE;SYMBOL SYMBOL VISIBLE NONE;LEVEL LEVEL VISIBLE NONE;TEXT TEXT VISIBLE NONE;MAPSIZE MAPSIZE VISIBLE NONE;MAPSCALE MAPSCALE VISIBLE NONE;MAPNUMBER MAPNUMBER VISIBLE NONE;AUTOWHO AUTOWHO VISIBLE NONE;AUTOMETHOD AUTOMETHOD VISIBLE NONE;AUTODATE AUTODATE VISIBLE NONE;STDSIZE STDSIZE VISIBLE NONE;STDFONT STDFONT VISIBLE NONE;STDBOLD STDBOLD VISIBLE NONE;STDITALIC STDITALIC VISIBLE NONE;$ID $ID VISIBLE NONE;$SYMBOL $SYMBOL VISIBLE NONE;$LEVEL $LEVEL VISIBLE NONE;$SIZE $SIZE VISIBLE NONE;$TEXT $TEXT VISIBLE NONE;$OFFSETX $OFFSETX VISIBLE NONE;$OFFSETY $OFFSETY VISIBLE NONE;$JUSTIFY $JUSTIFY VISIBLE NONE;$FIT $FIT VISIBLE NONE;$ALIGN $ALIGN VISIBLE NONE")

    # Process: Import Coverage Annotation
    arcpy.ImportCoverageAnnotation_conversion(AnnoScaleIGDS, AnnoScale, "1200", "CLASSES_FROM_LEVELS", "NO_MATCH", "NO_SYMBOL_REQUIRED", "STANDARD", "", "AUTO_CREATE", "AUTO_UPDATE")

    # Calc fields (function)
    CalcFields(AnnoScale)
    print ("Done with import- " + scale)
    
# Do Taxlot Anno

TaxlotAnnoCov = "..\\taxlotan\\annotation.igds"
TaxlotAnnoFeature = "..\\townedgeo.gdb\\TaxlotsFD\\TaxlotNumberAnno"
TaxlotNumberAP = "..\\townedgeo.gdb\\TaxlotsFD\\TaxlotNumberAP"

print TaxlotAnnoFeature
arcpy.DeleteFeatures_management(TaxlotAnnoFeature)
 
for scale in scales:
    scaleft = int(scale)  * int(12) 
    mapscale =  "ms = " + str(int(scaleft)) 

    
    TaxlotAnnoLayer = "TaxlotLayer " + scale 
    TaxlotAnnoScaleFeat = "..\\townedgeo.gdb\\TaxlotsFD\\TaxlotNumberAnno" + scale + "Scale"



    if int(scale) == 100: 
        APFeatures = TaxlotAnnoScaleFeat

    else:
        APFeatures =  (APFeatures + ";" + TaxlotAnnoScaleFeat)
    
    arcpy.Delete_management(TaxlotAnnoScaleFeat)
    
    arcpy.MakeFeatureLayer_management(TaxlotAnnoCov, TaxlotAnnoLayer, mapscale , "", "FID FID VISIBLE NONE;Shape Shape VISIBLE NONE;IGDS# IGDS# VISIBLE NONE;IGDS-ID IGDS-ID VISIBLE NONE;SYMBOL SYMBOL VISIBLE NONE;LEVEL LEVEL VISIBLE NONE;TEXT TEXT VISIBLE NONE;MAPSIZE MAPSIZE VISIBLE NONE;MAPSCALE MAPSCALE VISIBLE NONE;MAPNUMBER MAPNUMBER VISIBLE NONE;AUTOWHO AUTOWHO VISIBLE NONE;AUTOMETHOD AUTOMETHOD VISIBLE NONE;AUTODATE AUTODATE VISIBLE NONE;STDSIZE STDSIZE VISIBLE NONE;STDFONT STDFONT VISIBLE NONE;STDBOLD STDBOLD VISIBLE NONE;STDITALIC STDITALIC VISIBLE NONE;$ID $ID VISIBLE NONE;$SYMBOL $SYMBOL VISIBLE NONE;$LEVEL $LEVEL VISIBLE NONE;$SIZE $SIZE VISIBLE NONE;$TEXT $TEXT VISIBLE NONE;$OFFSETX $OFFSETX VISIBLE NONE;$OFFSETY $OFFSETY VISIBLE NONE;$JUSTIFY $JUSTIFY VISIBLE NONE;$FIT $FIT VISIBLE NONE;$ALIGN $ALIGN VISIBLE NONE")
    arcpy.ImportCoverageAnnotation_conversion(TaxlotAnnoLayer, TaxlotAnnoScaleFeat , "1200", "CLASSES_FROM_LEVELS", "NO_MATCH", "NO_SYMBOL_REQUIRED", "STANDARD", "", "AUTO_CREATE", "AUTO_UPDATE")
    CalcFields(TaxlotAnnoScaleFeat)
    

# Append Scales to one anno feature class

arcpy.Delete_management(TaxlotNumberAP)
arcpy.AppendAnnotation_management(APFeatures, TaxlotNumberAP, "1200", "CREATE_CLASSES", "NO_SYMBOL_REQUIRED", "NO_AUTO_CREATE", "NO_AUTO_UPDATE")

#  Calculate Unique FeatureID


arcpy.AddField_management(TaxlotNumberAP, "MapScale", "LONG", "", "", "", "", "NULLABLE", "","Mapscale")

arcpy.CalculateField_management(TaxlotNumberAP, "FeatureID", "!OBJECTID!", "PYTHON", "")
arcpy.CalculateField_management(TaxlotNumberAP, "MapScale", "!MS!", "PYTHON", "")

# Append into taxlotnumber anno feature class

arcpy.Append_management(TaxlotNumberAP, TaxlotAnnoFeature, "NO_TEST","","")

# Join tables

arcpy.MakeTableView_management(TaxlotNumberAP, "TaxlotNumberAP_tbl")
arcpy.MakeFeatureLayer_management(TaxlotAnnoFeature, "TaxlotAnnoFeature_Lyr","FeatureID > 0")

arcpy.AddJoin_management( "TaxlotAnnoFeature_Lyr", "FeatureID", "TaxlotNumberAP_tbl", "FeatureID", "KEEP_ALL")

# Calc Fields

arcpy.CalculateField_management("TaxlotAnnoFeature_Lyr", "TaxlotNumberAnno.VerticalAlignment", "[TaxlotNumberAP.VerticalAlignment]", "VB", "")
arcpy.CalculateField_management("TaxlotAnnoFeature_Lyr", "TaxlotNumberAnno.HorizontalAlignment", "[TaxlotNumberAP.HorizontalAlignment]", "VB", "")   

arcpy.RemoveJoin_management("TaxlotAnnoFeature_Lyr", "")


arcpy.CalculateField_management(TaxlotAnnoFeature, "VerticalAlignment", "[VerticalAlignment]", "VB", "")
arcpy.CalculateField_management(TaxlotAnnoFeature, "HorizontalAlignment", "[HorizontalAlignment]", "VB", "")    

# clean up

for scale in scales:
    TaxlotAnnoScaleFeat = "..\\townedgeo.gdb\\TaxlotsFD\\TaxlotNumberAnno" + scale + "Scale"                             
    # Delete
    print TaxlotAnnoScaleFeat 
    arcpy.Delete_management(TaxlotAnnoScaleFeat)
    
arcpy.Delete_management(TaxlotNumberAP)

# Do Taxcode Anno------------------------------------------------------

TaxCodeAnnoCov = "..\\taxcodan\\annotation.igds" 
TaxCodeAnnoFeature = "..\\townedgeo.gdb\\TaxlotsFD\\TaxCodeAnno"

arcpy.Delete_management(TaxCodeAnnoFeature)

ImportAnno(TaxCodeAnnoCov,TaxCodeAnnoFeature)
CalcFields(TaxCodeAnnoFeature)

arcpy.AddField_management(TaxCodeAnnoFeature, "MapScale", "LONG", "", "", "", "", "NULLABLE", "NON_REQUIRED", "MapScale")
arcpy.CalculateField_management(TaxCodeAnnoFeature, "MapScale", "[MS]", "VB", "")



print "Done with Taxcode Anno"


