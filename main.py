import flet as ft

def main(page: ft.Page):
    # PONEMOS FONDO AMARILLO CHILLÓN
    # Si ves amarillo, la App funciona.
    # Si ves blanco, el problema es el móvil.
    page.bgcolor = "yellow"
    
    # Centramos todo
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.add(
        ft.Text(
            "¡FUNCIONA!", 
            size=40, 
            color="black", 
            weight="bold"
        ),
        ft.Text(
            "Si ves esto, ya podemos\nvolver a poner el formulario.",
            size=20,
            color="black",
            text_align="center"
        ),
        ft.ElevatedButton("Tócame", on_click=lambda e: print("Vivo"))
    )

ft.app(target=main)
