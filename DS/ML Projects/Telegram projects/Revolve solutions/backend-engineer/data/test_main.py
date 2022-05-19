from main import *

def test_days():
    assert days(flights)== 365

def test_cities():
    assert cities(flights,airports) == ['Newark', 'New York']

def test_relationship():
    assert relationship(flights,planes) == "one-to-many relationship"

def test_most_delays_manf():
    assert most_delays_manf(flights) == ['EMBRAER', 2589621.0]

def test_two_connected_cities():
    assert two_connected_cities(flights) == ['New York', 'Los Angeles']



# output
"""

pytest test_main.py
================================================================== test session starts ===================================================================
platform win32 -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\Documents\Pandas\Projects\pandas\Telegram projects\Revolve solutions\backend-engineer\data
plugins: anyio-2.2.0, dash-2.0.0
collected 5 items                                                                                                                                         

test_main.py .....                                                                                                                                  [100%]

============================================================== 5 passed, 1 warning in 6.45s ==============================================================

"""