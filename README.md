# NCAAB-SCORE-PREDICTOR

## Model Version:
This is currently V0, operating as the baseline for future versions to be tested against, the model is currently being backtested to ensure accuracy and viability.

### Methodology: 

The model operates on the simple assumption that a game is determined by two things: pace and efficiency, pace is calculated by the predicted possessions in a game and efficiency is calculated by the predicted points per possession, each part is calculated by their own models.

Possessions is calculated using:
Field Goals Taken/Allowed
Fouls Drawn/Committed
Turnovers and Turnovers forced
Off and Def rebounds and Rebounds allowed

a Monte Carlo Simulation, using: mean, variance, and standard deviation to produce a range of possible results for each variable. Right now the model simulates 10,000 possible outcomes for each variable before they are weighed by their opponents own variables creating 10,000 predicted values for Field Goals Attempted, Free Throws, Offensive Rebounds, and Turnovers, these are then fed into the possession calculation: FGA + (0.475 * FTA) - ORB + TOV to create 10,000 possible games.

Efficiency is calculated using the player efficiency model, in which team performance is adjusted based on opponent performance, and then strength of schedule averages, this is to ensure that a team scoring 15% more efficiently on a bad opponent is not given the same rating as a team scoring 15% more efficiently on a good opponent, the rating works so that PPP (points per possession) and PAPP(points allowed per possession) are inverse, a good PPP will be higher than 1.00, which is the average, and a good PAPP will be lower than 1, which is still the average.

### Current Limitations
Noted shortcoming of the model are as follows:

-All coefficients and variable relations are currently unoptimized

-No current adjustments for Home and away games 

-No player impact or player injury consideration

-Expected efficiency is currently based on a single season average, not a range of possible values.

### Future Versions
V1 is expected to be finished on Oct 21. It will include the following:

-Proper coefficients and variable relations (determined through xgboost)

-Home/Away/Neutral court adjustments
