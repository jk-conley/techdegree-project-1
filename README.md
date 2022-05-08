# Python Techdegree Project-1
This is my first project with Treehouse for the Python Techdegree.
It is a number guessing game that has a range of 1-10.
The player first is given the intro message and brief instructions.
They are prompted for their first guess. If the player enters anything
other than an int in the number range they will receive an error Message
and be asked to try again.

After entering their first guess, the guess is checked if it is correct, too low, or too high. Depending on where the guess falls, the player is informed of the outcome.

If it is too low, they are told the number is higher as a hint for their next guess.
If it is too high, they are told the number is lower as a hint for their next guess.
If they guess the correct number, the program will check their number of guesses against the high score. If their guess count is lower than the current high score, They will be informed they not only won the game but beat the high score.

After the winning announcements, the player is asked if they want to play again.
The program validates the user response to be either a yes or no. If they use anything else they are given an error message and are asked again to use a yes or no response.
If they select yes the program selects a new random number and verifies it is not the same as in the previous game.
If they select no, the player gets a goodbye message and the game ends.

************************************************************************
**Notes on my experience with the project.

This was a lot of fun and challenging at the same time. I think the biggest help in approaching this program was breaking it up into smaller pieces like in the examples Craig gave in various lessons (using tasks and pseudo code). Taking time to break it up and approaching it this way, made it less overbearing and easier to think through.

It was challenging though, to understand when I should break something off from the main start_game function and create its own separate function to try and clean up the code. I tried to catch myself with the DRY principle mentioned. If I found I was going to repeat the code, I tried turning it into a function. I'm sure there are more areas in my code where I could have done this and look forward to keep improving on having more presentable and easier to follow code.

Another challenge I came across was with the validation section. I ended up hitting a weird bug that made my validation go into an infinite loop with the exception statement. Initially I tried print statements to see what was happening, but couldn't catch anything from there. So I opened up a workshop and tried soloing out my while loop with try and except. I used a very simple setup and it worked in the workshop without creating an infinite loop.

So, I decided to try a simpler step by step approach to adding it into my program. I broke the try and except statement I initially made up into pieces. Separating the range check from the value type error check.

First I put a basic try and except statement in the first spot I needed it(was going to be repeated so I wanted to eventually turn it into a function). It worked, with no while loop present. Then I added the while loop. It worked without going into an infinite loop (Yay)! So I took that bit of code and put it into a function and used it in all the instances to test if it worked, and it did work. Next was adding the range check. Since I didn't have success having them all together, I decided to follow the steps as before.
I put the range check into one spot of the code to initially test it. When it was working and catching any number out of the range, I put it into it's own function and added it to the validation function. It worked and I was able to check for all the errors corresponding to what was asked!

I learned that even with a task that has already been broken up, it might be a good idea to even break that up further, if needed.

This was a great first project and I look forward to what is next! So far I'm interested in using python towards data engineering, data science, or quality software engineering. I currently work in quality assurance for my current job in a factory, so I'm curious to see what opportunities this will open up :).
