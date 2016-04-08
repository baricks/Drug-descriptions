import urllib
import json
import sys
import random

#make a function to strip each text
#make a function to get a random word
def randomize(lists):
    random_line = random.choice(lists)
    return random_line

#make a function to build the drug name
def druggie(name_starts, name_parts, name_endings):
    name_1 = randomize(name_starts)
    name_2 = randomize(name_parts).lower()
    name_3 = randomize(name_parts).lower()
    name_4 = randomize(name_endings)
    return name_1 + name_2 + name_3 + name_4

name = sys.argv[1]
word = sys.argv[2]
word_2 = sys.argv[3]
complete_disorder = word+" "+word_2

#build the url
url = "https://api.fda.gov/drug/event.json?api_key=eijdKy1R2alvbAxzgTnSQP9UOtPXMRJfTLZ0zIzS&search=patient.drug.drugindication:"+word+"&limit=25"

response = urllib.urlopen(url).read()
data = json.loads(response)

#build the drug name
i = random.randint(0, 25)
for drug in data['results'][i]['patient']['drug'][0]['openfda']['generic_name']:
    name_1 = drug[0:3]
    name_2 = drug[3:len(drug)]

name_parts = [name_1, name_2]

name_endings = list()
for line in open('name_endings.txt'):
    name_endings.append(line.strip())

name_starts = list()
for line in open('name_starts.txt'):
    name_starts.append(line.strip())

drug_name = druggie(name_starts, name_parts, name_endings)
#drug_name = randomize(name_starts) + randomize(name_parts).lower() + randomize(name_parts).lower() + randomize(name_endings)

#########################################################################

#drug-related adjectives
adjectives = list()
for line in open('drug_adj.txt'):
    adjectives.append(line.strip())

#descriptions
description_sentence = list()
for line in open('description.txt'):
    description_sentence.append(line.strip())

#body parts
body_parts = list()
for line in open('body_parts.txt'):
    body_parts.append(line.strip())

#first part of the syndrome phrase (i.e. disease-related adjectives)
syndrome_1 = list()
for line in open('syndrome.txt'):
    syndrome_1.append(line.strip())

#second part of the syndrome phrase
syndrome_2 = list()
for line in open('syndrome_2.txt'):
    syndrome_2.append(line.strip())

#adverbs
adverbs = list()
for line in open('adverbs.txt'):
    adverbs.append(line.strip())

#existing drugs
existing_drugs = list()
for line in open('existing_drugs.txt'):
    existing_drugs.append(line.strip())

#scientific fields
sciences = list()
for line in open('sciences.txt'):
    sciences.append(line.strip())

#side effects
side_effects = list()
for line in open('side_effects.txt'):
    side_effects.append(line.strip())

number = str(random.randint(0, 12))

print
print "Welcome to SmartPharmacist, " + name +"."
print
print "Based on our analysis of your condition, we would suggest you start with a low dosage of "+drug_name+" to treat your "+complete_disorder+"."
print
print drug_name+" is a "+randomize(adjectives)+" drug that is "+randomize(description_sentence)+" "+complete_disorder+" and "+randomize(syndrome_1)+" "+randomize(body_parts)+" "+randomize(syndrome_2)+"."
print
print "Suggested daily dosage is "+number+" pills a day taken orally, or rubbing the gel form of the drug on your "+randomize(syndrome_1)+" "+randomize(body_parts)+"."
print
print randomize(adverbs)+", individuals suffering from "+complete_disorder+" "+randomize(syndrome_2)+" were prescribed "+randomize(existing_drugs)+" and "+randomize(existing_drugs)+", but new advancements in the field of "+randomize(body_parts)+" "+randomize(sciences)+" has helped doctors better remedy this disorder."
print
print "Side effects of "+drug_name+" may include: "+randomize(side_effects)+", "+randomize(syndrome_1)+" "+randomize(body_parts)+", "+randomize(side_effects)+", "+randomize(side_effects)+", "+randomize(syndrome_1)+" "+randomize(body_parts)+", and "+randomize(side_effects)+"."
