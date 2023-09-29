import pandas as pd

# List of city data files
URL = "D:\\idle-firefighter-tycoon\\Assets\\Assets\\Data"
CityData = [f'{URL}\\CityData0{i}.xlsx' for i in range(1, 4)]
IFFT_TSL = 'IFFT Task System List.xlsx'
# Read sheet names from the Excel file
sheets_IFFT = pd.ExcelFile(IFFT_TSL).sheet_names

# Iterate over each city data file
for i, city_file in enumerate(CityData):
    # Get the corresponding 3 sheets for each city data file                                                                                
    sheets = sheets_IFFT[i * len(CityData): (i + 1) * len(CityData)]

    # Read data from the city file
    city_data = pd.read_excel(city_file, sheet_name='_Tasks')
    city_data_item_type = city_data['ItemType']
    city_data_item_type = city_data_item_type.fillna(0)
    # Read data from the corresponding sheets in the IFFT file
    ifft_data = pd.concat([pd.read_excel(IFFT_TSL, sheet_name=sheet)['ItemType'] for sheet in sheets])
    ifft_data = ifft_data.fillna(0)

    # Check if the lengths of the two Series match
    if len(city_data_item_type) != len(ifft_data):
        print(f"The data from {city_file} and IFFT do not match in length.")
        continue

    # Find indices where the two Series do not match
    non_matching_indices = [idx for idx, (city_val, ifft_val) in enumerate(zip(city_data_item_type, ifft_data)) if city_val != ifft_val]

    # Print information if there are non-matching values
    if non_matching_indices:
        print(f"The data from {city_file} and IFFT do not match at the following positions:")
        for idx in non_matching_indices:
            print(f"Position {idx}: city_data = {city_data_item_type.iloc[idx]}, ifft_data = {ifft_data.iloc[idx]}")
    else:
        print(f"The data from {city_file} and IFFT are synchronized.")