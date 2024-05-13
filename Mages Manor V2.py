
#### THE ITEM ZONE ####

# function for checking if painting in room and description thereof (includes shrunken variant)
      
def paintingHere():
    if 'a fancy painting' in room2Contents:
        return "You see a fancy painting hanging at one end of the dining table."
    elif 'a shrunken fancy painting' in room2Contents:
        return "A tiny, postage stamp-sized painting hangs from a nail on the wall."
    else:
        return "There is a blank spot on the wall where a painting used to hang."

def paintingDesc():
    if 'a fancy painting' in room2Contents:
        print("It is a large painting of Milo the Mage in a solid gold frame. Talk about a selfie!")
    elif 'a shrunken fancy painting' in room2Contents:
        print("This painting of Milo has been shrunken down to the size of a postage stamp.")
    elif 'a shrunken fancy painting' in playerInv:
        print("""The painting you hold is a gold-framed portait of Milo The Mage.
You are essentially in possession of the world's fanciest wallet photo.""")
    else:
        print("""There is no painting in this room. Knowing you, you probably
stole it already.""")

# Function for checking if sword in room and description of sword

def swordHere():
    if 'an ancient sword' in room4Contents:
        return "You do, however, spot an ancient sword in the umbrella stand by the front door."
    else:
        return " "

def swordDesc():
    if playerLocation == 4 and 'an ancient sword' in room4Contents:
        print("""The sword has a gleaming silver handle inlaid with gems and its
razor-thin blade glows with a faint white light, like moonlight.""")
    elif 'an ancient sword' in playerInv:
        print("""The sword you carry has a gleaming silver handle inlaid with gems
and its razor-thin blade glows with a faint white light, like moonlight.""")
    elif 'a broken ancient sword' in playerInv:
        print("""Damn, you really goosed this thing, huh? Guess it was meant mostly for show. The hilt might still be worth something, at least.""")
    else:
        print("There's no sword here.")

# Function for checking if sleep spell is in room and description of sword

def sleepSpellHere():
    if 'a sleep spell' in room5DeskContents:
        print("""The desk is cluttered, but in the mess of papers and open ink pots you see a scroll containing the sleep spell.""")
    else:
        print("""You search the desk, but find nothing besides several notes from the
Larcenia Society of Arcanists saying Milo needs to pay his annual dues.""")

def sleepSpellDesc():
    if playerLocation == 5 and 'a sleep spell' in room5DeskContents:
        print("""It is a small scroll with magical runes carved on it that pulse with a faint golden
light. You suspect you could use the scroll to cast a sleep spell.""")
    elif 'a sleep spell' in playerInv:
        print("""You hold a small scroll with magical runes carved on it that pulse with a faint golden
light. You suspect you could use the scroll to cast a sleep spell.""")
    else:
        print("There is no sleep spell here.")

# Function for book Here and description
def bookHere():
    if 'Spell Scrolls For Dummies' in room5Contents:
        return """A copy of the classic arcane tome "Spell Scrolls For Dummies" rests on an end table
next to the chair."""
    else:
        return ""

# Function for book in study

def bookDesc():
    if 'Spell Scrolls For Dummies' in room5Contents:
        print("""This book is considered essential for mages of any level. Spell scrolls are, after all,
the easiest way to make magic accessible to the common layperson, as they allow that person to use a spell
one time by reading from the scroll. Spell scrolls are the bridge between arcanists and the world at large
(not to mention an excellent side hustle if you're a caster trying to make rent).""")
    elif 'Spell Scrolls For Dummies' in playerInv:
        print("""You hold Milo's copy of this book, which is considered essential for mages of any level.
Spell scrolls are, after all, the easiest way to make magic accessible to the common layperson, as they
allow that person to use a spell one time by reading from the scroll. Spell scrolls are the bridge between
arcanists and the world at large (not to mention an excellent side hustle if you're a caster trying
to make rent).""")
    else:
        print("There is no book here.")

# Function for Mirror
def mirrorHere():
    if 'a gold hand mirror' in room9Contents:
        return """A hand mirror with a polished gold frame and handle rests on the lip of the sink."""
    else:
        return ""

def mirrorDesc():
    if playerLocation == 9 and 'a gold hand mirror' in room9Contents:
        print("""The mirror has a gold handle and frame carved to resemble branches and flowers. It is
surely made by the dryad smiths of Hightree, given the quality and plant motifs.""")
    elif 'a gold hand mirror' in playerInv:
        print("""The mirror has a gold handle and frame carved to resemble branches and flowers. It is
surely made by the dryad smiths of Hightree, given the quality and plant motifs.""")
    else:
        print("There is no mirror here.")

# Function for Decanter
def decanterHere():
    if playerLocation == 14 and 'a crystal decanter' in room14Contents:
        return ("""and a crystal decanter on the table.""")
    else:
        return ""

def decanterDesc():
    if playerLocation == 14 and 'a crystal decanter' in room14Contents:
        print("""The decanter on the table refracts the light like a prism, each facet shining with a
different hue. There is no drink in it, but the decanter alone would fetch a high price.""")
    elif 'a gold hand mirror' in playerInv:
        print("""The decanter you hold refracts the light like a prism, each facet shining with a
different hue. There is no drink in it, but the decanter alone would fetch a high price.""")
    else:
        print("There is no decanter here.")

# SHRINK SPELL FUNCTIONS

def shrinkSpellHere():
    if playerLocation == 10 and 'a shrink spell' in room10LuggageContents:
        print("""The suitcase is full of robes, hats, and socks, all shrunken down to travel size,
no doubt to be un-shrunk later. Tucked into a pocket in the suitcase's lid is a scroll containing the runes for
a shrinking spell.""")
    else:
        print("""The suitcase is full of robes, hats, and socks, all shrunken down to travel size,
no doubt to be un-shrunk later.""")

def shrinkSpellDesc():
    if playerLocation == 10 and 'a shrink spell' in room10LuggageContents:
        print("""The scroll is made of fine white parchment. The runes for a shrinking spell are
inscribed upon the paper in glowing purple ink.""")
    elif 'a shrink spell' in playerInv:
        print("""This scroll is made of fine white parchment. The runes for a shrinking spell are
inscribed upon the paper in glowing purple ink.""")
    else:
        print("There is no spell scroll here.")

