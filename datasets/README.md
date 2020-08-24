# Dataset info

Each CSV file contains a month. Content is separated by semicolon ';' as there are some values with comma ','.

## Description of columns

Column | Description
------ | -----------
id | An identity of each row in the database
month | The month of data collection
year | The year of data collection
datetime | The timestamp of data collection
depth | The depth of the URL (usually ZERO for domain level)
urlid | An identity of each URL in the data collection
url | The endpoint of data portal in the form of URL
domain | The domain return by urllib - sometimes it is different from URL. Please, consider URL 
platform | The identified open data software platform. See table below for the 8 considered ones
dataset_total | Number os datasets inside the data portal
domain_country | The returned country obtained by ccTLD - method 1
ip_country | The returned country obtained by IP - method 2
country_name | The considered country according the method that worked
country_alpha-2_code | The standardized ISO 3166-1 country codes (see https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
root_domain | The root domain of data portal
rank | Indicates if the data portal is duplicated within datasets (whether > 1)

## Identified open data software platforms

N# | Platform | Link for information
-- | -------- | --------------------
1 | CKAN | https://docs.ckan.org/
2 | DKAN | https://dkan.readthedocs.io/en/latest/admin/
3 | Socrata | https://dev.socrata.com/
4 | OpenDataSoft | https://data.opendatasoft.com/api/v2/console
5 | ArcGIS Open Data | https://www.esri.com/en-us/arcgis/products/arcgis-open-data | https://akharris.github.io/arc-swag
6 | uData | https://pypi.org/project/udata/
7 | Junar | https://www.junar.com/ https://junar.github.io/docs/en/_sections/01-index.html
8 | PublishMyData | https://www.swirrl.com/

