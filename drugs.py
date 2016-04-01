import urllib
import json
import sys
import random

#user inputs (1) their name; and (2) their condition/disease.
name = sys.argv[1]
word = sys.argv[2]
word_2 = sys.argv[3]
complete_word = word+" "+word_2

#build the drug name
url = "https://api.fda.gov/drug/event.json?api_key=eijdKy1R2alvbAxzgTnSQP9UOtPXMRJfTLZ0zIzS&search=patient.drug.drugindication:"+word+"&limit=25"

response = urllib.urlopen(url).read()
data = json.loads(response)

i = random.randint(0,25)
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

drug_name = random.choice(name_starts) + random.choice(name_parts).lower() + random.choice(name_parts).lower() + random.choice(name_endings)

#drug-related adjectives
adjectives = list()
for line in open('drug_adj.txt'):
	adjectives.append(line.strip())
random_drug_adj = random.choice(adjectives)

#descriptions
description_sentence = list()
for line in open('description.txt'):
	description_sentence.append(line.strip())
random_description_sentence = random.choice(description_sentence)

#body parts
body_parts = list()
for line in open('body_parts.txt'):
	body_parts.append(line.strip())
random_body_part = random.choice(body_parts)
random_body_part_b = random.choice(body_parts)
random_body_part_c = random.choice(body_parts)
random_body_part_d = random.choice(body_parts)

#first part of the syndrome phrase (i.e. disease-related adjectives)
syndrome_1 = list()
for line in open('syndrome.txt'):
	syndrome_1.append(line.strip())
random_syndrome_1_a = random.choice(syndrome_1)
random_syndrome_1_b = random.choice(syndrome_1)
random_syndrome_1_c = random.choice(syndrome_1)
random_syndrome_1_d = random.choice(syndrome_1)

#second part of the syndrome phrase
syndrome_2 = list()
for line in open('syndrome_2.txt'):
	syndrome_2.append(line.strip())
random_syndrome_a = random.choice(syndrome_2)
random_syndrome_b = random.choice(syndrome_2)

#adverbs
adverbs = list()
for line in open('adverbs.txt'):
	adverbs.append(line.strip())
random_adverb = random.choice(adverbs).capitalize()

#existing drugs
existing_drugs = list()
for line in open('existing_drugs.txt'):
	existing_drugs.append(line.strip())
random_existing_drug_a = random.choice(existing_drugs).capitalize()
random_existing_drug_b = random.choice(existing_drugs).capitalize()

#scientific fields
sciences = list()
for line in open('sciences.txt'):
	sciences.append(line.strip())
random_science = random.choice(sciences)

#side effects
side_effects = list()
for line in open('side_effects.txt'):
	side_effects.append(line.strip())
random_side_effect_a = random.choice(side_effects)
random_side_effect_b = random.choice(side_effects)
random_side_effect_c = random.choice(side_effects)
random_side_effect_d = random.choice(side_effects)

number = str(random.randint(0,12))

print
print "Welcome to SmartPharmacist, " + name +"." 
print
print "Based on our analysis of your condition, we would suggest you start with a low dosage of "+drug_name+" to treat your "+complete_word+"."
print
print drug_name+" is a "+random_drug_adj+" drug that is "+random_description_sentence+" "+complete_word+" and "+random_syndrome_1_a+" "+random_body_part+" "+random_syndrome_b+"." 
print
print "Suggested daily dosage is "+number+" pills a day taken orally, or rubbing the gel form of the drug on your "+random_syndrome_1_d+" "+random_body_part_d+"."
print
print random_adverb+", individuals suffering from "+complete_word+" "+random_syndrome_a+" were prescribed "+random_existing_drug_a+" and "+random_existing_drug_b+", but new advancements in the field of "+random_body_part+" "+random_science+" has helped doctors better remedy this disorder."
print
print "Side effects of "+drug_name+" may include: "+random_side_effect_a+", "+random_syndrome_1_b+" "+random_body_part_b+", "+random_side_effect_b+", "+random_side_effect_c+", "+random_syndrome_1_c+" "+random_body_part_c+", and "+random_side_effect_d+"."




















