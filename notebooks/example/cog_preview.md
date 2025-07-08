# COG Preview Example Notebook

This example Jupyter notebook demonstrates how to quickly preview a Cloud Optimized GeoTIFF (COG) using Python. It is designed as a simple starting point for users who want to visualize geospatial raster data stored in COG format.

## Overview

The notebook walks through the following steps:

1. **Opening a COG**: Uses the `rasterio` library to open a COG file from a URL or local path.
2. **Efficient Data Access**: Reads either a low-resolution overview (if available) or a small window of the image to minimize data transfer and speed up visualization.
3. **Visualization**: Displays the preview using `matplotlib` with a grayscale colormap.

## Usage

1. Set the `cog_url` variable to the path or URL of your COG file.
2. Run each cell in order.
3. The notebook will display a quick preview of the raster data.

## Notes

- This notebook is intended for demonstration and educational purposes.
- For large COGs, using overviews is highly recommended for performance.
- You can adapt the code to preview different bands or use color composites for multi-band imagery.

## See Also

- [Cloud Optimized GeoTIFF](https://www.cogeo.org/)
- [Rasterio Documentation](https://rasterio.readthedocs.io/)
- [Matplotlib Documentation](https://matplotlib.org/)
