## External Spatial Data Catalogs

- [Alberta Government Open Data](https://open.alberta.ca/opendata)
- [AltaLIS Open Data](https://www.altalis.com/)
- [Arctic-Boreal Vulnerability Experiment (ABoVE) Products](https://daac.ornl.gov/cgi-bin/dataset_lister.pl?p=34)
- [Awesome GEE Community Catalog](https://developers.google.com/earth-engine/datasets)
- [Google Earth Engine Data Catalog](https://developers.google.com/earth-engine/datasets)
- [National Terrestrial Ecosystem Monitoring System for Canada (NTEMS)](https://opendata.nfis.org/mapserver/nfis-change_eng.html).

Spectral Indices

- [Awesome Spectral Indices](https://github.com/awesome-spectral-indices/awesome-spectral-indices?tab=readme-ov-file)

## Scripts for extracting and processing spatial data

- [Google Earth Engine Functions](https://github.com/bgcasey/google_earth_engine_functions)
- R
- ArcGIS Python

## Metadata standards

All spatial data should include a readme `.txt` file with metadata that complies with the **ISO 19115: Geographic information - Metadata standard** and should include:

- **Title**: Dataset name (e.g., "Global Land Cover 2020").
- **Abstract**: A brief description of the data.
- **Spatial extent**: Bounding coordinates.
- **Temporal extent**: Date range of data collection.
- **Resolution**: Spatial and temporal.
- **Source**: Original provider (e.g., NASA, Copernicus).
- **Licensing**: Usage rights and restrictions

## Data Storage

Once downloaded, data should be stored in separate folders with the following structure:

| **Item**                                                              | **Description**                                                                                         |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <span style="color:#7D3C98">**data_type/**</span>                     | Folder for organizing data by type (climate, vegetation structure, spectral, etc.)                      |
| ├── <span style="color:#5E2D30FF">**data/**</span>                    | Folder containing the spatial data (rasters, shapefiles) and metadata                                   |
| │   ├── <span style="color:#008E90FF">data.tif</span>                 | Raster data                                                                                             |
| │   ├── <span style="color:#008E90FF">data.shp</span>                 | Vector data                                                                                             |
| │   ├── <span style="color:#008E90FF">readme.md</span>                | Readme file includes a product description, citation, and metadata                                      |
| │   ├── <span style="color:#008E90FF">data_process.{js, R, py}</span> | Script to process spatial data (e.g. calculate indices, mosaic tiles, calculate focal statistics, etc.) |
| │   ├── <span style="color:#008E90FF">data_extract.R</span>           | R file for summarizing spatial data to point locations                                                  |


**Example directory:**


| **Item**                                                                       | **Description**                                                                      |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| <span style="color:#7D3C98">**climate/**</span>                                | Folder for climate-related data sources                                              |
| ├── <span style="color:#5E2D30FF">**temperature/**</span>                      | Subfolder for temperature data                                                       |
| │   ├── <span style="color:#008E90FF">temperature.tif</span>                   | Raster data for temperature                                                          |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for temperature   |
| │   ├── <span style="color:#008E90FF">temperature_process.{js, R, py}</span>   | Script to process temperature spatial data                                           |
| │   ├── <span style="color:#008E90FF">temperature_extract.R</span>             | R file for summarizing temperature data to point locations                           |
| ├── <span style="color:#5E2D30FF">**precipitation/**</span>                    | Subfolder for precipitation data                                                     |
| │   ├── <span style="color:#008E90FF">precipitation.tif</span>                 | Raster data for precipitation                                                        |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for precipitation |
| │   ├── <span style="color:#008E90FF">precipitation_process.{js, R, py}</span> | Script to process precipitation spatial data                                         |
| │   ├── <span style="color:#008E90FF">precipitation_extract.R</span>           | R file for summarizing precipitation data to point locations                         |
| <span style="color:#7D3C98">**spectral/**</span>                               | Folder for spectral-related data sources                                             |
| ├── <span style="color:#5E2D30FF">**NDVI/**</span>                             | Subfolder for NDVI (Normalized Difference Vegetation Index) data                     |
| │   ├── <span style="color:#008E90FF">NDVI.tif</span>                          | Raster data for NDVI                                                                 |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for NDVI          |
| │   ├── <span style="color:#008E90FF">NDVI_process.{js, R, py}</span>          | Script to process NDVI spatial data                                                  |
| │   ├── <span style="color:#008E90FF">NDVI_extract.R</span>                    | R file for summarizing NDVI data to point locations                                  |
| ├── <span style="color:#5E2D30FF">**NBR/**</span>                              | Subfolder for NBR (Normalized Burn Ratio) data                                       |
| │   ├── <span style="color:#008E90FF">NBR.tif</span>                           | Raster data for NBR                                                                  |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for NBR           |
| │   ├── <span style="color:#008E90FF">NBR_process.{js, R, py}</span>           | Script to process NBR spatial data                                                   |
| │   ├── <span style="color:#008E90FF">NBR_extract.R</span>                     | R file for summarizing NBR data to point locations                                   |
| <span style="color:#7D3C98">**vegetation_structure/**</span>                   | Folder for vegetation structure-related data sources                                 |
| ├── <span style="color:#5E2D30FF">**canopy_height/**</span>                    | Subfolder for canopy height data                                                     |
| │   ├── <span style="color:#008E90FF">canopy_height.tif</span>                 | Raster data for canopy height                                                        |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for canopy height |
| │   ├── <span style="color:#008E90FF">canopy_height_process.{js, R, py}</span> | Script to process canopy height spatial data                                         |
| │   ├── <span style="color:#008E90FF">canopy_height_extract.R</span>           | R file for summarizing canopy height data to point locations                         |
| ├── <span style="color:#5E2D30FF">**canopy_cv/**</span>                        | Subfolder for canopy coefficient of variation (CV) data                              |
| │   ├── <span style="color:#008E90FF">canopy_cv.tif</span>                     | Raster data for canopy CV                                                            |
| │   ├── <span style="color:#008E90FF">readme.md</span>                         | Readme file includes a product description, citation, and metadata for canopy CV     |
| │   ├── <span style="color:#008E90FF">canopy_cv_process.{js, R, py}</span>     | Script to process canopy CV spatial data                                             |
| │   ├── <span style="color:#008E90FF">canopy_cv_extract.R</span>               | R file for summarizing canopy CV data to point locations                             |
