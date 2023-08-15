def get_materials(val):
    if val == val:
        val = eval(val)
        materials = []
        for material in val:
            if material.get('name'):
                materials.append(material.get('name').lower())
            else:
                pass
        if materials:
            return f"СОСТАВ: {', '.join(materials)}".replace(';', ',')
        else:
            return 'Состав не указан'
    else:
        return 'Состав не указан'
