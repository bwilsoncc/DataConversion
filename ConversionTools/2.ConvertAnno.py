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
import arcpy,os,time,datetime,traceback,sys

# Functions ------------------------------------------------------------------------

#calcfield Functions - field calc sizes for annotation features

def CalcFields(Anno):
    # Process: Calculate Field
    #arcpy.CalculateField_management(Anno, "FontName", "[STDFONT]", "VB", "")

    # Process: Calculate Field (2)
    #arcpy.CalculateField_management(Anno, "FontSize", "[STDSIZE]", "VB", "")

    # Process: Calculate Field (3)
    #arcpy.CalculateField_management(Anno, "Bold", "[STDBOLD]", "VB", "")

    # Process: Calculate Field (13)
    #arcpy.CalculateField_management(Anno, "Italic", "[STDITALIC]", "VB", "")

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

arcpy.env.overwriteOutput = True

# logfile

arcpy.Delete_management ("2ConvertAnnoLog.txt")
logfile = open("2ConvertAnnoLog.txt", "w")
logfile.write ("2ConvertAnno log"+ '\n')
starttime =  str(datetime.datetime.now())
logfile.write ('\n' + '\n' + "StartTime:" + starttime + '\n' + '\n')
               
#relpath = os.path.dirname(sys.argv[0])

relpath = sys.argv[1]
print ("path: " + relpath)

mxdpath = (relpath + "\\TaxMapConvert.mxd")
print (mxdpath + '\n' + '\n')
print ("-----------------------------------------------")

mxd = arcpy.mapping.MapDocument(mxdpath)
    
# Local variables:
try:

    scales = ["0100","0200","0400","2000"]
    for scale in scales:
        
        AnnoScaleIGDS = "TaxmapAnno" + scale + ".igds"
        print (AnnoScaleIGDS)
        AnnoScaleCovLyr = arcpy.mapping.ListLayers(mxd, AnnoScaleIGDS)[0]
        print (AnnoScaleCovLyr)
        
        AnnoScale = "townedgeo.gdb\\Anno" + scale + "Scale" 
        print AnnoScale
    
        #AnnoScale = "..\\townedgeo.gdb\\Anno0100Scale"  
        print AnnoScaleIGDS +  "---" + AnnoScale

        mapscale =  "mapscale = " + str(int(scale)) 
        print mapscale
                                         
        # Delete 
        arcpy.Delete_management(AnnoScale)

        # Process: Import Coverage Annotation
        arcpy.ImportCoverageAnnotation_conversion(AnnoScaleCovLyr,AnnoScale, "1200", "CLASSES_FROM_LEVELS", "NO_MATCH", "NO_SYMBOL_REQUIRED", "STANDARD", "", "AUTO_CREATE", "AUTO_UPDATE")

        # Calc fields (function)
        CalcFields(AnnoScale)
        
        # Clean up template features
        AnnoScaleLyr = AnnoScale + "lyr" 
        arcpy.MakeFeatureLayer_management(AnnoScale, AnnoScaleLyr, "TextString LIKE 'LEVEL%'" , "", "")
        arcpy.DeleteFeatures_management(AnnoScaleLyr)
        
        print ("Done with import- " + scale)
        logfile.write ("Done with import- " + scale + '\n')
    # Do Taxlot Anno -------------------------------------------------------------------------------------------------

    TaxlotAnnoCov = arcpy.mapping.ListLayers(mxd, "TaxLotAn.igds")[0]
    TaxlotAnnoFeature = "townedgeo.gdb\\TaxlotsFD\\TaxlotNumberAnno"
    
    # Delete 
    arcpy.Delete_management(TaxlotAnnoFeature)

    # Process: Import Coverage Annotation
    arcpy.ImportCoverageAnnotation_conversion(TaxlotAnnoCov, TaxlotAnnoFeature, "1200", "CLASSES_FROM_LEVELS", "NO_MATCH", "NO_SYMBOL_REQUIRED", "STANDARD", "", "AUTO_CREATE", "AUTO_UPDATE")

    # Clean up template features
    arcpy.MakeFeatureLayer_management(TaxlotAnnoFeature, "TxLtLyrToDelete", "TextString = '99999'" , "", "")
    arcpy.DeleteFeatures_management("TxLtLyrToDelete")                                  

    # Calc fields (function)
    CalcFields(TaxlotAnnoFeature)
    print ("Done with import- TAXLOTANNOFEATURE" )
    logfile.write ("Done with import- TAXLOTANNOFEATURE" + '\n')


    # Do Taxcode Anno------------------------------------------------------

    TaxCodeAnnoFeature = "townedgeo.gdb\\TaxlotsFD\\TaxCodeAnno"
    TaxCodeAnnoCov = arcpy.mapping.ListLayers(mxd, "TaxCodAn.igds")[0]

    # Delete 
    arcpy.Delete_management(TaxCodeAnnoFeature)

    # Process: Import Coverage Annotation
    arcpy.ImportCoverageAnnotation_conversion(TaxCodeAnnoCov, TaxCodeAnnoFeature, "1200", "CLASSES_FROM_LEVELS", "NO_MATCH", "NO_SYMBOL_REQUIRED", "STANDARD", "", "AUTO_CREATE", "AUTO_UPDATE")

    # Clean up template features
    arcpy.MakeFeatureLayer_management(TaxCodeAnnoFeature, "TxCdLyrToDelete", "TextString = '99-99'" , "", "")
    arcpy.DeleteFeatures_management("TxCdLyrToDelete")
    
    # Calc fields (function)
    CalcFields(TaxCodeAnnoFeature)
    print ("Done with import- TaxCodeAnnoFeature" )
    logfile.write ("Done with import- TaxCodeAnnoFeature" + '\n')
    
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

