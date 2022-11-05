from api.main import api

def table_from_api():
    for item in api().json:
        print(item)
    return api().json
