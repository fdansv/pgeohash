class GeoPoint:

    def __init__(self, lat, lon, precision):
        if lat > 90 or lat < -90:
            return
        if lon > 180 or lon < -180:
            return
        self.pointLat = lat
        self.pointLon = lon
        self.precision = precision

        self.hash()

    def hash(self):
        i = 0
        northLimit = 90
        eastLimit = 180
        southLimit = -90
        westLimit = -180
        hashString = ""
        while(i < self.precision):
            if self.pointLon < (eastLimit + westLimit)/2:
                hashString = hashString + "0"
                eastLimit = (eastLimit + westLimit)/2
            else:
                hashString = hashString + "1"
                westLimit = (eastLimit+westLimit)/2
            if (self.pointLat < (northLimit + southLimit)/2):
                hashString = hashString + "1"
                northLimit = (northLimit + southLimit)/2
            else:
                hashString = hashString + "0"
                southLimit = (northLimit + southLimit)/2
            i += 1
        self.theHash = hashString

    def precision(self, precision):
        self.precision = precision
        hash(self)

point = GeoPoint(51.52153, -5.1274, 10)
print point.theHash


class BoundingBox:
    coords = []
    n = 90
    s = -90
    e = -180
    w = 180
    geoPoint = GeoPoint()
    precision = 0

    def __init__(self, hash):
        self.hash = hash
        self.fromHash()
        self.calculatePrecision()

    def fromHash(self):
        hashCopy = self.hash
        while hashCopy != "":
            if hashCopy[0:2] == "0":
                self.e = (self.e + self.w)/2
            else:
                self.w = (self.e + self.w)/2
            if hashCopy[1:3] == "0":
                self.s = (self.n + self.s)/2
            else:
                self.n = (self.n + self.s)/2
            hashCopy = hashCopy[2:]
