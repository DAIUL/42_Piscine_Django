#!/usr/bin/python3

import sys

BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"

def coor_to_bin(value, min, max, bits):
	
	result = ""

	for _ in range(bits):
		mid = (min + max) / 2
		if value > mid:
			result += "1"
			min = mid
		else:
			result += "0"
			max = mid
	
	return result

def inter_bin(lon_bin, lat_bin):
	
	result = ""

	for lon_bit, lat_bit in zip(lon_bin, lat_bin):
		result += lon_bit + lat_bit

	return result

def bin_to_hash(geo_bin):
	
	result = ""

	while len(geo_bin) % 5 != 0:
		geo_bin += "0"

	for i in range(0, len(geo_bin), 5):
		chunk = geo_bin[i:i+5]
		index = int(chunk, 2)
		result += BASE32[index]

	return result

def co_to_geohash(lon, lat, bits=30):

	lon_bin = coor_to_bin(lon, -180, 180, bits)
	lat_bin = coor_to_bin(lat, -90, 90, bits)
	geo_bin = inter_bin(lon_bin, lat_bin)
	geohash = bin_to_hash(geo_bin)

	return geohash


def main(argv):

	print(co_to_geohash(argv[0], argv[1]))

if __name__ == '__main__':
	main([2.2945, 48.8584])