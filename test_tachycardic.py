from tachycardic import is_tachycardic
import pytest


@pytest.mark.parametrize('myIn, Expect', [

	('tachycardic', True),
	('ta chyC ardic     ', True),
	('tachcardc', True),
	('TachCarDc', True),
	('large bottoms', False),
	('tac-e-car-dic', False),
	('taceecadc', False),
	('Tic-tac-toe-hy-car-dic', False)

	])


def test_is_tachycardic(myIn,Expect):
	re = is_tachycardic(myIn)

	assert re == Expect