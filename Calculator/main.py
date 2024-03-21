import functions
import flet as ft
from flet import colors

buttons = [
    {'operator': 'C', 'font': colors.BLACK, 'background': colors.BLUE_GREY_100},
    {'operator': '±', 'font': colors.BLACK, 'background': colors.BLUE_GREY_100},
    {'operator': '%', 'font': colors.BLACK, 'background': colors.BLUE_GREY_100},
    {'operator': '/', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator': '7', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '8', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '9', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': 'X', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator': '4', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '5', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '6', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '-', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator': '1', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '2', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '3', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '+', 'font': colors.WHITE, 'background': colors.ORANGE},
    {'operator': '0', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '.', 'font': colors.WHITE, 'background': colors.WHITE24},
    {'operator': '=', 'font': colors.WHITE, 'background': colors.ORANGE},
]


def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_width = 270
    page.window_height = 380
    page.title = 'Calculator'
    page.window_always_on_top = True
    page.window_resizable = False

    result = ft.Text(value='0', color=colors.WHITE, size=20)

    def select(e):
        act_value = result.value if result.value not in ('0', 'Error') else ''
        value = e.control.content.value

        if value.isdigit():
            value = act_value + value
        elif value == 'C':
            value = '0'
        else:
            if act_value and act_value[-1] in ('/', 'X', '-', '+', '.'):
                act_value = act_value[:-1]

            value = act_value + value

            if value[-1] in ('=', '%', '±'):
                value = functions.calculate(signal=value[-1], act_value=act_value)

        result.value = value
        result.update()

    display = ft.Row(
        width=270,
        controls=[result],
        alignment='end',
    )

    btn = [ft.Container(
        content=ft.Text(value=btn['operator'], color=btn['font']),
        width=50,
        height=50,
        bgcolor=btn['background'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
    ) for btn in buttons]

    keyboard = ft.Row(
        width=270,
        wrap=True,
        controls=btn,
        alignment='end'
    )

    page.add(display, keyboard)


ft.app(target=main)
