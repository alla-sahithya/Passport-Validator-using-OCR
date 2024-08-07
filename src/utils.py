from datetime import datetime


def date_check(date):
    """
    This function is to parse the date string using multiple formats
    @params:
    - date: The date string to parse

    return:
    - datetime: A datetime object if the string is successfully parsed else None
    """
    # List of different date formats to parse the date string
    date_formats = [
        '%m/%d/%Y',  # MM/DD/YYYY
        '%d/%m/%Y',  # DD/MM/YYYY
        '%Y-%m-%d',  # YYYY-MM-DD
        '%Y/%m/%d',  # YYYY/MM/DD
        '%B %d, %Y',  # Month Day, Year
        '%d %B %Y'   # Day Month Year
    ]
    # Trying to parse the date string using each format in the list
    for format in date_formats:
        try:
            return datetime.strptime(date, format)
        except ValueError:
            # If the parsing fails with the current format, then continue to the next one
            continue  
    return None  # Return None if none of the formats match indicating the date is not valid


def check_license_expiry(expiry_date):
    """
    This function is to check if the license is expired or not based on the expiry date
    @params:
    - expiry_date: The expiry date of the driver's license
    
    return:
    - A message indicating whether the licence is accepted (valid) or expired
    """
    # Trying to check the date using the date_check function
    expiry_date = date_check(expiry_date)

    # If the date_check function returns None, the date format is invalid
    if not expiry_date:
        return 'Invalid date format'
    
    # Getting the current date and time
    current_date = datetime.now()

    # Comparing the parsed expiry date with current date
    if expiry_date > current_date:
        # If the expiry date is in the future, the license is still valid
        status = 'Accepted'
        date_formatted = expiry_date.strftime('%m/%d/%Y')  # Formatting the date
        return f"Expires: {date_formatted}\n{status}"  # Return message format
    else:
        # If the expiry date is in the past, the license hs expired
        status = 'Expired'
        date_formatted = expiry_date.strftime('%m/%d/%Y')
        return f"Expires: {date_formatted}\nWarning: {status}"