def burnSpellHere():
    if 'a burn spell' in room16Contents:
        print("""After rummaging around in the clutter of the attic for a little, you find a
scroll containing the burn spell.""")
    else:
        print("There is nothing worth stealing among the junk in the attic, not even some spare change.")

def burnSpellDesc():
    if 'a burn spell' in room16Contents:
        print("""The scroll is yellowed and tattered, but the ember-red runes written on the parchment still
glow with power.""")
    elif 'a burn spell' in playerInv:
        print("""The scroll you hold is yellowed and tattered, but the ember-red runes written on the parchment still
glow with power.""")
    else:
        print("""There is no spell scroll here.""")



def carpetDesc():
    if carpetFlipped == False:
        return "A long, blue carpet runs the length of the hallway."
    if carpetFlipped == True:
        if 'a note' in room8Contents:
            return "A long, blue carpet runs the length of the hallway. One end of it has been turned over to reveal a note."
        elif 'a note' not in room8Contents:
            return "A long, blue carpet runs the length of the hallway. One end of it has been turned over."

def flipCarpet():
    if carpetFlipped == False:
        print("You flip back one end of the carpet and find a hastily scribbled note beneath it.")
    elif carpetFlipped == True:
        if 'a note' in room8Contents:
            print("You've already turned over the carpet, there is a note beneath it.")
        else:
            print("You've already turned over the carpet. There is nothing else there.")

def noteDesc():
    if (playerLocation == 8) and ('a note' in room8Contents) and (noteVisible == True):
        print("""The note on the floor says:

Milo--
    If you're trying to remember where you put your burning spell, look to high places.
                                                            -- Milo
                                                            """)
    elif 'a note' in playerInv:
        print("""The note you hold says:

Milo--
    If you're trying to remember where you put your burning spell, look to high places.
                                                            -- Milo
                                                            """)
    else:
        print("What note? There's no note here. Why would there be a note here?")

def keyHere():
    if ('a silver key' in room13Contents) and ((mimicAlive == False) or (mimicShrunk == True)):
        return "A shining silver key is on the floor, covered in mimic slime."
    elif ('a silver key' in room13Contents) and ((mimicAlive == True) and (mimicSleep == True)):
        return "You see a glint of silver between the sleeping mimic's teeth."
    else:
        return ""

def keyDesc():
    if playerLocation == 13 and ('a silver key' in room13Contents) and (mimicAlive == False or mimicShrunk == True):
        print("""It is a simple silver key. Its head has been smithed to resemble a dragon's head. There are
traces of mimic slime on it.""")
    elif 'a silver key' in playerInv:
        print("""You hold a simple silver key. Its head has been smithed to resemble a dragon's head. There are
traces of mimic slime on it.""")
    else:
        print("There is no key here.")

def mimicHere():
    if mimicSeen == False:
        return "and a white birch chest sits next to it."
    elif mimicSeen == True and mimicAlive == True and mimicShrunk == False and mimicSleep == False:
        return "and a mimic disguised as a white birch chest sits next to it."
    elif mimicSeen == True and mimicAlive == True and mimicShrunk == True:
        return ""
    elif mimicSeen == True and mimicAlive == True and mimicSleep == True:
        return "and a mimic lies beside the bed, snoring peacefully."
    elif mimicSeen == True and mimicAlive == False:
        return "and the broken remains of a mimic lay next to it."
    else:
        return ""

def mimicDesc():
    if mimicSeen == False:
        print("""Upon studying the chest, it becomes clear that it is, in fact, a mimic DISGUISED as a chest. You should have guessed given most chests don't breathe.""")
    elif mimicSeen == True and mimicAlive == True and mimicShrunk == False and mimicSleep == False:
        print("""The mimic sits next Milo's bed, awaiting an unsuspecting person to open it. Either Milo somehow knows how to coax what items he needs from the mimic, or he just has a sick sense of humor. Possibly both.""")
    elif mimicSeen == True and mimicAlive == True and mimicShrunk == True:
        print("""The mimic is no longer here. It skittered under the bed after you shrank it to the size of a
mouse, remember?""")
    elif mimicSeen == True and mimicAlive == True and mimicSleep == True:
        print("""The mimic is out cold, thanks to that sleep spell. You can probably safely reach inside its
toothy maw now, if you're feeling lucky.""")
    elif mimicSeen == True and mimicAlive == False:
        if 'a silver key' in room13Contents:
            print("""The mimic's corpse lies on the bedroom's plush carpet. The smell coming from the remains will stay with you for many nights to come. You see a silver key among its remains.""")
        else:
            print("""The mimic's corpse lies on the bedroom's plush carpet. The smell coming from the remains will stay with you for many nights to come.""")
    else:
        print("""There is no mimic here""")

