import json
from utils import *
from ocr import drivers_license


def main():
    # Load the configuration from the JSON file
    with open("./configs/config.json") as f:
        config = json.load(f)

    # Extracting the configuration details
    api_key = config.get("api_key")
    account_name = config.get("account_name")
    endpoint_name = config.get("endpoint_name")
    version = config.get("version")
    input_file_path = config.get("input_file_path")

    # Validating configuration details
    if not all([api_key, account_name, endpoint_name, version, input_file_path]):
        print("Missing configuration details")
        return 
    
    try:
        # Calling the drivers license function to process the license
        output = drivers_license(api_key, account_name, endpoint_name, version, input_file_path)
    except Exception as e:
        print(f"Error processing the driver's license")
        return
    
    # Initializing the variables to store the extracted values
    last_name = ""
    first_name = ""
    expiry_date = ""

    # Iterating through the fields in the parsed document and storing required information
    for name, value in output.document.inference.prediction.fields.items():
        if name == 'date_of_expiry':
            expiry_date = check_license_expiry(str(value))
        elif name == 'last_name':
            last_name = str(value)
        elif name == 'first_name':
            first_name = str(value)
    
    full_name = f"{first_name} {last_name}"
    print(full_name)
    print(expiry_date)


if __name__ == "__main__":
    main()
