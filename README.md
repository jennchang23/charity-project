# Charity Project

# ETL Project Submission
by Samir Sundar, Jade Guo, Jennie Chang, Sanaz Shahbazian, Jack Oremus

## Project Overview

<p align="center">
  <img width="460" height="200" src="images/netflix.png">
</p>
<p align="center">
  <img width="300" height="75" src="images/rotten_tomatoes.jpg">
</p>

Bring Rotten Tomatoes ratings to Netflix movies
- Join Netflix data and Rotten Tomatoes data by movie name & release year

## EXTRACT
Data Sources found on Kaggle:
- Netflix Movies and TV Shows by Shivam Bansal
- Rotten Tomatoes - Movies and Critics datasets by Stefano Leone
  
Both datasets were in CSV format

## TRANSFORM - What data cleaning/transformation was required?
- Cleaning
  - Both datasets: replace all null values with "NA"
  - Netflix: kept all columns as is as Netflix data serves as parent dataset
  - Netflix: renamed "listed_in" to "genre" and "title" to "movie_title" to be more explicit
  - Rotten Tomatoes: renamed "in_theaters_date" to "RT_release_date"
  - Rotten Tomatoes: exclude all columns except for rotten_tomatoes_link, movie_title, in_theaters_date, tomatometer_status, tomatometer_rating, audience_rating
   - Filtered both datasets for movies specifically (excluded TV shows)
  
- Joining
  - Join datasets based on unique key concatenated by movie title and release year as these are the two columns that exist in both datasets and have a higher likelihood of being the same across both. Release year was included in case some movies are a remake of an original movie.
  
<p align="center">
  <img width="800" height="550" src="images/Netflix_RT_ERD_Diagram_cropped.png">
</p>
   

## LOAD
 - Load the final table to a relational database - Postgres SQL as we don't have any non-relational data.
 