def mimic(action):
    if (("open" in action) or ("search" in action)) and ("chest" in action) and mimicSeen == False:
        print("""You grab hold of the chest's lid and flip it back, only to see a cavernous mouth lines with teeth and a forked tongue lashing back and forth. It is at this moment that you realize that the chest is, in fact, a mimic. This extra bit of knowledge does not make being devoured whole any more palatable though.""")
        mimicOutcome = 'eaten'
        return mimicOutcome
    elif (("open" in action) or ("search" in action) or ("reach inside" in action)) and (("chest" in action) or ("mimic" in action)) and mimicSeen == True:
        if mimicAlive == True and mimicSleep == False:
            print("""Whoa there, partner, I do believe we just established this here is a mimic. Tryin' to root around its innards while it's alive and kickin' is probably a bad idea. Don't ask my why I'm talkin' like a cowboy now.""")
        elif mimicAlive == True and mimicSleep == True:
            print("""You gingerly reach into the maw of the snoring mimic. You pull out a shining silver key, covered in mimic slime.""")
            mimicOutcome = 'key taken'
            return mimicOutcome
    elif (("take" in action) or ("get" in action)) and mimicSeen == False:
        print("""The chest is too big to carry with you.""")
    elif (("take" in action) or ("get" in action)) and mimicSeen == True:
        if mimicAlive == True:
            if mimicShrunk == True:
                print("""It's a nice thought, but you don't know where the mimic skittered off to after you made it pint-sized.""")
            elif mimicSleep == True:
                print("""While not actively a threat anymore, the mimic is still too large to carry.""")
            else:
                print("""Trying to pick up a live mimic would be like trying to pick up a rabid wolverine that also had acidic spit, i.e: ill-advised.""")
        else:
            print("""Why would you want to pick up a dead mimic? Ew.""")
    elif (("use" in action) or ("swing" in action)) and ("sword" in action):
        if 'a broken ancient sword' in playerInv:
            if mimicAlive == False or mimicShrunk == True:
                print("There is no mimic to attack.")
            elif mimicAlive == True and mimicShrunk == False:
                print("""The broken sword might make for a decent prison shiv, but its shattered blade is insufficient for mimic-slaying. The mimic chortles as you try to stab it with the broken sword before eating you whole.""")
                mimicOutcome = 'eaten'
                return mimicOutcome
        elif 'an ancient sword' in playerInv:
            if mimicAlive == False or mimicShrunk == True:
                print("There is no mimic to attack.")
            elif mimicAlive == True and mimicShrunk == False:
                print("""You swing your sword at the mimic. The sword's blade flashes bright white as it makes contact with the mimic's hide. When your vision clears, your sword's blade has shattered and the mimic lies in a charred heap on the floor. The light glints off a silver key lying among the remains.""")
                playerInv.remove('an ancient sword')
                playerInv.append('a broken ancient sword')
                mimicOutcome = 'mimic defeated'
                return mimicOutcome
        else:
            print("""You do not have a sword.""")
    elif "shrink" in action:
        if 'a shrink spell' in playerInv:
            print("""You read the shrinking spell written on the scroll. The mimic explodes in a puff of purple smoke. Once the smoke clears, you can see the mimic is now the size of a small mouse. For a moment it sits there on the carpet, trembling, before hacking up a silver key and skittering under Milo's bed.""")
            mimicOutcome = 'mimic shrunk'
            return mimicOutcome
        else:
            print("""You don't have a shrink spell.""")
    elif "burn" in action:
        if 'a burn spell' in playerInv:
            print("""You read the burn spell written on the scroll. A tendril of flame springs from the page and arcs toward the mimic, wreathing it in flame! When the flame dissipates, the mimic is a smoldering heap on the ground. The light glints off a silver key lying among the remains.""")
            mimicOutcome = 'mimic burned'
            return mimicOutcome
        else:
            print("""You don't have a burn spell.""")
    elif "sleep" in action:
        if 'a sleep spell' in playerInv:
            print("""You read the sleep spell written on the scroll. Motes of gold light rise off the page and fall upon the mimic. Within moments, it is fast asleep, snoring loudly. Its mouth opens with each snore, and you can see a glint of silver inside.""")
            mimicOutcome = 'mimic asleep'
            return mimicOutcome
        else:
            print("""You don't have a sleep spell.""")
    else:
        print("Please try another command!")

def crystalHere():
    if '''Milo's Crystal''' in room15Contents:
        return "At the far end of the hall, you see a crystal the size of your head resting on a marble pedestal."
    else:
        return "At the far end of the hall stands an empty marble pedestal."

def crystalDesc():
    if ('''Milo's Crystal''' in room15Contents) and (playerLocation == 15):
        print("""This is it. This is what you came for. The myriad facets of the crystal shimmer with colors that defy description.""")
    elif '''Milo's Crystal''' in playerInv:
        print("""You take out the crystal to examine it. Its myriad facets shimmer with colors that defy description. You can see why Milo would consider it a prize.""")
    else:
        print("""There is no crystal here.""")

def plantHere():
    if plantSeen == False:
        return """The base of the pedestal is enveloped in deep red vines."""
    elif plantSeen == True and plantAlive == True and plantShrunk == False:
        return """Bloodroot vines wrap around the base of the pedestal."""
    elif plantSeen == True and plantAlive == True and plantShrunk == True:
        return """Tiny vines no taller than a blade of grass grow at the base of the pedestal."""
    elif plantSeen == True and plantAlive == False:
        return """The mangled remains of the bloodroot vines lay around the pedestal."""
    else:
        return ""

def plantDesc():
    if plantSeen == False:
        print("""Taking a look at the vines, it becomes clear to you that these are bloodroot vines, a carnivorous breed of plant often grown for home defense.""")
    elif plantSeen == True and plantAlive == True and plantShrunk == False:
        print("""The vines wrap around the base of the pedestal and also spread out onto the floor around it. You know if you get too close, they will catch hold of you and wring the life out of you.""")
    elif plantSeen == True and plantAlive == True and plantShrunk == True:
        print("""The miniature vines lash at the air around them, though they are too small to be a threat.""")
    elif plantSeen == True and plantAlive == False:
        print("""The mangled remains of the vines are scattered on the floor around the pedestal. One or two pieces still twitch out of reflex.""")
    else:
        print("""There are no vines here.""")

