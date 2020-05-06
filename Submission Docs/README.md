China Plays Russian Roulette

1) Starting The Project

The following folders (all stored within project/) are needed to run the project: data/ static/ templates/ and application.py
From within the directory project/ use CS50s flask server to access the web application.
$ flask run
When the server is running the web application will be available through https://a6b3e403-f1e4-495f-81bd-825c136c88a8-ide.cs50.xyz:8080/

2) Navigating The Project

The index (home) page which is first presented is a welcome page which allows you to explore the two functions of the project. Each of these functions, and the home page, can be accessed by clickable links always available at the top of the page.
Supplementary details about the data are provided by Twitter, accessable via the clickable link at the bottom.

3) Using the functions - Custom Filter

On clicking through to the Custom Filter page the user is presented with 5 filters, any combination of which may be implementd.
3 of the filters Follower Count, likes received and tweet date will always have a value, though they default to values which return the entire datset (>= 0 and after 1Jan2000 respectively)
The filters which have no default value provided (language and is retweet) can be left blank, in which case no filtering will take place based on these values, or added as additional filters.
All fields have controls in place to prevent unacceptable values, eg non-dates or non-integers.

4) Using the functions - Custom Filter results

On submitting the custom filter search the user is presented with a table containing all pertinent information for each tweet that meets the criteria.
If no tweets meet the criteria then an error message is displayed and the user is returned to the create filter page.
In the table of results the header shows the total count, which can be between 1 and 39990.
Id data is provided first, then metadata, then finally the content of the hashtags and tweets. You may need to scroll right to see all this data on your screen.
User ID for each tweet is displayed and clickable. Clicking this will take you to the "all user tweets" results page for that user
The query can be rerun by clicking the Custom Filter link at the top of the page, or by returnign to the home page

5) Using the functions - Tweets by User

These results can be accessed by 2 routes. (1) By following the nav link to Tweets by User, and then entering a known user id. Eg from further research, or that the user has been working on for a while. or (2) by accessing the results directly from clicking on the user id in the custom filter table.
If taking route 1, error conditions are prompted if entering no user id or a user id which is not in the database.
Some user IDs have been hashed by twitter (see their data) so user ids can be any combination of numbers and letters
I anticipate most users to reach the results page by click through from the filters

6) Using the functions - Tweets by User - Results

First shown is a search box for USER ID, prefilled with the query.
Next the user has control over how to sort the data, by field and ascending or descending.
Finally the table of results is presented in the same format as before (scrollable in both directions)
The heading of the table provides summary data which may be of interest for larger users and data sets.

7) The data
The data is restricted to ~40k tweets taken from the first tranche of data released. The web application would work equally with a bigger database, which will be provided separately, though is currently not referenced in the web app due to size constraints.

Enjoy!

