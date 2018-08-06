# Game_ratings
## Intro

This project should end up having two main parts. The first part will analyze video games from a data set that I pulled off of Kaggle. This data will essentially all the user to look at graphs to see what was the best video game by year. The second part of the project, as it's planned now, is to web scrape metacritic so that a user will be able to see a games mean and the standard deviation of its score. 

As stated, the data may be found at Kaggle at the following link: https://www.kaggle.com/gregorut/videogamesales

The school shooting data came from the Washington Post's github repo and may be found at the following link: https://github.com/washingtonpost/data-school-shootings


# Getting started
### Installing

1. Clone the repo
2. Run [sudo] pip3 install or pip3 install flask
3. Run python3 main.py to run the application
6. Visit localhost:5000 to see the application

### Technology Stack

1. Flask-0.12
2. Python-3.4
3. Pandas-0.18.1
4. Numpy-1.11.0
5. MySQL-5.6.26

### Operation

Once the program is downloaded, simply run the program as you would any other python program.
Then follow the address, which your console/terminal tells you to go to see the
website.

# Issues / Other
The web scraping is working although there seems to be a slight issue with some of the value that are returned. I almost believe that this is an issue with Metacritic but I'll be looking into it more. It appears that some ratings on metacritic will change from time to time. I believe that I've fixed this issue. Metacritic placed user scores on their professional critics page so once I realized that I fixed this problem...I hope! 

The only 'somewhat' problem is that I'm using the csv data to help with autocomplete on the scraping.html page. This works for some games but Metacritic has to have their game typed a particular way. Thus Halo 5 cannot be Halo 5 or Halo 5: guardians but Halo 5 guardians. I'm still wondering if there is a way I could possibly fix this. 


# Preview

To see a video that talks about this project please go here: COMING SOON

Blog entry: COMING SOON
