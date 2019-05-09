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

    if binomial:
        try:
            cmp = ComplexNumber.binomial(float(elements[0]), float(elements[1]))
        except ValueError:
            raise InvalidSintaxError
    elif elements[1].endswith("pi"):
        pi_mult = elements[1].replace("pi", "", 1)
        pi_mult = pi_mult if pi_mult != "" else 1
        try:
            cmp = ComplexNumber.polar_with_pi(float(elements[0]),  float(pi_mult))
        except ValueError:
            raise InvalidSintaxError
    else:
        try:
            cmp = ComplexNumber.polar_with_decimal(float(elements[0]), float(elements[1]))
        except ValueError:
            raise InvalidSintaxError

    return cmp

