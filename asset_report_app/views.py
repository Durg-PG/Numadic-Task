# asset_report_app/views.py
# from .models import VehicleData
from django.db import models
from .models import VehicleData
import pandas as pd
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VehicleDataSerializer



# def haversine(lat1, lon1, lat2, lon2):
#     # Define the haversine function as you provided before
#     # ...

@api_view(['GET'])
def generate_asset_report(request, start_time, end_time):
    # Convert start_time and end_time from epoch format to datetime objects
    from datetime import datetime
    start_time_datetime = datetime.fromtimestamp(start_time)
    end_time_datetime = datetime.fromtimestamp(end_time)

    # Query the data from the database for the specified time period
    queryset = VehicleData.objects.filter(case_open__gte=start_time_datetime, case_open__lte=end_time_datetime)

    # Serialize the data to a pandas DataFrame
    serializer = VehicleDataSerializer(queryset, many=True)
    data_df = pd.DataFrame(serializer.data)

    # Perform calculations and generate the asset_report_df DataFrame
    # Assuming you have the code to calculate distance_traveled, average_speed, and other required information


    # Convert asset_report_df to Excel
    excel_file_path = "C:\\Users\Durgesh PG\Documents\Zoom\asset_report.xlsx"
    asset_report_df.to_excel(excel_file_path, index=False)

    # Return the Excel file as a downloadable attachment in the HTTP response
    with open(excel_file_path, 'rb') as file:
        response = HttpResponse(file.read(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=asset_report.xlsx'

    return response



# from zipfile import ZipFile
# import pandas as pd
# import io

# # Step 1: Read vehicle trails
# # Assuming NU-raw-location-dump.zip is unzipped in a folder named "trails"
# vehicle_trails = []
# with ZipFile("C:\\Users\\Durgesh PG\\Downloads\\NU-raw-location-dump.zip", 'r') as zip_file:
#     for csv_file in zip_file.namelist():
#         if csv_file.endswith('.csv'):
#             # Read the bytes of the CSV file from the zip archive
#             csv_bytes = zip_file.read(csv_file)
#             # Use pd.read_csv() on the bytes to read the CSV data
#             df = pd.read_csv(io.BytesIO(csv_bytes), low_memory=False)
#             # Process the DataFrame (df) here if needed
#             vehicle_trails.append(df)

# import pandas as pd
# from math import radians, sin, cos, sqrt, atan2

# # Assuming your DataFrame is named "df"
# distance_traveled_list = [0]  # Initialize the first element with 0

# for i in range(1, len(df)):
#     lat1 = df.loc[i, 'lat']
#     lon1 = df.loc[i, 'lon']
#     lat2 = df.loc[i - 1, 'lat']
#     lon2 = df.loc[i - 1, 'lon']
#     distance = haversine(lat1, lon1, lat2, lon2)
#     distance_traveled_list.append(distance)

# df['DistanceTraveled'] = distance_traveled_list














# # import pandas as pd
# # from math import radians, sin, cos, sqrt, atan2

# # # Assuming you have already filtered the DataFrames based on the specified time period and stored them as 'df' and 'trip_info_df'.

# # # Step 2: Group the vehicle trail DataFrame by 'lic_plate_no'
# # grouped_df = df.groupby('lic_plate_no')

# # # Step 3: Calculate the average speed and number of speed violations for each vehicle
# # vehicle_info = []
# # for vehicle, trail_df in grouped_df:
# #     # Calculate the average speed for each vehicle
# #     average_speed = trail_df['spd'].mean()

# #     # Calculate the number of speed violations for each vehicle
# #     num_speed_violations = trAail_df['osf'].sum()

# #     # Calculate the distance traveled for each vehicle
# #     distance_traveled = trail_df['DistanceTraveled'].sum()

# #     # Calculate the number of trips completed by each vehicle
# #     num_trips_completed = len(trail_df)

# #     # Fetch the transporter name from trip_info_df based on the vehicle number
# #     transporter_name = trip_info[trip_info['vehicle_number'] == vehicle]['transporter_name'].iloc[0]

# #     # Append the results to the list
# #     vehicle_info.append({
# #         'License plate number': vehicle,
# #         'Distance': distance_traveled,
# #         'Number of Trips Completed': num_trips_completed,
# #         'Average Speed': average_speed,
# #         'Transporter Name': transporter_name,
# #         'Number of Speed Violations': num_speed_violations
# #     })

# # # Convert the results list to a DataFrame
# # asset_report_df = pd.DataFrame(vehicle_info)

# # # Print the generated asset_report_df DataFrame
# # print(asset_report_df)