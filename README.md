# PS4PKG
**[!NOT CURRENTLY RELEASED!]**

A PS4 fPKG Game list using the psxhax site

All links included are from www.psxhax.com and I claim no ownership over any of their contents.

Some background:
I initially started work on this version on the 15th July and have slowly worked on it and added more features.
The first version using psxhax was made on the 14th May and worked very differently and was way more complicated and time consuming to use

The very first fPKG viewer I made uses dlps and was made when I was a lot less used to python

# Features
Below are the different features I have added.

### [Searching and Genre Selection]

![searchandgenre](https://github.com/user-attachments/assets/b283d22b-9d70-4a13-9682-3729d0a87c0a)



### [Viewing Dumped Games and their Dump Dates]

![ezgif-6-b27f861335](https://github.com/user-attachments/assets/a3dc1061-1c88-476c-ae51-4b44ddc47f50)

The date format here is in MM-DD-YY as that is how it's recorded on psxhax's list.

### [API]

![Screenshot_4](https://github.com/user-attachments/assets/a6b641a3-96fc-4ec0-bd25-c6d71946f9d9)

You have two options of www.alldebrid.com and www.real-debrid.com to download via direct links (1fichier, mega, mediafire)

The API Key is stored in plaintext in the /bin folder

In the future it will be stored encrypted but this is low priority at the moment.


### [Backup + Recover]

Backup and recover will make a backup prefixed with todays date to make it easier to know which backup is which.

Recover then lets you select one of these backups and revert the games list back to how it was when the backup was taken.

The backups are stored in the programs /bin/cache folder.

![Screenshot_3](https://github.com/user-attachments/assets/0c12c2e0-be48-4e44-ad76-df24c7eb5081)


# Installation
First things first you're gonna need Python, you can get it here: https://www.python.org/downloads/

Once you've got python installed open up `install.bat` and wait for it to finish installing / updating each component.

To run the program click into the folder path, type `cmd` and then `python app.py`

You will need an account on www.psxhax.com and the 'Member', 'Verified' and 'Contributor' badges like this:

![Screenshot_2](https://github.com/user-attachments/assets/2454e58d-1573-47b4-baa9-692f6cd6740d)

there is a guide on how to get them on-site which can be found here:

https://www.psxhax.com/threads/psxhax-member-verification-thread-for-receiving-blue-verified-badge.5824/#post-117077



You will need to enter your psxhax cookie values. These can be found using [EditThisCookie](https://www.editthiscookie.com/). The input screen can then be found by going to Settings -> PSXHAX Credentials

(These are only needed if you are going to use the download button, which scrapes the links from the page. Using Open Page is not affected by them)

![Screenshot_1](https://github.com/user-attachments/assets/a04c2b9e-dbc8-4387-b18c-5c1b7bd0f5ca)

These are stored locally in the cache folder in plaintext and are only passed to psxhax and nowhere else. (you can confirm this by reading through the code)

while I plan to add some encryption on these cookies it is not a priority at the moment as nothing in the file indicates what site they are for
# Bugs
Please make me aware of any bugs you come across!

Known Bugs:
- The 'X' Close buttons do not work [this is a problem with the gui so I cannot fix]

# Changelog
