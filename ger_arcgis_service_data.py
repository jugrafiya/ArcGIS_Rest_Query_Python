import requests
import json
import sys


# -5721308%2C-1158544
URL = "https://services9.arcgis.com/wueYtvO9SJNklLr0/ArcGIS/rest/services/Concessao/" \
      "FeatureServer/0/query?where=1%3D1&objectIds=&" \
      "time=&geometry=$$1&geometryType=esriGeometryPoint&inSR=&" \
      "spatialRel=esriSpatialRelIntersects&resultType=none&distance=0.0&units=esriSRUnit_Meter&returnGeodetic=false&" \
      "outFields=*&returnGeometry=true&returnCentroid=false&multipatchOption=xyFootprint&maxAllowableOffset=&" \
      "geometryPrecision=&outSR=&datumTransformation=&applyVCSProjection=false&returnIdsOnly=false&" \
      "returnUniqueIdsOnly=false&returnCountOnly=false&returnExtentOnly=false&returnDistinctValues=false&" \
      "orderByFields=&groupByFieldsForStatistics=&outStatistics=&having=&resultOffset=&resultRecordCount=&" \
      "returnZ=false&returnM=false&returnExceededLimitFeatures=true&quantizationParameters=&" \
      "sqlFormat=none&f=json&token="


out_field='NOME'

def main(geom):
    response = requests.get(URL.replace("$$1",str(geom)))
    resp_text= response.text

    resp_json = json.loads(resp_text)

    #print (resp_json['features'])

    for feat in resp_json['features']:
        print (out_field, " : ", feat['attributes'][out_field])


if __name__=='__main__':
    geometry= sys.argv[1:]
    main(geometry[1])


