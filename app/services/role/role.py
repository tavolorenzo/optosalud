from data.models import role

def create_role(roleDescription, access): #OK
    role.create_role(roleDescription, access)

def view_role(roleId): #OK
    return role.view_role(roleId)

def update_role(roleId, roleDescription, access): #OK
    role.update_role(roleId, roleDescription, access)
    