import json
import urllib

def encodes_dict(dict_):
    for k, v in dict_.items():
        dict_[k] = v.encode('utf-8')

    return dict_

def make_google_request(coop):
    base_url = 'http://maps.google.com/maps/api/geocode/json?%s'

    search = "%(address)s %(district)s %(city)s" % coop
    get_params = urllib.urlencode({'sensor':'false', 'address':search})
    url = base_url % get_params

    return urllib.urlopen(url)

def retrieve_lat_and_long_from_response(response):
    google_data = json.load(response)

    if not google_data['results']:
        return None

    return google_data['results'][0]['geometry']['location']

def updates_coop_dict(coop_dict, map_location):
    dict_ = coop_dict.copy()

    lat_lng = "%(lat)s,%(lng)s" % map_location
    dict_['lat_long'] = lat_lng

    return dict_

def construct_json_file(filename, coops):
    print '['
    for coop in coops:
        print '\t{'
        for k, v in coop.items():
            print u"\t\t%s: %s" % (k, v.decode('ascii'))
        print '\t},'
    print ']'

coops = []
with open('dados_corretos.json', 'r') as fp:
    coops = json.load(fp)

coops_with_lat_lng = []

for coop in coops:
    if len(coops_with_lat_lng) > 2:
        break
    coop_utf_8 = encodes_dict(coop.copy())
    response = make_google_request(coop_utf_8)
    map_location = retrieve_lat_and_long_from_response(response)

    if map_location:
        coop_utf_8 = updates_coop_dict(coop_utf_8, map_location)
        coops_with_lat_lng.append(coop_utf_8)

construct_json_file('saida.json', coops_with_lat_lng)

#print 'Cooperativas parseadas: %d' % len(coops)
#print 'Cooperativas achadas: %d' % len(coops_with_lat_lng)
