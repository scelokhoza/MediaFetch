

def filter_audio_formats(formats):
    """
    Filters the available formats to include only those with audio codecs,
    a valid file size, and excludes 'webm' formats.

    Args:
        formats (list): List of format dictionaries.

    Returns:
        list: Filtered list of audio formats.
    """
    return [
        f for f in formats
        if f.get('acodec') != 'none'
        and f.get('acodec') is not None
        and (f.get('filesize') or f.get('filesize_approx'))
        and 'webm' not in f.get('ext', '')
    ]
