import flet as ft

def main(page: ft.Page):
    page.bgcolor = "yellow"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    page.add(
        ft.Text("¡ARRANCÓ!", size=40, weight="bold", color="black"),
        ft.Text("Tablet Moderna Detectada", size=20, color="black")
    )

ft.app(target=main)
