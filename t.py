import logging
from landez import MBTilesBuilder

logging.basicConfig(level=logging.DEBUG)

mb = MBTilesBuilder(stylefile="yourstyle.xml", filepath="kochi.mbtiles")
mb.add_coverage(bbox=(-180.0, -90.0, 180.0, 90.0),
                zoomlevels=[0, 1])
mb.run()
