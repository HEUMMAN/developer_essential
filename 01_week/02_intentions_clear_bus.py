ADULT_AGE = 19
CHILD_FEE = 800
ADULT_FEE = 1300
THE_ELDERLY_AGE = 65


def ride_bus(bus, user):
    if bus.is_full():
        return
    user.get_on(bus)
    if user.age < ADULT_AGE:
        user.pay(CHILD_FEE)
    elif user.age > THE_ELDERLY_AGE:
        pass
    else:
        user.pay(ADULT_FEE)

    if bus.location == user.dstination:
        user.get_off(bus)
