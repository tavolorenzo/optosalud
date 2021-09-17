from data.models import sector as sector_model

def create_sector(name, photoURI, rooms):
    sector_model.create_sector(name, photoURI, rooms)

def update_sector(sectorId, name, photoURI, status, rooms):
    sector_model.update_sector(sectorId, name, photoURI, status, rooms)

def view_sector(sectorId):
    sector_model.view_sector(sectorId)
