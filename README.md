# emmaDataChallenge
Steps to run the script
- You need python 2.7 and the dependencies mentioned in requirements.txt. Script to run is main.py. Please enter the
database credentials and file path when prompted. 
If you change the following parameters in the postgres, it will reduce the load time
max_wal_size = 2GB

NOTE: Please note that in the file load_user_data_queries at line 60, I have added an extra column. It's because file has a tab
after 59th column which postgres considers as another column.


Database design
- There is one-to-many relationship between userProfile table and relationship table. user_profile table has fields which
are accessing, filtering or supporting common search queries (user_id,, public, completion_percentage, gender, region, 
last_login, registration and age). Other fields are part of data field (json blob). It is useful to list these details 
but searching might be slow depending how you are indexing this column. 


How would a hybrid system (PostgreSQL + <something else>) help you optimize for the
optimal situation like ad-hoc searching, fast importing of large amounts of data, fast exporting and quick responses
for gathering large amounts of data.
- A hybrid system of PostgreSQL and Elasticsearch will be very helpful in the above mentioned scenario. If one wants to
find out all friends of a user with profession as "acting", I will get friend list from the Postgres and then use
Elastic search to find the profession as "acting". Import and exporting could be handled by Postgres itself by doing 
batch import/export. Also, for quick response for large data, this hybrid approach should work well.


What type of hybrid systems would you supplement with for searching? Analytics? Bulk
importing and exporting?
- As I mentioned for search and bulk import and export, Postgres and Elastic search combined should work. 
Also, NoSQL like mongoDb could be helpful too by storing all of the user information in one document along with relationship.
For Analytics, OLAP system like Redshift will be beneficial.


What kind of scale and growth issues or gains do you feel this approach gives you?
- For scaling an growth, sharding of the user profiles table based on certain criteria like region will be helpful. This 
will help system grow horizontally. 


What changes would you make if you knew the system was read heavy? Write heavy?
- If its a read heavy system, cache (client/server) with master slave configuration of the database is very helpful. 
If its a write heavy system, Sharding data and adding more nodes will be helpful.

What are some ways you could expose this design via an HTTP API?
- The API's I can expose with this design are
Create new user,
Create new relationship,
Get user details with friend list,
Update user detail and friends,
Searching based on certain criteria,  
Delete a relationship,
Delete a user.
