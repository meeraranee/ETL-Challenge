FINAL PROJECT REPORT FOR "CHOC IT LIKE IT'S HOT"

Extract:
We extracted data from our two Kaggle datasets: 
chocolate and coffee. We cleaned up our two datasets
in a Jupyter Notebook, dropping the columns that were
not needed. We kept four columns, "company", "country_of_origin",
"flavor_rating", "grading_year". The data was formatted using PostGreSQL in pgAdmin 4. 

Transform:
We imported our chocolate and coffee CSVs from kaggle into
a Jupyter Notebook. We then selected the four columns we
wanted and created a new dataframe only including said columns.
We exported our clean choclate and coffee datasets as two new CSV files.
These are the CSVs that we imported and combined into our SQL table.
We first created a database called "ChocItLikeItsHot" and then created
a table displaying our four extracted columns. Lastly, we imported our
CSVs into our SQL table and exported our CSV file which combined both
datasets as well as our final SQL code.

Load:
Our final database was created using PostGreSQL.
We chose PostGreSQL because we believed it would be
a simple way to display our data. If we were to repeat
this project, we would try using MongoDB and combine
more datasets and possibly venture into using an API.
