import numpy as np
import astropy.io.ascii as ascii
import astropy.io.fits as fits
from astropy import units as u
from astropy.coordinates import Angle, SkyCoord
from regions import CircleSkyRegion, CirclePixelRegion, write_ds9, PixCoord

from mirisim.skysim.builder import scenemaker

    # A description of what this file should do:

    #   * Read in an input file that contains coordinates. these will usually be pixel coordinates.
    #       - scene file: offsets in arcseconds, offset from centre
    #       - sextractor output files: coordinates in pixels
    #   * Assemble the coordinates, object size, and label. only the coordinates are essential.
    #   * Write out into a DS9 region file.
    
    
    



def read_scene(infile=None):
    
    '''
    This function will read in a MIRISim scene file and return a list of regions. Working notes:
    - consider only the coordinates, not the sizes
    - assume a fixed pixel scale of 0.11 arcsec/px to convert from arcsec to pixels.
    
    Input
    -----
    - infile: a .ini file containing the scene.
     
    '''
    r = Angle(10., 'arcsec')
    sc = scenemaker(configfile=infile)
    coord_list = []
    for src in sc.sources:
        if hasattr(src, 'Cen'):
            x,y,name = src.Cen[0], src.Cen[1], src.name
            c = SkyCoord(x, y, unit='arcsec')
            reg = CircleSkyRegion(c, r)
            coord_list.append(reg)

    return coord_list
    
#=============================================================================

def read_sextractor(infile=None):
    '''
    This function will read in a sectractor output and return a list of regions. Working notes:
    - how do the SexTractor coordinates work? the test files ones don't make sense for MIRI.
    
    Input
    -----
    - infile: the sextractor output file
     
    '''
    
    # sextractor files can be read in with astropy.io.ascii hurrah
    t = ascii.read(infile)
    
    # now format each line into a CirclePixelRegion object
    coord_list = []
    
    for i in range(len(t)):
        reg = CirclePixelRegion(center=PixCoord(x=t['X_IMAGE'][i], y=t['Y_IMAGE'][i]), radius=t['FWHM_IMAGE'][i]/2.)
        coord_list.append(reg)
    
    return coord_list
    

#=============================================================================    
    
def make_regions(file=None, filetype=None, outfile='ds9.reg'):

    '''
    This function will read in the input file of type "filetype" and write out to a DS9 region file. 
    
    Parameters
    ----------
    - file:     filename [string]
    - filetype: type of file, to determine format. supported: 'sextractor', 'scene' [string]
    - outfile:  output filename. default: 'ds9.reg'. [string]
    
    
    '''
    
    # code to read in the input file
    
    if (filetype=='sextractor'):
        reg_list = read_sextractor(infile=file)
        # the list of regions can be written to a DG9 region file: 
        write_ds9(reg_list, outfile, coordsys='physical')
    
    elif (filetype=='scene'):
        reg_list = read_scene(infile=file)
        # the list of regions can be written to a DG9 region file: 
        write_ds9(reg_list, outfile)
    
    else:
        raise IOError('Input filetype not recognised!')
        

# adjust coordinates to get pixel (x,y) coordinates


# write out into a region file
    
    return 0

#=============================================================================

if __name__ == "__main__":
    import sys
    make_regions(file=sys.argv[1], filetype=sys.argv[2], outfile=sys.argv[3])