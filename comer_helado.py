apetece_helado_input = input("Te apetece un helado? (Si / No):").upper()
if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Si escribes una respuesta que no sea ni si ni no lo cuento como un no")
    apetece_helado = "NO"

tienes_dinero_input = input("Tienes dinero para un helado? (Si / No):").upper()
esta_tu_tia_input = input("Esta tu tia? (Si / No):").upper()


apetece_helado = apetece_helado_input == "SI"
puedes_permitirtelo = tienes_dinero_input or esta_tu_tia_input == "SI"

if apetece_helado and puedes_permitirtelo:
    print("Aqui tienes tu helado de chocolate")
else:
    print("Lo siento, te has quedado sin helado")