def plant(action):
    if (("get" in action) or ("take" in action)) and (("crystal" in action) or ("gem" in action)) and plantSeen == False:
        print("""You step toward the pedestal and stretch a hand out to grab the crystal. As you do, one of the vines lashes out and takes hold of your wrist. Ah, you realize, these are bloodroot vines, a carnivorous plant commonly grown for home defense. The vines proceed to constrict you until your vision goes dark. They do not find a body.""")
        plantOutcome = 'strangled'
        return plantOutcome
    elif ((("get" in action) or ("take" in action)) and ("crystal" in action) or ("gem" in action)) and plantSeen == True:
        if plantAlive == True and plantShrunk == False:
            print('The part of your brain that likes being alive says, "Hmmmm, better not."')
        elif plantAlive == True and plantShrunk == True:
            plantOutcome = 'crystal taken'
            return plantOutcome
        elif plantAlive == False:
            plantOutcome = 'crystal taken'
            return plantOutcome
    elif (("take" in action) or ("get" in action)) and plantSeen == False:
        print("""The vines have a tight grip on the marble pedestal. Dislodging them would probably be more trouble than it's worth.""")
    elif (("take" in action) or ("get" in action)) and plantSeen == True:
        if plantAlive == True:
            if plantShrunk == True:
                print("""While tiny, you suspect trying to pick the miniature bloodroot vines would only result in bloody fingers.""")
            else:
                print("""I respect your horticultural ambitions, but I urge you to consider a different course of action.""")
        else:
            print("""What purpose would picking up dead murder-plant pieces serve? Please be serious.""")
    elif (("use" in action) or ("swing" in action)) and ("sword" in action):
        if 'a broken ancient sword' in playerInv:
            if plantAlive == False:
                print("There are no vines left to attack.")
            elif plantShrunk == True:
                print("This is a bad time to worry about trimming the grass, don't you think?")
            elif plantAlive == True and plantShrunk == False:
                print("""Your broken sword is lacking in reach, but the vines are not. They're, like, 99% reach, in fact. They use said reach to swat the broken sword out of your hand and proceed to constrict you.""")
                plantOutcome = 'strangled'
                return plantOutcome
        elif 'an ancient sword' in playerInv:
            if plantAlive == False:
                print("There are no vines left to use your sword on.")
            elif plantShrunk == True:
                print("""Using this enchanted, ancient sword to kill inch-high vines would be a little bit overkill. You wouldn't want to tarnish the blade, would you?""")
            elif plantAlive == True and plantShrunk == False:
                print("""You swing your sword at the vines. As the blade hits home, there is a flash of light and a hissing sound. When your vision clears, the vines lie in tatters around the pedestal and the blade of your sword is broken.""")
                playerInv.remove('an ancient sword')
                playerInv.append('a broken ancient sword')
                plantOutcome = 'plant defeated'
                return plantOutcome
        else:
            print("""You do not have a sword.""")
    elif "shrink" in action:
        if 'a shrink spell' in playerInv:
            print("""You read aloud from the scroll containing the shrink spell. Tendrils of purple smoke pour from the scroll and envelop the plant. When the smoke clears, the vines have shrunk and are only an inch tall, now looking more like highly discontented grass.""")
            plantOutcome = 'plant shrunk'
            return plantOutcome
        else:
            print("""You don't have a shrink spell.""")
    elif "burn" in action:
        if 'a burn spell' in playerInv:
            print("""You read from the scroll containing the burn spell. An arc of bright red flame shoots forth from the scroll and sears the plant. The plant's dessicated remains litter the floor.""")
            plantOutcome = 'plant burned'
            return plantOutcome
        else:
            print("""You don't have a burn spell.""")
    elif "sleep" in action:
        if 'a sleep spell' in playerInv:
            print("""You read from the scroll containing the sleep spell. Motes of gold light shower down upon the plant, but its vines continue to writhe menacingly. It occurs to you that plants don't actually need sleep.""")
            plantOutcome = 'plant still awake'
            return plantOutcome
        else:
            print("""You don't have a sleep spell.""")
    else:
        print("Please try another command!")

def atticDoorHere():
    if atticOpen == False:
        return "There is a closed attic door set into the ceiling, from which a cord hangs."
    if atticOpen == True:
        return "Above you is an open attic door with a ladder hanging down from it."

def atticDoor():
    if atticOpen == False:
        print("""You reach up and pull the cord connected to the attic door. The door swings open and a small ladder unfolds, leading up into darkness.""")
        return 'attic open'
    if atticOpen == True:
        print("""The attic door is already open, with the ladder hanging below it.""")

def hallDoor():
    if 'a silver key' in playerInv:
        print("""You use the silver key to unlock the door.""")
        return 'hall door unlocked'
    else:
        print("""You try to open the door to no avail.""")

def pianoHere():
    if 'a piano' in room3Contents:
        return "In the corner sits a large, ornate grand piano with gleaming ivory keys."
    elif 'a shrunken piano' in room3Contents:
        return "The miniature piano seems cartoonishly small compared to the rest of the furniture in the room."
    else:
        return ""

def pianoDesc():
    if ('a shrunken piano' in playerInv) or (('a shrunken piano' in room3Contents) and (playerLocation == 3)):
        print("""Even in miniature, the craftsmanship of this instruments shows through. You could probably unshrink it at a later date for sale or use.""")
    elif ('a piano' in room3Contents) and (playerLocation == 3):
        print("""The piano is expertly crafted and you suspect it would fetch a great sum if you could move the darn thing.""")
    else:
        print("""There is no piano here.""")
        
#### END ITEM ZONE ####

import webbrowser

def otherCmds():
    if action == ("inv" or "inventory"):
        inventoryCheck()
    elif (("look" in action) or ("examine" in action)) and ("sleep" in action) and (("spell" in action) or ("scroll" in action)):
        sleepSpellDesc()
    elif (("look" in action) or ("examine" in action)) and ("shrink" in action) and (("spell" in action) or ("scroll" in action)):
        shrinkSpellDesc()
    elif (("look" in action) or ("examine" in action)) and ("burn" in action) and (("spell" in action) or ("scroll" in action)):
        burnSpellDesc()
    elif (("look" in action) or ("examine" in action)) and (("spell" in action) or ("scroll" in action)):
        print("""Something tells you that you may want to be more specific about what spell or
scroll you're looking at. Try 'look <name> spell' or 'look <name> scroll'' instead""")
    elif (("look" in action) or ("examine" in action)) and ("mirror" in action):
        mirrorDesc()
    elif (("look" in action) or ("examine" in action)) and ("sword" in action):
        swordDesc()
    elif (("look" in action) or ("examine" in action)) and ("decanter" in action):
        decanterDesc()
    elif (("look" or "examine") in action) and ("painting" in action):
        paintingDesc()
    elif (("look" in action) or ("examine" in action) or ("read" in action)) and ("note" in action):
        noteDesc()
    elif (("examine" in action) or ("look" in action)) and ("key" in action):
        keyDesc()
    elif (("examine" in action) or ("look" in action) or ("read" in action)) and (("book" in action) or ("tome" in action)):
        bookDesc()
    elif (("examine" in action) or ("look" in action)) and ("piano" in action):
        pianoDesc()
    elif (("examine" in action) or ("look" in action)) and (("crystal" in action) or ("gem" in action)):
        crystalDesc()
    elif (action == "swing sword") or (action == "use sword"):
        swingSword()
    elif ("piano" in action) and ("play" in action):
        if ('a piano' in room3Contents) and (playerLocation == 3):
            print("You plink out a few notes on the piano.")
        elif ('a shrunken piano' in playerInv) or (('a shrunken piano' in room3Contents) and (playerLocation == 3)):
            print("""With some effort, you plink out a few notes on the tiny piano. At this size, the sound has a music-box quality to it.""")
        else:
            print("There is no piano here to play.")
    elif "shrink" in action:
        if "piano" in action:
            shrink('a piano')
        elif ("painting" in action) or ("portrait" in action):
            shrink('a fancy painting')
        else:
            print("""You get the feeling that this isn't the right place or time to use the shrinking spell.""")
    elif "archwiz" in action:
        if "wish" in action:
            print("Ask and ye shall receive!")
            playerInv.append('a burn spell')
            playerInv.append('a shrink spell')
            playerInv.append('a sleep spell')
            playerInv.append('a silver key')
            playerInv.append('an ancient sword')
    else:
        print("Please try another command!")
    

