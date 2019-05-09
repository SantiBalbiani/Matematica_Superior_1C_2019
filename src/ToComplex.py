from src.ComplexNumber import ComplexNumber


class InvalidSintaxError(Exception):
    pass


def to_complex(text):
    parsing = text.replace(" ", "")

    binomial = False
    if parsing[0] == "(" and parsing.endswith(")"):
        binomial = True
        parsing = parsing.replace("(", "", 1).replace(")", "", 1)
    elif parsing[0] == "[" and parsing.endswith("]"):
        parsing = parsing.replace("[", "", 1).replace("]", "", 1)
    else:
        raise InvalidSintaxError()

    elements = parsing.split(",")

    if len(elements) != 2:
        raise InvalidSintaxError()

    try:
        if binomial:
            real = float(elements[0])
            imaginary = float(elements[1])
            cmp = ComplexNumber.binomial(real, imaginary)
        elif elements[1].endswith("pi"):
            pi_mult = elements[1].replace("pi", "", 1)
            pi_mult = float(pi_mult) if pi_mult != "" else 1
            abs = float(elements[0])
            cmp = ComplexNumber.polar_with_pi(abs, pi_mult)
        else:
            abs = float(elements[0])
            phase = float(elements[1])
            if phase == 0:
                cmp = ComplexNumber.polar_with_pi(abs, 0)
            else:
                cmp = ComplexNumber.polar_with_decimal(abs, phase)
    except ValueError:
        raise InvalidSintaxError

    return cmp

