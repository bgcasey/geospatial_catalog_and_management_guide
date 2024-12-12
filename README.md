# Spatial Data Catalog and Management Guide
![In Development](https://img.shields.io/badge/Status-In%20Development-yellow)

A spatial data catalog and data management guide. 

for sourcing, organizing, and extracting spatial covariates. View a working list of predictor variables [here](https://github.com/bgcasey/spatial_data_catalog/blob/main/predictor_variable_list.csv).

The catalog documents all spatial data that has been pre-processed for the ABMI Science Centre. The catalog includes metadata, the relative path to the data on the Science Centre's internal server, and links to preprocessing scripts. 

This is a sibling repository to the Science Centre's geoprocessing/extraction repository.
Which contains genalized preprossing scripts and functions and vignette for summarizing spatial data to points and polygons using R.


---

## Table of Contents
- [1. Data Catalogs](#1-data-catalogs)
- [2. Scripts for Extracting and Processing Spatial Data](#2-scripts-for-extracting-and-processing-spatial-data)
- [3. Metadata Standards](#3-metadata-standards)
- [4. Data Storage](#4-data-storage)
- [5. Spatial Data Storage and Extraction Workflow](#5-spatial-data-storage-and-extraction-workflow)

---

## 1. Data Catalogs

### 1.1 Internal Catalog
- [Predictor Variable List](predictor_variable_list.csv)


### 1.2 External Catalog

- [Alberta Government Open Data](https://open.alberta.ca/opendata)
- [AltaLIS Open Data](https://www.altalis.com/)
- [Arctic-Boreal Vulnerability Experiment (ABoVE) Products](https://daac.ornl.gov/cgi-bin/dataset_lister.pl?p=34)
- [Awesome GEE Community Catalog](https://developers.google.com/earth-engine/datasets)
- [Google Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
- [National Terrestrial Ecosystem Monitoring System for Canada (NTEMS)](https://opendata.nfis.org/mapserver/nfis-change_eng.html)

**Spectral Indices**

- [Awesome Spectral Indices](https://github.com/awesome-spectral-indices/awesome-spectral-indices?tab=readme-ov-file)

---

## 2. Scripts for Extracting and Processing Spatial Data

- [Google Earth Engine Functions](https://github.com/bgcasey/google_earth_engine_functions)
- R
- ArcGIS Python

---

## 3. Metadata Standards

All spatial data should include a `readme.txt` file with metadata that complies with the **[North American Profile (NAP) of the ISO 19115: Geographic Information – Metadata Standard](https://www.fgdc.gov/standards/projects/incits-l1-standards-projects/NAP-Metadata)**. Metadata should include:


- **Title**: Clear and descriptive name.
- **Abstract**: Concise summary of the dataset's purpose, content, and scope.
- **Spatial Extent**: Bounding coordinates.
- **Temporal Extent**: Timeframe of data (e.g., 2010–2020 or "Ongoing").
- **Spatial and Temporal Resolution**: The granularity of the data (e.g., "30m resolution, monthly intervals").
- **Lineage**: Origin, processing history, and data sources.
- **Access and Use Constraints**: Licensing, usage rights, and restrictions.

See the [Spatial Metadata Template](spatial_metadata_template.txt) for more information. 

---

## 4. Data Storage

Once downloaded, data should be stored in a spatial data directory with folders organized by data thematic type. The script [create_spatial_data_dir.py](scripts/create_spatial_data_dir.py) can be used to create an empty directory. Each spatial dataset should be stored in a subfolder stored within the corresponding thematic folder. Thematic folders are based on [ISO 19115 Topic Categories](https://nap.geogratis.gc.ca/metadata/register/registerItems-eng.html#RI_653). 

| **Folder (ISO Topic Category Name)** | **Description**                                                                  | **Examples**                                                                                                                                                                       |
| ------------------------------------ | -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **farming**                          | Rearing of animals and/or cultivation of plants.                                 | Agriculture, irrigation, aquaculture, plantations, herding, pests and diseases affecting crops and livestock.                                                                      |
| **biota**                            | Flora and/or fauna in natural environments.                                      | Wildlife, vegetation, biological sciences, ecology, wilderness areas, wetlands, habitat.                                                                                           |
| **boundaries**                       | Legal land descriptions.                                                         | Political and administrative boundaries.                                                                                                                                           |
| **climatologyMeteorologyAtmosphere** | Processes and phenomena of the atmosphere.                                       | Cloud cover, weather, climate, atmospheric conditions, climate change, precipitation.                                                                                              |
| **economy**                          | Economic activities, conditions, and employment.                                 | Production, labor, revenue, commerce, industry, tourism, forestry, fisheries, commercial or subsistence hunting.                                                                   |
| **elevation**                        | Height above or below sea level.                                                 | Altitude, bathymetry, digital elevation models, slope, derived products.                                                                                                           |
| **environment**                      | Environmental resources, protection, and conservation.                           | Environmental pollution, waste storage and treatment, environmental impact assessment, monitoring environmental risk, nature reserves.                                             |
| **geoscientificInformation**         | Information pertaining to earth sciences.                                        | Geology, minerals, geophysical features and processes, hydrology, glacial geology, erosion, geomorphology, sedimentation.                                                          |
| **health**                           | Health, health services, human ecology, and safety.                              | Disease, illness, public health, health services.                                                                                                                                  |
| **imageryBaseMapsEarthCover**        | Base maps.                                                                       | Land cover, topographic maps, imagery, annotations.                                                                                                                                |
| **intelligenceMilitary**             | Military bases, structures, activities.                                          | Barracks, training grounds, military transportation, information collection.                                                                                                       |
| **inlandWaters**                     | Inland water features, drainage systems, and their characteristics.              | Rivers and glaciers, salt lakes, water utilization plans, dams, currents, floods, water quality, hydrographic charts.                                                              |
| **location**                         | Positional information and services.                                             | Addresses, geodetic networks, control points, postal zones, place names.                                                                                                           |
| **oceans**                           | Features and characteristics of salt water bodies (excluding inland waters).     | Tides, tidal waves, coastal information, reefs.                                                                                                                                    |
| **planningCadastre**                 | Information used for appropriate actions for future use of the land.             | Land use maps, zoning maps, cadastral surveys, land ownership.                                                                                                                     |
| **society**                          | Characteristics of society and culture.                                          | Settlements, anthropology, archaeology, education, traditional beliefs, manners and customs, demographic data, recreational areas and activities.                                  |
| **structure**                        | Man-made construction.                                                           | Buildings, museums, churches, factories, housing, monuments, shops, towers.                                                                                                        |
| **transportation**                   | Means and aids for conveying persons and/or goods.                               | Roads, airports, airstrips, shipping routes, tunnels, nautical charts, vehicle and vessel locations, aeronautical charts, railways, trails.                                        |
| **utilitiesCommunication**           | Energy, water and waste systems, and communications infrastructure and services. | Hydro-electricity, geothermal, solar and nuclear sources of energy, water purification, sewage treatment, electricity and gas distribution, data communication, telecommunication. |


Spatial data folders should include all data and metadata necessary to ensure efficient and reproducible workflows.

| **Item**          | **Description**                                                                                                                                                                                                  |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **data_type/**    | Folder for organizing data by thematic type, including climate, vegetation structure, spectral imagery, elevation, or land use. This structure ensures clarity and accessibility for various spatial data types. |
| ├── **data/**     | Folder containing the spatial data (rasters, shapefiles) and metadata                                                                                                                                            |
| │   ├── data.tif  | Raster data                                                                                                                                                                                                      |
| │   ├── data.shp  | Vector data                                                                                                                                                                                                      |
| │   ├── readme.md | Readme file includes product metadata, description, citation, and GitHub links to preprocessing scripts.                                                                                                         |

---

## 5. Spatial Data Storage and Extraction Workflow

```mermaid
graph TD
    A[Source Spatial Data] --> B{Does the sourced data <br> require preprocessing?}
    B -->|Yes| C[Preprocess Data]
    B -->|No| D[Download Data]
    C --> D[Download Data]
    D --> E[Store Data]
    E --> F[Extract Data to ABMI Points]

    click A href "https://github.com/bgcasey/spatial_data_catalog/blob/main/predictor_variable_list.csv" "Go to Predictor Variable List"

```
