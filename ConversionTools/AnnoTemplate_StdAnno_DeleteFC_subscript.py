# ---------------------------------------------------------------------------
# AnnoTemplate_StdAnno_DeleteFC_subscript.py
# Created on: Tue Ocotober 31 2005 06:30:02 AM
#   (generated by ArcGIS/ModelBuilder)
# Created by: Laura Gordon, Polk County
# Usage: AnnoTemplate_StdAnno_DeleteFC_subscript <Line_Coverage> <Point_Coverage> 
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/Desktop10.0/ArcToolbox/Toolboxes/Data Management Tools.tbx")

# Script arguments...
# Feature Classes (final output locations)
StdAnno10 = sys.argv[1]
StdAnno20 = sys.argv[2]
StdAnno30 = sys.argv[3]
StdAnno40 = sys.argv[4]
StdAnno50 = sys.argv[5]
StdAnno100 = sys.argv[6]
StdAnno200 = sys.argv[7]
StdAnno400 = sys.argv[8]
StdAnno800 = sys.argv[9]
StdAnno2000 = sys.argv[10]
FLAnnoTaxlotNum = sys.argv[11]
FLAnnoTaxcode = sys.argv[12]
FLAnnoTaxlotAcres = sys.argv[13]

# Feature Layers (input locations)
#StdAnno10Input = sys.argv[11]
#StdAnno20Input = sys.argv[12]
#StdAnno30Input = sys.argv[13]
#StdAnno40Input = sys.argv[14]
#StdAnno50Input = sys.argv[15]
#StdAnno100Input = sys.argv[16]
#StdAnno200Input = sys.argv[17]
#StdAnno400Input = sys.argv[18]
#StdAnno800Input = sys.argv[19]
#StdAnno2000Input = sys.argv[20]




# Process: Delete the Feature Classes if they already exist...
intCount = 1
while intCount <= 13:
    if intCount == 1 :
        strVariable = StdAnno10
        gp.addmessage("Checking StdAnno10")
    if intCount == 2 :
        strVariable = StdAnno20
        gp.addmessage("Checking StdAnno20")
    if intCount == 3 :
        strVariable = StdAnno30
        gp.addmessage("Checking StdAnno30")
    if intCount == 4 :
        strVariable = StdAnno40
        gp.addmessage("Checking StdAnno40")
    if intCount == 5 :
        strVariable = StdAnno50
        gp.addmessage("Checking StdAnno50")
    if intCount == 6 :
        strVariable = StdAnno100
        gp.addmessage("Checking StdAnno100")
    if intCount == 7 :
        strVariable = StdAnno200
        gp.addmessage("Checking StdAnno200")
    if intCount == 8 :
        strVariable = StdAnno400
        gp.addmessage("Checking StdAnno400")
    if intCount == 9 :
        strVariable = StdAnno800
        gp.addmessage("Checking StdAnno800")
    if intCount == 10 :
        strVariable = StdAnno2000
        gp.addmessage("Checking StdAnno2000")
    if intCount == 11 :
        strVariable = FLAnnoTaxlotNum
        gp.addmessage("Checking TaxlotNum")
    if intCount == 12 :
        strVariable = FLAnnoTaxcode
        gp.addmessage("Checking Taxcode")
    if intCount == 13 :
        strVariable = FLAnnoTaxlotAcres
        gp.addmessage("Checking TaxlotAcres")
        
    if strVariable <> "#":
        myshape = strVariable
        gp.addmessage (myshape)
        if gp.Exists(myshape):
            gp.delete( myshape )
            gp.addmessage("DELETED FEATURE CLASS")
    intCount = intCount + 1

# Process: Create the new feature classes of standard annotation from the feature layers...
#intCount = 11
#while intCount <= 20:
#    if intCount == 11 :
#        strInputVariable = StdAnno10Input
#        strOutputVariable = StdAnno10
#        gp.addmessage("Checking StdAnno10")
#    if intCount == 12 :
#        strVariable = StdAnno20Input
#        strOutputVariable = StdAnno20
#        gp.addmessage("Checking StdAnno20")
#    if intCount == 13 :
#        strVariable = StdAnno30Input
#        strOutputVariable = StdAnno30        
#        gp.addmessage("Checking StdAnno30")
#    if intCount == 14 :
#        strVariable = StdAnno40Input
#        strOutputVariable = StdAnno40
#        gp.addmessage("Checking StdAnno40")
#    if intCount == 15 :
#        strVariable = StdAnno50Input
#        strOutputVariable = StdAnno50
#        gp.addmessage("Checking StdAnno50")
#    if intCount == 16 :
#        strVariable = StdAnno100Input
#        strOutputVariable = StdAnno100
#        gp.addmessage("Checking StdAnno100")
#    if intCount == 17 :
#        strVariable = StdAnno200Input
#        strOutputVariable = StdAnno200
#        gp.addmessage("Checking StdAnno200")
#    if intCount == 18 :
#        strVariable = StdAnno400Input
#        strOutputVariable = StdAnno400
#        gp.addmessage("Checking StdAnno400")
#    if intCount == 19 :
#        strVariable = StdAnno800Input
#        strOutputVariable = StdAnno800
#        gp.addmessage("Checking StdAnno800")
#    if intCount == 20 :
#        strVariable = StdAnno2000Input
#        strOutputVariable = StdAnno2000
#        gp.addmessage("Checking StdAnno2000")

#    if strVariable <> "#" and strOutputVariable <> "#":
#        gp.addmessage("READY TO CREATE!!!")
#        #gp.ImportCoverageAnnotations_conversion("annotation.lease", CALGARY, "true", "false", "500", "false", "false", "", "true", "true")
#        gp.addmessage(strVariable)
#        gp.addmessage(strOutputVariable)
#        #gp.ImportCoverageAnnotations_conversion(strVariable, strOutputVariable, "true", "false", "1200", "false", "false", "", "true", "true")
#        #gp.ImportCoverageAnnotations_conversion(strVariable, strOutputVariable, 1200)
#        gp.ImportCoverageAnnotations_conversion("P://ModelingWorkshop_10-13-05//Clatsop//ConvertedCoverages//taxmap//annotation.igds", strOutputVariable, "true", "false", "1200")
#        gp.addmessage("Created a new feature class")

#    #Increment while loop
#    intCount = intCount + 1
    
