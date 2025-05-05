from random import choice,choices,shuffle
import csv, json
itemList = {"book":["instructional tool","instruction manual","entertainment device","printed material","image holder","entertainment object"],
            "painting":["image holder","art object","culture tool"],
            "photograph":["image holder","culture tool","printed material","machine output"],
            "spoon":["technology object","entertainment object","scooping tool","dining tool"],
            "shovel":["technology object","construction tool","scooping tool"],
            "fork":["technology object","entertainment object","stabbing tool","dining tool"],
            "knife":["technology object","entertainment object","stabbing tool","dining tool","weapon device"],
            "sword":["technology object","entertainment object","stabbing tool","dining tool","weapon device"],
            "bucket":["technology object","construction tool","scooping tool","storage device"],
            "ball":["instructional tool","entertainment device","entertainment object","art object","culture tool"],
            "cup":["technology object","dining tool","storage device"]}
materialList ={"organic":["wood","cotton","fiber","bone","leather","ivory","carapace","wool","linen","papyrus"],
               "inorganic":["metal","stone","gold","silver","iron","steel","plastic","bronze","gemstones","quartz","copper","radioactive materials","plaster"],
               "technological":["film"]}
#in archeology organic = used to be alive, inorganic = never alive
class SpawnObj():
    def __init__(self):
        self.name:str = ""
        self.shape = ""
        self.color = ""
        self.purpose = ""
        self.sizeBase = ""
        self.size = {"height":"","weight":""}
        self.material = ""
        self.location = ""
        self.tags = []
        self.actual = ""
        self.model = ""#path
        self.neighbors = ""#knn?
    def __str__(self):
        return f"Item:\nA {self.color} {self.shape} made of {self.material}.\
        \nHeight: Approx {self.size["height"]}\
        \nWeight: Approx {self.size["weight"]}\n\
        Purpose: {self.purpose}"
    
#material determines color?

#bone includes teeth, carapace, fish scales)
#hide includes (includes skin, fur, hair, leather, sinew gut, etc.)
#hr: Artifactual (any artifacts made from human remains)
# hr: Mummified (includes fortuitous desiccation) 
#Osteological human bones
#Ceramic is fired. Clay, Mud, and Soil are unfired.
#Add "see also"
materialList = {"animal":["antler","bone","coral","feather","hair","hide","horn","ivory","other","quill","shell"],
                "composite":["antler","artifactual","bone","ceramic","clay","coral","feather","fibers","glass","hair","hide","horn","ivory","metal","mud","mummified","osteological","other animal materials","other human remains","other mineral materials","other plant materials","paper","quill","reeds","shell","soil","stone","synthetic","unidentified","unknown","wood"],
                "human remains":["artifactual","mummified","osteological","other"],
                "mineral":["ceramic","clay","glass","metal","mud","other","soil","stone","synthetic"],
                "vegetal":["fibers","other","paper","reeds","wood"],
                "unidentified":["unidentified"]}
# Abrader = sander
category = ["apparel","tool","product"]
tagOpts = [
   ["protective equipment","medical equipment","combat equipment","textile equipment","recording equipment"],
   ["entertainment device","communication device","illumination device","transportation device","musical device","trapping device"],
   ["cultural item","stabbing item","scooping item","storage item","slashing item","decorative item"],
   ["dining tool","cutting tool","maker tool","prediction tool","investigative tool","launching tool"]]
