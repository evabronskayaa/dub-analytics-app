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
            return f"Состав: {', '.join(materials)}".replace(';', ',')
        else:
            return 'Состав не указан'
    else:
        return 'Состав не указан'
    

def get_sizes(val):
    if val == val:
        val = eval(val)
        sizes = []
        for size in val:
            if size.get('name'):
                sizes.append(f"{size.get('name').lower()}/{size.get('origName').upper()}")
            else:
                pass
        if sizes:
            return f"Размеры: {', '.join(set(sorted(sizes)))}".replace(';', ',')
        else:
            return 'Размер не указан'
    else:
        return 'Размер не указан'
    

def get_manufacturer(val):
    if val == val:
        val = eval(val)
        for info in val:
            if info.get('name') == 'Страна производства':
                return f"Страна производства: {info.get('value')}"
        return 'Страна производства не указана'
    else:
        return 'Страна производства не указана'
    

def get_color(val):
    if val == val:
        return f"Цвет: {val}"
    else:
        return 'Цвет не указан'
