def find_cosa(curr_or_pow, volt_or_none=None) -> float:  # Функция находит значение cosa
    # (где а - угол между нормалью к БС и направлением на Солнце)
    power_fact = 0.09  # Фактическая мощность имеющейся БФ(константа, известна на стадии изготовления)
    if volt_or_none == None:
        cosa = curr_or_pow / power_fact
    else:
        power_moment = curr_or_pow * volt_or_none
        cosa = power_moment / power_fact
    if cosa > 1:
        cosa = 1
    return round(cosa, 3)