def dirFail():
    print("You can't go that way here!")

# FUNCTION for checking player's inventory. Prints message in response.

def inventoryCheck():
    if action == ("inv" or "inventory"):
        if playerInv == []:
            print("You have NOTHING!")
        else:
            print("INVENTORY: " + ", ".join(playerInv))
            if usedSpells == []:
                return
            else:
                print("\nUSED SPELLS: " + ", ".join(usedSpells))
            if calcScore() == 1:
                print("\nYou have found", calcScore(), "extra treasure.")
            else:
                print("\nYou have found", calcScore(), "extra treausres.")
    else:
        return

# Function for opening chest to look inside

def chestOpen(container):
    if container == []:
        print("You open it, but there is nothing inside.")
    else:
        print("Inside, you see" + item + ".")

# FUNCTION for trying to get an item. If item is in container, it removes from
# container's list and appends to player's inventory list. If item is NOT in
# container, prints response message.

def getItem(container,item):
    if item not in container:
        print("That item isn't here.")
    else:
        container.remove(item)
        playerInv.append(item)
        if item == 'an ancient sword':
            print("You attach the sword to your belt. This is one of the rumored treasures! Way to go!")
        elif item == 'a gold hand mirror':
            print("With careful hands, you pick up the mirror. This is one of the rumored treasures! Nicely done!")
        elif item == 'a crystal decanter':
            print("You consign the decanter to hammerspace. This is one of the rumored treasures! Bravo!")
        elif item == 'a shrunken fancy painting':
            print("You pocket the tiny, tiny painting. This is one of the rumored treasures! Well played!")
        elif item == '''Milo's Crystal''':
            print("""You carefully reach out and take Milo's crystal off of its pedestal. You found what you've came for! Now you just have to make it back out of the mansion.""")
        elif item == 'a shrunken piano':
            print("""While not what you came for, this miniature piano could be unshrunk at a later date, either for sale or use. You put it in your pocket.""")
        else:
            print("You pick up " + item + ".")

def shrink(item):
    if 'a shrink spell' in playerInv:
        if item == 'a piano' and playerLocation == 3: 
            print("""You read aloud from the spell scroll. The piano is consumed in a cloud of purple smoke. When it clears, you see it has shrunken down to the size of a deck of cards.""")
            room3Contents.remove('a piano')
            room3Contents.append('a shrunken piano')
            playerInv.remove('a shrink spell')
            usedSpells.append('a shrink spell')
        elif item == 'a fancy painting' and playerLocation == 2:
            print("""You read aloud from the spell scroll and watch as the painting shrinks down to the size of a postage stamp.""")
            room2Contents.remove('a fancy painting')
            room2Contents.append('a shrunken fancy painting')
            playerInv.remove('a shrink spell')
            usedSpells.append('a shrink spell')
        else:
            print("""You get the feeling that this isn't the right place or time to use the shrinking spell.""")
    else:
        print("You do not have a shrink spell.")

def swingSword():
    if 'an ancient sword' in playerInv:
        print("You swing the sword around in the air. Yes, you feel very cool.")
    else:
        print("You forgot your sword at home, remember?")

def calcScore():
    playerScore = 0
    if 'an ancient sword' in playerInv:
        playerScore = playerScore + 1
    if 'a shrunken fancy painting' in playerInv:
        playerScore = playerScore + 1
    if 'a gold hand mirror' in playerInv:
        playerScore = playerScore + 1
    if 'a crystal decanter' in playerInv:
        playerScore = playerScore + 1
    if 'a broken ancient sword' in playerInv:
        playerScore = playerScore + 0.5
    return playerScore

# initial statements to set things as they oughta be.

room1Contents = []
room2Contents = ['a fancy painting'] #painting Here and description functions done
room3Contents = ['a piano']
room4Contents = ['an ancient sword'] #sword functions done
room5Contents = ['Spell Scrolls For Dummies']
room5DeskContents = ['a sleep spell'] 
room8Contents = ['a note']
room9Contents = ['a gold hand mirror']
room10LuggageContents = ['a shrink spell']
room13Contents = ['a silver key']
room14Contents = ['a crystal decanter']
room15Contents = ['''Milo's Crystal''']
room16Contents = ['a burn spell']
usedSpells = []

def introText():
    print("""Welcome to Mage's Manor!

You are THE FORGETFUL THIEF, the most skilled thief in the city of LARCENIA. 
Your expertise for breaking and entering is matched only by your ability to 
FORGET ALL OF YOUR EQUIPMENT. You have just snuck into the manor of MILO THE 
MAGE,in search of the CRYSTAL that is his prize possession. You have, once 
again,forgotten all of your thieving tools at home, but the job must go on! 
Use what's in the manor to find the CRYSTAL and GET OUT THE WAY YOU CAME.

You've also heard rumors there are 4 OTHER TREASURES in the house. If you're
feeling bold, see if you can find them before leaving!

Would you like some instructions on how to play this game? (Y/N)

*****
""")
    action = input("> ")
    action = action.lower()
    if action == "y":
        tutorial()
    else:
        return

def tutorial():
    print("""This is a text-based adventure game. You interact with the world
by typing what you want to do and pressing enter. Some common commands are:

    GO <DIRECTION>, <DIRECTION>, or <FIRST LETTER OF DIRECTION>
        EX: 'go north', 'north', or 'n'
    LOOK
        Gives you a description of the room you're currently in.
        EX: 'look'
    LOOK <OBJECT> or EXAMINE <OBJECT>
        Gives you a detailed description of a specific item or object.
        EX: 'look piano' or 'examine piano' 
    TAKE <OBJECT> or GET <OBJECT>
        Pick up an object in the room.
        EX: 'take sword' or 'get sword'
    SEARCH <OBJECT>
        Closely examine an object to see if it holds anything else.
        EX: 'search chest'
    USE <OBJECT>
        Try to use a specific object, either in your inventory or in the room.
        EX: 'use sword'

There are other commands besides these, so don't hesitate to experiment!

***
""")

