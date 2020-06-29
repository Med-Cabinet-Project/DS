# DS

# Med Cabinet API


Med Cabinet is a cannibis recommendation service. Users are able to query a 2K + database to get recommendations based on medical conditions/symptoms, positive effects they wish to experience, and specific strains types they are interested. If the user knows or wants to find out more about a specific strain, they can query the name directly, as well. 


## BASE URL
[https://med-cabinet-project.herokuapp.com/] (https://med-cabinet-project.herokuapp.com/)

Here user can see a json list holding dictioanries of all the different strains and different information about it.


### ENDPOINTS
* "/<strain>"

User enters a string query for a strain name and they get a json object, similar to the one below: 

```
[https://med-cabinet-project.herokuapp.com/Afpak](https://med-cabinet-project.herokuapp.com/Afpak)
description: "Afpak, named for its dir…ving difficulty eating."
flavor: 	 "Pine,Spicy/Herbal,Earthy"
medical: 	 "Depression,Insomnia,Pain,Stress,Lack of Appetite"
negative: 	 "Dizzy"
positiveL 	 "Relaxed,Creative,Focused,Sleepy,Happy"
rating: 	 4.2
type: 	     "hybrid"
```

* "/data"
User can view a static html table of all the different strains stored in the Postgres Database.

* "/types/<race>"
Users can enter the specific type/family of weed they are interested in, i.e. hybrid, indica, sativa This query return a randomized list of five strains that are in this category.

```
[https://med-cabinet-project.herokuapp.com/types/indica](https://med-cabinet-project.herokuapp.com/types/indica)
```

* "/medical/<medical>"
Users can enter specific medical conditions/symptoms and they will receive 5 different strains said to 
treat or help with the condition. 

List of medical conditions in database
- Depression
- Eye Pressure
- Fatigue
- Headaches
- Inflammation
- Insomnia
- Lack of Appetite
- Muscle Spasms
- Nausea
- Pain
- Seizures
- Spasticity
- Stress

```
[https://med-cabinet-project.herokuapp.com/medical/depression](https://med-cabinet-project.herokuapp.com/medical/depression)

flavor:	  "Earthy,Sweet,Pine"
id: 	  250
medical:  "Depression,Pain,Stress,Cramps,Lack of Appetite"
name:	  "Blue Champagne"
negative: "Dizzy,Dry Mouth,Paranoid,Dry Eyes,Anxious"
positive  "Euphoric,Happy,Creative,Energetic,Uplifted"
type:     "hybrid"
```

* "/positive/<positive>"

Users can enter specific positive effects they wish to experiences and they will receive 5 different 
strains that allow the user to experience said feeling. 

List of positive effects in database
- Creative
- Energetic
- Euphoric
- Focused
- Giggly
- Happy
- Hungry
- Relaxed
- Sleepy
- Talkative
- Tingly
- Uplifted

```
[https://med-cabinet-project.herokuapp.com/positive/happy](https://med-cabinet-project.herokuapp.com/positive/happy)

flavor:	  "Woody,Sweet,Diesel"
id:  	  1734
medical:  "Depression,Pain,Stress,Nausea,Headache,Headaches"
name:	  "Sweet Diesel"
negative: "Dizzy,Dry Mouth,Paranoid,Dry Eyes"
positive: "Relaxed,Happy,Energetic,Talkative,Uplifted"
type:  	  "sativa"
```

* "/flavors/<flavors>"

Users can query the database for specific flavors that they enjoy and will receive 5 different strains 
that come in that flavor. 

```
[https://med-cabinet-project.herokuapp.com/flavors/earthy](https://med-cabinet-project.herokuapp.com/flavors/earthy)

	
flavor:	  "Earthy,Sweet,Citrus"
id:  	  782
medical:  "Depression,Pain,Stress,Fatigue,Headaches"
name:	  "Golden Goat"
negative: "Dizzy,Dry Mouth,Paranoid,Dry Eyes,Anxious"
positive:  "Relaxed,Euphoric,Happy,Energetic,Uplifted"
type:	
```

* "/query/<medical>/<medical>/<positive>"

Users are looking for more specific strains are able to query the database based on two medical symptoms 
and one positive effect they are looking to achieve. This query will return up to 5 strains if there are 
matches in the database. 

```
[https://med-cabinet-project.herokuapp.com/query/nausea/pain/happy](https://med-cabinet-project.herokuapp.com/query/nausea/pain/happy)

flavor:	  "Citrus,Flowery,Sweet"
id:	      1371
medical:  "Depression,Pain,Stress,Nausea,Headache,Fatigue"
name:	  "Pandora's Box"
negative: "Dizzy,Dry Mouth,Paranoid,Dry Eyes"
positive: "Euphoric,Happy,Creative,Energetic,Uplifted"
type:	  "sativa"

```


## Code Links

Below are links to resources used to create this project. 

* Datasets (https://github.com/Med-Cabinet-Project/DS/tree/master/web_app/stats_model/csv) 
cannabis.csv is a merged dataframe of both the strains.csv (csv created from the [Strains's API](http://strains.evanbusse.com/)) and the csv from [Kaggle](https://www.kaggle.com/kingburrito666/cannabis-strains). 

* Pickled models (https://github.com/Med-Cabinet-Project/DS/tree/master/web_app/stats_model/pickle_models)
These are the pickled dictionaries used for the home route and the strains route

* API (https://github.com/Med-Cabinet-Project/DS/tree/master/web_app)
This is where the code for creating the different endpoints can be located. 


## Testing
used curl to test that endpoints were able to retrieve correct information 
i.e. curl med-cabinet-project.herokuapp.com/query/pain/depression/happy

```
[{"flavor":"Berry,Earthy,Sweet","id":1370,"medical":"Depression,Insomnia,Pain,Stress,Lack of Appetite","name":"Panda OG","negative":"Paranoid,Anxious","positive":"Relaxed,Euphoric,Happy,Talkative,Focused","type":"hybrid"},{"flavor":"Citrus,Pine,Honey","id":1276,"medical":"Depression,Insomnia,Pain,Stress,Lack of Appetite,Headache","name":"Neptune Kush","negative":"Dizzy,Dry Mouth,Dry Eyes","positive":"Relaxed,Hungry,Happy,Uplifted,Giggly","type":"indica"},{"flavor":"Lemon,Citrus,Pine","id":973,"medical":"Depression,Pain,Stress,Nausea,Headache,Headaches","name":"Jack the Ripper","negative":"Dry Mouth,Paranoid,Dry Eyes,Anxious","positive":"Euphoric,Happy,Energetic,Talkative,Uplifted","type":"sativa"},{"flavor":"Sweet,Vanilla,Earthy","id":236,"medical":"Depression,Insomnia,Pain,Stress,Nausea","name":"Blissful Wizard","negative":"","positive":"Relaxed,Euphoric,Happy,Creative,Talkative","type":"hybrid"},{"flavor":"Citrus,Lemon,Earthy","id":870,"medical":"Depression,Pain,Stress,Lack of Appetite,Fatigue","name":"Harmony","negative":"Dizzy,Dry Mouth,Dry Eyes","positive":"Relaxed,Euphoric,Happy,Creative,Uplifted","type":"hybrid"}]
```