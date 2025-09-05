# Octonion-calculator

## Table of Contents
- [Intoduction](#intoduction)  
- [Description](#description)   
- [Installation](#installation)  
- [Usage](#usage)   
- [License](#license)
- [Dependencies](#dependencies)
- [Testing](#testing)  
- [Citation](#citation)

## Intoduction

This project was primarily created as a playground to experiment with GitHub CI/CD pipelines and to practice using pytest in real test scenarios.

That said, the project itself is fully functional — if, for any reason, you ever need a calculator for octonions and complex numbers, feel free to use this code

## Description

The project is a simple calculator for complex numbers and octonions.
It implements the following operations: addition, subtraction, multiplication, division, inversion, and conjugation.


## Installation

```bash
git clone
cd complex_numbers_calculator
pip install -e .
```

## Usage

```python
from complex_numbers_calculator import Calculator
from complex_numbers_calculator.models import ComplexNumber

sequence = [1.0, -3.0]
first_complex = ComplexNumber(sequence)

sequence2 = [2.0, 5.0]
second_complex = ComplexNumber(sequence2)

calc = Calculator(engine_name='complex_number')

result = calc.multiply(first_complex, second_complex)
print(result)
> ComplexNumber(17.00, -1.00)
```
### Engines

The calculator is built around an engine system.
To choose the working mode — complex numbers or octonions.
You HAVE TO select the corresponding engine:
- complex_number
- octonion

Owervise, you will get an error.

### Functions

It should also be noted that all public arithmetic functions (except for the norm) are immutable.
In other words, operations such as addition, subtraction, etc.
always create a new number object instead of modifying the existing one.

### Components and Norm

If you need to access the norm or the array of component values of a complex number,
you should directly use the corresponding attributes of the object.

```python
sequence = [1.0, -3.0]
first_complex = ComplexNumber(sequence)
print(first_complex.norm)
> 3.1622776601683795
print(first_complex.components)
> [ 1. -3.]
```

## License

This project is licensed under the [GPLv3 License](https://www.gnu.org/licenses/gpl-3.0.en.html).

## Dependencies

- Python ≥ 3.10  
- numpy ≥ 1.26.1,<2.0  

> **Note:** Package was developed and tested on the versions listed above.  
> It has not been tested on earlier versions, so compatibility with lower versions is not guaranteed.
> However, only minimal functionality from the NumPy library was used,
> so in theory the project should also work with earlier versions.

## Testing

For program testing I was using **pytest**. If you want to run test by yourself you can do it in testing directory.
```bash
cd tests
pytest
```
You also can use **pytest** with **-v** flag if you want to get more info abaout runnig tests.

## Citation

As a reference calcualtions results I was using this claculator:
https://robaina.github.io/cayley-dickson-calculator

Special thanks to its author, [Ángel R. Obaína](https://github.com/robaina), for making this tool publicly available.