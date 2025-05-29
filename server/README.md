# Academic Status Classification in Portugal

Machine learning based application for classification of academic status of college students in Portugal

## How To Clone This Repository

## Bash

```
git clone https://github.com/Vympel87/academic_status.git
```

## How To Create Virtual Environment (venv)

### Windows (PowerShell)

```
python -m venv venv
```

### Linux / MacOS

```
python3 -m venv venv
```

## How To Activate Virtual Environment (venv)

### Windows (PowerShell)

```
.\venv\Scripts\Activate.ps1
```

If you use cmd.exe:

```
.\venv\Scripts\activate.bat
```

### Linux / MacOS (bash/zsh)

```
source venv/bin/activate
```

## How To Deactivate Virtual Environment (venv)

```
deactivate
```

## Install Dependencies

After the venv activated run:

```
pip install -r requirements.txt
```

## Create Environment Variable File

* Change .env.example file to .env
* Change the correct value of the variable inside your .env file

## Running a Server

```
uvicorn main:app --reload
```

## Contributors

* Agung (ML Engineer) dwiagungfebriyanto@gmail.com
* Fadhil (Web Developer) fadhillatmojo@gmail.com
* Rafa (Software Engineer) yudhistirarb727@gmail.com
