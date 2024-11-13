# PS4PKG

> [!NOTE]
> PLEASE READ THE INSTALL SECTION!

https://github.com/carpetbomb/PS4PKG?tab=readme-ov-file#installation

A PS4 fPKG Game list using the psxhax site

All links included are from www.psxhax.com and I claim no ownership over any of their contents.



# Features
Below are the different features I have added.

### [Fastmode(ish)]
This makes the search a bit faster by just showing links with no game icon or description


### [Viewing Dumped Games and their Dump Dates]

- **The date format here is in `MM-DD-YY` as that is how it's recorded on psxhax's list.**

### [API]

- You have two options of www.alldebrid.com and www.real-debrid.com to download via direct links (1fichier, mega, mediafire)

- The third option is `none` which will open a webpage of the download link.

- You can find your alldebrid API key here: https://alldebrid.com/account/

- You can find your real-debrid API key here: https://real-debrid.com/apitoken


### [Backup + Recover]

- Backup and recover will make a backup prefixed with todays date to make it easier to know which backup is which.

- Recover then lets you select one of these backups and revert the games list back to how it was when the backup was taken.

- The backups are stored in the programs /bin/cache folder.

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

These are stored locally in the cache folder and are only passed to psxhax and nowhere else. `(you can confirm this by reading through the code)`

# UPDATING

- Whenever a new update is released here aditional info will be included in the release

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
