# FE 595: Python for Finance
# Homework 4
# Abraham Jimenez-Berlanga
# CWID 10444147

# Required Libraries
#Request to use GET REST API
from requests import get
#Regular Expressions for cleaning the data
import re as re
#for NLP textblob and different package within TextBlob
from textblob import TextBlob, Word, Blobber
from textblob.classifiers import NaiveBayesClassifier
from textblob.taggers import NLTKTagger
#Pandas for operate with Dataframes
import pandas as pd


#the Urls variable contains all the documents extracted from the discussion board
Urls = (
'https://sit.instructure.com/files/4653201/download?download_frd=1&verifier=aWl6ZvPwzQ6wPLZ8H6yTh7O1lJ4Dq9ryBWReSW3M',
'https://sit.instructure.com/files/4653202/download?download_frd=1&verifier=RiSLiI3W1QZnGN7Oq4dF3mjM0zE3TcnARy1jnHUr',
'https://sit.instructure.com/files/4653446/download?download_frd=1&verifier=SucCkdEmzGqm1k4vUxHAXkLtDHKy2ljscYOBps1q',
'https://sit.instructure.com/files/4653447/download?download_frd=1&verifier=bvAHTS2yRlc0MYTZzDOhKOXMppjbLJGX25WZuyRi',
'https://sit.instructure.com/files/4655884/download?download_frd=1&verifier=82Rk8fyWKUWLPoLeKnEkBVGYszgz1zMuqr1Yvxmv',
'https://sit.instructure.com/files/4655885/download?download_frd=1&verifier=vxxJURlsHhTNxzlceA2hsikGIx9HPA4Dd5ftVC68',
'https://sit.instructure.com/files/4660438/download?download_frd=1&verifier=oiifnM4whzkOWcCVeaCNmPkbWReL0HrkORoYJYlL',
'https://sit.instructure.com/files/4660440/download?download_frd=1&verifier=tifQvxM3nkdoRARw2KvMvLgexX1uujqGV17sEVZB',
'https://sit.instructure.com/files/4666549/download?download_frd=1&verifier=UiLyIz7iutN7ez6GqmzCUnjc53x4QrcCavc4sNpR',
'https://sit.instructure.com/files/4666550/download?download_frd=1&verifier=io9Ijw6wJoZEhmJdjZMu16qzpjk14EZWrvK2QHq9',
'https://sit.instructure.com/files/4667718/download?download_frd=1&verifier=DU8ObbY9paHuz4wW8YGKgovfhtNmQaQvHkJyIRhZ',
'https://sit.instructure.com/files/4667719/download?download_frd=1&verifier=SHKFDKg3xC2y9ab9BqQlqcUbnjolQAvvKPrTurqN',
'https://sit.instructure.com/files/4668745/download?download_frd=1&verifier=5PC9mvQsJzgZx9kK7Z4LslhPzReB8k5XbUS47n0C',
'https://sit.instructure.com/files/4668746/download?download_frd=1&verifier=DpD1L3FZ55oGVyi76k1qEljBI4h9OkSX2atSJQtY',
'https://sit.instructure.com/files/4669155/download?download_frd=1&verifier=eBCwLZIxM7d6qmByB0KWeoi3DQ3Xc90vc5iySeQ1',
'https://sit.instructure.com/files/4669156/download?download_frd=1&verifier=oet2oKbLFOhLuh34rc5H9ttoPLi17x67vOAavPhV',
'https://sit.instructure.com/files/4670532/download?download_frd=1&verifier=cJYQR7ihFvUrw6zwLv8f8iJkuAHxnIXfBDGHrxJO',
'https://sit.instructure.com/files/4670535/download?download_frd=1&verifier=Lo0mnKX2sgdhXdbIYenSfDbAs7eTXdKYgWnNp3rC',
'https://sit.instructure.com/files/4671622/download?download_frd=1&verifier=mNLpQ95JU0YC6aeDmXxMNm4A4I8OPy5nyCnoq9n3',
'https://sit.instructure.com/files/4671626/download?download_frd=1&verifier=J3MZSWBzl03ALzxnSckLLyOh7dppbmxnUfHYqFvn',
'https://sit.instructure.com/files/4672315/download?download_frd=1&verifier=Xv1E95CsSraWVB5EKkzMfQnwMHDBbYOzgrFi0t9B',
'https://sit.instructure.com/files/4672317/download?download_frd=1&verifier=WssW7pSdz9Jxe52T2NEaTN20Sf1qOenVomOgkW86',
'https://sit.instructure.com/files/4672527/download?download_frd=1&verifier=ln55QWKRZczHm5Bc2TbGjqLtaG4mixVuLiGHWZYD',
'https://sit.instructure.com/files/4672530/download?download_frd=1&verifier=VU4NlKLDDuTOiOrrnLLf47IRyOOGx8rD7GGZb1Bo',
'https://sit.instructure.com/files/4674975/download?download_frd=1&verifier=ZheCIHwc0UFwXjmJqRG65P9ZcUzFt8fm9Dqpqrwa',
'https://sit.instructure.com/files/4674976/download?download_frd=1&verifier=GKyV60Y1wi3oG8M5vK9yV53iFGBmPabPpD1Uq9Jz',
'https://sit.instructure.com/files/4675673/download?download_frd=1&verifier=JpPv9gSadHwkDmG9unJuLJQ1RHNPq8RAKyPF3fuL',
'https://sit.instructure.com/files/4675674/download?download_frd=1&verifier=doxOFRXHcnrJ8EsiKN8LQRTtkIczq9m0Jr33OG91',
'https://sit.instructure.com/files/4676819/download?download_frd=1&verifier=0AuOeXPVjUGWvBxhFuibtLx1ttUt6wU5vSEb6dBJ',
'https://sit.instructure.com/files/4676820/download?download_frd=1&verifier=s2T86S3ZxBWPIqKmVk7B1AcOb1rjzOpE0rGr3sI0',
'https://sit.instructure.com/files/4677946/download?download_frd=1&verifier=16cJvD3YVWaJ1FhkJIY2tZo3pyTAA2q1Z7WoMNke',
'https://sit.instructure.com/files/4677947/download?download_frd=1&verifier=Ka04t7lioeP1kmwKe1NdYCBaSl1pYCq7VkfBK7t1',
'https://sit.instructure.com/files/4678026/download?download_frd=1&verifier=GolTN9BYLKNWPmSfNXyF6QNQixjITKFqLTkqq79d',
'https://sit.instructure.com/files/4678030/download?download_frd=1&verifier=I0ulyJuf2Zg879NouvYXtMpYATItfz0UkxVGyq8v',
'https://sit.instructure.com/files/4691540/download?download_frd=1&verifier=tQBKXLAbC6xQgXXOZSzp52aHZ8ygCRLAEEMTk5hm',
'https://sit.instructure.com/files/4691541/download?download_frd=1&verifier=e2cygvJb2uMgwuJv0Ryu3LOatuRHY9I4sxKAySsD')



