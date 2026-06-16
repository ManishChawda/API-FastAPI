# API-FastAPI

FastAPI examples for integrating with Sophos Central APIs.

## Features

* OAuth Authentication
* Access Token Generation
* Tenant Information Retrieval
* Firewall Inventory Retrieval
* FastAPI REST Endpoints

## Requirements

* Python 3.11+
* FastAPI
* Requests

## Installation

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
```

## Run

```bash
uvicorn fastapi_sophosapi:app --reload
```

## Learning Objectives

* FastAPI Fundamentals
* REST APIs
* OAuth Authentication
* API Development

## Author

Manish Chawda
