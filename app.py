import uuid
from fastapi import FastAPI

app = FastAPI()

packages = list()

@app.get("/api/pickup/points")
def get_pickup_points():
    return {
        "success": True,
        "pickupPoints": [
            {"pickupPointId":"ed709b83-5488-4e77-8dda-fd9ae28cb2e7","name":"Ronstring","address":"0 David Plaza"},
            {"pickupPointId":"60ce85b1-66a3-4577-a599-eb684466137a","name":"Tampflex","address":"090 Knutson Drive"},
            {"pickupPointId":"f1d5b2b0-6e61-43cd-8662-9dd1191d6de1","name":"Zontrax","address":"2 Schlimgen Junction"},
            {"pickupPointId":"7834e4b5-4500-4d1a-aad5-2baee970cc69","name":"Zamit","address":"718 Carpenter Road"}
        ]
    }


@app.post("/api/package/new")
def new_package(package: dict):
    package["packageId"] = uuid.uuid4().__str__()
    packages.append(package)

    return {
        "success": True,
        "packageId": package["packageId"]
    }


@app.get("/api/package/all")
def get_all_packages():
    return {
        "success": True,
        "packages": packages
    }
