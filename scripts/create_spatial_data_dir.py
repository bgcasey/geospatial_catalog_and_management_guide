import os

# Dictionary of ISO topic categories with their descriptions (used as subfolders)
iso_topic_categories = {
    "farming": ["agriculture", "irrigation"],
    "biota": ["wildlife", "vegetation", "ecology", "wetlands"],
    "boundaries": ["administrativeBoundaries"],
    "climatologyMeteorologyAtmosphere": ["temperature", "atmosphericConditions", "precipitation"],
    "economy": ["forestry", "energy"],
    "elevation": ["DEM", "terrainAnalysis"],
    "environment": ["pollution", "environmentalImpact", "riskMonitoring"],
    "geoscientificInformation": ["geology", "soil"],
    "imageryBaseMapsEarthCover": ["landCover", "satelliteImagery"],
    "inlandWaters": ["rivers", "lakes", "waterQuality"],
    "transportation": ["roads"]
}

# Base directory for spatial data
base_dir = "spatialData"

# Create the base directory 
os.makedirs(base_dir, exist_ok=True)

# Create topic category folders and their subfolders
for category, subfolders in iso_topic_categories.items():
    category_path = os.path.join(base_dir, category)
    os.makedirs(category_path, exist_ok=True)
    for subfolder in subfolders:
        subfolder_path = os.path.join(category_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
    print(f"Created folder structure for: {category}")

print("Spatial data directory structure with camelCase subfolders created successfully.")
