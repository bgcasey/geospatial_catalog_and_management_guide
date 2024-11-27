rProject_template

The readme for your rProject should include a top level description of the project, and a map of content that describes the directory structure and descriptions of your project files.


| **Item**                 | **Description**                   |
| ------------------------ | --------------------------------- |
| **0_data/**              | Raw and manipulated data          |
| ├── external/            | Raw data from external sources    |
| ├── processed/           | Data that has been manipulated    |
| **1_code/**              | Code and scripts for analysis     |
| ├── GEE/                 | Google Earth Engine scripts       |
| │   └── gee_git_clone.sh | Script to clone GEE repository    |
| ├── r_scripts/           | R scripts for data processing     |
| │   └── r_module.R       | Template R script                 |
| │   └── r_function.R     | Template R function               |
| **2_pipeline/**          | Data processing pipeline          |
| **3_output/**            | Results of analysis               |
| ├── data/                | Processed datasets                |
| ├── figures/             | Generated figures                 |
| ├── maps/                | Generated maps                    |
| ├── models/              | Model outputs                     |
| └── tables/              | Tables from analysis              |
| **4_writing/**           | Manuscript and reports            |
| ├── manuscript/          | Drafts of the manuscript          |
| └── reports/             | Reports and additional documents  |
| **5_presentations/**     | Presentation materials            |
| ├── slides/              | Presentation slides (e.g., .pptx) |
| └── posters/             | Conference posters                |
| **README.md**            | Project overview and instructions |
