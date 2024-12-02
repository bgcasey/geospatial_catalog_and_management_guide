# Spatial Data Catalog and Management Guide
![In Development](https://img.shields.io/badge/Status-In%20Development-yellow)

A spatial data catalog and guide for sourcing, organizing, and extracting spatial covariates. View a working list of predictor variables [here](https://github.com/bgcasey/spatial_data_catalog/blob/main/predictor_variable_list.csv).

---

## Table of Contents
- [1. Data Catalogs](#1-data-catalogs)
- [2. Scripts for Extracting and Processing Spatial Data](#2-scripts-for-extracting-and-processing-spatial-data)
- [3. Metadata Standards](#3-metadata-standards)
- [4. Data Storage](#4-data-storage)
- [5. Spatial Data Storage and Extraction Workflow](#4-spatial-data-storage-and-extraction-workflow)

---

## 1. Data Catalogs

### 1.1 Internal Catalog
- [predictor_variable_list.csv](predictor_variable_list.csv)


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

Once downloaded, data should be stored in separate folders with the following structure. 
Spatial data should be organized by data type and include all of the necessary preprocessing and data extraction scripts to ensure efficient and reproducible workflows.


| **Item**                                                              | **Description**                                                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <span style="color:#7D3C98">**data_type/**</span>                     | Folder for organizing data by type (climate, vegetation structure, spectral, etc.)                      |
| ├── <span style="color:#5E2D30FF">**data/**</span>                    | Folder containing the spatial data (rasters, shapefiles) and metadata                                   |
| │   ├── <span style="color:#008E90FF">data.tif</span>                 | Raster data                                                                                             |
| │   ├── <span style="color:#008E90FF">data.shp</span>                 | Vector data                                                                                             |
| │   ├── <span style="color:#008E90FF">readme.md</span>                | Readme file includes a product description, citation, and metadata                                      |
| │   ├── <span style="color:#008E90FF">data_process.{js, R, py}</span> | Data preprocessing script (e.g., calculate indices, mosaic tiles, calculate focal statistics, etc.) |
| │   ├── <span style="color:#008E90FF">data_extract.R</span>           | Reproducable R script for summarizing spatial data to point locations                                                  |


**Example directory:**


| **Item**                                                                       | **Description**                                                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| <span style="color:#7D3C98">**climate/**</span>                                | Folder for climate-related data sources                                              |
| ├── <span style="color:#5E2D30FF">**temperature/**</span>                      | Subfolder for temperature data                                                       |
| │   ├── <span style="color:#008E90FF">temperature.tif</span>                   | Raster data for temperature                                                          |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for temperature   |
| │   ├── <span style="color:#008E90FF">temperature_process.{js, R, py}</span>   | Preprocessing script for temperature spatial data                                           |
| │   ├── <span style="color:#008E90FF">temperature_extract.R</span>             | R file for summarizing temperature data to point locations                           |
| ├── <span style="color:#5E2D30FF">**precipitation/**</span>                    | Subfolder for precipitation data                                                     |
| │   ├── <span style="color:#008E90FF">precipitation.tif</span>                 | Raster data for precipitation                                                        |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for precipitation |
| │   ├── <span style="color:#008E90FF">precipitation_process.{js, R, py}</span> | Preprocessing script for precipitation spatial data                                         |
| │   ├── <span style="color:#008E90FF">precipitation_extract.R</span>           | R file for summarizing precipitation data to point locations                         |
| <span style="color:#7D3C98">**spectral/**</span>                               | Folder for spectral-related data sources                                             |
| ├── <span style="color:#5E2D30FF">**NDVI/**</span>                             | Subfolder for NDVI (Normalized Difference Vegetation Index) data                     |
| │   ├── <span style="color:#008E90FF">NDVI.tif</span>                          | Raster data for NDVI                                                                 |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for NDVI          |
| │   ├── <span style="color:#008E90FF">NDVI_process.{js, R, py}</span>          | Preprocessing script for NDVI spatial data                                                  |
| │   ├── <span style="color:#008E90FF">NDVI_extract.R</span>                    | R file for summarizing NDVI data to point locations                                  |
| ├── <span style="color:#5E2D30FF">**NBR/**</span>                              | Subfolder for NBR (Normalized Burn Ratio) data                                       |
| │   ├── <span style="color:#008E90FF">NBR.tif</span>                           | Raster data for NBR                                                                  |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for NBR           |
| │   ├── <span style="color:#008E90FF">NBR_process.{js, R, py}</span>           | Preprocessing script for NBR spatial data                                                    |
| │   ├── <span style="color:#008E90FF">NBR_extract.R</span>                     | R file for summarizing NBR data to point locations                                   |
| <span style="color:#7D3C98">**vegetation_structure/**</span>                   | Folder for vegetation structure-related data sources                                 |
| ├── <span style="color:#5E2D30FF">**canopy_height/**</span>                    | Subfolder for canopy height data                                                     |
| │   ├── <span style="color:#008E90FF">canopy_height.tif</span>                 | Raster data for canopy height                                                        |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for canopy height |
| │   ├── <span style="color:#008E90FF">canopy_height_process.{js, R, py}</span> | Preprocessing script for canopy height spatial data                                         |
| │   ├── <span style="color:#008E90FF">canopy_height_extract.R</span>           | R file for summarizing canopy height data to point locations                         |
| ├── <span style="color:#5E2D30FF">**canopy_cv/**</span>                        | Subfolder for canopy coefficient of variation (CV) data                              |
| │   ├── <span style="color:#008E90FF">canopy_cv.tif</span>                     | Raster data for canopy CV                                                            |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for canopy CV     |
| │   ├── <span style="color:#008E90FF">canopy_cv_process.{js, R, py}</span>     | Preprocessing script for canopy CV spatial data                                            |
| │   ├── <span style="color:#008E90FF">canopy_cv_extract.R</span>               | R file for summarizing canopy CV data to point locations                             |

---

## 4. Spatial Data Storage and Extraction Workflow
