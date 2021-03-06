# Code of Conscience

## About
Today, despite its protective status, one third of the world's reserves are under threat from human activity. It’s hard to monitor and stop humans from destroying our planet, but could we stop the machines they use?

Code of Conscience is an open-source software based intervention that can shutdown heavy machines in protected land areas. To make the system available for all vehicles (including older ones) we produced a small, low-cost chip - with GPS, 4G and data storage.

The system code is available here for free to everyone.

Any Construction Equipment company can access and adapt it to their own system or any company can demand it to be implemented on their or their partners fleet.

Find out more at https://www.codeofconscience.org/

## Installation

Install dependencies
```sh
pip3 install -r requirements.txt
```

Download the latest WDPA Dataset shapefile (.shp) from https://www.protectedplanet.net/. Inside this archive you will find a number of files. Locate `WDPA_MONYEAR-shapefile-polygons.shp` and `WDPA_MONYEAR-shapefile-polygons.shx` (eg `WDPA_Aug2019-shapefile-polygons.shp` and `WDPA_Aug2019-shapefile-polygons.shx`) as save them in the root of this repo.

Open `CodeOfConscience.py` and edit the `shapefile` variable to reflect the name of the .shp file you have just downloaded eg:
```python
shapefile = "WDPA_Aug2019-shapefile-polygons.shp"
```

Set the `machineLocation` (Longitude, Latitude) to a location you'd like to check
```python
machineLocation = Point(175.8704514016789, -37.73493520423763)
```

Run the tool to check the location
```sh
python3 CodeOfConscience.py
```

## Validation Kit
An off-the-shelf validation kit to run the Code of Conscience Python code could be constructed using the following:

1. Raspberry Pi Model 3+ or Model 4: https://www.adafruit.com/product/3775
2. SixFab Raspberry Pi Hat: https://sixfab.com/product/raspberry-pi-cellular-iot-application-hat/
3. (Optional) Weatherproof case: https://sixfab.com/product/raspberry-pi-ip65-weatherproof-iot-project-enclosure/
4. (Optional) The kit includes an antenna for the GPS and LTE Cellular but you can purchase more here: https://sixfab.com/product/lte-gnss-dual-u-fl-antenna/
5. (Optional) You are likely to require a DCDC converter to step the power down if you don’t have a 5V USB port available: https://www.tindie.com/products/omzlo/pi-jack-power-your-raspberry-pi-from-6v-to-28v/

Details of the Code of Conscience hardware architecture can be found [here](hardware/CodeofConscienceValidationHardwareArchitecture.png), and the SixFab hat schematic can be found [here](hardware/Sixfab_RPi_CellularIoT_App_Hat_Schematic.PDF).