def assign_label_group(original_label):
    # Define a mapping of original labels to broader categories
    label_mapping = {
        'verse': 'Verse',
        'chorus': 'Chorus',
        'silence': 'Silence',
        'intro': 'Intro',
        'outro': 'Outro',
        'end': 'End',
        'interlude': 'Interlude',
        'transition': 'Transition',
        'bridge': 'Bridge',
        'head': 'Head',
        'solo': 'Solo',
        'instrumental': 'Instrumental',
        'pre-chorus': 'Pre-Chorus',
        'pre-verse': 'Pre-Verse',
        'post-chorus': 'Post-Chorus',
        'coda': 'Coda',
        'main_theme': 'Theme',
        'secondary_theme': 'Theme',
        'theme': 'Theme',
        'fade-out': 'Fade-out',
        'no_function': 'Other',
    }
    
    # Convert the original label to lowercase and check the mapping
    # If not found, default to 'Other'. Capitalize the first letter of the result.
    return label_mapping.get(original_label.lower(), 'Other').capitalize()
