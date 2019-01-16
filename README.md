# Mad Gab Generator

This generator was inspired by "Mad Gab", a fun, competitive card game played among friends, where the "guessers" must sound out a mad gab
phrase and figure out the original phrase through phonetic manipulation. For example, the mad gab phrase "Bone apple tea" translates
to "Bon appetit".

Whether you want to play a fun, unique round of Mad Gab with your friends, or create a set of key phrases to study with for school,
the Mad Gab Generator allows you to create customized mad gab phrases from any string of English words.

#How to set up database

1. Enter "core/db.conf" with your mysql database credentials
2. import database with this command:
    -"mysql -u username -p -h localhost boneapp < ./scripts/db_scripts/data.sql"

## How to run on a local host
Change into the "core" repository and type `flask run` in the terminal.
Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in an internet browser. If the "Mad Gab!" button doesn't work, you will either
need to clear your caches (?) or use a web browser in incognito.

Note: Check the requirements.txt file for packages you might need to install

## Terms of Use

Mad Gab Generator does not target our service to children under 18, and we do not permit those under 18 on our service.

## Senpais
**Dev Team: Cynthia Zhang, Felix Zhao, Jason Chen, Shirlyn Tang, Tony Sun**

Created at [SBHacks 2019](https://devpost.com/software/mad-gab-generator)
