[WIP] Lost Ark SDK
============
[![GitHub Stars](https://img.shields.io/github/stars/jordanhoare/pybot-lostark.svg)](https://github.com/jordanhoare/pybot-lostark/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/jordanhoare/pybot-lostark.svg)](https://github.com/jordanhoare/pybot-lostark/issues) [![Current Version](https://img.shields.io/badge/version-0.5.0-green.svg)](https://github.com/jordanhoare/pybot-lostark) 

A computer-vision based python SDK for the AMMORPG 'Lost Ark' [Python, OpenCV].  The bot functions by generating a canvas image (window capture) to leech the outputted graphics and identify frames. The majority of modules/core scripts use these frames in bitmap finding algorithms (pattern matching with different color-spaces), then send mouse and keyboard actions using pyautogui.



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

<details>
  <summary>Module Completion Status</summary>

</br>

- Player Automation
    ```
    :hourglass: Fishing 
  - [ ] Mining
  - [ ] Herbalore
  - [ ] Woodcutting

    ```
- Initialise poetry:
    ```
    poetry build
    ```
- This project is being restructured currently, so for now activate the poet shell and run the draft auto_fishing script. pyautogui.click(x,y) can be reconfigured for screen position.
    ```
    poetry shell
    pybot-lostark/draft/modules/auto_fishing.py
    ```
</details>

</br>



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

<details>
  <summary>Requirements</summary>

</br>

- [Git](https://git-scm.com/) for command-line interface 
- [Pyenv](https://github.com/pyenv/pyenv) for Python version management tool
- [Poetry](https://python-poetry.org/docs/) for dependency management and packaging
</details>

</br>

<details>
  <summary>Reproduction on a local machine</summary>

</br>

- Clone the GitHub repository to an empty folder on your local machine:
    ```
    gh repo clone jordanhoare/pybot_lostark
    ```
- Initialise poetry:
    ```
    poetry build
    ```
- This project is being restructured currently, so for now activate the poet shell and run the draft auto_fishing script. pyautogui.click(x,y) can be reconfigured for screen position.
    ```
    poetry shell
    pybot-lostark/draft/modules/auto_fishing.py
    ```
</details>

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



