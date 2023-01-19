import json
import codecs
import pandas as pd
import math

def GenerateJsonFile():
    outputJSON = codecs.open('Corpus/CorpusJSON.json', 'w', encoding='utf-8')
    datafile = pd.read_csv('Corpus/180543P_Corpus.csv')

    for i in range(datafile.shape[0]):
        dict_ = {}
        tamilHeadings = ["பாடலின் பெயர்","பாடல் வரிகள்","பாடலாசிரியர்","பாடகர்", "இசையமைப்பாளா்","திரைப்படம்","வெளியிடப்பட்ட ஆண்டு","உருவக அணி","உருவக அணி வகை","மூலப்பொருள்","இலக்கு","விளக்கம்"]
        englishHeadings = ["Title","Lyrics", "Lyricist", "Singer", "Composer", "Album", "Year", "Metaphor", "Type of Metaphor", "Source domain" ,"Target domain","Interpretation"]

        for j in range (len(englishHeadings)):
            tamilField = tamilHeadings[j]
            englishField =englishHeadings[j]

            if (not (isinstance(datafile[englishField][i], str)))  :
                if (math.isnan(datafile[englishField][i])):
                    datafile[englishField][i] = datafile[englishField][i-1]

            dict_[tamilField] = str(datafile[englishField][i]).replace("\n", " ").replace(".0","").replace("\t","")

        outputJSON.write('{ "index" : { "_index" : "metaphors_db", "_id" :' + str(i) + ' } }\n')
        json.dump(dict_, outputJSON, ensure_ascii=False)
        outputJSON.write('\n')

    print("-----Completed Writing Index JSON File------")

if __name__ == "__main__":
    GenerateJsonFile()