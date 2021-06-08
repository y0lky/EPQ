import csv

database = open('/Users/yannkull/Desktop/HoC-GE2019-results-by-constituency-csv.csv') # Import Data

maker = ["Bath and North East Somerset", "Bedfordshire", "Berkshire", "Bristol", "Buckinghamshire",
"Cambridgeshire", "Cheshire", "Cornwall", "County Durham", "Cumbria", "Derbyshire", "Devon", "Dorset",
"East Riding of Yorkshire", "East Sussex", "Essex", "Gloucestershire", "Greater London", "Greater Manchester",
"Hampshire", "Herefordshire", "Isle of Wight", "Isles of Scilly", "Kent", "Lancashire",
"Leicestershire", "Lincolnshire", "London", "Merseyside", "Norfolk", "North Somerset", "North Yorkshire",
"Northamptonshire", "Northumberland", "Nottinghamshire", "Oxfordshire", "Rutland", "Shropshire",
"Somerset", "South Gloucestershire", "South Yorkshire", "Staffordshire", "Suffolk", "Surrey", "Tyne and Wear",
"Warwickshire", "West Midlands", "West Sussex", "West Yorkshire", "Wiltshire", "Worcestershire", "Clwyd", "Dyfed",
         "Gwent", "Gwynedd", "Mid Glamorgan", "Powys", "South Glamorgan", "West Glamorgan", "Scotland", "Avon",
         "Northern Ireland", "Humberside", "Durham", "Gwent and Mid Glamorgan", "Hereford and Worcester",
         "Hertfordshire", "Cleveland"]

counties = {}

for c in maker:
    counties[c] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for row in database:
    data = row.split(",")
    votes = counties[data[0]]
    votes[0] += int(data[1])
    votes[1] += int(data[2])
    votes[2] += int(data[3])
    votes[3] += int(data[4])
    votes[4] += int(data[5])
    votes[5] += int(data[6])
    votes[6] += int(data[7])
    votes[7] += int(data[8])
    votes[8] += int(data[9])
    votes[9] += int(data[10])
    votes[10] += int(data[11])
    votes[11] += int(data[12])



