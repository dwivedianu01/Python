from datetime import datetime

def format_date_to_iso(input_date_string):
    try:
        # Parse the input date string into a datetime object.
        input_date = datetime.strptime(input_date_string, '%Y-%m-%dT%H:%M:%SZ')

        # Format the datetime object in ISO 8601 format with milliseconds and "Z".
        iso_string = input_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

        return iso_string
    except ValueError:
        # Handle invalid input date string here (e.g., return an error message).
        return "Invalid date format"

# Example usage:
input_date_string = "2023-09-25 10:15:30"  # Replace with your input date string
formatted_date = format_date_to_iso(input_date_string)
print(formatted_date)
print(format_date_to_iso('2023-09-13T00:00:00Z'))
print(format_date_to_iso('2023-09-13'))

#{'_id': 28, 'number': 'SD1', 'description': 'sss', 'startDate': '2023-09-13T00:00:00Z', 'expiryDate': '2023-10-01T00:00:00.000Z', 'status': 'Approved', '__v': 8}
