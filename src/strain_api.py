import requests

# URLs
base_url = requests.get('strainapi.evanbusse.com/API_KEY')
effects_url = requests.get('strainapi.evanbusse.com/API_KEY/searchdata/effects')
flavors_url = requests.get('strainapi.evanbusse.com/API_KEY/searchdata/flavors')

# Get all strains (Use sparingly -- requires a lot of computing power)
strains_url = requests.get('strainapi.evanbusse.com/API_KEY/strains/search/all')

# Search for strains by name
requests.get('strainapi.evanbusse.com/API_KEY/strains/search/name/NAME')

# Search for strains by race (Available races: Sativa, Indica, and Hybrid)
strainapi.evanbusse.com/API_KEY/strains/search/race/RACE
# Search for strains by effect
strainapi.evanbusse.com/API_KEY/strains/search/effect/EFFECT
# Search for strains by flavor
strainapi.evanbusse.com/API_KEY/strains/search/flavor/FLAVOR

response = requests.get("strainapi.evanbusse.com/API_KEY/searchdata/effects
")
print(response.status_code)
