import datetime as dt
import glob
import os
import pathlib as pl

import xdg
import ia256utilities.filesystem as fs

__author__ = "IceArrow256"
__version__ = '4'


def get_home_path():
    """
    :rtype: str
    """
    return str(pl.Path.home())


def get_config_path():
    """
    :rtype: str
    """
    return str(xdg.XDG_CONFIG_HOME) + "/MitsuScreenshots/config.json"


def get_screenshots_path():
    """
    :rtype: str
    """
    config = fs.load_json(get_config_path())
    if "screenshotsPath" in config:
        return config["screenshotsPath"]
    else:
        return get_home_path() + "/Pictures/Screenshots"


def get_unsorted_path():
    config = fs.load_json(get_config_path())
    if "unsortedPath" in config:
        return config["unsortedPath"]
    else:
        return get_screenshots_path() + "/Unsorted"


def keep_screenshots_path(path: str):
    config = fs.load_json(get_config_path())
    if os.path.isdir(path):
        config["screenshotsPath"] = path
        fs.save_json(config, get_config_path())


def keep_unsorted_path(path: str):
    config = fs.load_json(get_config_path())
    if os.path.isdir(path):
        config["unsortedPath"] = path
        fs.save_json(config, get_config_path())


def organize_screenshots(unsorted_path=get_unsorted_path(), screenshots_path=get_screenshots_path()):
    if os.path.isdir(unsorted_path) and os.path.isdir(screenshots_path):
        yield "Start"
        count = 0
        screenshots = glob.glob(unsorted_path + "/*.*")
        for screenshot in screenshots:
            time = dt.datetime.fromtimestamp(os.path.getmtime(screenshot))
            suffix = pl.Path(screenshot).suffix
            new_screenshot_name = "{}.{:02d}.{:02d} {:02d}:{:02d}:{:02d}{}".format(
                time.year, time.month, time.day, time.hour, time.minute, time.second, suffix)
            dirs = "/{}/{:02d}/{:02d}/".format(time.year, time.month, time.day)
            try:
                os.makedirs(screenshots_path + dirs)
            except FileExistsError:
                pass
            yield "From {} to {}".format(screenshot, screenshots_path + dirs + new_screenshot_name)
            os.rename(screenshot, screenshots_path + dirs + new_screenshot_name)
            count += 1
        yield "Nya! Processed {} images.".format(count)
