from pathlib import Path

def get_refresh_token() -> str:
    filepath = r"C:\Users\OK\source\repos\test_media_files\_api"
    filepath = Path(filepath).joinpath( "dropbox_refresh_token.txt")
    with open(filepath ,"r") as f:
        buf:str = f.read()
    return buf.strip()

def get_access_token() -> str:
    filepath = r"C:\Users\OK\source\repos\test_media_files\_api"
    filepath = Path(filepath).joinpath( "dropbox_access_token.txt")
    with open(filepath ,"r") as f:
        buf:str = f.read()
    return buf.strip()

def get_api_key() -> str:
    filepath = r"C:\Users\OK\source\repos\test_media_files\_api"
    filepath = Path(filepath).joinpath( "dropbox_api_key.txt")
    with open(filepath ,"r") as f:
        buf:str = f.read()
    return buf.strip()

def get_security_key() -> str:
    filepath = r"C:\Users\OK\source\repos\test_media_files\_api"
    filepath = Path(filepath).joinpath( "dropbox_security_key.txt")
    with open(filepath ,"r") as f:
        buf:str = f.read()
    return buf.strip()

if __name__ == '__main__':
    ACCESS_TOKEN = get_access_token()
    print("ACCESS_TOKEN = {}".format(ACCESS_TOKEN))
    API_KEY = get_api_key()
    print("API_KEY = {}".format(API_KEY))
    SECURITY_KEY = get_security_key()
    print("SECURITY_KEY = {}".format(SECURITY_KEY))