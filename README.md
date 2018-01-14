# python_forex_quotes

python_forex_quotes is a Python Library for fetching realtime forex quotes

# Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
    - [List of Symbols available](#get-the-list-of-available-symbols)
    - [Get quotes for specific symbols](#get-quotes-for-specified-symbols)
    - [Convert from one currency to another](#convert-from-one-currency-to-another)
- [Support / Contact](#support-and-contact)
- [License / Terms](#license-and-terms)

## Requirements
* Python 2.7.*
* An API key which you can obtain for free at http://1forge.com/forex-data-api

## Installation
```
pip install python_forex_quotes
```
## Usage

### Instantiate the client
```python
import python_forex_quotes

#You can get an API key for free at 1forge.com
client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')
```

### Get the list of available symbols:

```python
import python_forex_quotes
client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

print client.getSymbols()
```

### Get quotes for specified symbols:
```python
import python_forex_quotes
client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

print client.getQuotes(['EURUSD', 'GBPJPY'])
```

### Convert from one currency to another:
```python
import python_forex_quotes
client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

print client.convert('EUR', 'USD', 100)
```

### Check if the market is open:
```python
import python_forex_quotes
client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

if client.marketIsOpen() == True:
    print "Market is open!"

```

### Check your usage / quota limit:
```python
import python_forex_quotes
client = python_forex_quotes.ForexDataClient('YOUR_API_KEY')

print client.quota()
```

## Support and Contact
Please contact me at contact@1forge.com if you have any questions or requests.

## License and Terms
This library is provided without warranty under the MIT license.
