__version_info__ = (0, 15, 0)
version = __version__ = "0.15.0"

try:
    from mwlib._gitversion import gitid, gitversion
except ImportError:
    gitid = gitversion = ""

display_version = gitversion or version
