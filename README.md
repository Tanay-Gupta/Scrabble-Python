# Scrabble+
Four players play Scrabble+. For each hand
   of Scrabble+, every player enters a word in the
   scoreboard, getting a score that depends on the value
   of the letters composing the inserted word.

   Players create their own words by choosing them from a
   hand of 8 tiles, which are replaced once the word
   has been played until they are exhausted. The total number of
   tiles is 130.  The game ends when a player manages to
   finish all the tiles in their hand and there are no more tiles available
   to replace those just played: this happens because
   all the tiles are in the scoreboard and in the hand of
   the other players.
   
   At the end of the game, the player with the highest score wins,
   considering that for each tile that remains unplayed
   (that is, which remains in a player's hand when the game ends)
   3 points are subtracted.
   
   The scores are calculated as follows:
   
   ```
    1 point:  E, A, I, O, N, R, T, L, S, U
    2 points: D, G
    3 points: B, C, M, P
    4 points: F, H, V, W, Y
    5 points: K
    8 points: J, X
   10 points: Q , Z
   ```
   
   Design a function ex1(g1, g2, g3, g4, dim_hand, num_letters) that returns the
   scores of a game of Scrabble+ played among the four players, with
   the variant that the number of initial letters is "num_letters" instead of
   130, and that the number of letters available to each player is "dim_hand".
   g1, g2, g3 and g4 are lists of strings that contain the sequence of
   words inserted by player 1, player 2, player 3 and player 4,
   respectively, in every round.
   
   Ex.: dim_hand=5, num_letters=40
     g1 = ['seta','peeks','deter']
     g2 = ['reo','pumas']
     g3 = ['xx','xx']
     g4 = ['frs','bern']
     
     Notice that 5 tiles are given to each of the four players already
     at the beginning of the game, thus num_letters decreases accordingly.
     
   ```
   dim_hand - num_letters - word - score
5 5 5 5    20            seta    4  0  0  0
5 5 5 5    16            reo     4  3  0  0
5 5 5 5    13            xx      4  3 16  0
5 5 5 5    11            frs     4  3 16  6
5 5 5 5     8            peeks  15  3 16  6
5 5 5 5     3            pumas  15 12 16  6
5 3 5 5     0            xx     15 12 32  6
5 3 3 5     0            bern   15 12 32 12
5 3 3 1     0            deter  21 12 32 12
0 3 3 1     0                     GAME OVER
-------------------------------------------
Final score                     21  3 23  9
```

The TIMEOUT for each test is 0.5 seconds.

NOTICE: it’s forbidden to:
    - import other libraries
    - use global variables
    - open files
