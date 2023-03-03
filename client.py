def loadRequests(self):
        dicte = {}
        requests = open("location")

        # Header = Row 0. REMOVE [1:] IF FILE DOES NOT CONTAIN HEADER.

        lines = requests.readlines()[1:]

        for line in lines:
            

            # Parse line to words.
            line = line.replace("\n","")
            words = line.split(" ")
            #print(words)

            key = words[1]
            value = words[2]
            # Check if keyword found in words[0]
            # Assumption , can have similar value but must have different key.
            if ((words[0] == "put" or words[0] == "get")) and (key not in self.datastore):``
                  dicte[words[0]] = ()
                #self.datastore[key] = value
                #print("Key pair added "+ key + ":" + value)
            
            
            # Operation Key Value
            requests.close()
