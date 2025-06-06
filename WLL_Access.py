import requests
from requests.adapters import HTTPAdapter, Retry
import json

#Obtain your v2 Api keys from the weatherlink site of your device
#weatherlink, login, account information (little person)
api_Key    = "your api key"
api_Secret = "your api secret key"
deviceId = "your device Id"
#Obtain station Id from address line in weatherlink when displaying data
# https://api.weatherlink.com/v2/current/{station-id}?api-key={YOUR API KEY} for current conditions

def FtoC(val: float):
    c = 1.0
    C = (val-32) * 5 / 9
    return C

print("Requesting")
url_api_v2 = "https://api.weatherlink.com/v2/current/"+deviceId+"?api-key="+api_Key

headers	= {
  "X-Api-Secret" : api_Secret,
  "Content-Type" : "application/json"
}
response = requests.get(url_api_v2, headers=headers)
#n2 = "%.2f" % n1
print("Status Code:", response.status_code)
print("Response Text:", response.text)
input()
json_data = response.json()
Station_Id = json_data['station_id_uuid']
print ("Station Id : ", Station_Id)
print("Temperature In: ", "%.1f"%(FtoC(json_data['sensors'][0]['data'][0]['temp_in'])),"°C")
print("Temperature Out: ", "%.1f"%(FtoC(json_data['sensors'][3]['data'][0]['temp'])),"°C")
print("Wind Chill: ", "%.1f"%(FtoC(json_data['sensors'][3]['data'][0]['wind_chill'])),"°C")
print("Humidity: ", json_data['sensors'][3]['data'][0]['hum'],"%")
print("Dew Point: ", "%.1f"%(FtoC(json_data['sensors'][3]['data'][0]['dew_point'])),"°C")
print("Heat Index: ", "%.1f"%(FtoC(json_data['sensors'][3]['data'][0]['heat_index'])),"°C")
print("Pressure: ", "%.1f"%((json_data['sensors'][2]['data'][0]['bar_absolute']) * 33.863886666667),"hPA")
print("THW Index: ", "%.1f"%(FtoC(json_data['sensors'][3]['data'][0]['thw_index'])),"°C"," what it 'feels' like out in the shade")
print("THSW Index: ", "%.1f"%(FtoC(json_data['sensors'][3]['data'][0]['thsw_index'])),"°C", " what it 'feels' like out in the sun")
print("Wet Bulb: ", "%.1f"%(FtoC(json_data['sensors'][3]['data'][0]['wet_bulb'])),"°C", "to assess heat stress, snowfall prediction if negative")
print("Rain Daily:", json_data['sensors'][3]['data'][0]['rainfall_daily_mm'], "mm")
print("Rain Monthly: ", json_data['sensors'][3]['data'][0]['rainfall_monthly_mm'],"mm")
print("Rain Yearly: ", json_data['sensors'][3]['data'][0]['rainfall_year_mm'],"mm")
print("Rain Rate: ", json_data['sensors'][3]['data'][0]['rain_rate_hi_mm'],"mm")
print("Rain Last 24Hr: ", json_data['sensors'][3]['data'][0]['rainfall_last_24_hr_mm'],"mm")
print("Wind Direction: ", json_data['sensors'][3]['data'][0]['wind_dir_last'],"°")
print("Wind Speed: ", json_data['sensors'][3]['data'][0]['wind_speed_hi_last_2_min'],"mph")
print("Solar Radiation: ", json_data['sensors'][3]['data'][0]['solar_rad'], "W/M2")

print("Rx State: ", json_data['sensors'][3]['data'][0]['rx_state'])
#print(json_data['sensors'][3]['data'][0]['rainfall_last_24_hr_mm'])

