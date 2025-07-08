# NDVI Calculation Example Notebook

This example Jupyter notebook demonstrates how to calculate the Normalized Difference Vegetation Index (NDVI) from a Cloud Optimized GeoTIFF (COG) using Python geospatial libraries. It is designed for users interested in remote sensing and vegetation analysis.

## Overview

The notebook walks through the following steps:

1. **Opening a COG**: Loads a multi-band COG file using `rioxarray`.
2. **Bounding Box Clipping**: Optionally clips the raster to a user-specified bounding box, transforming coordinates if needed.
3. **Band Selection**: Selects the NIR (band 8) and Red (band 4) bands required for NDVI calculation.
4. **NDVI Computation**: Calculates NDVI using the standard formula and handles potential division by zero.
5. **Visualization**: Displays the NDVI image using a suitable color map for interpretation.

## Usage

1. Set the `cog_url` variable to the path or URL of your COG file.
2. Optionally, set the `bbox` variable to a bounding box in EPSG:4326 coordinates.
3. Run each cell in order.
4. The notebook will display the calculated NDVI image.

## Notes

- The notebook is intended for demonstration and educational purposes.
- The COG must contain at least bands 4 (Red) and 8 (NIR) for NDVI calculation.
- Handles coordinate transformation if the raster CRS differs from EPSG:4326.
- You can adapt the code to use different bands or indices as needed.
- Useful for quick vegetation health checks and remote sensing analysis.
