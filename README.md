[WIP] Lost Ark SDK
============
[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/pybot-lostark.svg)](https://github.com/jordanhoare/pybot-lostark/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/pybot-lostark.svg)](https://github.com/jordanhoare/pybot-lostark/issues) [![Current Version](https://img.shields.io/badge/version-0.5.0-green.svg)](https://github.com/jordanhoare/pybot-lostark) 

A computer-vision based python SDK for the AMMORPG game 'Lost Ark'. This repo will include scripts that automate player-like mechanics such as: walking, healing, attacking, item collection and skill training [Python, OpenCV].

![Alt Text](https://media.giphy.com/media/H542PcWInziUIs3jDA/giphy-downsized-large.gif)
```bash
####################################
>>> Lost Ark (9900746) window was located.
>>> Trade Skill Quickslot is already selected.
>>> No durability left on your tool. Attempting to repair tools.
>>> Closing repair window and restarting bot.
>>> Restarting bot... Idled for: 00:01:32
>>> Stopping script due to low energy.
>>> Script finished after: 00:12:41
####################################
```


</br>


## Module Completion Status
#### Player Automation 
  :hourglass: Fishing 
  - [ ] Mining
  - [ ] Herbalore
  - [ ] Woodcutting


## Feature Development
#### Continuation Checks
  :hourglass: Use pet menu to repair tool when low durability
  - [x] Change to lifeskill-quickslot if combat-quickslot is selected


  

#### HUD
  - [ ] Create overlay with loot count tracker

#### Movement
  - [ ] Identify player's coordinates
  - [ ] Waypoint selection

#### Hp/Mp Restoration
  - [ ] Retrieve player healthpoints
  - [ ] Restore healthpoints with potion

#### BattleList
  - [ ] Retrieve list of nearby monsters 
  - [ ] Use 'x' spellcast when monster is near center of the screen


</br>

## Disclaimer
- This project is for educational purposes.  Use at your own risk.

 
</br>

## Requirements 
- Python (3.8.2)
- Poetry (https://python-poetry.org/docs/)

</br>


## Running the app

```bash
# clone the repo, navigate to the project folder.  to start the venv, run:
poetry update
poetry shell
```

</br>

</br>

<p align="center">
    <a href="https://www.linkedin.com/in/jordan-hoare/">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="https://www.kaggle.com/jordanhoare">
        <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" />
    </a>&nbsp;&nbsp;
    <a href="mailto:jordanhoare0@gmail.com">
        <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
    </a>&nbsp;&nbsp;
</p>



