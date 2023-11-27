# WP_media_descritption
This repository contains scripts to create HTML-Links for media in Wordpress and to uplaod them as the description-tag in bulk.

WP Media Description is a collection of Python 3 scripts designed to simplify the process of managing image descriptions in WordPress. These scripts are currently in development and focus on individual steps of the workflow. The following Python libraries are required: pandas, requests, and os.

## Scripts Included

1. **1_Create_Table**: To kickstart the process, run this script to create an initial Excel file listing all JPG files. This file will serve as the foundation for the subsequent steps.

2. **Upload Check Script**: This script checks whether all files from the specified folder have already been uploaded to WordPress. It provides a list of missing files directly in the console for easy identification.

3. **Excel to HTML Description Script**: This script takes an Excel spreadsheet as input, specifically looking at columns containing image names and links. It generates HTML descriptions based on this data, making it easier to create image descriptions for WordPress.

4. **ID Lookup Script**: Using the same Excel spreadsheet, this script searches for image IDs based on file names. It helps establish a connection between image files and their respective WordPress IDs.

5. **Description Upload Script**: Once the HTML descriptions are generated and image IDs are found, this script uploads the descriptions to the corresponding IDs, ensuring that image descriptions are synchronized with the WordPress media library.

## Getting Started

To use these scripts effectively, follow these steps:

1. Clone or download this repository to your local machine.

2. Set up the necessary configuration parameters in each script, such as WordPress credentials and file paths.

3. Run the scripts individually in the order described above, following the prompts and instructions provided within each script.

4. Review the README files within each script's folder for detailed usage guidelines and examples.

## Contributions and Issues

We welcome contributions to enhance the functionality of these scripts. If you encounter any issues or have suggestions for improvements, please open an issue in this repository. Contributions through pull requests are also appreciated.

## License

This project is licensed under the [MIT License](LICENSE), which means you are free to use, modify, and distribute the code while retaining the original license and attribution.

