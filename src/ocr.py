from mindee import Client, AsyncPredictResponse, product


def drivers_license(api_key, account_name, endpoint_name, version, input_file_path):
    """
    Mindee API function to parse the driver's license
    @params:
    - api_key: str - your Mindee API key
    - account_name: str - the Mindee account name
    - endpoint_name: str - the API endpoint name
    - version: str - the version of the endpoint
    - input_file_path: str - the path to the document image file

    rertun: 
    - output: the parsed document result
    """
    try:
        # Intializing the Mindee client with the API key
        client_mindee = Client(api_key=api_key)
        # Creating an endpoint using the account and endpoint information
        endpoint = client_mindee.create_endpoint(
            account_name=account_name,
            endpoint_name=endpoint_name,
            version=version
        )

        # Loading the license document from the input path
        input_license = client_mindee.source_from_path(input_file_path)
        output: AsyncPredictResponse = client_mindee.enqueue_and_parse(
            product.GeneratedV1,
            input_license,
            endpoint=endpoint
        )

        return output  # Return the document result
    
    except Exception as e:
        # Printing an error message and raising an exception if any error is encountered
        print(f"Failed to process the document")
        raise