"""
{
  "station_id_uuid": "station Id",
  "sensors": [
    {
      "lsid": 414278,
      "data": [
        {
          "temp_in": 76.8,
          "tz_offset": 3600,
          "heat_index_in": 76.2,
          "dew_point_in": 53.4,
          "ts": 1749222046,
          "hum_in": 44.2
        }
      ],
      "sensor_type": 243,
      "data_structure_type": 12
    },
    {
      "lsid": 414276,
      "data": [
        {
          "battery_voltage": 4703,
          "wifi_rssi": -76,
          "network_error": null,
          "ip_v4_gateway": "192.168.0.1",
          "bluetooth_version": null,
          "bgn": null,
          "firmware_version": 1636079858,
          "tz_offset": 3600,
          "local_api_queries": 49744,
          "rx_bytes": 9222171,
          "health_version": 1,
          "radio_version": 621020416,
          "ip_address_type": 1,
          "link_uptime": 690518,
          "input_voltage": 4637,
          "tx_bytes": 184823765,
          "ip_v4_netmask": "255.255.255.0",
          "rapid_records_sent": 294920,
          "uptime": 780442,
          "touchpad_wakeups": 66,
          "ip_v4_address": "192.168.0.101",
          "bootloader_version": 1550707628,
          "espressif_version": 1534381024,
          "dns_type_used": null,
          "network_type": 1,
          "ts": 1749222000
        }
      ],
      "sensor_type": 504,
      "data_structure_type": 15
    },
    {
      "lsid": 414277,
      "data": [
        {
          "bar_absolute": 29.652,
          "tz_offset": 3600,
          "bar_sea_level": 29.796,
          "bar_offset": -0.001,
          "bar_trend": 0.015,
          "ts": 1749222046
        }
      ],
      "sensor_type": 242,
      "data_structure_type": 12
    },
    {
      "lsid": 414281,
      "data": [
        {
          "rx_state": 0,
          "wind_speed_hi_last_2_min": 12,
          "hum": 53.1,
          "wind_dir_at_hi_speed_last_10_min": 225,
          "wind_chill": 65.5,
          "rain_rate_hi_last_15_min_clicks": 0,
          "thw_index": 63.8,
          "wind_dir_scalar_avg_last_10_min": 270,
          "rain_size": 2,
          "uv_index": null,
          "tz_offset": 3600,
          "wind_speed_last": 15,
          "rainfall_last_60_min_clicks": 0,
          "wet_bulb": 53.6,
          "rainfall_monthly_clicks": 77,
          "wind_speed_avg_last_10_min": 6.62,
          "wind_dir_at_hi_speed_last_2_min": 266,
          "rainfall_daily_in": 0.023622047,
          "wind_dir_last": 233,
          "rainfall_daily_mm": 0.6,
          "rain_storm_last_clicks": 32,
          "tx_id": 1,
          "rain_storm_last_start_at": 1748929980,
          "rain_rate_hi_clicks": 0,
          "rainfall_last_15_min_in": 0,
          "rainfall_daily_clicks": 3,
          "dew_point": 48,
          "rainfall_last_15_min_mm": 0,
          "rain_rate_hi_in": 0,
          "rain_storm_clicks": 44,
          "rain_rate_hi_mm": 0,
          "rainfall_year_clicks": 1064,
          "rain_storm_in": 0.3464567,
          "rain_storm_last_end_at": 1749034861,
          "rain_storm_mm": 8.8,
          "wind_dir_scalar_avg_last_2_min": 279,
          "heat_index": 63.8,
          "rainfall_last_24_hr_in": 0.023622047,
          "rainfall_last_60_min_mm": 0,
          "trans_battery_flag": 0,
          "rainfall_last_60_min_in": 0,
          "rain_storm_start_time": 1749101221,
          "rainfall_last_24_hr_mm": 0.6,
          "rainfall_year_in": 8.377953,
          "wind_speed_hi_last_10_min": 16,
          "rainfall_last_15_min_clicks": 0,
          "rainfall_year_mm": 212.8,
          "wind_dir_scalar_avg_last_1_min": 272,
          "temp": 65.5,
          "wind_speed_avg_last_2_min": 5.5,
          "solar_rad": 279,
          "rainfall_monthly_mm": 15.4,
          "rain_storm_last_mm": 6.4,
          "wind_speed_avg_last_1_min": 4.93,
          "thsw_index": 67.7,
          "rainfall_monthly_in": 0.6062992,
          "rain_rate_last_mm": 0,
          "rain_rate_last_clicks": 0,
          "rainfall_last_24_hr_clicks": 3,
          "rain_storm_last_in": 0.2519685,
          "rain_rate_last_in": 0,
          "rain_rate_hi_last_15_min_mm": 0,
          "rain_rate_hi_last_15_min_in": 0,
          "ts": 1749222046
        }
      ],
      "sensor_type": 43,
      "data_structure_type": 10
    }
  ],
  "generated_at": 1749222381,
  "station_id": 112555
}
"""