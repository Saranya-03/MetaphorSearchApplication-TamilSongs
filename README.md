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
1. Provide the meaning of the metaphors for users who wants to know the meaning or idea of the metaphor in Tamil song.
2. User can search based on type of metaphor or source domain the metaphor or target domain of the metaphor.

Framework: Apache Solr is used as the information retrieval library
