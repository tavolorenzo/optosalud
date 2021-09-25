from data.models import role

def create_role(roleDescription, access):
    role.create_role(roleDescription, access)

def view_role(roleId):
    return role.view_role(roleId)

def update_role(roleId, roleDescription, access):
    role.update_role(roleId, roleDescription, access)
    