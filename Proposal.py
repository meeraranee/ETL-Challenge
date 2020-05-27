PROPOSAL FOR "CHOC IT LIKE IT'S HOT"

Where is the data coming from? (at least two sources)
- The data is coming from kaggle.com: https://www.kaggle.com/rtatman/chocolate-bar-ratings & https://www.kaggle.com/volpatto/coffee-quality-database-from-cqi?select=arabica_data_cleaned.csv

Where is the data going to? (postgres, mongo, etc; some type of database not a flat file like a CSV.)
- We are using PostGres.

What will be the structure of the data in the final database? What tables/columns/types/etc.
- The structure of the data in the final database will include the following columns: "Country of Origin", "Company", "Flavor Rating", "Grading Date".

What steps are required to take the data from its current form into its final form and who is responsible for each step?
- We are cleaning up both datasets and extracting our specified columns. Matt cleaned up the dates for our Coffee dataset so that the columns for the dates show only years. Meera converted the grading scales for the cacao bean flavor profiles in both datasets (scales of 1-5 and 1-10) so that they can be easily compared. Madison extracted the columns needed (named above) from both datasets and combined them into one dataset.
