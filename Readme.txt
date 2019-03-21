# FE 595: Python for Finance
# Homework 4
# Abraham Jimenez-Berlanga
# CWID 10444147

########################################################################################################################
#the file Homework4 contains a variable and 3 functions
########################################################################################################################

########################################################################################################################
#Variable URLs
########################################################################################################################

the variable URL has been created to avoid the manual task of extracting the files from a Discussion board. 
The process to generate the variable is:
1. Go to the discussion portal using Chrome
2. doing left click select "inspect" (or Ctrl+Shift+I)
3. in the console, paste the following: urls = $$('a'); for (url in urls) console.log ( urls[url].href )
4. the console will show all the http links from the discussion board. Using left click, save the results in a TXT
5. open the TXT with excel and filter all the http containing "download" and clean it.
6. copy it and paste adding what it is needed to create a variable containing the http as a sttring list.

########################################################################################################################
#getandmerge
########################################################################################################################
#getandmerge(list_files,Input_type)
the function will go over the list and one by one will read the content of the files, as result it will return the name of the file with all the characters, additionally it will print the name.

The getandmerge function has two mandatory inputs:
- list_files: list with the local path or http addresses where the files with the characters can be find
- Input_type: type of list provided. Possible values: TXT if local path or URL for web

example:
- with URLs

>>> Urls = ('https://sit.instructure.com/files/4653201/download?download_frd=1&verifier=aWl6ZvPwzQ6wPLZ8H6yTh7O1lJ4Dq9ryBWReSW3M',
'https://sit.instructure.com/files/4653202/download?download_frd=1&verifier=RiSLiI3W1QZnGN7Oq4dF3mjM0zE3TcnARy1jnHUr',
'https://sit.instructure.com/files/4653446/download?download_frd=1&verifier=SucCkdEmzGqm1k4vUxHAXkLtDHKy2ljscYOBps1q')

>>> getandmerge(Urls,"URL")
You can find all the characters in the file mergedlist.txt


- with local path
Files =("male.txt","female.txt")

getandmerge(Files,"TXT")



########################################################################################################################
#cleanandevaluate
########################################################################################################################
#cleanandevaluate(File_name) 
This function will load the input file line by line and will perform the following cleaning steps:
- remove the following (shortening the line length) if any of the following is find:
	- Extra space at the beginning
	- "'" simbol at the beginning
	- "/n" supposing that it is at the end of the line
	- removing any of the following variations from the end of the line
		- " They fight crime!"
		- " They fight crime"
		- " They fight crim"
- if the characters are all presented in one line, it will split in one line per character
- lines without any male/female identifier (she/he) will be removed
- lines empty will be removed

At the same time that some of the cleaning is performed, the function will:
- evaluate if it is a male/female character
- score the polarity of the character (from -1 to 1) using TextBlob

As result, the function will return:
- the worst female character (in case that there are several with the same score, it will be providing the last record -first one starting from the end- based on the order)
- the best female character (in case that there are several with the same score, it will be providing the first one based on the order)
- the worst male character (in case that there are several with the same score, it will be providing the last record -first one starting from the end- based on the order)
- the best male character (in case that there are several with the same score, it will be providing the first one based on the order)
- I will give back the format back as found on the "they fight crime web" using first the best male and female and second the worst male and female
- finally, it will save the clean list in a local file and the name will be given as return

the function has only one mandatory input and it is the field name with the characters.



Example:

>>> cleanandevaluate('mergedlist.txt')
The worst female character is: She's a chain-smoking tomboy hooker with an evil twin sister
The best female character is: she's an orphaned antique-collecting fairy princess with an incredible destiny.
The worst male character is: He's a suicidal ninja hairdresser plagued by the memory of his family's brutal murde
The best male character is: He's a superhumanly strong misogynist gangster looking for a cure to the poison coursing through his veins.
He's a superhumanly strong misogynist gangster looking for a cure to the poison coursing through his veins. she's an orphaned antique-collecting fairy princess with an incredible destiny. They fight Crime!
He's a suicidal ninja hairdresser plagued by the memory of his family's brutal murde She's a chain-smoking tomboy hooker with an evil twin sister They fight Crime!
'cleanedlist.txt'



########################################################################################################################
#topdescriptions
########################################################################################################################
#topdescriptions(Filename)
This function will pick a file with characters and it will apply some NLP using TextBlob. The NLP will be used to identify all the descriptors (adjetives), identify how many times are being used in the text and provide the top 10.

The function has only one mandatory input and it is the field name with the characters.

Example:

>>> topdescriptions('cleanedlist.txt')
The 10 most common descriptions for characters:
wrong            147
secret            55
fast              37
last              36
American          35
hard-bitten       35
impetuous         34
dead              32
radical           30
sweet-toothed     30