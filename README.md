# Shortener links with servise bit.ly

The program for working with the API of the link shortening service [https://bitly.com](https://bitly.com)

### Software environment and installation:

Python3 should already be installed.

### Program installation:

Download the code: [https://github.com/VAChess777/Lesson2_web_servises_API_Devman](https://github.com/VAChess777/Lesson2_web_servises_API_Devman), or clone the `git` repository to a local folder:
```
git clone https://github.com/VAChess777/Lesson2_web_servises_API_Devman.git
```

Register on the site [https://bitly.com](https://bitly.com) and get a personal token. Place the token in the `.env` file:
```
BIT_TOKEN=your token
```

### Installing dependencies:
 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```bach
pip install -r requirements.txt
```

### How to run the program:

Run the script with the command:
```bach
python main.py {url}
```

### How the program works:

The `main.py` program prompts the user for a link address. Parses the entered link. Depending on the entered link, 
transforms the link into a shortened `bit.ly` link or displays the number of clicks on the `bit.ly` link.

### Features works of the program:

The `main.py` program contains the functions:

* The `is_bitlink` function - checks the link via the `bit.ly` API. Is the incoming link a shortened `bit.ly` link?
* The `shorten_link` function transforms a link into a shortened `bit.ly` link.
* The `count_clicks` function counts the number of clicks on the shortened `bit.ly` link.

### Project Goals

This code was written for educational purposes as part of an online course for web developers at [dvmn.org](https://dvmn.org/).
