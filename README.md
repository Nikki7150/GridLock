# GRIDLOCK

## Description
Yes, THis is just another TicTacToe game. But its slightly different. I made it first using only Python by follwing a tutorial I found on youtube (love the tutorial, by the way).
I basically taught me how to make my own intelligent computer algorithm such that the computer never loses and only ties or wins. Its such an intelligent strategy and such good logic. 
I tried it out and I loved it. So i thought "why not make it a website?"
And here it is, completely made into a website using Flask to connect the backend and the frontend code. 
I know i could have just made this in JavaScript and called it a day. I just would have had to covert the python to JS and thats pretty simple, but I wanted to challenge myself
and because I was in the mood to do some python and then make my life harder by converting it into a website. 
Anyways, I love it. I might add future updates to it to make it better and include the updates listed below. Hope you guys love this game!

## Future additions
- Sign-in
- Streaks
- Multiplayer server
- more modes

## Technologies used
- Python
- Flask
- HTML
- CSS
- JavaScript

## How to Run
- open this project on this link: https://gridlock-6v89.onrender.com/
- choose which mode you want to play in
- the user always starts the game
- click on one of the cells
- if multiplayer:
    - 'x' user play first
    - 'o' user play next on the same device
    - so on...
- if dumb and/or genius computer
    - user always play first
    - after you play, wait for the computer and then proceed
- keep playing until you or your competitor wins!
- Have Fun!!

## Set up and Run locally

1. Clone the repository:
```bash
git clone https://github.com/Nikki7150/GridLock.git
cd GridLock
```

2. Create a virtual environment (Optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies
```
pip install flask
pip install -r requirements.txt
```

4. Run the Flask app
```bash
python app.py
```

5. Open your browser and go to:
http://127.0.0.1:5000/
... or click on the link in your terminal

Now play to your hearts content!
