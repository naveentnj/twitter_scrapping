# Twitter Scrapping Project with SNS Scrap tools
In these various python libraries has been used such as 

## SNScrape twitter Module
> SNScrape twitter Module is used scrap data from twitter based on the user request for a specific username like elon or specific content like post on sustainability and environment
> Using specific keywords like " from: , since: , until: " get a specific username tweets or a specific content from twitter and we can set date range.

## Pymongo
>Pymongo is used to connect with Mongo DB server and execute Mongo DB commands
>Here it is used to store the data in MongoDB as records

## Pandas
>Pandas is used to store the scrapped data in DataFrame
>It is helpful in converting the DF into CSV, JSON and Dict File


### The working flow of the app
>It will take the input text data or username based on the user selection 
>It will scrap the data with snscrap python package and get the number of tweets as the user request
>Then it will store the scrapped data in structured data frame format
>When user clicked the Store in mongo_db it will convert the dataframe into dict format and store it in the mongodb using pymongo

