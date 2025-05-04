import csv,re,json

def load_gcbr() :
    # load GCBR names and regular expressions from the reference file (GCBRs.csv)
    # returns a list of dictionaries {"name","regex":[]}
    lg_gcbr_object = []
    with open("GCBRs.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter="\t")
        header_row = next(csv_reader)
        for line in csv_reader:
            resource_name = line[0]
            entry = {"name": resource_name,
                     "name_regex":re.compile("\\b" + resource_name + "\\b",re.IGNORECASE),
                     "acc_num_regex":[]}
            for i in range(1,len(line)) :
                entry["acc_num_regex"].append(re.compile("\\b"+line[i]+"\\b", re.IGNORECASE))
            lg_gcbr_object.append(entry)
    return lg_gcbr_object

def match_gcbr(text,gcbr_object) :
    # match all GCBR names and regular expressions in a text
    output = {"names":[],"accession_numbers":[]}
    for resource in gcbr_object :
        # GCBR names
        # regex strategy includes word boundaries and lowercasing
        if (re.search(resource["name_regex"],text)) :
            if (resource["name"] not in output["names"]) : # 
                output["names"].append(resource["name"])
        # GCBR accession numbers
        for acc_num_regex in resource["acc_num_regex"] :
            for acc_num in re.findall(acc_num_regex,text) :
                output["accession_numbers"].append(acc_num)
    return output


# load GCBR names and regex for accession numbers
gcbr = load_gcbr()
print("GCBR names and regex loaded")

# load collection
collection = []
with open("collection_sample.json","r",encoding = "utf-8") as file :
    collection = json.loads(file.read())
print("Collection loaded")

# match
results = []
print("Starting experiment")
for document in collection :
    print("\tprocessing",document["_id"])
    identified_mentions = match_gcbr(document["text"],gcbr)
    results.append({"docid":document["_id"],
                    "identified_mentions":identified_mentions})

# export
export_filename = "export.json"
with open(export_filename,"w",encoding="utf-8") as file :
    file.write(json.dumps(results,indent=2))
print("Results exported in",export_filename)
