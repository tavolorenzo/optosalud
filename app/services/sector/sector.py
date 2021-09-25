from data.models import sector as sector_model

def create_sector(name, photoURI, rooms):
    sector_model.create_sector(name, photoURI, rooms)

def update_sector(sectorId, name, photoURI, status, rooms):
    sector_model.update_sector(sectorId, name, photoURI, status, rooms)

def view_sector(sectorId):
    return sector_model.view_sector(sectorId)

def view_sectors():
    return sector_model.view_sectors()

def search_sectorId_ny_name(name):
    return sector_model.search_sectorId_ny_name(name)