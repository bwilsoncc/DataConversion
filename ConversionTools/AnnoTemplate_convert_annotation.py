# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# AnnoTemplate_convert_annotation.py
# Created on: 2017-12-08 10:16:31.00000
# Description: 
# Convert annotation from coverages to feature classes.
# ---------------------------------------------------------------------------
from __future__ import print_function
import arcpy
import sys, os

def aprint(msg):
    """ print to console and AddMessage """
    print(msg)
    arcpy.AddMessage(msg)
    return

def deletefc(fc):
    """ Delete a feature class if it exists. """
    msg = "Feature class '%s'" % fc
    if arcpy.Exists(fc):
        arcpy.Delete_management(fc)
        msg += " deleted."
    else:
        msg += " doesn't exist."
    print(msg)
    arcpy.AddMessage(msg)
    return

def fix_fontsize(outputfc):
    aprint("Fixing fontsize.")
    arcpy.CalculateField_management(outputfc, "FontSize", "!MAPSIZE!", "PYTHON", "")

def fix_caret(outputfc):
    aprint("Fixing caret.")
    arcpy.CalculateField_management(outputfc, "TEXT_",      "!TEXT_!.replace('^',u'\xb0')",      "PYTHON", "")
    arcpy.CalculateField_management(outputfc, "TextString", "!TextString!.replace('^',u'\xb0')", "PYTHON", "")
    return True

def import_anno(annolayer, outputfc, linkedfc, reference_scale):
    aprint("Importing %s to %s Linked FC: %s" % (annolayer.name, outputfc, linkedfc)) 
    linked = "STANDARD"
    if linkedfc: linked = "FEATURE_LINKED"     
    arcpy.ImportCoverageAnnotation_conversion(annolayer, outputfc, reference_scale, 
                                              "CLASSES_FROM_LEVELS", "NO_MATCH", "NO_SYMBOL_REQUIRED", 
                                              linked, linkedfc,
                                              "AUTO_CREATE", "AUTO_UPDATE")
    return
    
def convert_anno(mxd, df, destination, reference_scale, overwrite):
    """ Convert coverage annotation to feature class annotation. """
        
    linklist = [   # (Layer name, output featureclass, featurelinked_fc)
                ("StdAnno.igds 10 scale",   "Anno0010scale",    ""),
                ("StdAnno.igds 20 scale",   "Anno0020scale",    ""),
                ("StdAnno.igds 30 scale",   "Anno0030scale",    ""),
                ("StdAnno.igds 40 scale",   "Anno0040scale",    ""),
                ("StdAnno.igds 50 scale",   "Anno0050scale",    ""),
                ("StdAnno.igds 100 scale",  "Anno0100scale",    ""),
                ("StdAnno.igds 200 scale",  "Anno0200scale",    ""),
                ("StdAnno.igds 400 scale",  "Anno0400scale",    ""),
                ("StdAnno.igds 800 scale",  "Anno0800scale",    ""),
                ("StdAnno.igds 2000 scale", "Anno2000scale",    ""),
                
                ("FLAnno.igds TaxlotNum",   "TaxlotsFD/TaxlotNumberAnno",  "TaxlotsFD/Taxlot"     ),
                ("FLAnno.igds Code",        "TaxlotsFD/TaxCodeAnno",       "TaxlotsFD/Taxcode"    ),
                #("FLAnno.igds Subdivision", "TaxlotsFD/SubdivisionAnno",   "TaxlotsFD/Subdivision"),
                ("FLAnno.igds TaxlotAcres", "TaxlotsFD/TaxlotAcresAnno",   "TaxlotsFD/Taxlot"     ),
           ]
    
    for (layername, outputname, linkedname) in linklist:
        
        annolayer = arcpy.mapping.ListLayers(mxd, layername, df)[0]

        linkedfc = ""
        if linkedname: 
            linkedfc = os.path.join(destination, linkedname)
            if not arcpy.Exists(linkedfc):
                aprint("ERROR: skipping \"%s\", because linked fc \"%s\" does not exist." % (layername,linkedname))
                continue
    
        outputfc  = os.path.join(destination, outputname)

        if overwrite or (not arcpy.Exists(outputfc)):
            if overwrite: deletefc(outputfc)
            import_anno(annolayer, outputfc, linkedfc, reference_scale)
                
        if arcpy.Exists(outputfc):
            aprint("Fixing fields in \"%s\" feature class." % outputname)
            fix_fontsize(outputfc)
            fix_caret(outputfc)

    return True

# "overwrite" means skip existing annotation classes
# so you can set it to "false" to just do the calc field steps (which is fast)
    
overwrite = False
try:
    mxdname          = sys.argv[1] # Normally this should be set to CURRENT
    output_workspace = sys.argv[2]
    overwrite_str    = sys.argv[3] # true or false
    if overwrite_str == "true":
        overwrite = True
except IndexError:
    print("Usage: %s <mxd name> <output workspace>" % (sys.argv[0]))
    mxdname = "C:/GeoModel/Clatsop/AnnoTemplate.mxd"
    output_workspace = "C:\\GeoModel\\Clatsop\\ORMAP-SchemaN_08-21-08.mdb"
    overwrite = True

#arcpy.AddMessage("Overwrite = \"%s\" %s" % (overwrite, type(overwrite)))
#arcpy.env.overwriteOutput = True

mxd = arcpy.mapping.MapDocument(mxdname)

df = arcpy.mapping.ListDataFrames(mxd)[0]
print("Dataframe:", df.name)    
reference_scale = "1200"

convert_anno(mxd, df, output_workspace, reference_scale, overwrite)

del mxd # release schema locks