objectHeader = ["category","name","materials","size","tags","purpose"]
sizeOpts = ["any","small","medium","large"]
# objectNames = []
apparelObjects = {
    "apron":{"materials":[("animal",["hide"]),("vegetal",["fibers","paper","reeds"]),("mineral",["synthetic"])],
             "size":[sizeOpts[0]],
             "purpose":"Often used to prevent unwanted splashing.",
             "tags":[tagOpts[0][1],tagOpts[0][0],tagOpts[3][4],tagOpts[3][0]]},
    "belt":{"materials":[("animal",["hide","shell","ivory","bone"]),("composite",["hide","metal"]),("human remains",["artifactual"]),("mineral",["ceramic","metal","synthetic"]),("vegetal",["fibers","reeds","wood"])],
            "size":[sizeOpts[1],sizeOpts[2]],
            "purpose":"Tool used in both technology and apparel to provide tension. In some cultures, unconventionally large versions were used as a reward for prowess on the battlefield.",
            "tags":[tagOpts[0][2],tagOpts[2][3],tagOpts[2][0],tagOpts[2][5]]},
    "bracelet":{"materials":[("animal",["bone","coral","feather","hair","hide","ivory","shell"]),("composite",["fibers","ceramic"]),("mineral",["ceramic","glass","metal","stone","synthetic"]),("vegetal",["fibers","paper","wood"])],
            "size":[sizeOpts[1]],
            "purpose":"An apparel item that humans often placed on their upper extremities for decorative purposes.",
            "tags":[tagOpts[0][0],tagOpts[2][0],tagOpts[2][5],tagOpts[1][0]]},
        "blouse / shirt":{"materials":[("animal",["feather","hair","hide"]),("composite",["synthetic","fibers"]),("mineral",["synthetic"]),("vegetal",["fibers","paper","reeds","wood"])],
            "size":[sizeOpts[1],sizeOpts[2]],
            "purpose":"An apparel item that humans wore for protection from the elements. Formed from 4 holes.",
            "tags":[tagOpts[0][0],tagOpts[2][0],tagOpts[2][5],tagOpts[1][1]]},
        "bow, hair":{"materials":[("",[""])],
            "size":[sizeOpts[1]],
            "purpose":"A decorative item formed by combining loops and knots. Often used to secure and decorate hair.",
            "tags":[tagOpts[1][5],tagOpts[2][0],tagOpts[1][1],tagOpts[1][5]]},
        "hat, top":{"materials":[("vegetal",["other","others"]),("mineral",["synthetic"]),("animal",["other"])],
                "size":[sizeOpts[1]],
                "purpose":"An apparel item often used to protect the head. Often associated with formal occasions.",
                "tags":[tagOpts[0][0],tagOpts[2][5],tagOpts[2][0],tagOpts[1][0]]},
        "bow, tie":{"materials":[("vegetal",["other","fibers"]),("mineral",["synthetic"]),("animal",["other"])],
                "size":[sizeOpts[1]],
                "purpose":"An apparel item often used to secure the collar. Formed from loops and knots and often associated with formal occasions.",
                "tags":[tagOpts[2][0],tagOpts[1][0],tagOpts[1][5],tagOpts[2][5]]}
} #ceramic belt = sander?; purpose ref = WWE
toolObjects = {
   "axe":{"materials":[("animal",["antler","bone","ivory","shell"]),("composite",["wood","metal"]),("mineral",["ceramic","metal","synthetic","stone"])],
          "size":[sizeOpts[1],sizeOpts[2]],
          "purpose":"Versatile tool used in combat and for resource gathering",
          "tags":[tagOpts[0][2],tagOpts[2][4],tagOpts[3][1],tagOpts[3][2]]},
    "arrow":{"materials":[("animal",["bone","coral"]),("composite",["wood","feather","stone"]),("mineral",["ceramic","glass","metal","stone","synthetic"])],
             "size":[sizeOpts[1]],
             "purpose":"Often used as a combat tool or to illustrate a point.",
             "tags":[tagOpts[0][2],tagOpts[1][1],tagOpts[2][1],tagOpts[2][0]]},
    "awl":{"materials":[("animal",["horn","ivory","quill"]),("composite",["metal","wood"]),("mineral",["metal"]),("vegetal",["wood"])],
           "size":[sizeOpts[1]],
           "purpose":"Tool used to put holes in fabric.",
           "tags":[tagOpts[2][0],tagOpts[2][1],tagOpts[3][2],tagOpts[0][3]]},
    "bag":{"materials":[("animal",["hair","hide","shell"]),("composite",["hide","metal","ceramic","synthetic"]),("mineral",["synthetic"]),("vegetal",["fibers","paper"])],
           "size":[sizeOpts[1],sizeOpts[2]],
           "purpose":"Versatile storage device. Occasionaly used to denote social standing.",
           "tags":[tagOpts[2][5],tagOpts[1][3],tagOpts[2][0],tagOpts[2][3]]},
    "ball":{"materials":[("animal",["hide"]),("composite",["fibers","synthetic","wood"]),("mineral",["ceramic","glass","stone","synthetic"]),("vegetal",["fibers","paper","wood"]),("unidentified",["unidentified"])],
            "size":[sizeOpts[0]],
            "purpose":"Spherical object with many cultural and technological applications.",
            "tags":[tagOpts[1][0],tagOpts[2][0],tagOpts[2][5],tagOpts[3][2]]},
    "basket":{"materials":[("vegetal",["fibers","reeds","wood"]),("mineral",["synthetic"])],
              "size":[sizeOpts[1],sizeOpts[2]],
              "purpose":"Storage tool for light cargo. Often decorative.",
              "tags":[tagOpts[1][3],tagOpts[2][0],tagOpts[2][3],tagOpts[2][5]]},
    "band, rubber":{"materials":[("mineral",["synthetic","other"]),("vegetal",["other","wood"])],
                    "size":[sizeOpts[1]],
                    "purpose":"Useful tool for securing bundles of small items.",
                    "tags":[tagOpts[1][3],tagOpts[1][0],tagOpts[2][3],tagOpts[3][2]]},
    "beaker":{"materials":[("mineral",["glass","synthetic"])],
              "size":[sizeOpts[1]],
              "purpose":"Storage item often used by human researchers.",
              "tags":[tagOpts[0][1],tagOpts[2][0],tagOpts[2][3],tagOpts[3][4]]},
    "bowl":{"materials":[("animal",["bone","ivory","shell","hide"]),("mineral",["ceramic","glass","metal","stone","synthetic"]),("vegetal",["paper","fibers","wood"])],
            "size":[sizeOpts[0]],
            "purpose":"Versatile item often used for dining, storage, and decoration.",
            "tags":[tagOpts[2][0],tagOpts[2][3],tagOpts[2][5],tagOpts[3][0]]},
        "caltrops":{"materials":[("animal",["bone","quill","shell"]),("mineral",["ceramic","glass","metal","stone","synthetic"])],
            "size":[sizeOpts[1]],
            "purpose":"A weapon thrown on the ground to deter persuers or ambush travelers. Often scattered on roadways.",
            "tags":[tagOpts[0][2],tagOpts[0][0],tagOpts[2][1],tagOpts[1][5]]},
        "caltrops, LEGO":{"materials":[("mineral",["synthetic"])],
            "size":[sizeOpts[1]],
            "purpose":"A toy version of a weapon thrown on the ground to deter persuers or ambush travelers. Often scattered in resting locations or assembled into unique shapes. Effectiveness of this device's role in heightening pain tolerance and perception is unknown",
            "tags":[tagOpts[0][2],tagOpts[0][0],tagOpts[2][0],tagOpts[3][2]]},
        "bow, weapon":{"materials":[("composite",["hide","wood","fibers"]),("mineral")],
            "size":[sizeOpts[1],sizeOpts[2]],
            "purpose":"A weapon used to throw projectiles far distances. Two handed device.",
            "tags":[tagOpts[0][2],tagOpts[3][5],tagOpts[2][0],tagOpts[1][0]]},
        "box":{"materials":[("composite",["fibers","synthetic"]),("vegetal",["fibers","paper","wood"]),("mineral",["ceramic","glass","metal","synthetic"])],
            "size":[sizeOpts[0]],
            "purpose":"A storage tool usually comprised of 6 sides when closed. May open and close through the use of flaps or a removable side.",
            "tags":[tagOpts[2][3],tagOpts[1][3],tagOpts[2][0],tagOpts[1][5]]},
        "box, decorative":{"materials":[("composite",["fibers","synthetic","paper"]),("vegetal",["fibers","paper","wood"])],
            "size":[sizeOpts[0]],
            "purpose":"A storage tool usually comprised of 6 sides when closed. May open and close through the use of flaps or a removable side. Actual dimensions and contents are often hidden to create an entertainment device.",
            "tags":[tagOpts[2][3],tagOpts[2][0],tagOpts[1][0],tagOpts[2][5]]}
}
#add labrynth ref if glass ball
productObjects = {
   "antler artifact":{"materials":[("animal",["antler"])],
                      "size":[sizeOpts[0]],
                      "purpose":"Decorative item popular with human resource gatherers. Wall mounted object.",
                      "tags":[tagOpts[1][1],tagOpts[2][0],tagOpts[0][2],tagOpts[2][5]]},
    "bead":{"materials":[("animal",["bone","coral","hide","horn","ivory","shell"]),("human remains",["artifactual"]),("mineral",["ceramic","glass","metal","stone","synthetic"]),("vegetal",["fibers","reeds","wood"])],
            "size":[sizeOpts[1]],
            "purpose":"Decorative item often used when creating apparel. Generally stored in multiples.",
            "tags":[tagOpts[0][3],tagOpts[2][0],tagOpts[2][5],tagOpts[3][2]]},
    "bell":{"materials":[("mineral",["metal"])],
            "size":[sizeOpts[0]],
            "purpose":"Instrument and cultural item often used to decorate apparel.",
            "tags":[tagOpts[2][5],tagOpts[1][0],tagOpts[2][0],tagOpts[3][2]]},
    "disk, coin":{"materials":[("mineral",["metal"])],
            "size":[sizeOpts[1]],
            "purpose":"A highly significant - but common - cultural disk used in commerce.",
            "tags":[tagOpts[1][1],tagOpts[2][0],tagOpts[1][3],tagOpts[0][0]]},
        "blanket":{"materials":[("animal",["hair","hide","quill","shell","feather"]),("composite",["fibers","hide"]),("mineral",["synthetic"]),("vegetal",["fibers","paper","reeds","other"])],
            "size":[sizeOpts[0]],
            "purpose":"Cultural item usually used for warmth and decoration. Often found in locations set apart for resting.",
            "tags":[tagOpts[0][0],tagOpts[2][0],tagOpts[2][3],tagOpts[2][5]]},
        "bow, decorative":{"materials":[("animal",["hide"]),("composite",["metal","fibers","synthetic"]),("mineral",["synthetic"]),("vegetal",["fibers","paper","reeds","wood"])],
            "size":[sizeOpts[0]],
            "purpose":"A decorative item formed by combining loops and knots. Often used to secure and seal storage containers",
            "tags":[tagOpts[0][3],tagOpts[2][1],tagOpts[2][5],tagOpts[3][2]]},
        "chest, tooth fairy":{"materials":[("composite",["synthetic","human remains","bone"])],
                "size":[sizeOpts[1]],
                "purpose":"A very small decorative storage device used to ceremonially store small bones shed by prepubecient humans during the growth stage.",
                "tags":[tagOpts[2][0],tagOpts[2][3],tagOpts[1][3],tagOpts[1][5]]},
        "chest":{"materials":[("vegetal",["wood"]),("composite",["metal","wood","fibers"])],
                "size":[sizeOpts[0]],
                "purpose":"A storage device popularized in the pre-flight era of humanity. Smaller versions were later adapted to be used for travel.",
                "tags":[tagOpts[2][3],tagOpts[2][0],tagOpts[2][5],tagOpts[1][3]]},
        "disk, compact (CD)":{"materials":[("mineral",["metal","synthetic"])],
                "size":[sizeOpts[1]],
                "purpose":"A round storage device for digital information. Often used for preserving music.",
                "tags":[tagOpts[0][4],tagOpts[1][1],tagOpts[2][3],tagOpts[1][0]]},
        "disk, floppy":{"materials":[("mineral",["synthetic","metal"])],
                "size":[sizeOpts[1]],
                "purpose":"A quadrilateral storage device for digital information. Originally used for storing executable code. Culturally used as a save icon.",
                "tags":[tagOpts[0][4],tagOpts[1][3],tagOpts[2][3],tagOpts[3][4]]},
        "cassette, video":{"materials":[("mineral",["synthetic","metal"])],
                "size":[sizeOpts[1]],
                "purpose":"A quadrilateral storage device for digital information. Often used for recording visual information.",
                "tags":[tagOpts[0][4],tagOpts[1][3],tagOpts[2][3],tagOpts[2][0]]},
        "cassette, compact":{"materials":[("mineral",["synthetic","metal"])],
                "size":[sizeOpts[1]],
                "purpose":"A quadrilateral storage device for digital information. Often used for recording audio information.",
                "tags":[tagOpts[0][4],tagOpts[2][3],tagOpts[1][5],tagOpts[2][0]]}
}
counterItem = 0
outPath = "assets/itemOpts.json"
outPathCSV = "assets/itemOpts.csv"
jsonPrep = {}
for listObj in range(3):
    objectType = None
    if listObj == 0:
        objectType = "Apparel"
        listObj = apparelObjects
    elif listObj == 1:
        objectType = "Tool"
        listObj = toolObjects
    elif listObj == 2:
        objectType = "Product"
        listObj = productObjects
    else:
        print("Error accessing list")
    for k, v in listObj.items():
        # v["materials"]
        # v["size"]
        # v["purpose"]
        # v["tags"]
        v["objectType"] = objectType
        v["modelLink"] = None
        v["screenShotLink"] = None
        v["relatedItems"] = []
        jsonPrep[k] = v
        counterItem += 1
