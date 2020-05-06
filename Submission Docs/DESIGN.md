China Plays Russian Roulette
1)	Implementing the SQL database

Chinadata.db is implemented with 2 tables, tweets and users, though only tweets is used in the final project. The tables are designed to replicate the data which is provided by Twitter, with each column replicated from the csv file which is distributed. The reason for this is future flexibility. Whilst the project has focussed solely on Chinese state sponsored tweets, Twitter provides and regularly updates this data for numerous other countries. The implementation is independent of the country under investigation. A new country could be studied by replicating the database structure, populating with the new csv file, and changing the db source in the application.py file.

Population of the db was carried out offline, in a PyCharm IDE, having imported various modules using Anaconda. The Panda module is eventually used to quickly copy the csv to SQL database using the scripts in the Offline folder. The panda module was used because, whilst less flexible than running a for loop over specific values, it was considerably quicker, having been optimised for the task. Due to size constrains in cs50 IDE only a reduced form of chinadata.db was included, which ahs 40k tweets. The full database is stored in a google drive and could be added as the source if the web application were hosted from a different depository. The small database was used to show the code for the application works as expected.

2)	Application.py

The first part of the file, replicating the distribution code from CS50 finance, imports the necessary modules to serve a Flask based web app using a SQL database.

There are 4 routes.

Home, redirects to the index page.

Index provides a welcome and instructions for the site usage through rendering of home.html.

The other two routes represent the major functions of the project, namely user search and custom filters.

The /display route implements the custom filter. When the method is GET the route renders the displayask.html template, which contains the entry form for filters. This same template is also rendered when the method is POST, but the filter returns 0 results. In this instance displayask.html is rendered with the addition of an apology message. The function is carried out by the /display route,  method = post, which indicates a successful custom filter request. The 5 filter fields are converted in strings which are empty if the filter is empty, allowing the user to enter any combination of the 5 filters and more/less than logic for 3 of them. This filter is concatenated to the db.execute query, ensuring only the correct results are returned.
Rows which match the filters are returned in “rows”, a variable which contains a list of dictionaries. From here the desired data is extracted, cleaned and formatted for table display, such that only one set of data needs to be passed to the html template. This is dictindex, which is a list of dictionaries, where each list item represents a tweet, and for each tweet there is a key-value pair for each column.

The resulting information is displayed in display.html with each row populated by a for loop. Whilst most of the <td> elements contain just information, the second column contains a button. The value displayed on the button is the userid, whilst clicking on the button allows the user to access all the tweets by that user. This is achieved by a hidden text field, which contains the same value of userid as is displayed. The button carries out the submit function for this form, which submits the userid to route /user with method post.

This is identical to what happens when a user manually enters a userid in userask.html template.

In both cases user.html is rendered with information for the table produced in an analogous manner as for display.html. The main point of difference for user.html is the ability to custom sort the data. This is done by reposting the user id to /user but with an additional parameter specified in the SQL query, which selects the column by which to sort the data and the order. The most challenging bit of the whole project (for something so little!) was to make the dropdown menus hold the submitted values after the form is resubmitted, rather than defaulting to their original values. This is ultimately achieved by the inclusion of a jquery script in the body of the user.html page. I did not separate the script out as it is very short, contained, and by being included reduced the need for a more complex chain of event listeners. The script defines a function which sets an ID element to a specific value, and then calls the function twice on both drop down menus, with the values specified by variables orderfield and orderby. The variables are passed, with the list of tweet data, from application.py which has received them as part of the post request.

James Hutt
4th Dec 2019

