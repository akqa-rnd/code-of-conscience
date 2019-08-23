import geopandas as gpd
from shapely.geometry import Point,Polygon
from joblib import Parallel, delayed
import multiprocessing
from functools import partial

machineLocation = Point(174.902197,-36.863418)

url = "protectedAreaMap.shp"
df = gpd.read_file(url)

def processInput(i,point):
    return point.within(df.loc[i].geometry)

def isInProtectedArea (machineLocation):
    num_cores = multiprocessing.cpu_count() 
    process=partial(processInput, point=machineLocation)
    with multiprocessing.Pool(num_cores) as p:
        result = p.map(process, range(len(df)))           
    if sum(result):
        print("The machine is inside a protected area")
    else:
        print("The machine is not inside a protected area")


isInProtectedArea(machineLocation)




