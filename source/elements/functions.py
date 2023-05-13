import json


def open_config():
    with open('elements/config.json', 'r') as f:
        data = json.load(f)
        config = {
            'version': data['Version'],
            'appearance': data['Appearance'],
            'accent_color': data["Accent_Color"],
            'sawin_show': data["SAWIN_SHOW"],
            'sawin_automin': data["SAWIN_AUTOMIN"]}
        f.close()

    return config
