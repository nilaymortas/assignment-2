#!/usr/bin/env python
# coding: utf-8

# In[87]:


file_handle = open("/home/mortasn/shared_folder/MOBG2143/assignment_2/16s_database.fasta", 'r')
file_lines = file_handle.readlines()
file_handle.close()


# In[88]:


seq_id = []
sequence = ""
sequence_array = []

dict_seq_id_seq = {}

for line in file_lines:
    if ">" in line:
        seq_id.append(line)
    else:
        sequence += line

seq_id = [file_handle.replace("\n", "") for file_handle in seq_id]

sequence_array = [file_handle.replace("\n", "") for file_handle in sequence_array]


# In[89]:


stop_codons = ["UAG", "UAA", "UGA"]
start_codon = "AUG"

array_extracted = []
array_extracted2 = []

for sequence in sequence_array:
    
    start_codon_index = sequence.find(start_codon)
    stop_codon_index = sequence[start_codon_index:].find(stop_codon)

    # extracted_sequence dizisine start ve stop kodonları dahil
    #extracted_sequence2 dizisine start ve stop kodonları dahil değil
    extracted_sequence = sequence[start_codon_index:start_codon_index + stop_codon_index + 3]
    extracted_sequence2 = sequence[start_codon_index + 3:start_codon_index + stop_codon_index]
    
    array_extracted.append(extracted_sequence)
    array_extracted2.append(extracted_sequence2)


# In[90]:


save_coding_region = open(r'/home/mortasn/coding_region.fasta', 'w+')
save_coding_region.write(coding_region)
save_coding_region.close()


# In[91]:


seq_id_len = len(seq_id)
array_extracted2_len = len(array_extracted2)

min_len = min(seq_id_len, array_extracted2_len)

coding_region1 = str()

for k in range(min_len):
    coding_region1 = coding_region1+seq_id[k] + "\n" + array_extracted2[k] +"\n"


# In[92]:


coding_region_lengths = []

for i in array_extracted2:
    coding_region_lengths.append(len(i))


# In[93]:


sequence_identifiers = []

for identifier in seq_id:
    id = identifier.split(" ")[0]
    sequence_identifiers.append(id[1:])


# In[94]:


zip_iterator = zip(sequence_identifiers, coding_region_lengths)
dict_lengths = dict(zip_iterator)


# In[95]:


import pickle

f = open(r'/home/mortasn/lengths.pickle','wb')
pickle.dump(dict_lengths,f)
f.close()


# In[96]:


sequence_identifiers2 = []
domain_phylum_class = []

for seq_id in seq_id:
    id = seq_id.split(" ")
    sequence_identifiers2.append(id[1])

for sequence_id in sequence_identifiers2:
    three_fields = sequence_id.split(";")
    domain_phylum_class.append(three_fields[0:3])


# In[97]:


zip_iterator2 = zip(sequence_identifiers, domain_phylum_class)
dict_columns = dict(zip_iterator2)


# In[98]:


with open(r'/home/mortasn/dictionary.tsv', 'wt') as file:
    for k in range(len(sequence_identifiers)):
        argument1 = []
        
        argument1.append(sequence_identifiers[k])
        argument1.append(domain_phylum_class[k][0])
        argument1.append(domain_phylum_class[k][1])
        
        if len(domain_phylum_class[k]) > 2:
            argument1.append(domain_phylum_class[k][2])
        else:
            argument1.append("")
     
        line = "\t".join(argument1)
        file.write(line+"\n")

