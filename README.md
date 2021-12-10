# Data Conversion project

We moved from ArcInfo 9 to ArcMap 10 so all the old coverages etc were managed with AML.
I had to move all the data into ArcGIS Enterprise feature classes. That's what this
project is for.

# Some details

I use a single python script to call a series of operations.

In testing, I generally process one township or one row of townships
because it's faster. One township takes something like 5-10 minutes,
the entire county takes around 2-3 hours.

In very general terms --

  for each township 
     import coverages for township from K drive
     preprocess the township in AML to produce intermediary coverages
     build geometry feature classes in filegeodatabase
     build annotation feature classes 

Once each township is converted then another pass combines the data for
each township into a single file geodatabase.

Source data is copied from K drive to a copy on C,
then it's processed to produce a set of intermediate coverages,
then the coverages are converted into a file geodatabase.

Geometry (points, lines, polygons) so far is very easy to deal with, and I
consider that part to be "done".

Annotation is still elusive.
