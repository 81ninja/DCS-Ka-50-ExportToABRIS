import json
from urllib.request import urlopen
import os
import sys

class PointFeature:
    description=""
    location=(0,0)
    icon=""
    properties=[]

class ServerReader:
    url=""
    def __init__(self,url):
        self.url=url
    def readPoints(self, file):
        fileUrl=self.url+file
        objects=json.load(urlopen(fileUrl));
        features=[]
        for object in objects['features']:
            ptFtr=PointFeature()
            ptFtr.location=object['geometry']['coordinates']
            ptFtr.properties=object.get('properties')
            if ptFtr.properties:
            	ptFtr.description=ptFtr.properties.get('description')
            	ptFtr.icon=ptFtr.properties.get('icon')
            else:
            	ptFtr.properties={'description' : "", 'icon' : ""}
            	ptFtr.description=""
            	ptFtr.icon=ptFtr.properties.get('icon')
            features.append(ptFtr)
        return features