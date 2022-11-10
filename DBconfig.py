import configparser
def config(filename='database.ini',section='postgresql'):
    parse = configparser.ConfigParser()
    parse.read(filename)

    db={}
    if parse.has_section(section):
        params = parse.items(section)
        for param in params:
             db[param[0]]= param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
def AlConfig(filename='database.ini',section='SQLAlchemy'):
    parse = configparser.ConfigParser()
    parse.read(filename)
    db=0
    if parse.has_section(section):
        param = parse.items(section)
        for params in param:
            db=params[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
    

  