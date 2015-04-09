import json

d = {"data":
        [{"name": "sameer"}
         ]
     }
print ('1 in dicionary form: ', d)

j1 = json.dumps (d)
print ('2 in JSON form created from dictionary: ', j1)

j2 = json.dumps ('{"data":[{"name": "sameer"}]}')
print ('3 in JSON created from string: ', j2)



