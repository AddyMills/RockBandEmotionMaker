from vgreaper import get_reaper_item, get_midi_data, write_midi_data, vg_log
from vgmidi import MIDINote, MIDIEvent, add_text_event, add_note, remove_notes, remove_events
import os

visemes_text = {   'Base': 50,
    'head_rot_neg_x': 51,
    'head_rot_neg_y': 52,
    'head_rot_neg_z': 53,
    'head_rot_pos_x': 54,
    'head_rot_pos_y': 55,
    'head_rot_pos_z': 56,
    'jaw_fwd': 57,
    'jaw_left': 58,
    'jaw_open': 59,
    'jaw_right': 60,
    'l_brow_dn': 61,
    'l_brow_up': 62,
    'l_cheek_puff': 63,
    'l_frown': 64,
    'l_lids': 65,
    'l_lip_pull': 66,
    'l_lolid_up': 67,
    'l_lolip_dn': 68,
    'l_lolip_roll': 69,
    'l_lolip_up': 70,
    'l_mouth_pucker': 71,
    'l_open_pucker': 72,
    'l_smile_closed': 73,
    'l_smile_open': 74,
    'l_sneer_narrow': 75,
    'l_squint': 76,
    'l_uplip_roll': 77,
    'l_uplip_up': 78,
    'm_brow_dn': 79,
    'm_brow_up': 80,
    'm_lips_close': 81,
    'r_brow_dn': 82,
    'r_brow_up': 83,
    'r_cheek_puff': 84,
    'r_frown': 85,
    'r_lids': 86,
    'r_lip_pull': 87,
    'r_lolid_up': 88,
    'r_lolip_dn': 89,
    'r_lolip_roll': 90,
    'r_lolip_up': 91,
    'r_mouth_pucker': 92,
    'r_open_pucker': 93,
    'r_smile_closed': 94,
    'r_smile_open': 95,
    'r_sneer_narrow': 96,
    'r_squint': 97,
    'r_uplip_roll': 98,
    'r_uplip_up': 99,
    'smile_01': 100,
    'smile_02': 101,
    'tongue_dn': 102,
    'tongue_left': 103,
    'tongue_out': 104,
    'tongue_right': 105,
    'tongue_roll': 106,
    'tongue_up': 107
}

visemes_note = {   50: 'Base',
    51: 'head_rot_neg_x',
    52: 'head_rot_neg_y',
    53: 'head_rot_neg_z',
    54: 'head_rot_pos_x',
    55: 'head_rot_pos_y',
    56: 'head_rot_pos_z',
    57: 'jaw_fwd',
    58: 'jaw_left',
    59: 'jaw_open',
    60: 'jaw_right',
    61: 'l_brow_dn',
    62: 'l_brow_up',
    63: 'l_cheek_puff',
    64: 'l_frown',
    65: 'l_lids',
    66: 'l_lip_pull',
    67: 'l_lolid_up',
    68: 'l_lolip_dn',
    69: 'l_lolip_roll',
    70: 'l_lolip_up',
    71: 'l_mouth_pucker',
    72: 'l_open_pucker',
    73: 'l_smile_closed',
    74: 'l_smile_open',
    75: 'l_sneer_narrow',
    76: 'l_squint',
    77: 'l_uplip_roll',
    78: 'l_uplip_up',
    79: 'm_brow_dn',
    80: 'm_brow_up',
    81: 'm_lips_close',
    82: 'r_brow_dn',
    83: 'r_brow_up',
    84: 'r_cheek_puff',
    85: 'r_frown',
    86: 'r_lids',
    87: 'r_lip_pull',
    88: 'r_lolid_up',
    89: 'r_lolip_dn',
    90: 'r_lolip_roll',
    91: 'r_lolip_up',
    92: 'r_mouth_pucker',
    93: 'r_open_pucker',
    94: 'r_smile_closed',
    95: 'r_smile_open',
    96: 'r_sneer_narrow',
    97: 'r_squint',
    98: 'r_uplip_roll',
    99: 'r_uplip_up',
    100: 'smile_01',
    101: 'smile_02',
    102: 'tongue_dn',
    103: 'tongue_left',
    104: 'tongue_out',
    105: 'tongue_right',
    106: 'tongue_roll',
    107: 'tongue_up'
}

SINGLE_LEN = 480 // (32 // 4) # 32nd note

def weight_to_velocity_channel(weight):
    channel = weight // 128
    velocity = weight // (channel + 1)
    return velocity, channel

def a3_notes_to_text(track):
    lipsync_item = get_reaper_item(track)
    if lipsync_item is None: 
        return

    lipsync_data = get_midi_data(lipsync_item)

    valid_notes = []
    for note in lipsync_data.notes:
        if isinstance(note, MIDINote):
            if note.note in visemes_note and (note.status & 0xf0) == 0x90:
                valid_notes.append(note)

    remove_events(lipsync_data)

    for note in valid_notes:
        text = visemes_note[note.note]
        channel = note.status & 0x0f
        velocity = note.velocity
        vis_weight = velocity * (channel + 1)

        text_final = "[%s %s]" % (text, vis_weight)

        add_text_event(lipsync_data, note.apos, text_final, "text")

    write_midi_data(lipsync_item, lipsync_data)

def a3_text_to_notes(track):
    lipsync_item = get_reaper_item(track)
    if lipsync_item is None: 
        return

    lipsync_data = get_midi_data(lipsync_item)

    valid_events = []
    for note in lipsync_data.notes:
        if isinstance(note, MIDIEvent):
            raw_text = note.text.replace('[','').replace(']','')
            tok = raw_text.split(' ')

            if len(tok) != 2:
                continue

            viseme = tok[0]
            try:
                weight = int(tok[1])
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

