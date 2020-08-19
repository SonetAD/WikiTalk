# WikiTalk

WikiTalk is a voice search engine.I've created this for helping people quickly search and getting information in a concise way.

## Features of WikiTalk
1.It can search for current and old news bassed on user input.User can give any topic as input.
2.It is capable to search for any information on web and make a summary on that information.
3.It gives output in audio format so that user can eassily listen news & other search result.
4.While searching for news,user can specify how many news they want to listen on there given topic.

## Special feature of WikiTalk
It has been coded such way so that if somehow there will some issues(like network issue or api faillure issue),the software won't give any error.It will try again and again untill the issue will solve.When it can solve the issue,it will give the output.

## Documentation
Here is the documentation of WikiTalk

### Language
WikiTalk has been built on python 3.8.2

### Module &  Api Documentation

#### Wikipedia
In this project I've used a library called wikipedia to collect data from wikipedia.I've used two methods of this library-
*title
*summary

#### newsapi
In this project I've also used a python library called newsapi.This library is actually linked with the official news api-[News api](https://newsapi.org/)
I've used one class from this library called NewsapiClient.More specifically get_everything method of the class.

#### gtts module
In this project,I've used gtts modult to convert text to speech.

#### termcolor & pyfiglet
Thesre module have used to customize text while starting the app.

#### os module
This python built in module was used to delate temporary audio files.

#### playsound
This module has been to play audio file 


### Function Documentation

####raw_audio
This function takes string as input and give a audio file as output.

#### greatings
This function makes sure that raw_function will work perfectly.If any unexpected issue happens,this fintion will takes care of it.


## Developer and License info
This project has been created ubder the MIT license.

Developer:Sonet Adhikary.(space, space)
 E-mail:sonet.ad101@gmail.com


