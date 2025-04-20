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
        self.size = {"height":"","weight":""}
        self.material = ""
        self.location = ""
        self.tags = []
        self.actual = ""
        self.neighbors = ""#knn?
    def __str__(self):
        return f"Item:\nA {self.color} {self.shape} made of {self.material}.\
        \nHeight: Approx {self.size["height"]}\
        \nWeight: Approx {self.size["weight"]}\n\
        Purpose: {self.purpose}"
    
#material determines color?
tagOpts = {"device": ["technological","cultural","instructional"]}
#bone includes teeth, carapace, fish scales)
#hide includes (includes skin, fur, hair, leather, sinew gut, etc.)
#hr: Artifactual (any artifacts made from human remains)
# hr: Mummified (includes fortuitous desiccation) 
#Osteological human bones
#Ceramic is fired. Clay, Mud, and Soil are unfired.
materialList = {"animal":["antler","bone","coral","feather","hair","hide","horn","ivory","other","quill","shell"],
                "composite":["antler","artifactual","bone","ceramic","clay","coral","feather","fibers","glass","hair","hide","horn","ivory","metal","mud","mummified","osteological","other animal materials","other human remains","other mineral materials","other plant materials","paper","quill","reeds","shell","soil","stone","synthetic","unidentified","unknown","wood"],
                "human remains":["artifactual","mummified","osteological","other"],
                "mineral":["ceramic","clay","glass","metal","mud","other","soil","stone","synthetic"],
                "vegetal":["fibers","other","paper","reeds","wood"],
                "unidentified":["unidentified"]}
# Abrader = sander