def areYouReady():
    print("Are you ready to begin? (Y/N)")
    action = input("> ")
    action = action.lower()
    if action == "y":
        return "y"
    if action == "n":
        print("Oh. Uhhh... I didn't really expect you so that. Have a nice day, I guess?")
        input("> ")

introText()
areYouReady()

#Flags relevant to player status
alive = True
playerInv = []
playerLocation = 1
roomRefresh = True
finishedGame = False

#Lots of environment flags, jeez.
carpetFlipped = False
atticOpen = False
burnVisible = False
sleepVisible = False
shrinkVisible = False
noteVisible = False
mimicAlive = True
mimicSeen = False
mimicShrunk = False
mimicSleep = False
plantAlive = True
plantSeen = False
plantShrunk = False
hallUnlocked = False

while (alive == True) and (finishedGame == False):

#ROOM 1 - KITCHEN
    while playerLocation == 1 and roomRefresh == True:
        print("""You stand in a cozy, well maintained kitchen. A window looks
out over a garden growing along the side of the house. In one corner is the
cellar door you used to sneak into the manor. There are doorways to the north
and south.""")
        roomRefresh = False
    while playerLocation == 1 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (action == "n") or ("north" in action):
            playerLocation = 2
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            playerLocation = 3
            roomRefresh = True
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        elif ("cellar" in action):
            if ('''Milo's Crystal''' in playerInv):
                finishedGame = True
                break
            else:
                print("You can't leave the mansion until you find Milo's Crystal, remember?")
        else:
            otherCmds()

# ROOM 2 - DINING ROOM
    while playerLocation == 2 and roomRefresh == True:
        print("""You are in a long dining room. The entire northern wall of
the dining room is stained glass windows depicting Milo's many magical mis-
adventures. The table is laid out with shining sets of flatware.""",paintingHere(),
"""Exits are west and south.""")
        roomRefresh = False
    while playerLocation == 2 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("take" or "get") in action) and ("painting" in action):
            if 'a fancy painting' in room2Contents:
                print("It's a nice painting, but it's too large to carry with you.")
            elif 'a shrunken fancy painting' in room2Contents:
                getItem(room2Contents,'a shrunken fancy painting')
            else:
                print("""There is no painting in this room. Knowing you, you probably
stole it already.""")
        elif (action == "w") or ("west" in action):
            playerLocation = 1
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            playerLocation = 4
            roomRefresh = True
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        else:
            otherCmds()

# ROOM 3 - PARLOR
    while playerLocation == 3 and roomRefresh == True:
        print("""You are in a parlor with plush red carpet and ornate wall-paper.
A soft-looking couch sits in front of a bank of windows looking out on the lawn.""",
pianoHere(),"""Exits are to the
north and east.""")
        roomRefresh = False
    while playerLocation == 3 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("take" or "get") in action) and ("piano"):
            if 'a piano' in room3Contents:
                print("You're a thief, not a mover. Think again.")
            elif 'a shrunken piano' in room3Contents:
                getItem(room3Contents,'a shrunken piano')
            else:
                print("There is no piano here.")
        elif (action == "n") or ("north" in action):
            playerLocation = 1
            roomRefresh = True
        elif (action == "e") or ("east" in action):
            playerLocation = 4
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            dirFail()
        else:
            otherCmds()

# ROOM 4 - FOYER
    while (playerLocation == 4 and roomRefresh == True) and ('an ancient sword' in room4Contents):
        print("""You stand in a large foyer with high ceilings. A large crystal chandelier hangs
overhead. A loft on the second floor looks down onto the foyer. You also see
doorways to the west and east. The manor's front door is at the south end of
the foyer, but it's probably best not to walk out the front carrying all your
loot.""",swordHere())
        roomRefresh = False
    while (playerLocation == 4 and roomRefresh == True) and ('an ancient sword' not in room4Contents):
        print("""You stand in a large foyer with high ceilings. A large crystal chandelier hangs
overhead. A loft on the second floor looks down onto the foyer. You also see
doorways to the west and east. The manor's front door is at the south end of
the foyer, but it's probably best not to walk out the front carrying all your
loot.""",swordHere())
        roomRefresh = False
    while playerLocation == 4 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif ("swing" in action) and ("chandelier" in action):
            print("I like where your heads at, but it's a little far up.")
        elif (("get" in action) or ("take" in action)) and "sword" in action:
            getItem(room4Contents,'an ancient sword')
        elif (action == "n") or ("north" in action):
            playerLocation = 2
            roomRefresh = True
        elif (action == "e") or ("east" in action):
            playerLocation = 6
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            print("""What did I just say about going out the front door? You just got out of the
clink a little while ago. You can't do another nickel.""")
        elif (action == "w") or ("west" in action):
            playerLocation = 3
            roomRefresh = True
        else:
            otherCmds()

# ROOM 5 - STUDY

    while playerLocation == 5 and roomRefresh == True:
        print("""You stand in Milo's study. A surprisingly unassuming desk is crammed into one
corner, and is stacked with a variety of papers and scrolls. The back wall of
the study is taken up by a vast fireplace. Embers still glow in the ash. A large
green armchair sits in front of the fireplace.""",bookHere(),"""The only exit is north.""")
        roomRefresh = False
    while playerLocation == 5 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("search" in action) or ("look" in action)) and ("desk" in action):
            sleepSpellHere()
        elif (("get" in action) or ("take" in action)) and (("spell" in action) or ("scroll" in action)):
            getItem(room5DeskContents,'a sleep spell')
        elif (("get" in action) or ("take" in action)) and (("book" in action) or ("tome" in action)):
            getItem(room5Contents,'Spell Scrolls For Dummies')
        elif (action == "n") or ("north" in action):
            playerLocation = 6
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        else:
            otherCmds()

# ROOM 6 - F1 STAIRCASE

    while playerLocation == 6 and roomRefresh == True:
        print("""This narrow hall consists of a set of stairs leading up to the second floor, a
doorway to the west, and a heavy oak door to the south. A liminal space, if
there ever was one.""")
        roomRefresh = False
    while playerLocation == 6 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        elif (action == "s") or ("south" in action):
            playerLocation = 5
            roomRefresh = True
        elif (action == "w") or ("west" in action):
            playerLocation = 4
            roomRefresh = True
        elif ("up" in action) or (action == "use stairs" or action == "climb stairs"):
            playerLocation = 7
            roomRefresh = True
        else:
            otherCmds()

