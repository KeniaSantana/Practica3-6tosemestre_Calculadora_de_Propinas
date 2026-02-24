import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de Propinas"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Campo monto
    txt_monto = ft.TextField(
        label="Monto de la cuenta",
        width=300,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    # Textos de resultados
    txt_porcentaje = ft.Text("Propina: 5%")
    txt_propina = ft.Text("Propina calculada: $0.00")
    txt_total = ft.Text("Total a pagar: $0.00", size=20, weight="bold")

    # Función que calcula
    def calcular(e):
        try:
            monto = float(txt_monto.value)
        except:
            monto = 0

        porcentaje = slider.value
        propina = monto * (porcentaje / 100)
        total = monto + propina

        txt_porcentaje.value = f"Propina: {porcentaje:.0f}%"
        txt_propina.value = f"Propina calculada: ${propina:.2f}"
        txt_total.value = f"Total a pagar: ${total:.2f}"

        page.update()

    # Slider
    slider = ft.Slider(
        min=5,
        max=25,
        divisions=7,   # 8 posiciones
        value=5,
        label="{value}%",
        on_change=calcular,
        width=300
    )

    txt_monto.on_change = calcular

    page.add(
        ft.Text("Calculadora de Propinas", size=25, weight="bold"),
        txt_monto,
        slider,
        txt_porcentaje,
        txt_propina,
        txt_total
    )

ft.app(target=main)