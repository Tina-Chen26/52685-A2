# Project name：
- PopLoop
- Live Demo：https://earsketch.gatech.edu/earsketch2/?sharing=i40iYxUfEAK0A0c8cDdjbA

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

## General Information
- This project is a short, section-based pop composition made in EarSketch with Python.
- The reason I make pop music is because I greatly admire pop singer Taylor Swift and I am also a fan of pop music.
- To gain a deeper understanding of the components of popular music.

## Technologies Used 
- EarSketch (web)
- Python (EarSketch API)
- EarSketch sound packs: AK_UNDOG, RD, IRCA, COMMON, JWOLF, Y01, DUBSTEP, CIARA, OS

## Features
- Sectioned flow: A (build), B (main groove + variations), C (lift/outro)
- Layered textures: bass, shakers, acoustic guitars, pads, FX risers
- Volume shaping: gentle fades and emphasis moments via setEffect
- Quick fills: one-line makeBeat pattern for pre-drop interest

## Screenshots
<img width="1510" height="798" alt="截屏2025-10-27 13 28 36" src="https://github.com/user-attachments/assets/16561806-762c-4588-b397-f1a9a4da3510" />

## Setup
*Requirements：
- Modern browser (Chrome/Edge/Firefox)
- Free account at https://earsketch.gatech.edu/

Install / Start：
- Open earsketch → Start Coding → Python
- Create a new account
- Click Run → Play
- Use Share to generate a live demo link

## Usage
- Ways to personalize 
- Tune the tempo in setTempo(100) for different vibes (90 = mellow, 120 = energetic).
- Swap any item in the sounds[...] list to change tone and groove.
- Move/resize sections by editing fitMedia(..., startBar, endBar).
- Increase or decrease the volume with setEffect(..., VOLUME, GAIN, ...).
- Write the fill pattern (fillA) to set up your favorite beat.

from earsketch import *

setTempo(100)

# Music
- sounds = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
- sounds [0] = AK_UNDOG_BASS_2
- sounds [1] = AK_UNDOG_PERC_SHAKER_1
- sounds [2] = AK_UNDOG_ACOUSTIC_GUITAR_3
- sounds [3] = RD_RNB_808SOLODRUMS_5
- sounds [4] = IRCA_BOMBA_SICA_CORTIJO_ELEC_PIANO
- sounds [5] = COMMON_LOVE_DRUMBEAT_1
- sounds [6] = AK_UNDOG_SFX_1
- sounds [7] = AK_UNDOG_ACOUSTIC_GUITAR_2
- sounds [8] = OS_OPENHAT06
- sounds [9] = RD_ROCK_POPRHYTHM_DRUM_PART_2
- sounds [10] =JWOLF_COTG_THEME_DRUMBEAT
- sounds [11] = RD_EDM_SFX_RISER_AIR_1
- sounds [12] = CIARA_SET_KICK_2
- sounds [13] = Y01_CRASH_1
- sounds [14] = DUBSTEP_DRUMLOOP_MAIN_001
- sounds [15] = DUBSTEP_PAD_001
- sounds [16] = AK_UNDOG_PERC_CYMB_1

# Section A
- fitMedia(sounds[0],1,1,17)
- fitMedia(sounds[1],2,2,17)
- fitMedia(sounds[2],3,4,16)
- fitMedia(sounds[3],4,8,16)
- fitMedia(sounds[9],5,25,29)

# Section B
- fitMedia(sounds[0],1,17,33)
- fitMedia(sounds[3],2,17,33)
fitMedia(sounds[5],3,19,33)
fitMedia(sounds[6],3,17.5,19)
fitMedia(sounds[7],4,21,55)
fitMedia(sounds[8],4,20,21.5)
fitMedia(sounds[10],3,37,55)
fitMedia(sounds[11],3,34,37)
fitMedia(sounds[12],5,39,55)
fitMedia(sounds[13],2,45,46)
fitMedia(sounds[13],2,49,50)
fitMedia(sounds[13],2,41,42)
fitMedia(sounds[13],2,53,54)

#Section C
- fitMedia(sounds[7],3,57,80)
- fitMedia(sounds[14],4,61,80)
- fitMedia(sounds[15],5,65,80)
- fitMedia(sounds[16],1,73,75)
- fitMedia(sounds[16],1,77,79)

# Fade in/Fade out
- setEffect(0, VOLUME, GAIN, -5, 1, 1, 33)
- setEffect(3, VOLUME, GAIN, -20, 8, 0, 17)
- setEffect(7, VOLUME, GAIN, 1, 48, -10, 53)
- setEffect(12, VOLUME, GAIN, 1, 39, -60, 53)
- setEffect(9, VOLUME, GAIN, -30, 25, -5, 29)
- setEffect(5, VOLUME, GAIN, -30, 19, -10, 33)
- setEffect(10, VOLUME, GAIN, -10, 37, -30, 53)
- setEffect(14, VOLUME, GAIN, -30, 61, -10, 80)


- setEffect(0, DISTORTION, DISTO_GAIN, 5, 2)

#Fills
- fillA="0---0---0-0-0-0-0"
- makeBeat(AK_UNDOG_PERC_HATS_4, 3, 56, fillA )


- finish()

*Export
- In EarSketch: Export → choose MP3/WAV.

## Project Status
-  In progress — refining transitions, testing alternate bridges/outs.

## Room for Improvement
-For sections B and C, improve the bass parts by reducing their volume.

*To Do
- Randomize fill patterns for subtle variation
- Offer multiple tempo presets (90 / 110 / 128 BPM)

## Acknowledgements
- Built with EarSketch and its amazing sound library
- Creative spark: I make pop music because I love Taylor Swift
- Thanks to open educational resources and classmates who gave feedback

## Contact
- Author: Kexin Chen
- Email: kexin.chen@student.uts.edu.au
- GitHub: @Tina-Chen26
- Project Link: https://earsketch.gatech.edu/earsketch2/ OR https://earsketch.gatech.edu/earsketch2/?sharing=i40iYxUfEAK0A0c8cDdjbA
