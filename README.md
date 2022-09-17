# PythonBehaviouralAnalysisGratton
#### This folder contains a series of lines of code used to analyse the behavioural data from a combined EEG study
#### It is not the only use, it essentially contains how to run an analysis from a specific set of csv files
#### Prior to using it, all CSV files have to be renamed to numbers
#### The CSV format we used had the following headers: Trial, Cue, Side, Flanker, Target, Congruency, Response, Reaction
#### Consecuently the code transforms those columns into the needed ones for the analysis within the loop.
___________________________________________________________________
#### The included graph lines of code are for Violin plots
___________________________________________________________________
#### The first section is for reaction time, the second for accuracy
#### Therefore the first section filters non accurate responses, after accounting and extracting those Gratton effect specific trials
#### the way of extracting Gratton trials is highly inneficient and there is probably better code for it
#### The code written identifies incongruent trials and creates a new column stating True if the trial is incongruent
#### Moves it one row ahead
#### And that way it identifies those trials that follow an Incongruent one.
