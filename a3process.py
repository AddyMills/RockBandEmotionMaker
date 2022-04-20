from vgreaper import get_reaper_item, get_midi_data, write_midi_data, vg_log
from vgmidi import MIDINote, MIDIEvent, add_text_event, add_note, remove_notes, remove_events
from reaper_python import *
import os

tracks = ["emotion1", "emotion2", "emotion3", "emotion4"]

visemes_text = {'Squint': 48,
    'Blink': 49,
    'Brow_aggressive': 50,
    'Brow_down': 51,
    'Brow_dramatic': 52,
    'Brow_openmouthed': 53,
    'Brow_pouty': 54,
    'Brow_up': 55,
    'Wide_eyed': 56,
    '-': 57,
    'exp_banger_oohface_01': 58,
    'exp_banger_roar_01': 59,
    'exp_banger_slackjawed_01': 60,
    'exp_banger_teethgrit_01': 61,
    'exp_dramatic_happy_eyesclosed_01': 62,
    'exp_dramatic_happy_eyesopen_01': 63,
    'exp_dramatic_mouthopen_01': 64,
    'exp_dramatic_pouty_01': 65,
    'exp_rocker_bassface_aggressive_01': 66,
    'exp_rocker_bassface_cool_01': 67,
    'exp_rocker_shout_eyesclosed_01': 68,
    'exp_rocker_shout_eyesopen_01': 69,
    'exp_rocker_shout_quick_01': 70,
    'exp_rocker_slackjawed_01': 71,
    'exp_rocker_smile_intense_01': 72,
    'exp_rocker_smile_mellow_01': 73,
    'exp_rocker_soloface_01': 74,
    'exp_rocker_teethgrit_happy_01': 75,
    'exp_rocker_teethgrit_pained_01': 76,
    'exp_spazz_eyesclosed_01': 77,
    'exp_spazz_snear_intense_01': 78,
    'exp_spazz_snear_mellow_01': 79,
    'exp_spazz_tongueout_front_01': 80,
    'exp_spazz_tongueout_side_01': 81,
    '-': 82,
    'Bump_hi': 83,
    'Bump_lo': 84,
    'Cage_hi': 85,
    'Cage_lo': 86,
    'Church_hi': 87,
    'Church_lo': 88,
    'Earth_hi': 89,
    'Earth_lo': 90,
    'Eat_hi': 91,
    'Eat_lo': 92,
    'Fave_hi': 93,
    'Fave_lo': 94,
    'If_hi': 95,
    'If_lo': 96,
    'Neutral_hi': 97,
    'Neutral_lo': 98,
    'New_hi': 99,
    'New_lo': 100,
    'Oat_hi': 101,
    'Oat_lo': 102,
    'Ox_hi': 103,
    'Ox_lo': 104,
    'Roar_hi': 105,
    'Roar_lo': 106,
    'Size_hi': 107,
    'Size_lo': 108,
    'Squint': 109,
    'Though_hi': 110,
    'Though_lo': 111,
    'Told_hi': 112,
    'Told_lo': 113,
    'Wet_hi': 114,
    'Wet_lo': 115,

}

visemes_note = {48: 'Squint',
    49: 'Blink',
    50: 'Brow_aggressive',
    51: 'Brow_down',
    52: 'Brow_dramatic',
    53: 'Brow_openmouthed',
    54: 'Brow_pouty',
    55: 'Brow_up',
    56: 'Wide_eyed',
    57: '-',
    58: 'exp_banger_oohface_01',
    59: 'exp_banger_roar_01',
    60: 'exp_banger_slackjawed_01',
    61: 'exp_banger_teethgrit_01',
    62: 'exp_dramatic_happy_eyesclosed_01',
    63: 'exp_dramatic_happy_eyesopen_01',
    64: 'exp_dramatic_mouthopen_01',
    65: 'exp_dramatic_pouty_01',
    66: 'exp_rocker_bassface_aggressive_01',
    67: 'exp_rocker_bassface_cool_01',
    68: 'exp_rocker_shout_eyesclosed_01',
    69: 'exp_rocker_shout_eyesopen_01',
    70: 'exp_rocker_shout_quick_01',
    71: 'exp_rocker_slackjawed_01',
    72: 'exp_rocker_smile_intense_01',
    73: 'exp_rocker_smile_mellow_01',
    74: 'exp_rocker_soloface_01',
    75: 'exp_rocker_teethgrit_happy_01',
    76: 'exp_rocker_teethgrit_pained_01',
    77: 'exp_spazz_eyesclosed_01',
    78: 'exp_spazz_snear_intense_01',
    79: 'exp_spazz_snear_mellow_01',
    80: 'exp_spazz_tongueout_front_01',
    81: 'exp_spazz_tongueout_side_01',
    82: '-',
    83: 'Bump_hi',
    84: 'Bump_lo',
    85: 'Cage_hi',
    86: 'Cage_lo',
    87: 'Church_hi',
    88: 'Church_lo',
    89: 'Earth_hi',
    90: 'Earth_lo',
    91: 'Eat_hi',
    92: 'Eat_lo',
    93: 'Fave_hi',
    94: 'Fave_lo',
    95: 'If_hi',
    96: 'If_lo',
    97: 'Neutral_hi',
    98: 'Neutral_lo',
    99: 'New_hi',
    100: 'New_lo',
    101: 'Oat_hi',
    102: 'Oat_lo',
    103: 'Ox_hi',
    104: 'Ox_lo',
    105: 'Roar_hi',
    106: 'Roar_lo',
    107: 'Size_hi',
    108: 'Size_lo',
    109: 'Squint',
    110: 'Though_hi',
    111: 'Though_lo',
    112: 'Told_hi',
    113: 'Told_lo',
    114: 'Wet_hi',
    115: 'Wet_lo',
}

