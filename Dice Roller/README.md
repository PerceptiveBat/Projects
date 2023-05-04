# **ASoIaF Web Dice Roller**
#### Video Demo:  https://youtu.be/cr1uIdAGtBs
#### Description: *A web based dice roller fo the ASoIaF miniatures game**

The concept of this project is a web based dice roller that uses 6 sided dice. The user will be able to input two values, representing number of dice and target number, create random dice results and reroll any and all of those results, if he so wishes.

The project was made using HTML5, CSS and Javascript. Having used python before, I decided to use these programming languages mainly for practice. I decided to place the CSS code inside the html file, since the code was rather short. The aesthetic of the dice roller was loosely based on CMON's ASoIaF website. The dice roller is made to fit into any device screen the user is using, that being desktop, laptop, smartphone or tablet.

The dice roller gives the user the ability to choose between rolling attack or defense dice in the form of a drop down menu, and then choose the number of dice to roll and the target number, both in the form of counters. Finally, there are two buttons, ROLL DICE and REROLL DICE, which call the rollDice() and rerollSelectedDice() functions respectively.

The implemented functions, written in Javascript, are the following:

rollDice(): The function takes the input of a number from one to twelve made by the user using the form explained above and creates an equal amount of random numbers from one to six. Then it compares each of those numbers to a target number, given once again by the user in the same fashion, and for each randomly generated number that meets or beats the target number, the successes total is increased by one. The total number of successes is displayed for the user to see.

function markReroll(die): Allows the user to click on dice roll results to select them for rerolls. It adds or removes the toggle class .reroll from the die roll to enable the rerollSelectedDice() function to know which dice results to reroll.

rerollSelectedDice(): It rerolls dice results that where selected by the user and compares them to the target number once more. Then, the updateSuccesses() function is called.

updateSuccesses(): Updated the number of seccesses after rerolls have taken place. Called after the rollDice() and rerollSelectedDice() functions. Calculated the new number of successes by adding the number of successes of the rerolled dice.

The code has two unimplemented functions: rerollSuccesses() and rerollFailures(), both integral parts of the miniatures game. The purpose they will serve is still achievable manually, but their future implemantation will make it automatic.