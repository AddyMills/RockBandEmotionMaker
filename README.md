# Rock Band Emotion Maker
A script to convert MIDI notes to emotions readable by Rock Band 2/3/4. Allows addition of emotions not available otherwise.

Usage: Add RBEM as a script to Reaper. This script will read tracks named "emotion\#" where \# is a number from 1-4.

Place notes on the notes outlined below with a velocity of 0-127 and a channel of 1 or 2 allowing you to go from 0-255 in strength. Channel 1 will go from strength 0-127 (skipping 1), and channel 2 will go from strength 128-255 (skipping 129). Running the script will then place text events in the track. Copy this to a track named "LIPSYNC\#" where \# is 1-4 and let Onyx create a milo file to be used in-game.

Use in combination with lipsync2midi (which will create your LIPSYNC tracks for you) in order to add emotions quicker to your own songs: https://github.com/AddyMills/RB-Tools

The script will create events in between two other events. That is, if you want your character to slowly transition into a viseme, all you need to do is place two events, your first event, and your last event, and the script will fill in the rest:

https://user-images.githubusercontent.com/74471839/158006726-b692466e-a21f-40c1-9df1-ff62150bdf5d.mp4

Please see the following video for a demonstration of the different emotions available:

https://www.youtube.com/watch?v=D5VSSrYH5c4

The MIDI notes that correspond to different notes are as follows:

* 49: 'Blink',
* 50: 'Brow_aggressive',
* 51: 'Brow_down',
* 52: 'Brow_dramatic',
* 53: 'Brow_openmouthed',
* 54: 'Brow_pouty',
* 55: 'Brow_up',
* 56: 'Wide_eyed',

* 58: 'exp_banger_oohface_01',
* 59: 'exp_banger_roar_01',
* 60: 'exp_banger_slackjawed_01',
* 61: 'exp_banger_teethgrit_01',
* 62: 'exp_dramatic_happy_eyesclosed_01',
* 63: 'exp_dramatic_happy_eyesopen_01',
* 64: 'exp_dramatic_mouthopen_01',
* 65: 'exp_dramatic_pouty_01',
* 66: 'exp_rocker_bassface_aggressive_01',
* 67: 'exp_rocker_bassface_cool_01',
* 68: 'exp_rocker_shout_eyesclosed_01',
* 69: 'exp_rocker_shout_eyesopen_01',
* 70: 'exp_rocker_shout_quick_01',
* 71: 'exp_rocker_slackjawed_01',
* 72: 'exp_rocker_smile_intense_01',
* 73: 'exp_rocker_smile_mellow_01',
* 74: 'exp_rocker_soloface_01',
* 75: 'exp_rocker_teethgrit_happy_01',
* 76: 'exp_rocker_teethgrit_pained_01',
* 77: 'exp_spazz_eyesclosed_01',
* 78: 'exp_spazz_snear_intense_01',
* 79: 'exp_spazz_snear_mellow_01',
* 80: 'exp_spazz_tongueout_front_01',
* 81: 'exp_spazz_tongueout_side_01',

* 83: 'Bump_hi',
* 84: 'Bump_lo',
* 85: 'Cage_hi',
* 86: 'Cage_lo',
* 87: 'Church_hi',
* 88: 'Church_lo',
* 89: 'Earth_hi',
* 90: 'Earth_lo',
* 91: 'Eat_hi',
* 92: 'Eat_lo',
* 93: 'Fave_hi',
* 94: 'Fave_lo',
* 95: 'If_hi',
* 96: 'If_lo',
* 97: 'Neutral_hi',
* 98: 'Neutral_lo',
* 99: 'New_hi',
* 100: 'New_lo',
* 101: 'Oat_hi',
* 102: 'Oat_lo',
* 103: 'Ox_hi',
* 104: 'Ox_lo',
* 105: 'Roar_hi',
* 106: 'Roar_lo',
* 107: 'Size_hi',
* 108: 'Size_lo',
* 109: 'Squint',
* 110: 'Though_hi',
* 111: 'Though_lo',
* 112: 'Told_hi',
* 113: 'Told_lo',
* 114: 'Wet_hi',
* 115: 'Wet_lo',

## Special Thanks
Kueller - The code in this script was mainly written by kueller (whose repo this one was forked from). I rewrote the notes to text fuction with my own code for this project.

Canon/C0Assassin - For providing me with an edited version of Kueller's script that started the work on adding emotions to RB2/3/4
