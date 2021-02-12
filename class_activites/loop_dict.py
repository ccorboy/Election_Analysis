counties_dict = {"Arapahoe": "422829", "Denver": "463353", "Jefferson": "432438"}

#get keys of a dict.
for county in counties_dict.keys():
    print(county)


# get values of a dict.
for voters in counties_dict.values():
    print(voters)


# dictionary_name[key] method
for county in counties_dict:
    print(counties_dict[county])




#get() method
for county in counties_dict:
    print(counties_dict.get(county))



#get key-value pairs of dictionary (items()method)
for key, value in counties_dict.items():
    print(key + " county has " + value + " registered voters.")




# get each dicitionary in a list of dicitonaries
voting_data = [{"county": "Arapahoe", "registered_voters": 422829}, {"county": "Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)


#get values from a list of dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)


#values only
for county_dict in voting_data:
    print(county_dict['registered_voters'])




#get keys only
for county_dict in voting_data:
    print(county_dict['county'])

# f-string with dict.
counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jeffereson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters. ")


for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")



# multiple f-strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (f"You received {candidate_votes:,} number of votes. " f"The total number of votes in the election was {total_votes:,}. " f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes. ")

print(message_to_candidate)