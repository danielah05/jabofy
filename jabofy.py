import numpy as np
from PIL import Image
import sys, os

for file in sys.argv[1:]:
    f, e = os.path.splitext(file)
    outfile = f + "_jabofied.png"
    input = Image.open(file)
    width, height = input.size
    scalewidth = width*2+1
    scaleheight = height*2+1
    bg = Image.new("RGBA", (scalewidth, scaleheight), (0, 0, 0))
    scaleimage = input.resize([scalewidth, scaleheight], Image.BILINEAR)
    
    scaleimage_np = np.array(scaleimage)
    bg_np = np.array(bg)
    
    alphamask = scaleimage_np[:, :, 3] == 0
    
    bg_np[alphamask, 3] = 0
    
    final = Image.fromarray(bg_np)
    
    finalreal = Image.alpha_composite(final, scaleimage)
    
    imagecrop = (0, 0, scalewidth-1, scaleheight-1)
    
    finalrealbutactually = finalreal.crop(imagecrop)
    
    finalrealbutactually.save(outfile, "PNG")