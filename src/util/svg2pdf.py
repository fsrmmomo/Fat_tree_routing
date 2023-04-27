import cairosvg
import os
svg_file = '../../svg2pdf/svg/2-bf.svg'


pdf_file = '../../svg2pdf/pdf/2-bf.pdf'
res = cairosvg.svg2pdf(url=svg_file,write_to=pdf_file)