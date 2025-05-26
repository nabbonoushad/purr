from pynput import mouse

def track():
    def move(x, y):
        print(f'Pointer moved to {(x, y)}')

    def click(x, y, button, pressed):
        print(f'{"Pressed" if pressed else "Released"} at {(x, y)}')
        if not pressed:
            return False

    def scroll(x, y, dx, dy):
        print(f'Scrolled {"down" if dy < 0 else "up"} at {(x, y)}')

    with mouse.Listener(
        on_move=move,
        on_click=click,
        on_scroll=scroll
    ) as listener:
        listener.join()

    return None