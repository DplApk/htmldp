import flet as ft
import datetime
import traceback # Para poder leer los errores

def main(page: ft.Page):
    # --- 1. CONFIGURACIÓN DE SEGURIDAD ---
    # Ponemos fondo gris suave para saber si la app ha cargado (si ves gris, es que Python funciona)
    page.bgcolor = "#f0f0f0"
    page.theme_mode = "light"
    page.scroll = "auto" # Scroll automático para evitar bloqueos
    page.padding = 20

    # Variable para el selector de archivos
    file_picker = ft.FilePicker()

    # --- 2. EL "CAZADOR DE ERRORES" ---
    # Envolvemos TODO en un Try/Except. Si falla, nos lo dirá.
    try:
        # Añadimos el selector al inicio
        page.overlay.append(file_picker)

        # --- LÓGICA DE GUARDADO ---
        def guardar_archivo(e: ft.FilePickerResultEvent):
            if e.path:
                try:
                    # Contenido HTML (Falso Word)
                    html = f"""
                    <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word'>
                    <head><meta charset="utf-8"></head>
                    <body style="font-family: Arial; padding: 20px;">
                        <h2 style="text-align: center;">ATESTADO {txt_atestado.value}</h2>
                        <p><b>Fecha:</b> {txt_fecha.value}</p>
                        <p><b>Delito:</b> {dd_delito.value}</p>
                        <hr>
                        <h3>IDENTIFICADO</h3>
                        <p><b>Nombre:</b> {txt_nombre.value}</p>
                        <p><b>DNI:</b> {txt_dni.value}</p>
                    </body>
                    </html>
                    """
                    
                    with open(e.path, "w", encoding="utf-8") as f:
                        f.write(html)
                    
                    page.snack_bar = ft.SnackBar(ft.Text(f"✅ Guardado en: {e.path}"), bgcolor="green")
                    page.snack_bar.open = True
                    page.update()
                except Exception as ex:
                    page.snack_bar = ft.SnackBar(ft.Text(f"Error guardando: {ex}"), bgcolor="red")
                    page.snack_bar.open = True
                    page.update()

        # Conectar el guardado
        file_picker.on_result = guardar_archivo

        def btn_click(e):
            nombre = f"Atestado_{datetime.datetime.now().strftime('%H%M')}.doc"
            file_picker.save_file(dialog_title="Guardar Word", file_name=nombre)

        # --- CONTROLES (FORMULARIO) ---
        titulo = ft.Text("DILIGENCIA POLICIAL", size=24, weight="bold", color="blue", text_align="center")
        
        txt_atestado = ft.TextField(label="Nº Atestado", bgcolor="white")
        txt_fecha = ft.TextField(label="Fecha", value=datetime.date.today().strftime("%d/%m/%Y"), bgcolor="white")
        
        dd_delito = ft.Dropdown(
            label="Delito",
            bgcolor="white",
            options=[
                ft.dropdown.Option("Seguridad Vial"),
                ft.dropdown.Option("Robo"),
                ft.dropdown.Option("Violencia Género"),
            ]
        )
        
        txt_dni = ft.TextField(label="DNI", bgcolor="white")
        txt_nombre = ft.TextField(label="Nombre Completo", bgcolor="white")
        
        btn = ft.ElevatedButton(
            "GENERAR DOCUMENTO", 
            icon=ft.icons.SAVE, 
            bgcolor="blue", 
            color="white", 
            height=50,
            on_click=btn_click
        )

        # --- 3. AÑADIR A PANTALLA (Uno a uno para asegurar) ---
        page.add(
            ft.Column([
                titulo,
                ft.Divider(),
                txt_atestado,
                txt_fecha,
                dd_delito,
                ft.Divider(),
                txt_dni,
                txt_nombre,
                ft.Divider(),
                btn,
                ft.Text("Versión Segura v1.0", size=10, color="grey", text_align="center")
            ])
        )
    
    except Exception as e:
        # --- SI ALGO FALLA, ESTO SALDRÁ EN PANTALLA ROJA ---
        page.bgcolor = "white"
        page.add(
            ft.Text("¡ERROR AL INICIAR!", color="red", size=30, weight="bold"),
            ft.Text(f"Por favor, envía una foto de esto:", color="black"),
            ft.Container(
                content=ft.Text(traceback.format_exc(), color="red", size=12),
                bgcolor="#ffebee",
                padding=10,
                border=ft.border.all(1, "red")
            )
        )
        page.update()

ft.app(target=main)
