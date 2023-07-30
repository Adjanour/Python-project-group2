from string import Template

def format_money(money_amount, currency_symbol="$", decimal_places=2, thousands_separator =","):
    """
    Format a money amount with the appropriate currency symbol, decimal places, and thousands separator.

    Parameters:
        money_amount (float): The money amount to be formatted.
        currency_symbol (str, optional): The currency symbol to be used (default is "$").
        decimal_places (int, optional): The number of decimal places to be displayed (default is 2).
        thousands_separator (str, optional): The thousands separator (default is ",").

    Returns:
        str: The formatted money amount as a string.
    """
    money_format = Template("${amount}")
    formatted_amount = "{:,.{}f}".format(money_amount, decimal_places)
    formatted_money = money_format.substitute(amount=formatted_amount)
    return f"{currency_symbol}{formatted_money}"

# Example usage:
money_amount = 123456156561565565.67
formatted_money = format_money(money_amount)
print(formatted_money)
