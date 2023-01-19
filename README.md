Here I proposed a search application for metaphors in Tamil songs. Metaphor is a figure of speech in a word or phrase which really describes an object or idea instead of another which is not literally true but explains an idea or suggest a comparison. It’s mainly used in songs to add some flavor to the song which may be difficult to understand for some people. For getting the meaning or idea of the metaphors in Tamil songs, I proposed this search application.  

Initially I have planned to build a text corpus of metaphors contains more than 100 unique and best Tamil songs of A.R.Rahman, Anirudh, Ilaiyaraya and Yuvan Shankar Raja from 2000 to 2022. And each song should have at least one metaphor and must include all metaphors in the song. And for each song, I have planned to include following attributes:
1.	Title – Title of the song
2.	Lyrics – Full lyrics of the song in Tamil
3.	Lyricist – A person who writes the lyrics of the song.
4.	Singer – A person who sings the song
5.	Composer – A person who writes the music of the song
6.	Album – Movie name / Album name where the song includes.
7.	Year – Released year of the song
8.	Metaphor (All metaphors in the song). Metaphor contains following attributes:
i.	Type of Metaphor
ii.	Source domain
iii.	Target domain
iv.	Interpretation

I have planned to collect data from internet. If there are any other language words in the song, it must be converted into Tamil language. 

Scope of the project:
1.	Provide the meaning of the metaphors for users who wants to know the meaning or idea of the metaphor in Tamil song.
2.	User can search based on type of metaphor or source domain the metaphor or target domain of the metaphor.

Framework: Elastic Search is used as the information retrieval library

This repository contains both frontend and backend of the search application. It's used Elasticsearch to retrieve the information.

Directory Structure of the project:
  •	Corpus - It contains the original csv file and indexed json file which is generated by running IndexJSON.py
  •	templates - It contains 3 html files.
      o	Index.html - responsible for rendering form for the metaphor meaning search and search metaphors by some properties. 
      o	MetaphorMeaningResults.html - responsible for rendering results of metaphor meaning search.
      o SearchMetaphorsResults - responsible for rendering results of search metaphor by some properties.
  •	App.py - Flask backend to search using Elasticsearch and handling http request from clients.
  •	IndexJSON.py - Used to convert csv file to indexed JSON file.
  •	Query.py - Contains all the queries used in my search application.
  •	requirements.txt - contains packages to install (can be installed by running a command)
  

Steps need to follow to run the project:
  => Install elastic search and run elastic search. Go to http://localhost/5000/ to ensure Elasticsearch is running.
  => Install packages in the requirements.txt using "pip install -r requirements.txt" command
  => Run IndexJSON.py to convert csv file to indexed JSON file.
  => Add our index (metaphors_db) to elastic search by using "curl -X POST "localhost:9200/metaphors_db/_bulk?pretty" -H "Content-Type: application/json" --data-            binary @CorpusJSON.json" cpmmand
  => Now you can run your project by running App.py and Go to http://127.0.0.1:5000 to load the website.
  => Now you can search metaphors.....
  
• For the first form to search meaning of metaphors, you can enter a metaphor and click search. 
      o First, it does an interval search with max_gap =5 without considering the order of the phrase in the metaphor property. 
            eg: "நட்பில்  உயிர்"
      
      o For some entered metaphor phrases, it's possible to interval search count is zero, In that case, then it'll do a match search for any word in the phrase in the         metaphor property. 
            eg: "உயிர் நட்பில் உணர்ச்சி"
    
      o If both interval serach and match search return zero reults, then it'll will do a multi-match with the properties "உருவக அணி","உருவக அணி                     வகை","மூலப்பொருள்","இலக்கு","விளக்கம்"
            eg: "பிரகாசமான"

      o If all the above search results zero count, then it'll show "NO match found" message.
            eg: "அம்மா"
  
 • For the second form to search metaphors by type of metaphor, source domain and target domain,
      o It used boolean-search query. So, it'll look filter by keyword when type of metaphor is selected and must match with both source domain and target domain               query.
            eg: type of metaphor - "அழகு"
                source domain - "பால்"
                target domain - "பெண்"
