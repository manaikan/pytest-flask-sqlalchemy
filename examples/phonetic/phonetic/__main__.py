from .application import application as create_app
from .models import NATO

DABANAME = "Phonetic"
DABATYPE = "mssql"
PROTOCOL = "pymssql"
USERNAME = "sa"
PASSWORD = "cvd"
HOSTNAME = "DESKTOP-1AN9JVP"
HOSTPORT = ""
DABAHOST = f"{HOSTNAME}:{HOSTPORT}" if HOSTPORT else f"{HOSTNAME}"
DABA_URL = f"{DABATYPE}+{PROTOCOL}://{USERNAME}:{PASSWORD}@{DABAHOST}/{DABANAME}" # mssql+pymssql://sa:cvd@DESKTOP-1AN9JVP/PSPDB1

app = create_app(DABA_URL, include_models=[NATO])
app.run(host="0.0.0.0")