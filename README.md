# Chronos

Simple and easy to use time-related utility functions.

These are simple routines we caught ourselves constantly in need when developing projects in [Hackt](https://hackt.app). They're all a combination of native Python libraries that we wanted to standardize in a standlone library.

![Test Coverage](https://raw.githubusercontent.com/hacktlib/py-chronos/main/coverage.svg)
![PyPI](https://img.shields.io/pypi/v/pychronos)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code Style](https://img.shields.io/badge/code%20style-PEP8-lightgrey)](https://github.com/hhatto/autopep8/)
[![Code Formatter](https://img.shields.io/badge/formatter-autopep8-lightgrey)](https://github.com/hhatto/autopep8/)
[![Test Framework](https://img.shields.io/badge/testing-pytest-lightgrey)](https://github.com/pytest-dev/pytest/)


# Usage

Install from PyPI:

```python
pip install python_chronos
```

Import in your project(s):

```python
import chronos
```


## Get current UTC timestamp (`datetime` type)

```python
chronos.utc_now()
# datetime.datetime(2021, 2, 2, 3, 59, 11, 856368)
```


## UTC timestamp (`integer` type)

```python
chronos.utc_timestamp()
# 1612238428
```


## Past/Future UTC (`datetime` type)

The following function adds 10 minutes to the current UTC datetime:

```python
chronos.future_utc_datetime(minutes=10)
# datetime.datetime(2021, 2, 2, 4, 14, 3, 573054)
```

Similarly, the `past_utc_datetime` function does exactly what you have in mind:

```python
chronos.past_utc_datetime(minutes=10)
# datetime.datetime(2021, 2, 2, 3, 54, 3, 573054)
```

Any keyword arguments you would pass to [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objechttps://docs.python.org/3/library/datetime.html#datetime.timedeltats) will work with `future_utc_datetime` and `past_utc_datetime`.


## Past/Future UTC in UNIX timestamp (`integer` type)

```python
chronos.future_utc_timestamp(hours=2)
# 1612246043
```

Analogously, the `past_utc_timestamp` function will do exactly what you expect:

```python
chronos.past_utc_timestamp(hours=2)
# 1612238843
```

Again, any keyword arguments you would pass to [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#timedelta-objechttps://docs.python.org/3/library/datetime.html#datetime.timedeltats) will work with `future_utc_timestamp` and `past_utc_timestamp`.
