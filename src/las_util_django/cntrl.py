"""
File-Name: [app]/cntrl.py
File-Desc: parsing functions for las_util_django
App-Name: las_util_django
Project-Name: Las-Util-Django
Copyright: Copyright (c) 2019, DC Slagel
License-Identifier: BSD-3-Clause
"""
import io
from datetime import datetime
from .models import VersionInfo


def parse(las_file):
    """
    Parse the a las file

    Notes: currently this only parses the version section
    """
    io_stream = io.TextIOWrapper(las_file)
    
    entry_date = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    entry_filename = 'las_file-' + entry_date + '.las'

    entry = VersionInfo()
    entry.filename = entry_filename
    section = ''

    for line in io_stream.readlines():

        line = line.rstrip()

        if not line:
            continue

        # Lines beginning with '~' denote the next section header
        if line[0] == '~':
            section = line
            continue
        
        """
        Version section delimiters
        1. the first dot: '.'
        2. the first space after the dot: ' '
        3. the last colon that is not part of a time string
        """
        entry.name, remaining_string = line.split('.', maxsplit=1)
        entry.unit, remaining_string = remaining_string.split(' ', maxsplit=1)
        entry.value, entry.note = remaining_string.split(': ', maxsplit=1)

        entry.name = entry.name.strip()
        entry.value = entry.value.strip()
        entry.note = entry.note.strip()
        entry.section = section

        # Write entry to db
        entry.save()

        # Initialize next entry
        entry = VersionInfo()
        entry.filename = entry_filename

    return entry_filename
