from data.models import sector as sector_model

def create_sector(name, photoURI,rooms): #OK
    sector_model.create_sector(name, photoURI,rooms)

def update_sector(sectorId, name, photoURI, status,rooms): #OK
    sector_model.update_sector(sectorId, name, photoURI, status, rooms)

def view_sector(sectorId): #OK
    return sector_model.view_sector(sectorId)

def view_sectors():  #OK
    return sector_model.view_sectors()

def search_sectorId_ny_name(name): #OK
    return sector_model.search_sectorId_ny_name(name)