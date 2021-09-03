#!/usr/bin/env python3
import json

if __name__ == "__main__":

    with open("./config/zones.json", 'r') as f:
        zones_dict = json.load(f)

        for zone, dict_ in zones_dict.items():
            print(zone)        

            if not "parsers" in dict_.keys():
                print("##### No parsers")
            else:
                for parser in dict_["parsers"].keys():
                    print("-----%s"%(parser))