# First function, to get the files from the web/local directory and merge all of them
def getandmerge(Input:"List containing the file names or urls",Input_type:"Variable indicating if URLs or TXT file"):
    # list that it will contain all the characters
    full_list = []
    # Address the correct option
    # URL if the files has to be retrieved from a sharepoint or cloud drive
    if Input_type=="URL":
    # looping over the URL list to get all the files
        for URL in Input:
            file = get(URL)
            text_i = file.text
            full_list.append(text_i)
    # TXT if the files are in a local directory
    elif Input_type=="TXT":
    # looping over the file list to read all the files
        for file_i in Input:
            with open(file_i,'r') as input_file:
                text_i =input_file.read()
                full_list.append(text_i)
    # Save the list into a file
    with open('mergedlist.txt', 'w') as merged_file:
        merged_file.write("\n".join(full_list))
    # the ouput file name is printed in case that the function is not been called to store the return in a variable
    print('You can find all the characters in the file mergedlist.txt')
    # File name is returned
    return('mergedlist.txt')
    
getandmerge(Urls,"URL")

def cleanandevaluate(File_name:"Name of the file with the characters"):
    # the Input for the function is the filename that contains the characters
    # to be cleaned and processed
    # We define the list that we'll use for creating our dataframe
    # the dataframe will contain the character, if it is male or female
    # and the sentiment score
    final_list = []
    gender_list = []
    sentiment_list = []
    # first, we open the file and we read line by line, to ensure that we clean and
    # standarize the format
    with open(File_name,'r') as merged_file:
        for position,line in enumerate(merged_file):
            # Some of the characters had an extra space at the beginning, so we remove it
            # if there were more than 1 space, we should have replaced this simple if
            # with a function that will identify how many spaces and remove them
            if line[0] == " ":
                line = line[1:len(line)]
            # as happen with the space, there are some sentences that they have added a '
            # at front, so we need to remove it
            if line[0] == "'":
                line = line[2:len(line)]
            # due to the different formating when merging, some characters have an extrac /n
            # at the end of the character
            if bool(re.search("\n",line)):
                line = line[0:len(line)-2]
            # the next scenario to clean is to remove " They figth crime" I have choosen this approach
            # because of the simplicity, if there were more than the scenarios below, I should have
            # created a function that will found the "they" in the string, and remove all the characters
            # after They. I choose this approach because of the simplicity
            if bool(re.search(" They fight crime!",line)):
                line = line[0:len(line)-len(" They fight crime!")]
            if bool(re.search(" They fight crime",line)):
                line = line[0:len(line)-len(" They fight crime")]
            if bool(re.search(" They fight crim",line)):
                line = line[0:len(line)-len(" They fight crim")]
            if line[0:1]=='[':
            # one of the files has been saved with the list format (with [] delimiting the list and separated by ,
            # to clear this, once the record is identified -begins with [-, we convert it to a List
                line = list(line)
                for i in range(0, len(line)):
                    if bool(re.search("She's", line[i])):
                        gender_list.append("female")
                        final_list.append(line[i])
                        tb_line = TextBlob(line[i])
                        sentiment_list.append(tb_line.sentiment.polarity)
                    elif bool(re.search("He's", line[i])):
                        gender_list.append("male")
                        final_list.append(line[i])
                        tb_line = TextBlob(line[i])
                        sentiment_list.append(tb_line.sentiment.polarity)
            # while reading the file, one of the issues found was that the 50 chactares were stored as one
            # string, so we identify this scenario and additionally, moving forward, I'm going to identify
            # if it is male/femail and calculate the score for the character.
            elif bool(re.search("She's", line)) and len(line)>200 and (line[0] == "S" or line[1]=="S"):
                iprev =0
                for i in range(0, len(line)):
                    if i < (len(line) -5):
                        # although I could use the Regular Expressions for splitting the 50 characters
                        # saved as 1 string, i feel more confortable identifying in which position does "she's" begin
                        # and delimiting with it
                        if line[i:i+5] =="She's":
                            gender_list.append("female")
                            final_list.append(line[iprev:i])
                            # During the following steps, i will be using TextBlob, creating the tb_line object and using it
                            # to score the polarity
                            tb_line = TextBlob(line)
                            sentiment_list.append(tb_line.sentiment.polarity)
                            iprev = i
            elif bool(re.search("He's", line)) and len(line) > 200:
                iprev =0
                for i in range(0, len(line)):
                    if i < (len(line) -4):
                        if line[i:i+4] =="He's":
                            gender_list.append("male")
                            final_list.append(line[iprev:i])
                            tb_line = TextBlob(line)
                            sentiment_list.append(tb_line.sentiment.polarity)                            
                            iprev =i
            elif bool(re.search("She's", line)):
                gender_list.append("female")
                final_list.append(line)
                tb_line = TextBlob(line)
                sentiment_list.append(tb_line.sentiment.polarity)                
            elif bool(re.search("He's",line)):
                gender_list.append("male")
                final_list.append(line)
                tb_line = TextBlob(line)
                sentiment_list.append(tb_line.sentiment.polarity)
            elif bool(re.search("she's", line)):
                gender_list.append("female")
                final_list.append(line)
                tb_line = TextBlob(line)
                sentiment_list.append(tb_line.sentiment.polarity)
            elif bool(re.search("he's", line)):
                gender_list.append("male")
                final_list.append(line)
                tb_line = TextBlob(line)
                sentiment_list.append(tb_line.sentiment.polarity)
            else:
                # some of the characters were saved after removing the she's/he's leaving the characters un identified
                # althought it could be possible in some of them to identify if it was a male/female the number of records
                # identify vs processed will be really low
                # Additionally, after reading, empty lines are created because of the break page indicator. this still will remove
                # them from the final list
                scenario = "third"
        data_sentence = {'Sentence':final_list,'Gender':gender_list,'Sentiment':sentiment_list}
        # creation of the dataframe that it will be used for sorting and filtering
        dataframe_sentences = pd.DataFrame(data_sentence)
        dataframe_sentences.sort_values(by='Sentiment',ascending=False)
        female_score = dataframe_sentences[(dataframe_sentences.Gender == "female")]
        female_score = female_score.sort_values(by='Sentiment',ascending=False)
        female_score.index = list(range(1, len(female_score) + 1))
        male_score = dataframe_sentences[(dataframe_sentences.Gender == "male")]
        male_score = male_score.sort_values(by='Sentiment',ascending=False)
        male_score.index = list(range(1, len(male_score) + 1))
        # Results:
        print("The worst female character is:",female_score.at[len(female_score),"Sentence"])
        print("The best female character is:",female_score.at[1,"Sentence"])
        print("The worst male character is:",male_score.at[len(male_score),"Sentence"])
        print("The best male character is:",male_score.at[1,"Sentence"])
        print(male_score.at[1,"Sentence"],female_score.at[1,"Sentence"],"They fight Crime!")
        print(male_score.at[len(male_score),"Sentence"],female_score.at[len(female_score),"Sentence"],"They fight Crime!")
        # Saving the list cleaned to be used in further analysis if needed
        with open('cleanedlist.txt', 'w') as cleaned_file:
            for line_final in final_list:
                cleaned_file.write(line_final)
                cleaned_file.write("\n")
        # the ouput file name is printed in case that the function is not been called to store the return in a variable
        print('The list of characters cleaned can be found in cleanedlist.txt')
        # Name of the file with the final list as returned result
        return('cleanedlist.txt')

cleanandevaluate('mergedlist.txt')

def topdescriptions(File_name:"Name of the file with the characters"):
    # Function to identify most common descriptors
    # As input we'll include the list of characters cleaned
    with open(File_name,'r') as whole_file:
        # Reading the whole file, as TexBlob will be applied to the whole
        whole_text = whole_file.read()
        tb_text = TextBlob(whole_text)
        adj_list =[]
        # Once the TextBlob is created, a loop is performed over the list of words
        # to identify the descriptors (PoS like JJ are adjetives)
        for word,pos in tb_text.tags:
            if pos[0:2] =="JJ":
                adj_list.append(word)
        # Creating a Dataframe indicating how many times the adjetive is on the list
        count_dataframe = pd.Series(adj_list).value_counts()
        # Printing top ten
        print("The 10 most common descriptions for characters:")
        print(count_dataframe.head(n=10))

topdescriptions('cleanedlist.txt')