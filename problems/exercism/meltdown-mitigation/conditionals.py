def is_criticality_balanced(temperature: int, neutrons_emitted: int) -> bool:
    '''
    :param temperature: int
    :param neutrons_emitted: int
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    '''
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500_000


def reactor_efficiency(voltage: int, current: int,
                       theoretical_max_power: int) -> str:
    '''
    :param voltage: int
    :param current: int
    :param theoretical_max_power: int
    :return: str one of 'green', 'orange', 'red', or 'black'

    Efficiency can be grouped into 4 bands:

    1. green  ->   80-100% efficiency
    2. orange ->   60-79% efficiency
    3. red    ->   30-59% efficiency
    4. black  ->   <30% efficient

    These percentage ranges are calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    '''
    gen_pow = voltage * current
    efficiency = (gen_pow / theoretical_max_power) * 100
    if efficiency < 30:
        return "black"
    elif efficiency < 60:
        return "red"
    elif efficiency < 80:
        return "orange"

    return "green"


def fail_safe(temperature: int, neutrons_produced_per_second: int,
              threshold: int) -> str:
    '''
    :param temperature:
    :param neutrons_produced_per_second:
    :param threshold:
    :return: str one of: 'LOW', 'NORMAL', 'DANGER'

    - `temperature * neutrons per second` < 40% of threshold == 'LOW'
    - `temperature * neutrons per second` +/- 10% of `threshold` == 'NORMAL'
    - `temperature * neutron per second` is not in the above-stated ranges ==  'DANGER'
    '''
    reactivity = temperature * neutrons_produced_per_second
    percent = int((reactivity / threshold) * 100)
    print(percent)
    if percent < 40:
        return "LOW"
    elif percent <= 110 and percent >= 90:
        return "NORMAL"

    return "DANGER"
