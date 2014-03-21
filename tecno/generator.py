
def generate():
    objects = []
    for i in range(1, 6):
        objects.append({
            "model": "auth.User",
            "fields": {
                "username": "user_%s" % i,
                "first_name": "User %s Name" % i,
                "is_staff": True,
            },
        })
    # generando algo
    for i in range(1, 6):
        objects.append({
            "model": "tecno.Curso",
            "fields": {
                "nombre": "Curso_%s" % i,
                "codigo": "Codigo %s" % i,
                "creditos": i,
            },
        })
    #generando estudiantes
    for i in range(1, 6):
        objects.append({
            "model": "auth.User",
            "fields": {
                "username": "estudiante_%s" % i,
                "first_name": "Estudiante %s Name" % i,
            },
        })
    #generando estudiantes
    for i in range(1, 6):
        objects.append({
            "model": "tecno.Docente",
            "fields": {
                "nombre": "nombre %s" % i,
                "email" : "email%s@moco.com" % i,
            },
        })    
        
    return objects