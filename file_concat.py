# XML file combiner for
# Exploring Exoplanets
# Erin Braswell
# Final project, CS50, Fall 2013

import shutil
import xml.etree.ElementTree as ET, glob

# create a new global xml file
with open('systems.xml', 'wb') as outfile:

    # write the opening systems tag
    outfile.write("<systems>\n")

    # loop over all of the xml files in the updated catalog
    for filename in glob.glob('../open_exoplanet_catalogue/systems/*.xml'):

    # copy the contents of that file to the master xml file
        with open(filename) as readfile:
            shutil.copyfileobj(readfile, outfile)

    # write the closing systems tag
    outfile.write('</systems>')