# ROOM 7 - F2 STAIRCASE
#Potential commands: "slide staircase" "fall down staircase" "slide railing/bannister."

    while playerLocation == 7 and roomRefresh == True:
        print("""You are on the second-floor landing at the top of the staircase.
There is an open archway to the west and a wooden door to the south.""")
        roomRefresh = False
    while playerLocation == 7 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "s") or ("south" in action):
            playerLocation = 8
            roomRefresh = True
        elif (action == "w") or ("west" in action):
            playerLocation = 12
            roomRefresh = True
        elif (action == "e") or ("east" in action):
            dirFail()
        elif ("down" in action) or (action == "use stairs" or action == "climb stairs" or action == "climb down stairs" or action == "go downstairs"):
            playerLocation = 6
            roomRefresh = True
        else:
            otherCmds()
        

# ROOM 8 - SIDE CORRIDOR
#Potential Cmds: lift carpet, get note

    while playerLocation == 8 and roomRefresh == True:
        print("""You stand in a small corridor with several rooms shooting off
of it.""",carpetDesc(),"""There are doors to the north, east, south, and west.""")
        roomRefresh = False
    while playerLocation == 8 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("flip" in action) or ("search" in action) or ("move" in action)) and (("carpet" in action) or ("rug" in action)):
            if carpetFlipped == False:
                flipCarpet()
                carpetFlipped = True
                noteVisible = True
            else:
                flipCarpet()
        elif (("take" in action) or ("get" in action)) and ("note" in action):
            if noteVisible == False:
                print("You don't see any note here.")
            elif noteVisible == True:
                getItem(room8Contents,'a note')
        elif (action == "n") or ("north" in action):
            playerLocation = 7
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            playerLocation = 10
            roomRefresh = True
        elif (action == "w") or ("west" in action):
            playerLocation = 11
            roomRefresh = True
        elif (action == "e") or ("east" in action):
            playerLocation = 9
            roomRefresh = True
        else:
            otherCmds()

# ROOM 9 - BATHROOM
#potential commands: turn on tub,look mirror,take bath,take/look/examine mirror.

    while playerLocation == 9 and roomRefresh == True:
        print("""You are in a bathroom. The floor is made of gleaming white tiles
and the wallpaper shows images of birds in flight. A large, clawfoot tub takes
up one side of the room. Beside it is a marble sink with brass fittings.""",mirrorHere(),"""The
only exit is west.""")
        roomRefresh = False
    while playerLocation == 9 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("take" in action) or ("get" in action)) and ("mirror" in action):
            getItem(room9Contents,'a gold hand mirror')
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            playerLocation = 8
            roomRefresh = True
        elif (action == "e") or ("east" in action):
            dirFail()
        else:
            otherCmds()

# ROOM 10 - GUEST ROOM
#potential commands:look suitcase,open suitcase,take suitcase,look window (good opportunity for a city description here...)

    while playerLocation == 10 and roomRefresh == True:
        print("""You stand in the manor's guest room. A window looks out over
the front yard and the street. The bed's sheets and blankets are rumpled, like
someone has been sleeping here. In the corner you see a luggage rack with a
brown leather suitcase on it. There is a door to the north.""")
        roomRefresh = False
    while playerLocation == 10 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("search" in action) or ("look" in action)) and (("suitcase" in action) or ("luggage" in action)):
            shrinkSpellHere()
        elif (("get" in action) or ("take" in action)) and (("spell" in action) or ("scroll" in action)):
            getItem(room10LuggageContents,'a shrink spell')
        elif (action == "n") or ("north" in action):
            playerLocation = 8
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        else:
            otherCmds()

# ROOM 11 - LINEN CLOSET
#potential commands: take towel, open attic door

    while playerLocation == 11 and roomRefresh == True:
        print("""This is a small walk-in linen closet, less than two
arms-lengths across. A variety of towels, linens, and rags clutter the shelves.""",atticDoorHere(),
"""The exit back out into the hall is east.""")
        roomRefresh = False
    while playerLocation == 11 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("open" in action) or ("pull" in action)) and (("door" in action) or ("cord" in action)):
            atticDoorOutcome = atticDoor()
            if atticDoorOutcome == 'attic open':
                atticOpen = True
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            playerLocation = 8
            roomRefresh = True
        elif ((action == "up") or ("climb" and "ladder" in action)) and (atticOpen == True):
            playerLocation = 16
            roomRefresh = True
        else:
            otherCmds()

# ROOM 12 - LOFT

    while playerLocation == 12 and roomRefresh == True:
        print("""You stand in the loft, which adjoins the various spaces of the
second floor. Looking out over the railing on the southern side of the lift
gives you a view of the chandelier and the foyer below. There are doors to the
west and north, and an open archway to the east.""")
        roomRefresh = False
    while playerLocation == 12 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (action == "n") or ("north" in action):
            if hallUnlocked == False:
                print("""You try the northern exit but the door is locked.""")
            if hallUnlocked == True:
                playerLocation = 15
                roomRefresh = True
        elif (("open" in action) or ("unlock" in action) or ("force" in action)) and ("door" in action):
            hallDoorOutcome = hallDoor()
            if hallDoorOutcome == 'hall door unlocked':
                hallUnlocked = True
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            playerLocation = 13
            roomRefresh = True
        elif (action == "e") or ("east" in action):
            playerLocation = 7
            roomRefresh = True
        elif (("swing" or "use") in action) and ("chandelier" in action):
            print("""Hell yeah. You jump over the loft's railing and grab hold of the chandelier. You swing from it for a moment before letting go and nimbly landing in the hall below.\n""")
            playerLocation = 4
            roomRefresh = True
        else:
            otherCmds()