print(counterItem)

with open(outPath,"w") as jsonFile:
    json.dump(jsonPrep,jsonFile)
with open(outPathCSV,"w") as csvFile:
    writeObj = csv.writer(csvFile,dialect="excel")
    header = ["itemName","materials","size","purpose","tags","objectType","modelLink","screenShotLink","relatedItems"]
    header = ["itemName","itemContent","modelLink","screenShotLink"]
    writeObj.writerow(header)
    for k, v in jsonPrep.items():
        ContentBlurb = f"PURPOSE: {v["purpose"]}\nSIZE(S): {v["size"]}\nTAGS: {v["tags"]}\nOBJECT TYPE: {v["objectType"]}\nRELATED ITEMS: {v["relatedItems"]}"
        writeObj.writerow([k,ContentBlurb,v["modelLink"],v["screenShotLink"]])


#whatever gets tagged "decorative box" is used on "boxes" in the main area for Christmas and game anniversary; 
#whatever gets tagged "floppy disk" silouette replaces the save icon

# "item":{"materials":[("",[""])],
#             "size":[sizeOpts[]],
#             "purpose":"",
#             "tags":[tagOpts[][],tagOpts[][],tagOpts[][],tagOpts[][]]},



# Bottle
# Brush # Blank, Disk #Disk
# Buckle # Building Material # Cord # Button 
# Cane 
# Cord/Bead 
# Cordage 
# Core # Cauldron # Chisel 
# Chopper # Cleaver 
# Club 
# Colander  Container 
# Comb 
# Crystal
# Cup 
# Cylinder 
#  # Die # Dipper  Dish 
# Disk 
# Drill # Effigy, Animal 
# Effigy, Bird 
# Effigy Jar, Horned Lizard # Flute 
# Gaming Piece # Figurine # Guard, Wrist (watch)
# Hairpin  Handle # Hoe 
# Hook 
# Hoop 
# Human Remains 
# Ivory Artifact 
# Jar # Knife  Knot Ladder 
# Ladle Lamp 
# Leather Artifact # Loom Anchor 
# Loop  Mat Maul 
# Medal 
# Medicine Box 
# Medicine Stone Mug 
# Nail 
# Necklace 
# Necklace/Bracelet 
# Needle 
# Net #Pad 
# Paddle  
# Palette 
# Patch 
# Pebble 
#  Peg 
# Pendant  Pick  Pigment 
# Pipe 
# Pitcher 
# Pitcher, Effigy 
# Plank 
# Plaque 
# Plate # Poncho 
# Pot, Bird  Pouch and Contents # Quiver # Rattle 
# Raw Material 
# Ring  Robe Sandal # Sandal/Cord 
# Saucer # Scoop # Scraper  Shawl 
# Shell 
# Sherd Artifact (broken pottery or glass) 
# Shovel Blade # Sinker 
# Slab 
# Sled Runner 
# Sling 
# Snare # Sock  Spindle  Spoon 
# Stone Artifact 
# Stone, Polishing 
#  Textile 
# Textile Artifact/Plaster Cast 
# Thread 
# Throwing Stick # Toggle 
# Tooth Artifact 
# Tooth Fragment 
# Torch 
# Tray 
# Tube Unidentified Artifact 
# Vase 
# Vegetal Artifact 
# Vegetal Material 
# Vessel 
# Vessel, Effigy 
# "Weaving Stick"
# "Whetstone"
# "Whistle"
# "Wig/Cord" 
# "Winged Object"
# "Wood Artifact"
# "Wristlet"
# "Yarn"
# "Yarn/Cord"
# instruments


#rival factions also in location looking for minerals / riches / quartz / food / burnable materials




