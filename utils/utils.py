def format_amount(amount):
    formatted_amount = "{:,.0f}".format(amount).replace(",", ".")
    return formatted_amount
