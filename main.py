import threading


def divide():

    result = 10 / 0
    try:
        result = 10 / 0
        print("Resultado de la división:", result)
    except ZeroDivisionError as e:
        print("Excepción:", e)
        return e


t = threading.Thread(target=divide)
t.start()
t.join()


print("Hilo padre finalizado.")

# ------------------------------------