objectNames = {"abrader":{"modern":"sander","material":["mineral",("animal":"bone")],"purpose":"Long ago this tool was used to make items look more worn. This in some cultures made the human appear more desireable. Less frequently, versions of this tool were used to enpointify other tools. Recent studies suggest that these use-cases often had an inverse relationship throughout human history."},
"Adobe 
Adze Blade 
Adze Head 
Antler Artifact 
Apache Tear 
Apron 
Armor Slat 
Arrow 
Arrow Foreshaft 
Arrow Shaft 
Atlatl 
Atlatl Foreshaft 
Atlatl Shaft 
Awl 
Axe 
Bag 
Bag Handle 
Bag, Apron 
Bag, Awl 
Bag, Pipe 
Ball 
Band 
Basket 
Basket, Burden 
Basketry Fragment 
Basketry Fragment, Cord  
Basketry Fragment, Sherd  
Baton 
Batten 
Bead 
Beaker 
Beam 
Beamer 
Bell 
Belt 
Biface 
Blade 
Blank 
Blank, Disk 
Blanket 
Blouse 
Blubber Hook Prong 
Blubber Scraper 
Bola 
Bola Weight 
Bone Artifact 
Bottle 
Bottle, Water Bow 
Bow 
Bowl 
Bowl, Effigy 
Bowl, Rattle 
Bowl, Seed 
Bowl, Sherd 
Box 
Bracelet 
Brush 
Buckle 
Building Material 
Bull Roarer 
Bundle 
Bundle, Cord 
Burin 
Button 
Cane 
Cane Cigarette 
Canteen 
Canteen, Effigy 
Cauldron 
Censer 
Censer, Effigy 
Chisel 
Chopper 
Cigarette  
Clasp 
Clay Artifact 
Cleaver 
Club 
Colander 
Comb 
Concretion 
Container 
Coprolite 
Cord 
Cord/Bead 
Cordage 
Core 
Core, Chopper 
Core, Hammerstone 
Core Fragment 
Core/Microblade 
Core Tool 
Corn Husk Knot 
Corn Leaf Knot 
Cover 
Cover, Pot 
Cradle 
Cradle Board 
Cradle Board Belt  
Cradle Board Frame 
Crystal 
Cup 
Cylinder 
Dart, Atlatl  
Debitage 
Die 
Digging Stick 
Dipper 
Dipper Handle 
Dipper Sherd 
Discoid 
Discoid/Hammerstone 
Dish 
Disk 
Drill 
Endblade 
Effigy, Animal 
Effigy, Bird 
Effigy Jar, Horned Lizard 
Faunal Material 
Fetish 
Figurine 
Fire Drill 
Fire Drill Shaft 
Flake 
Flake, Retouched 
Flake Tool 
Flake, Utilized 
Flake, Waste 
Flaker 
Flesher 
Float 
Floral Material 
Flute 
Gaming Piece 
Gouge 
Gourd 
Gourd Jar 
Graver 
Grinding Slab 
Guard, Wrist 
Hairpin 
Hammerstone 
Handle 
Harpoon Foreshaft 
Harpoon Head 
Harpoon Part 
Harpoon Point 
Heddle Stick 
Hoe 
Hook 
Hoop 
Human Remains 
Ivory Artifact 
Jar 
Jar Base 
Jar, Cord 
Jar, Effigy 
Jar, Gourd 
Jar, Sherd  
Jar, Seed 
Jar, Seed, Bird Effigy 
Kiaha 
Kiaha Helping-stick 
Kilt 
Knife 
Knife Handle 
Knife, Tabular 
Knot 
Labret 
Ladder 
Ladle 
Ladle Rattle Handle 
Ladle, Effigy 
Lamp 
Leather Artifact 
Leister 
Lid 
Lime Container 
Line Weight 
Lintel 
Loom Anchor 
Loop 
Mano 
Mat 
Mat Fragment 
Mat/Basketry Fragment 
Mat/Cord 
Mattock Blade 
Maul 
Medal 
Medicine Box 
Medicine Stone 
Metate 
Microblade 
Moccasin 
Mug 
Nail 
Necklace 
Necklace/Bracelet 
Needle 
Needle Case 
Net 
Net Float 
Net, Burden 
Ojos de Dios 
Pad 
Paddle  
Palette 
Patch 
Pebble 
Pebble Tool 
Peg 
Pendant 
Pestle 
Pick 
Pick, Ice 
Pigment 
Pipe 
Pitcher 
Pitcher, Effigy 
Plank 
Plaque 
Plate 
Plate, Jar Base 
Plate, Legged 
Plate, Tripod 
Point, Bird 
Poncho 
Pot, Bird 
Pot Rest 
Pot Ring 
Pouch and Contents 
Prayer Feather 
Prayer Plume 
Prayer Stick 
Preform 
Projectile Point 
Punch 
Quid 
Quiver 
Rabbit Stick 
Rasp 
Rattle 
Raw Material 
Ring 
Ring Vessel 
Robe 
Robe/Belt 
Robe/Textile Fragment 
Rod 
Rope 
Rope/Cord 
Rope/Cord/Yarn 
Sample 
Sandal 
Sandal Last 
Sandal/Cord 
Saucer 
Scalp Lock 
Scat 
Scoop 
Scoop, Effigy 
Scraper 
Scraper, End 
Scraper, Side 
Seed Beater 
Shaft 
Shaft Smoother 
Shawl 
Shell 
Sherd Artifact 
Sherd Disc 
Sherd 
Sherd, Worked 
Shirt 
Shovel Blade 
Sinew Twister 
Sinker 
Slab 
Sled Runner 
Sling 
Snare 
Snare Stick 
Snowshoe 
Sock 
Soil 
Spall 
Spear Point 
Spindle 
Spindle Stick 
Spindle Whorl 
Split Twig Figurine 
Spoon 
Stone Artifact 
Stone, Polishing 
Stopper 
Strainer 
Strip 
Tablita 
Textile 
Textile Artifact/Plaster Cast 
Thread 
Throwing Stick 
Tinkler 
Toggle 
Tooth Artifact 
Tooth Fragment 
Torch 
Tray 
Tube 
Tumbler 
Tump Strap 
Ulu Blade 
Ulu Handle 
Unidentified Artifact 
Vase 
Vegetal Artifact 
Vegetal Material 
Vessel 
Vessel, Effigy 
"Weaving Stick"
"Whetstone"
"Whistle"
"Wig/Cord" 
"Winged Object"
"Wood Artifact"
"Wristlet"
"Yarn"
"Yarn/Cord"
"Yucca Knot"
"Yucca Knot/Raw Material"]