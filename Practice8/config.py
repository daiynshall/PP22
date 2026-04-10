from configparser import ConfigParser
from pathlib import Path

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    path = Path(__file__).resolve().parent / filename

    with open(path, 'r', encoding='utf-8-sig') as f:
        parser.read_file(f)

    if not parser.has_section(section):
        print("Loaded file:", path)
        print("Available sections:", parser.sections())
        raise Exception(f'Section {section} not found in the {filename} file')

    config = {}
    for param in parser.items(section):
        config[param[0]] = param[1]

    return config