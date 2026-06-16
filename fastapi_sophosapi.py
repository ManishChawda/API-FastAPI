from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# 🔐 Credentials
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")


# 🔹 Get Token
def get_access_token():
    url = "https://id.sophos.com/api/v2/oauth2/token"

    data = {
        "grant_type": "client_credentials",
        "CLIENT_ID": CLIENT_ID,
        "CLIENT_SECRET": CLIENT_SECRET,
        "scope": "token"
    }

    response = requests.post(url, data=data)
    return response.json()["access_token"]


# 🔹 Get Tenant + Region
def get_tenant_and_region(token):
    url = "https://api.central.sophos.com/whoami/v1"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(url, headers=headers)
    return response.json()


# 🔹 MAIN API (this replaces MCP tool)
@app.get("/firewalls")
def get_firewalls(location: str = ""):

    token = get_access_token()
    info = get_tenant_and_region(token)

    tenant_id = info["id"]
    api_host = info["apiHosts"]["dataRegion"]

    url = f"{api_host}/firewall/v1/firewalls"

    headers = {
        "Authorization": f"Bearer {token}",
        "X-Tenant-ID": tenant_id
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    result = []

    for fw in data.get("items", []):
        name = fw.get("hostname", "N/A")
        model = fw.get("model", "N/A")
        ip = fw.get("externalIpv4Addresses", [])
        status = fw.get("status", {}).get("connected", False)

        line = {
            "name": name,
            "model": model,
            "ip": ip,
            "online": status
        }

        if location:
            if location.lower() in name.lower():
                result.append(line)
        else:
            result.append(line)

    return {"firewalls": result}

