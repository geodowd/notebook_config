import argparse
import rasterio
from rasterio.windows import from_bounds
import numpy as np
import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate pixel-wise mean for multiple COGs over a bbox and display the result."
    )
    parser.add_argument(
        "--cogs",
        nargs="+",
        required=True,
        help="Paths or URLs to COG files (space-separated)",
    )
    parser.add_argument(
        "--bbox",
        nargs=4,
        type=float,
        required=True,
        metavar=("MINX", "MINY", "MAXX", "MAXY"),
        help="Bounding box: minx miny maxx maxy",
    )
    return parser.parse_args()


def read_window(cog_path, bbox):
    with rasterio.open(cog_path) as src:
        window = from_bounds(*bbox, transform=src.transform)
        data = src.read(1, window=window, masked=True)
    return data


def main():
    args = parse_args()
    bbox = args.bbox
    arrays = []
    for cog in args.cogs:
        try:
            arr = read_window(cog, bbox)
            arrays.append(arr)
        except Exception as e:
            print(f"Error processing {cog}: {e}")
    if not arrays:
        print("No valid COGs processed.")
        return
    # Stack and calculate pixel-wise mean
    stack = np.ma.stack(arrays)
    mean_img = np.ma.mean(stack, axis=0)
    # Display
    plt.figure(figsize=(8, 6))
    plt.imshow(mean_img, cmap="viridis")
    plt.colorbar(label="Mean Value")
    plt.title("Pixel-wise Mean Across COGs")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.show()


if __name__ == "__main__":
    main()