SINGLE_LEN = 480 // (32 // 4) # 32nd note

def weight_to_velocity_channel(weight):
    channel = weight // 128
    velocity = weight // (channel + 1)
    return velocity, channel

def a3_notes_to_text():
    for track in tracks:
        lipsync_item = get_reaper_item(track)
        if lipsync_item is None: 
            continue

        lipsync_data = get_midi_data(lipsync_item)

        valid_notes = []
        for note in lipsync_data.notes:
            if isinstance(note, MIDINote):
                if note.note in visemes_note and (note.status & 0xf0) == 0x90:
                    valid_notes.append(note)

        remove_events(lipsync_data)

        expressions = {}

        for note in valid_notes:
            text = visemes_note[note.note]
            channel = note.status & 0x0f
            velocity = note.velocity
            vis_weight = velocity + (128*channel)
            if velocity == 1:
                vis_weight -= 1
            if text not in expressions:
                expressions[text] = []
                expressions[text].append([note.apos, vis_weight])
            else:
                expressions[text].append([note.apos, vis_weight])

        interpolated = {}

        for x in expressions.keys():
            if x not in interpolated:
                interpolated[x] = []
            timeStrength = []
            for y in range(len(expressions[x])):
                try:
                    # RPR_ShowConsoleMsg(expressions[x][y])
                    timeDiff = (expressions[x][y+1][0] - expressions[x][y][0])/30 #Place an event every 30 ticks, i.e. 64th note
                    strengthDiff = (expressions[x][y+1][1] - expressions[x][y][1])/timeDiff
                    timeStrength.append([expressions[x][y][0], timeDiff, strengthDiff, expressions[x][y][1]])
                except Exception as e:
                    # RPR_ShowConsoleMsg(e)
                    pass
            
            for j, y in enumerate(timeStrength):
                for z in range(y[1]):
                    strength = int(round(y[3] + (y[2]*(z)),0))
                    if strength > 255:
                        strength = 255
                    if strength < 0:
                        strength = 0
                    text_final = "[%s %s %s]" % (x, strength, "hold")
                    add_text_event(lipsync_data, int(round(y[0]+(30*(z)),0)), text_final, "text")
        for x in expressions.keys():
            for y in expressions[x]:
                if y == expressions[x][-1]:
                    text_final = "[%s %s %s]" % (x, y[1], "hold")
                    add_text_event(lipsync_data, y[0], text_final, "text")

        write_midi_data(lipsync_item, lipsync_data)

def a3_text_to_notes():
    lipsync_item = get_reaper_item("audrey")
    if lipsync_item is None: 
        return

    lipsync_data = get_midi_data(lipsync_item)

    valid_events = []
    for note in lipsync_data.notes:
        if isinstance(note, MIDIEvent):
            raw_text = note.text.replace('[','').replace(' hold]','')
            tok = raw_text.split(' ')

            if len(tok) != 2:
                continue

            viseme = tok[0]
            try:
                weight = int(tok[1])
                if weight == 0:
                    weight +=1
            except ValueError:
                continue

            if viseme in visemes_text:
                valid_events.append([note, weight, viseme])

    remove_notes(lipsync_data)

    for data in valid_events:
        note = data[0]
        weight = data[1]
        viseme = data[2]

        pitch = visemes_text[viseme]
        velocity, channel = weight_to_velocity_channel(weight)
        add_note(lipsync_data, note.apos, 0x90 | channel, pitch, velocity)
        add_note(lipsync_data, note.apos + SINGLE_LEN, 0x80 | channel, pitch, 0)

    write_midi_data(lipsync_item, lipsync_data)