# ROOM 13 - MASTER BEDROOM
#potential commands:, sleep bed, look chest, look ceiling

    while playerLocation == 13 and roomRefresh == True:
        print("""This is the bedroom where Milo lays his pointy-hatted head. The ceiling is
painted blue-black and dotted with gold-leaf stars. A regal four-poster bed
takes up the center of the space,""", mimicHere(),keyHere(),
"""There are exits to the east and south.""")
        roomRefresh = False
    while playerLocation == 13 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("look" in action) or ("examine" in action)) and (("chest" in action) or ("mimic" in action)):
            mimicDesc()
            mimicSeen = True
        elif ("mimic" in action) or ("chest" in action):
            mimicOutcome = mimic(action)
            if mimicOutcome == 'eaten':
                alive = False
                break
            elif mimicOutcome == 'mimic defeated':
                mimicAlive = False
                mimicSeen = True
            elif mimicOutcome == 'mimic shrunk':
                mimicShrunk = True
                mimicSeen = True
                playerInv.remove('a shrink spell')
                usedSpells.append('a shrink spell')
            elif mimicOutcome == 'mimic burned':
                mimicAlive = False
                mimicSeen = True
                playerInv.remove('a burn spell')
                usedSpells.append('a burn spell')
            elif mimicOutcome == 'mimic asleep':
                mimicSleep = True
                mimicSeen = True
                playerInv.remove('a sleep spell')
                usedSpells.append('a sleep spell')
            elif mimicOutcome == 'key taken':
                room13Contents.remove('a silver key')
                playerInv.append('a silver key')
        elif (("take" in action) or ("get" in action)) and ("key" in action) and ((mimicSleep == True) or (mimicAlive == False) or (mimicShrunk == True)) and ('a silver key' in room13Contents):
            getItem(room13Contents,'a silver key')
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "s") or ("south" in action):
            playerLocation = 14
            roomRefresh = True
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            playerLocation = 12
            roomRefresh = True
        else:
            otherCmds()

# ROOM 14 - BALCONY
#potential commands:look city,sit table,climb balcony (prohibit)

    while playerLocation == 14 and roomRefresh == True:
        print("""You stand on the balcony outside Milo's bedroom. The cool night
air blows against your skin and you can see the lights of the city beyond the
edge of Milo's estate. There is a small bistro table and umbrella here""",decanterHere(),"""The entrance back into the house is north.""")
        roomRefresh = False
    while playerLocation == 14 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("take" in action) or ("get" in action)) and ("decanter" in action):
            getItem(room14Contents,'a crystal decanter')
        elif (action == "n") or ("north" in action):
            playerLocation = 13
            roomRefresh = True
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        else:
            otherCmds()

# ROOM 15 - TROPHY HALL
#potential commands:look gem (this is it, this is what you came for), look vines (the vines writhe!)
# look heads/look beasts
# check for traps (defer to vines)

    while playerLocation == 15 and roomRefresh == True:
        print("""You stand in Milo's trophy hall, where he stores the treasures
from his various magical conquests. The severed and stuffed heads of countless
mythical beasts line the walls.""",crystalHere(),plantHere(),"""The only exit is south.""")
        roomRefresh = False
    while playerLocation == 15 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif (("look" in action) or ("examine" in action)) and (("plant" in action) or ("vine" in action)):
            plantDesc()
            plantSeen = True
        elif (("look" in action) or ("examine" in action)) and (("crystal" in action) or ("gem" in action)):
            crystalDesc()
        elif ("plant" in action) or ("vine" in action) or ("crystal" in action) or ("gem" in action):
            plantOutcome = plant(action)
            if plantOutcome == 'strangled':
                alive = False
                break
            elif plantOutcome == 'plant defeated':
                plantAlive = False
                plantSeen = True
            elif plantOutcome == 'plant shrunk':
                plantShrunk = True
                plantSeen = True
                playerInv.remove('a shrink spell')
                usedSpells.append('a shrink spell')
            elif plantOutcome == 'plant burned':
                plantAlive = False
                plantSeen = True
                playerInv.remove('a burn spell')
                usedSpells.append('a burn spell')
            elif plantOutcome == 'plant still awake':
                plantSeen = True
                playerInv.remove('a sleep spell')
                usedSpells.append('a sleep spell')
            elif plantOutcome == 'crystal taken':
                getItem(room15Contents,'''Milo's Crystal''')
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "s") or ("south" in action):
            playerLocation = 12
            roomRefresh = True
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        else:
            otherCmds()

# ROOM 16 - ATTIC

    while playerLocation == 16 and roomRefresh == True:
        print("""You find yourself in the manor's attic. The ceilings are low
and bats roost in the rafters. The attic is cluttered with junk of all sorts--
boxes, trunks, mannequins (creepy!), racks of old wizard's robes, and more. A
single window at the end of the attic allows faint mooonlight in. The only exit
is the attic door leading back down to the second floor.""")
        roomRefresh = False
    while playerLocation == 16 and roomRefresh == False:
        action = input("> ")
        action = action.lower()
        if action == "look":
            roomRefresh = True
        elif ("search" in action):
            burnSpellHere()
        elif (("get" in action) or ("take" in action)) and (("scroll" in action) or ("spell" in action)):
            getItem(room16Contents,'a burn spell')
        elif (action == "n") or ("north" in action):
            dirFail()
        elif (action == "s") or ("south" in action):
            dirFail()
        elif (action == "w") or ("west" in action):
            dirFail()
        elif (action == "e") or ("east" in action):
            dirFail()
        elif (action == "down") or (("down" in action) or ("ladder" in action)):
            playerLocation = 11
            roomRefresh = True
        else:
            otherCmds()

while (alive == False) and (finishedGame == False):
    print("""================================\nYou had a good run, but you ultimately perished in Milo's manor. You managed to collect""",calcScore(),"""extra treasures before doing so.""")
    action = input("> ")

while (alive == True) and (finishedGame == True):
    print("""Congratulations! Using nothing but your cunning and an assortment
of random objects, you successfully robbed the home of MILO THE MAGE. """)
    if calcScore() == 0:
        print("")
    elif calcScore() == 1:
        print("""You were able to find""",calcScore(),"""extra treasure while you were at it.\n""")
    elif calcScore() == 4:
        print("""You were able to find all""",calcScore(),"""extra treasures while you were
at it. With the money from this job, you should finally be able to retire and live a
life of luxury somewhere in the Dragon Sea. You can almost taste the daiquiris now!\n""") 
    else:
        print("""You were able to find""",calcScore(),"""extra treasures while you were at it.\n""")
    print("""You emerge from a sewer grate in a nearby alleyway and slip off into the night.
There will be other houses to heist, places to pilfer, residences to ransack,
but tonight... THE FORGETFUL THIEF celebrates!

... Now you just have to remember where your HIDEOUT is.""")
    action = input("> ")
