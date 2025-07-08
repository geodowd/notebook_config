# COG Statistics Look Example Notebook

This example Jupyter notebook provides a quick overview of the key metadata and statistics for a Cloud Optimized GeoTIFF (COG) file. It is designed for users who want to inspect the properties of geospatial raster data before further analysis.

## Overview

The notebook walks through the following steps:

1. **Opening a COG**: Loads a COG file from a URL or local path using `rasterio`.
2. **Metadata Extraction**: Prints essential information such as image dimensions, number of bands, coordinate reference system (CRS), data type, bounds, and affine transform.

## Usage

1. Set the `cog_url` variable to the path or URL of your COG file.
2. Run each cell in order.
3. The notebook will print out the COG's metadata and statistics for review.

## Notes

- The notebook is intended for demonstration and educational purposes.
- Only metadata and basic statistics are displayed; no image data is visualized.
- Useful as a first step in any geospatial data analysis workflow to verify file properties.
