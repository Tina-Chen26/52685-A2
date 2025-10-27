from earsketch import *

setTempo(100)

# Music
sounds = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
sounds [0] = AK_UNDOG_BASS_2
sounds [1] = AK_UNDOG_PERC_SHAKER_1
sounds [2] = AK_UNDOG_ACOUSTIC_GUITAR_3
sounds [3] = RD_RNB_808SOLODRUMS_5
sounds [4] = IRCA_BOMBA_SICA_CORTIJO_ELEC_PIANO
sounds [5] = COMMON_LOVE_DRUMBEAT_1
sounds [6] = AK_UNDOG_SFX_1
sounds [7] = AK_UNDOG_ACOUSTIC_GUITAR_2
sounds [8] = OS_OPENHAT06
sounds [9] = RD_ROCK_POPRHYTHM_DRUM_PART_2
sounds [10] =JWOLF_COTG_THEME_DRUMBEAT
sounds [11] = RD_EDM_SFX_RISER_AIR_1
sounds [12] = CIARA_SET_KICK_2
sounds [13] = Y01_CRASH_1
sounds [14] = DUBSTEP_DRUMLOOP_MAIN_001
sounds [15] = DUBSTEP_PAD_001
sounds [16] = AK_UNDOG_PERC_CYMB_1

# Section A
fitMedia(sounds[0],1,1,17)
fitMedia(sounds[1],2,2,17)
fitMedia(sounds[2],3,4,16)
fitMedia(sounds[3],4,8,16)
fitMedia(sounds[9],5,25,29)

# Section B
fitMedia(sounds[0],1,17,33)
fitMedia(sounds[3],2,17,33)
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
fitMedia(sounds[7],3,57,80)
fitMedia(sounds[14],4,61,80)
fitMedia(sounds[15],5,65,80)
fitMedia(sounds[16],1,73,75)
fitMedia(sounds[16],1,77,79)

# Fade in/Fade out
setEffect(0, VOLUME, GAIN, -5, 1, 1, 33)
setEffect(3, VOLUME, GAIN, -20, 8, 0, 17)
setEffect(7, VOLUME, GAIN, 1, 48, -10, 53)
setEffect(12, VOLUME, GAIN, 1, 39, -60, 53)
setEffect(9, VOLUME, GAIN, -30, 25, -5, 29)
setEffect(5, VOLUME, GAIN, -30, 19, -10, 33)
setEffect(10, VOLUME, GAIN, -10, 37, -30, 53)
setEffect(14, VOLUME, GAIN, -30, 61, -10, 80)


setEffect(0, DISTORTION, DISTO_GAIN, 5, 2)

#Fills
fillA="0---0---0-0-0-0-0"
makeBeat(AK_UNDOG_PERC_HATS_4, 3, 56, fillA )


finish()
