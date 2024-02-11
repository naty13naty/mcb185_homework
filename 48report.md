### This report shows summary of the result of programs 45-47.
### By Natnael Tsegai

# Summary of 45dndstats.py
This program shows the average stat value for the following four different rules. 
   1. the first rule is rolling 3 six sided dice. I wrote the code in one lope, and I used
      *random.randit(1, 6)* to generate random rolls between *1 and 6*, for *10000 
      rolls/trials*. I obtained the final result by dividing the sum of the rolls by the
      total number of trials.
   2. The second rule is rolling 3 six sided dice, but re-rolling any 1s. I used the same
      procedure with the only exception being re-rolling the dice if the roll is a *1*.
   3. The third rule is rolling a pair of six-sided 3 times and taking the maximum each 
      time. I used the same procedure as the first two, and i also included a conditional
      statement that compares the result of the rolls from each dice, and to take the
      maximum with each roll.
   4. The last rule is to roll 4 six-sided dice, and to drop the lowest die roll. Similar 
      procedure was employed as the previous rules, but i also included conditional 
      statement that drops the lowest die roll and add the other 3 rolls.
      
the results i got for each rule are as follows:
      
      |   Rule    |   Result     |
      | ----------| -------------|
      |   3D6     |    10.5009   |
      |   3D6r1   |    11.7386   |
      |   3D6x2   |    13.4170   |
      |   4D6D1   |    12.2025   |
      
      
# Summary of 46savingthrows.py      
This program simulates saving throws against DCs of 5, 10, and 15, and shows the probability
of success *normally*, with *advantage*, and with *disadvantage*. The results of this 
program are summarized in this table below:
   
   |   DC  |    Adv    |
   | ------| ----------|
   |   5   |    0.954  |
   |   10  |    0.798  |
   |   15  |    0.489  |

   |  DC   |   Disadv  |
   | ------| ----------|
   |   5   |    0.642  |
   |   10  |    0.293  |
   |   15  |    0.088  |
   
   |  DC   |    Normal |
   | ------| ----------|
   |   5   |    0.802  |
   |   10  |    0.556  |
   |   15  |    0.308  |
   
   
# Summary of 47deathsaves.py

This program simulates the probability someone dies, stabilizes, or revives based one the 
result of *d20* die. The rules are as follows:
  - if the number of the roll is less than 10, you record a *failure*, and *3 failures*
    lead to *death*.
  - if the number of the roll is greater than 10 but less than 20, you record *success*
    and *3 successes* lead to *stabilize*.
  - if you're lucky and roll a 20, you gain i health, and you *revive*.
The results I got at the end are summarized below:

   |    die        |   0.4    |
   |    stabilize  |   0.417  |
   |    revive     |   0.183  |

   