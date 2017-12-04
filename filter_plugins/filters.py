import os.path


def format_mods_arg(mods):
    """Converts a list of mods into a -mod argument.

    >>> format_mods_arg(['ace', 'acex'])
    -mod=mods/pdg/@ace;mods/pdg/@acex
    """
    mod_path = 'mods/pdg'
    mods_with_paths = [os.path.join(mod_path, '@' + m) for m in mods]
    return '-mod={}'.format(';'.join(mods_with_paths))


class FilterModule(object):
    """Custom jinja2 filters."""

    def filters(self):  # pylint: disable=no-self-use
        return {
            'format_mods_arg': format_mods_arg,
        }
