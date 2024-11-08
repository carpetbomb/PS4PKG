# PS4PKG

> [!NOTE]
> PLEASE READ THE INSTALL SECTION!

https://github.com/carpetbomb/PS4PKG?tab=readme-ov-file#installation

A PS4 fPKG Game list using the psxhax site

All links included are from www.psxhax.com and I claim no ownership over any of their contents.

**Some background:**

- I initially started work on this version on the 15th July and have slowly worked on it and added more features.

- The first version using psxhax was made on the 14th May and worked very differently and was way more complicated and time consuming to use

- The very first fPKG viewer I made uses dlps and was made when I was a lot less used to python

# Features
Below are the different features I have added.

### [Fastmode(ish)]
This makes the search a bit faster by just showing links with no game icon or description

### [Searching and Genre Selection]

![searchandgenre](https://github.com/user-attachments/assets/b283d22b-9d70-4a13-9682-3729d0a87c0a)



### [Viewing Dumped Games and their Dump Dates]

![ezgif-6-b27f861335](https://github.com/user-attachments/assets/a3dc1061-1c88-476c-ae51-4b44ddc47f50)

- **The date format here is in `MM-DD-YY` as that is how it's recorded on psxhax's list.**

### [API]

![api](https://github.com/user-attachments/assets/2a3499b7-9ed8-48f6-b80e-4df52bccaf95)

- You have two options of www.alldebrid.com and www.real-debrid.com to download via direct links (1fichier, mega, mediafire)

- The third option is `none` which will open a webpage of the download link.

- You can find your alldebrid API key here: https://alldebrid.com/account/

- You can find your real-debrid API key here: https://real-debrid.com/apitoken


### [Backup + Recover]

- Backup and recover will make a backup prefixed with todays date to make it easier to know which backup is which.

- Recover then lets you select one of these backups and revert the games list back to how it was when the backup was taken.

- The backups are stored in the programs /bin/cache folder.

![Screenshot_3](https://github.com/user-attachments/assets/0c12c2e0-be48-4e44-ad76-df24c7eb5081)

### [Viewing Game]

![Screenshot_7](https://github.com/user-attachments/assets/e5501515-da1b-47c9-8159-df063d29f299)


> [!NOTE]
> This layout is likely not final.

# Installation
>[!WARNING]
>YOU **MUST** HAVE A **VERIFIED** ACCOUNT ON PSXHAX TO USE THIS PROGRAM

- You'll need to download the release and unzip it also download `install.bat` and `requirements.txt`.

- First things first you're gonna need Python, you can get it here: https://www.python.org/downloads/

- Once you've got python installed open up `install.bat` and wait for it to finish installing / updating each component.

- To run the program click into the folder path, type `cmd` and then `python app.py`

- You will need an account on www.psxhax.com and the 'Member', 'Verified' and 'Contributor' badges like this:

![Screenshot_2](https://github.com/user-attachments/assets/2454e58d-1573-47b4-baa9-692f6cd6740d)

- there is a guide on how to get them on-site which can be found here:

- https://www.psxhax.com/threads/psxhax-member-verification-thread-for-receiving-blue-verified-badge.5824/#post-117077



After you're verified you will need to enter your psxhax cookie values. These can be found using [EditThisCookie](https://www.editthiscookie.com/). The input screen can then be found by going to `Settings -> PSXHAX Credentials`


![Screenshot_1](https://github.com/user-attachments/assets/a04c2b9e-dbc8-4387-b18c-5c1b7bd0f5ca)

These are stored locally in the cache folder and are only passed to psxhax and nowhere else. `(you can confirm this by reading through the code)`

# UPDATING

- Whenever a new update is released here aditional info will be included in the update log at the bottom of the README

# Bugs
Please make me aware of any bugs you come across!

Known Bugs:

- [ ] - mediafire links precursed with 1file links will show as deleted
- [ ] - mediafire resolver broken
- [x] - ~~Games with multiple links only seem to let you download the last one found. I recommend just opening the page for now.~~
- [ ] - I haven't actually coded the Theme section yet lol
- [ ] - The 'X' Close buttons do not work `[this is a problem with the gui so I cannot fix]`
- [x] - ~~Not entirely a bug but it is unable to scrape any base64 links from pages~~
- [x] - ~~xf_user does not display properly in the credentials screen, this however, does not impact anything else.~~
- [x] - ~~On the main page it says 'Download' instead of 'Get Content' Easy fix that I ahven't gotten round to yet.~~
# Changelog (DD-MM-YY)

[**01/10/24**]

-Added toggles for 1File and MediaFire resolving
-settings file layout has changed, please delete the old settings.json file from the bin folder.

[**30/09/24**]

- Fixed 1File resolving

[**25/09/24**]

- First proper release
- Added another content id list
- Added 'search' option to search for game content
- stored settings etc in single json file instead of multiple text files
- probably others but can't remember

[**02/09/24**]

- Fixed program opening multiple of the same page of content

[**21/08/24**]

- Fixed multilink posts not downloading / copying properly

- fixed base64 check failing crashing the program

[**13/08/24**]

- Released!


[**10/08/24**]

- Added Fastmode and resolver


[**08/08/24**]

- Added Game Info (player count, rating, release date)

- Added base64 link support

- Added API option `none` to just open the download page

[**07/08/24**] 

- Added game image and description + Fixed game images, descriptions not found crashing program 


[**06/08/24**] 

- Added whether or not game was tested in the link view window

- Added Base64 Decoder

[**05/08/24**]

- xf_user now displays properly

- Main page now says 'Get Content' instead of 'Download'
