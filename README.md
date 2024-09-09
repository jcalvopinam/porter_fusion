# Porter Fusion

This feature provides a server for exposing files and directories located at the path specified by the `DOWNLOAD_FOLDER` variable. Users can easily access and download files from this location. Additionally, it supports file uploads to a designated folder, which is defined by the `UPLOAD_FOLDER` variable, ensuring that uploaded files are organized and stored in a predefined location. Both functionalities allow for easy management of file transfers, offering flexibility in sharing and receiving files on the server.

## Technology
- `Python3`

## Setup environment

### Virtual environment
- Enable and use virtual envs
```sh
# macOS/Linux:
source venv/bin/activate

# windows:
venv\Scripts\activate
```

### Secret key
- Generates a secret key
```python
import secrets
print(secrets.token_hex(16))
```

- Create the `.env` file in the root of the project, copy the key generate in the previous step
```properties
FLASK_SECRET_KEY=your_secret_key_here
```

### Customize folders
- By default:
    - `UPLOAD_FOLDER` variable points to `~/Download/porter`
    - `DOWNLOAD_FOLDER` variable points to `~/Download`
- To change the folder paths, create the `DOWNLOAD_PATH` and `UPLOAD_PATH` variables in the `.env` file and define the respective paths. e.g:
```properties
UPLOAD_PATH=/Users/dev/Downloads/porter
DOWNLOAD_PATH=/Users/dev/Downloads
```

- For production can be set as environment variables
```shell
# macOS/Linux:
export UPLOAD_PATH=/Users/dev/Downloads/porter
export DOWNLOAD_PATH=/Users/dev/Downloads

# windows
set UPLOAD_PATH=/Users/dev/Downloads/porter
set DOWNLOAD_PATH=/Users/dev/Downloads
```

### Install requirements
#### Development
- At the root of the project execute:
```pip
pip3 install -r requirements.txt
```

#### Production
- To install the module, at the root of the project run:
```sh
# using virtual env
pip3 install .

# this may require administrator permissions
python3 setup.py install

# by user (deactivate virtual env)
deactivate
pip3 install --user .
```

- To uninstall the module
```sh
pip3 uninstall porter_fusion
```

## Run
### Development
- At the root of project run:
```sh
python3 porter_fusion/app.py
```

- URL
```url
http://127.0.0.1:8081/
```

### Delivery
- After install as [Production](#production)
```sh
porter_fusion_web
```

- URL
```url
http://127.0.0.1:8081/
```
