import time
import sys

def main():
  ATTACK_MESSAGES = True
  TIME_SLEEP = False
  TIME_LIMIT = int(sys.argv[1])*100 # First argument # in hundredth seconds
  NUMBER_OF_TARGETS = int(sys.argv[2]) # Second argument 

  SPREAD_RECAST = 242
  FLAMETHROWER_CD = 6000
  FLAMETHROWER_RECAST = 100
  CROSSBOW_RECAST = 150
  AUTO_RECAST = 264
  BIOBLAST_CD = 1940 

  SPREAD_POTENCY = 180
  FLAMETHROWER_POTENCY = 100
  CROSSBOW_POTENCY = 180
  AUTO_POTENCY = 100.32
  BIOBLAST_POTENCY = 60

  #Upon end, Flamethrower hits one more time for a total of 11
  FLAMETHROWER_MAX_COUNT = 11
  CROSSBOW_MAX_COUNT = 5

  TIME_STEP = 2        
        
  #----------------------------Spread + Crossbow------------------------------
  totalDamage = 0
  heatGauge = 0

  spreadRecast = 0
  flamethrowerRecast = 0
  crossbowRecast = 0
  bioblastRecast = 0

  flamethrowerCD = 0
  autoCD = 0
  bioblastCD = 0

  totalTime = 0

  crossbowCount = 0
  flamethrowerCount = 0

  while (totalTime <= TIME_LIMIT):
    if (heatGauge >= 50):
      crossbowCount = CROSSBOW_MAX_COUNT
      heatGauge = 0

    if (crossbowCount > 0 and crossbowRecast <= 0):
      totalDamage += CROSSBOW_POTENCY * NUMBER_OF_TARGETS
      if ATTACK_MESSAGES: print("Crossbow:     %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (CROSSBOW_POTENCY, totalDamage, totalTime/100, heatGauge))
      crossbowRecast = CROSSBOW_RECAST
      crossbowCount -= 1
      spreadRecast = CROSSBOW_RECAST
      bioblastRecast = CROSSBOW_RECAST
    elif (bioblastCD <= 0 and bioblastRecast <= 0):
      totalDamage += BIOBLAST_POTENCY*6 * NUMBER_OF_TARGETS
      if ATTACK_MESSAGES: print("Bioblast:     %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (BIOBLAST_POTENCY*6, totalDamage, totalTime/100, heatGauge))
      bioblastCD = BIOBLAST_CD 
      spreadRecast = SPREAD_RECAST      
    elif (spreadRecast <= 0):
      totalDamage += SPREAD_POTENCY * NUMBER_OF_TARGETS
      if ATTACK_MESSAGES: print("Spread:       %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (SPREAD_POTENCY, totalDamage, totalTime/100, heatGauge))
      spreadRecast = SPREAD_RECAST
      bioblastRecast = SPREAD_RECAST
      heatGauge += 5
        
      if (autoCD <= 0):
        totalDamage += AUTO_POTENCY
        if ATTACK_MESSAGES: print("Auto:         %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (AUTO_POTENCY, totalDamage, totalTime/100, heatGauge))
        autoCD = AUTO_RECAST  
        
    spreadRecast -= TIME_STEP
    crossbowRecast -= TIME_STEP
    bioblastRecast -= TIME_STEP
    
    bioblastCD -= TIME_STEP
    autoCD -= TIME_STEP
    
    totalTime += TIME_STEP
    
    if TIME_SLEEP:
      time.sleep(0.02)

  print("Total potency in " + str(TIME_LIMIT/100) + " seconds: " + str(totalDamage) + " for Spread Shot, Bioblast, Crossbow, and Autoattack with " + str(NUMBER_OF_TARGETS) + " targets")
  print(" ")

  #----------------------------Flamethrower + Spread + Crossbow------------------------------
  totalDamage = 0
  heatGauge = 0

  spreadRecast = 0
  flamethrowerRecast = 0 
  crossbowRecast = 0
  bioblastRecast = 0

  flamethrowerCD = 1 # to start with bioblast first
  autoCD = 0
  bioblastCD = 0

  totalTime = 0

  crossbowCount = 0
  flamethrowerCount = 0

  while (totalTime <= TIME_LIMIT):
    if (heatGauge >= 50):
      crossbowCount = CROSSBOW_MAX_COUNT
      heatGauge = 0
    if (flamethrowerCD <= 0):
      flamethrowerCount = FLAMETHROWER_MAX_COUNT
      flamethrowerCD = FLAMETHROWER_CD
      
    if (flamethrowerCount > 0):
      if (flamethrowerRecast <= 0):
        totalDamage += FLAMETHROWER_POTENCY * NUMBER_OF_TARGETS
        if ATTACK_MESSAGES: print("Flamethrower: %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (FLAMETHROWER_POTENCY, totalDamage, totalTime/100, heatGauge))
        flamethrowerRecast = FLAMETHROWER_RECAST
        flamethrowerCount -= 1
    else:
      if (crossbowCount > 0 and crossbowRecast <= 0):
        totalDamage += CROSSBOW_POTENCY * NUMBER_OF_TARGETS
        if ATTACK_MESSAGES: print("Crossbow:     %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (CROSSBOW_POTENCY, totalDamage, totalTime/100, heatGauge))
        crossbowRecast = CROSSBOW_RECAST
        crossbowCount -= 1
        spreadRecast = CROSSBOW_RECAST
        bioblastRecast = CROSSBOW_RECAST
        flamethrowerRecast = CROSSBOW_RECAST
      elif (bioblastCD <= 0 and bioblastRecast <= 0):
        totalDamage += BIOBLAST_POTENCY*6 * NUMBER_OF_TARGETS
        if ATTACK_MESSAGES: print("Bioblast:     %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (BIOBLAST_POTENCY*6, totalDamage, totalTime/100, heatGauge))
        bioblastCD = BIOBLAST_CD 
        spreadRecast = SPREAD_RECAST 
        flamethrowerRecast = SPREAD_RECAST    
      elif (spreadRecast <= 0):
        totalDamage += SPREAD_POTENCY * NUMBER_OF_TARGETS
        if ATTACK_MESSAGES: print("Spread:       %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (SPREAD_POTENCY, totalDamage, totalTime/100, heatGauge))
        spreadRecast = SPREAD_RECAST
        bioblastRecast = SPREAD_RECAST
        heatGauge += 5
        
      if (autoCD <= 0):
        totalDamage += AUTO_POTENCY
        if ATTACK_MESSAGES: print("Auto:         %.2f     Potency: %.2f     Time: %.2f    Heat: %d" % (AUTO_POTENCY, totalDamage, totalTime/100, heatGauge))
        autoCD = AUTO_RECAST  
        
    spreadRecast -= TIME_STEP
    flamethrowerRecast -= TIME_STEP
    crossbowRecast -= TIME_STEP
    bioblastRecast -= TIME_STEP
    
    flamethrowerCD -= TIME_STEP
    bioblastCD -= TIME_STEP
    autoCD -= TIME_STEP
    
    totalTime += TIME_STEP
    
    if TIME_SLEEP:
      time.sleep(0.02)
    
  print("Total potency in " + str(TIME_LIMIT/100) + " seconds: " + str(totalDamage) + " for Flamethrower, Spread Shot, Bioblast, Crossbow, and Autoattack with " + str(NUMBER_OF_TARGETS) + " targets")

          

if __name__ == "__main__":
    main()