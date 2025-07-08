# Mean Value Calculation Example Notebook

This example Jupyter notebook demonstrates how to calculate the pixel-wise mean across multiple Cloud Optimized GeoTIFFs (COGs) within a specified bounding box. It is intended as a practical guide for users interested in basic raster data analysis and visualization.

## Overview

The notebook walks through the following steps:

1. **Reading COGs**: Loads multiple COG files from provided URLs or paths.
2. **Bounding Box Selection**: Automatically determines a small bounding box centered within the first COG, or allows for custom bounding box input.
3. **Windowed Data Extraction**: Reads only the data within the bounding box from each COG for efficiency.
4. **Mean Calculation**: Stacks the extracted arrays and computes the pixel-wise mean across all COGs.
5. **Visualization**: Displays the resulting mean image using a color map for easy interpretation.

## Usage

1. Set the `cog_url` variable to a comma-separated list of COG URLs or file paths.
2. Run each cell in order.
3. The notebook will automatically extract a small bounding box and calculate the mean image across the selected COGs.
4. The result is visualized as a color image.

## Notes

- The notebook is intended for demonstration and educational purposes.
- Only the first band of each COG is used in the calculation.
- If any COG cannot be read, it will be skipped with an error message.
- You can modify the bounding box logic to analyze different regions or use your own coordinates.
- Useful for quick statistical summaries or quality checks across multiple geospatial datasets.
