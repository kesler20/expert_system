from matplotlib import pyplot as plt
import pandas as pd
import math
import numpy as np

#-------------------------------------------------------------------------------------------
# FIRST SECTION CONCERNS WITH EXPLOSION SCENARIOS

explosion_message_1 = ''' 
    The most violent explosions usually result from dust/air mixtures that are fuel rich.
    Sudden release of stored energy, resulting pressure effects, blast, and missiles 
    •	Blast wave 
    •	Projectiles 
    •	Toxic decomposition products 
'''
types_of_explosions = {
    'Confined Vapour Cloud Explosion (CVCE)': 'A relatively small amount of flammable material, a few kilograms, can lead to an explosion when released into the confined space of a building.',
    'Unconfined vapour cloud explosions (UCVCE)':'This type of explosion results from the release of a considerable quantity of flammable gas, or vapour, into the atmosphere, and its subsequent ignition.',
    'Boiling liquid expanding vapour explosions (BLEVE)':'Boiling liquid expanding vapour explosions occur when there is a sudden release of vapour, containing liquid droplets, due to the failure of a storage vessel exposed to fire.',
    'Dust explosions' : 'A dust explosion involves the rapid combustion of dust particles that releases energy and usually generates gaseous reaction products.'
}

Types_of_fires = '''
    •   Flash – rapid leak igniting:
        Caused by ignition of flammable substances in air.
    •   Pool- pool of liquid igniting-bunds/ dikes. 
        Ignition of vapour evaporation from a pool of liquid.
    •   Jet – high pressure or small leak causing a jet igniting. 
        Layer burning - layer of powders burning may cause dust explosions 
'''

hazardous_situations = '''
    High speed venting of flammable gases 
    •   Steam leaks in hazardous areas 
    •   Vent lines containing flammable vapours
'''
Ignition_Sources = '''
    person 30mj
    spark discharge
    brush discharge
    corona discharge
    propagating brush discharge
    cone discharges
    mechanical discharges
'''
factors_that_change_MIE = '''
    •   atmosphere- i.e. oxygen concentration 
    •   Presence of flammable gases 
    •   For Solids MIE varies strongly with particle size and manufacturing method. 
    •   •Test all suppliers 
    •   Test all particle sizes expected – consider fines created by attrition
'''
charge_generation = '''
    Principal mechanism contact electrification 
    Flow of powder:
    Size reduction – (milling, grinding) 
        Drying operations 
        Filling and emptying bags/ FIBC/ Drum 
        Pneumatic transfer
    charge accumulation
    Contact and separation of powder results in charge of one polarity on the powder and the opposite on the vessel 
'''
Charging_mechanisms_depending_on = '''
    •   Powder resistivity 
    •   Physical form 
    •   Moisture content 
    •   Particle size 
    •   Contamination
'''

Charge_Accumulation = '''
    Charge may accumulate on: 
    Bulk powder 
    Drum 
    Personnel 
    Vessel 
    Transfer lines 
'''
resistivity = '''
    the ability of a liquid to generate and accumulate electrostatic charge depends on the electrical resistivity 
    if resistivity is < 10^8(Ωm) it can be considered low, if resistivity is between 10^8(Ωm) and 10^10(Ωm) it depends 
    and anything higher then 10^10(Ωm) can be considered a high resistivity.
'''
discharges_from_bulk_powders = '''
    Brush (up to 3mJ) 
    Sparks (energy dependant on capacitance) 
    Cone (energy 10- few hundred mJ) 
    Isolated conductors/ personnel: 
        Charged by contact with bulk powder or induction sparks (fn of capacitance) 
    Plastics: 
        Brush (3mJ), 
        high charging/ metal backing – propagating brush (.1000mJ)
    Precautions for Powder Handling:
    Antistatic additives don’t work on powders 
    Hard to control static build up:
        Earthing / grounding is required
        Avoid plastics (Powder < 3mJ) 
        Prevent propagating brush discharges
'''

static_charging_of_FIBCs = {
    'charged powder' : 'due to work in conveying system',
    'contact of powder with bag walls and powder going out' : 'charges bag & powder',
    'Other aspects' : 'contact with exteriosr and corona charging in vicinity'
}

Possible_static_discharges = {
    'brush' : 'from insulating powder of bag fabric',
    'cone' : 'from bulk insulating powder',
    'propagating brush' : 'from double layer across bag fabric',
    'spark' : 'from isolated conductors on/in bag and nearby',
    'incidents' : 'most due to poor earthing'
}

# -------------------------------------------------------------------------------------------
# THE SECOND SECTION DEALS WITH THE DESIGN CONSIDERSTIONS

Bleve_design_consideration_1 = '''
    Boiling Liquid Expanding Vapour Explosion (BLEVE)
    inter-connecting volumes can lead to pressure piling
    look at vented explosions versus confined deflregation
'''
Dust_explosion_consequences_1 = '''
    A dust explosion can result in: 
    The most violent explosions usually result from dust/air mixtures that are fuel rich.
    •	death or serious injury to workers. 
    •	destruction of plant and buildings.
    •	a large fireball. 
    •	secondary explosions.
    fire. put a link that goes down when you click each of these sections
'''
powders_design_reccomendations_and_insulation_and_ignition_prevention = '''
    Charge is usually generated:
    •   By contact 
    •   By work done on powder 
    Insulators Defined by resistivities (Rs>10^10Ω):
    •   Many Insulating materials are used: 
    •   Glass (lined vessels) 
    •   Plastics (pipes, vessels, packaging) 
    •   Paper (sacks) 
    •   Textiles (nylon, clothing, filter bags) 

    a flammable atmosphere is generated when there is an accumulation of electrostatic charge that is about to discharge 
    charge can be generated by walking across the floor, liquids flowing through a pipe and powder falls down a cut
    Charge can’t keep accumulating charge level set by: 
    •   Resistivity of the object 
    •   ionization can occur near the surface 
    •   The breakdown strength of the surrounding air (normally -3MVm)

    Plastics and insulators can retain charge for a long time:
    •   Discharges limited to 3mJ 
    •   DO NOT USE INSULATING PLASTICS WHERE SENSITIVE FLAMMABLE ATMOSPHERES ARE PRESENT (MIE 3 mJ)
    Different Plastics:
    Available in conducting grades 
    •   Conductive better than antistatic 
    •   Antistatic coatings can wear 

    Conductive plastics must be earthed
    •   All parts need resistance to earth 
    •   Pay attention to earthing linings 
    •   Can confirm conductivity by testing

    Typical precautions: 
    •   Earth all conducting objects 
    •   Avoid plastics 
    •   Avoid steam leaks in hazardous area of plants

    Personnel and footwear
    People- 10-30mj 
    •   Footwear 
    •   Antistatic / Static dissipative/ ESD/ SD (USA) 
    •   Need to test regularly 
    •   Need suitable floors 
    •   Conducting – used in explosive and semiconductor industries- only use where there is no risk of mains shock

    Clothing needs to be static dissipative,
    •   also, may need to be flame resistant

    floor:
    Conducting/ Antistatic available 
    •   Must be kept clean and avoid deposits 
    •   Beware contaminants 
    •   oil, power 

    Test on insulation and regularly 
    •   Resistance must be < 108 Ω
''' 
volume_of_receiving = r'C:\Users\HP\Documents\anaconda3\PYTHON2\OneDrive-2021-01-10\volume_of_receiving_vessle.png'

miscellaneous_design_reccomendations_1 = '''
    to control the entry on to the site of obvious sources of ignition; 
    such as matches, cigarette lighters and battery-operated equipment. 
    
    The use of portable electrical equipment, welding, spark-producing tools and
    the movement of petrol-driven vehicles would also be subject to strict control.
    Exhaust gases from diesel engines are also a potential source of ignition.
    
    Increase moisture content: 
    •	Raises energy needed for ignition 
    •	(ideally beyond what could be generated on the plant) 
    •	Generally, need more than 30 prcnt moisture content 
    •	Beware of dewatering in drums
'''
water_accumulate_at_bottom = r'C:\Users\HP\Documents\anaconda3\PYTHON2\OneDrive-2021-01-10\water_accumulate_at_bottom.png'

miscellaneous_design_considerations_2 = '''
    water can accumulate in low points in piping so we have drain valves
    If any part of the system goes below 0 degrees then ice can form, causing blockages and possible failure of moving parts. This is a danger not only for low temperature systems, 
    but from cooling which occurs when pressure is released, and liquids can expand very quickly.
    Two-phase flow from the presence of water in a hydrocarbon creates a static charge, which has been known to ignite flammable vapours. 
    Protection: Single phase fluid keep Velocity< 7m/s Two liquid phases keep Velocity
'''
unit_operations_that_require_design = '''
    unit operations that require careful design due to 70-80 percent of processed powders potentially explode include:
    •   Milling/ Grinding 
    •   Bag Filters 
    •   Cyclones 
    •   Pneumatic transfer Systems 
    •   Bucket Elevators 
    •   Dryers 
    •   Silos 
    •   Blenders 
    •   Flakers
'''
Powders_Properties_Considerations = {
    'Particle Size': 'smaller particles usually more sensitive and burn more violently',
    'Solvent content': 'Even small amounts of solvents can render powders very ignition sensitive and give rise to very vioelednt ignitions',
    'Moisture content': 'Ading water decreases sensitivity and explosion violence',
    'Concentration': 'Worst case in air is slightly fuel rich increasing oxygen concentration can make things much worse',
    'Temperature': 'increasing Temperature makes flammability characteristics worse'
}
Handling_liquids = '''
    Charge generated on insulating liquids:
    •	Reducing flow reduces charge 
    •	Use orifice plates 
    •	Limit Pump capacity Pipe six
    Filling precautions
    Avoid splash filling & mist formation:
    •	Use dip legs 
    •	Bottom fill 
    •	Limit inlet velocity
'''
Flashpoint_considerations = '''
    adding water increases the flashpoint of liquids that are soluble in water 
    e.g. ethanol/water

    - completely soluble liquids are non-flammable if diluted to <1 percent volume/volume of water
    - partially soluble liquids may be flammable at even <1 percent of volume/volume of water 
    e.g. MIBK
'''
Control_of_sources_of_ignition = '''
    powder decomposition
    pyrophoric type materials
    exothermic reactions
    fundamental understanding of materials 
'''
Control_of_static_electricity = '''
    earth all conducting plant items
    earth people
    minimise charge generation
    restrict use of plastics
'''
Explosion_measures = '''
    Containment 
    •	Design pressure above Pmax 
    Venting 
    •	Weak panel that fails 
    Suppression 
    •	Extinguish the flame before damaging pressure (CO2) 
    Isolation 
    •	Stop explosion moving to other vessels
    Types of explosion resistant design
    Explosion pressure resistant (EN - 13445)
    Explosion Pressure Shock Resistant (EN - 14460)
'''
chemical_barriers = '''
    Commonly used either side of where suppression is used.
    Use with Dusts, Gases and Vapours
    Detection by pressure or flame:
    •   Triggers firing of suppressant
'''
slam_shut_valves = '''
    Valves slam shut:
    On detection of pressure/ flame: 
    •   Needs to work very quickly! 
    •   Big valves- can it be fast enough 
    •   Can be used Vapour, gases, and vapours 
    •   Stops pressure, flame, burning particles & air flow
'''
# EN 16447
Flap_and_ventex_valves = '''
    For Dusts 
    Passive- pressure valve ahead of flame forces it shut 
    Stops propagation, burning particles and air flow:
    •   Cheap- reliability????? 
    •   Weak explosions may not trigger it, 
    •   Dust may obstruct
'''
Rotary_valves = '''
    •   Often used in powder equipment 
    •   Must stop detection of ignition
    •   Must be strong enough for explosion pressure 
    •   Gaps must be narrow enough to quench flame 
    •   Maintenance- no rodding!
'''
# EN - 12874
Flame_arrestors = '''
    •   Principles of operation 
    •   Ignition of flammable gas/ vapour/ mist 
    •   Flame propagates along to arrester 
    •   Arrester splits flame into framelets 
    •   Framelets go down narrow passages 
    •   Framelets drop in temp 
    •   Stops burning
'''
# standards EN - 15089
Explosion_Isolation = {
    'Active': [chemical_barriers, slam_shut_valves, 'spark detection'],
    'Passive': [Flap_and_ventex_valves, 'Diverters', Rotary_valves, Flame_arrestors]
}
# FOR DIVERTERS EN 16020
Primary_Safeguards = '''
    Primary Safeguard:
    •   Electrical conductors that can only store charge if isolated
    Operations generating charge in liquids are:
    Flow through pipes valves and especially fine filters 
    •   (especially 2 phase liquid/liquid or solid/ liquid) 
    •   Pouring from containers 
    Flow of 2 phase gas/liquid (e.g. wet steam) 
    Atomization of liquids (e.g. water washing, splash filing ) 
    Agitating 2 phase liquids or solid/ liquid mixtures 
    Gravity settling liquids or solids from liquid suspensions 
    Crystallization in insulating liquids (e.g. toluene, hexane)
    
    Required precautions during liquid handling:

    for restrictions keep flow at (1m/s for 2 liquid phases, 7/m/s for all liquids) 
    Avoid splash filling and mist formation (dip tube- subsurface filling) 
    Use relaxation tanks/ pipe volume Use antistatic additive

    Earthing of all conducting items:
    •   Conducting plant items 
    •   Conducting bulk liquids in lined vessels
    •   Moveable items (e.g. drums/ personnel) 
    •   Hand Tools 
    •   Control of charge generation rate Flow 
'''
Mitigation_measures = '''
    •	The most important mitigation measure is maintaining the process buildings in a clean condition. If you allow dust deposits to accumulate, they can provide the fuel for a secondary explosion.
    •	We can group more technical measures to mitigate an explosion into the following main categories: n explosion relief venting; n explosion suppression and containment; and n plant siting and construction.
    •	Design considerations (ensure that electrical equipment have Meltable fuses)
'''
reliability_of_inerting_system = '''
    Many factors will influence the overall reliability of an inerting system. 
    •	the location and number of atmospheric sampling points
    •	type of sensor head
    •	frequency of calibration of the sensor
    •	contaminants in the system that interfere with sensor readings
    •	provision of safe means of control or shutdown, if the oxygen concentration exceeds a predetermined level
    •	adequate supplies of inert gas for all foreseeable needs
    •	the number of locations where air may enter the plant
    •	the safety margin allowed when setting control levels for oxygen
    •	the reliability of any electronic control system
'''
Preventions = '''
    to prevent flammable atmospheres:
    Operate Below flash point 
    •	Operate below the lower flammable limit 
    •	Operate 50C below if possible 
    to prevent dust generation 
    •	Use aqueous pastes (some very wet pastes still form dust clouds) 
    •	Use inert gas
    to prevent flammable materials
    Avoid small particle size: 
    •	Large particles do no propagate flame readily 
    •	Use particle sizes of >500 microns 
    •	Avoid crushing/ attrition Produces fines 
'''
Dust_control_measures = '''
    Localise where dust may occur: 
    •	Reduce the concentration of the suspended dust below the LEL 
    •	In Europe ATEX directive requires plant to be free from deposited dust 
    controls over dust cloud formation
    •	preventing the explosive atmosphere by inerting
    •	avoiding ignition sources
    Good Housekeeping required:
    •	Avoids the possibility of secondary explosions 
    •	Avoids dust clouds from disturbed layers  
    •	Can use explosion rated vacuums (must be maintained as SCE) 
    •	Avoid Brushing- Wet if must brush 
    •	DO NOT BLOW it causes dust clouds & dust will settle elsewhere
'''
Design_protections = '''
    •	Housekeeping 
    •	Suppression and venting 
    •	Non-Sparking tools 
    •	Intrinsically safe vacuums 
    •	No dry brushing 
    •	Earthing and grounding 
    •	Testing all material 
    •	Change material to avoid if possible 
    •	Segregating / reduce quantity 
    •	Repair and solve causes of blockages, leaks etc. 
    •	Operating discipline
'''
Safe_operating_conditions = '''
    Specify safe operating envelope 
    •	Temperature, Pressure, and time 
    •	Specify appropriate equipment 
    •	Area classification/ Equipment T rating 
    •   Temperature and scale that are critical for packaging, transport, and storage 
    •   Electrical equipment T rating 
    •   Prevent thermal cycling 
    •   Contamination 
    •   Variations in heating 
    •   Variations in powder ( different batches)
'''
Elimination_of_ignition_sources = '''
    •	Needs data 
    •	Intimate understanding 
    •	Flammability characteristics 
    •	understanding of Plant, equipment, and operations 
    •	Challenge assumptions considering experience
    •	Safety Margin
'''
#Many processes involving flammable dusts use a series of interconnected units of plant, such as grinders, elevators, cyclones, 
# silos and filters. Unless you take appropriate precautions, an explosion occurring in any one unit of plant may spread from unit to unit causing extensive damage.
#rotary valves;  
# a choke of material in an intermediate hopper; 
# screw conveyors with a missing flight and baffle plate; 
# explosion suppression barriers;
# explosion isolation valves

hse_report_1st_rotary_valve = r'C:\Users\HP\Documents\anaconda3\PYTHON2\OneDrive-2021-01-10\hse_report_1st_rotary_valve.png'

#Rotary valves are commonly provided to control powder flow, or to act as an air lock. 
# If they are also intended to act as explosion chokes, they need rigid blades eg of metal, 
# that will not deform under a pressure wave

screw_conveyor_as_choke = r'C:\Users\HP\Documents\anaconda3\PYTHON2\OneDrive-2021-01-10\screw_conveyor_as_choke.png'


#Explosion suppression barriers, also called advanced inerting systems are similar to suppressors 
# used for major items of plant. A suppression barrier involves linking a pressure or optical detector 
# to a rapid-acting device designed to inject an inerting or suppressing material into a duct.

advanced_inerting_systems = r'C:\Users\HP\Documents\anaconda3\PYTHON2\OneDrive-2021-01-10\advanced_inerting_systems.png'

#Explosion isolation valves act by closing in milliseconds,
#  following detection of a flame or pressure rise by a sensor situated an appropriate distance towards the anticipated source of the explosion. 
# They have particular advantages where you want to avoid a hold up of material within the plant.

explosion_isolation_valve = r'C:\Users\HP\Documents\anaconda3\PYTHON2\OneDrive-2021-01-10\explosion_isolation_valve.png'

# IGNITION SOURCES PART OF THE SCENARIO
Common_ignition_sources = '''
    •	hot surfaces; 
    •	naked flames; 
    •	faulty or unsuitable equipment;
    •	overheating of moving mechanical plant eg by friction;
    •	impact sparks;
    •	electrostatic discharges; 
    •	spontaneous heating; 
    •	smoking materials.
'''
sources_of_fire = [ 'static electricity', 'process flames(open furnaces)', miscellaneous_design_reccomendations_1]

Control_of_heat_sources = '''
    electrical equipment
    hot surfaces
    hot work permit
    control of friction
    mechanical friction
    impact sparks
'''

# LEGISLATION
Dusts_regualtions = '''
    •	The Fire Precautions (Workplace) Regulations 19974
    •	The Provision and Use of Work Equipment Regulations 19985
    •	The Workplace (Health, Safety and Welfare) Regulations 19926
    •	The Control of Substances Hazardous to Health Regulations 19997
    •	The Equipment and Protective Systems for Use in Potentially Explosive 
    •	Atmospheres Regulations 19968
'''
permits_for_hot_work = '''
    permits for hot work need to set out clearly: 
    •	your arrangements for handover,
    •	the allowable range of work, 
    •	time limits on when the work may be done; 
    •	the precautions required.
    •	The ACOP to the DSEAR regulations gives further information.14-18
'''
Ex_sign_on_zoned_areas = '''
    DSEAR3 also requires the access points to zoned areas to be marked with 
    a yellow and black triangular Ex sign (see below), where the risk assessment 
    shows it will have some benefit. Signs might help remind employees where special rules apply
'''
Ex_sign_immage = r'C:\Users\HP\Documents\anaconda3\PYTHON2\OneDrive-2021-01-10\EX_SIGN.png'

fire_precaustions = 'to be taken in the design are given in the standards NFPA 30 (2003)'#open a link to the standard if wanted

#-------------------------------------------------------------------------------------------------------------------
# TESTS AND CALCULATIONS

#the autoignition temperature is the lowest temperature at which a gas or vapour spontaneously ignites without an ignition source, 
#this depends on pressure temperature, oxidizing atmosphere, vessel volume and the fuel/air concentration.
#Fuel, Formula, Maximum_Flame_Speed (m/s), Adiabatic_Flame_Temperature (K), Expansion_Factor, Autoignition_Temperature (+C)
Explosion_Properties_Data = {
    'Hydrogen H2': [22.1, 2318, 6.9, 400],
    'Methane CH4': [2.8, 2148, 7.5, 601],
    'Ethane C2H6': [3.4, 2168, 7.7, 515],
    'Propane C3H8': [3.3 ,2198, 7.9, 450],
    'n-Butane C4H10': [3.3, 2168, 7.9, 405],
    'Pentane C5H12': [3.4 ,2232, 8.1, 260],
    'Hexane C6H14': [3.4, 2221, 8.1, 225],
    'Acetylene C2H2': [14.8, 2598, 8.7, 305],
    'Ethylene C2H4': [6.5, 2248, 7.8, 490],
    'Propylene C3H6': [3.7 ,2208, 7.8, 460],
    'Benzene C6H6': [5, 2287, 8.1, 560],
    'Cyclohexane C6H12': [4.2, 2232, 8.1, 245]
}

'''
Limiting Oxygen Concentration (LOC)
    Limiting oxygen concentration (using nitrogen as inert gas NB<16 prcnt  can lead to unconsciousness and death)
'''
#Powder charging rates:
# operation and mass charge density (from to) in C/kg
# discharges of 5*10**(-8) C can be incendive !
powder_charging_rates = {
    'Sieving' : (10**(-11), 10**(-9)),
    'Pouring' : (10**(-9), 10**(-7)),
    'Scroll Feeding' : (10**(-8),10**(-6)),
    'Grinding' : (10**(-7), 10**(-6)),
    'Micronising' : (10**(-7), 10**(-4)),
    'Pneumatic Conveying' : (10**(-7), 10**(-3))
}

LOC_values = {
    'Rye Flour': (29, 13),
    'Organic Pigment': (10, 12),
    'Methyl Cellulose': (70, 10),
    'Beta Naphitol': (30, 7),
    'Sulphur': (30, 7),
    'Paraformaldehyde': (23, 6),
    'Aluminium': (22,5)
}

'''
where tau is the decay time to 1/e of charge dissipated (approx. 63 prcnt)
epsilon 0 is the relative permittivity of the powder (dielectric constant)
epsilon R is the permittivity of free space (8.85 x10^-12 F/m)
and rho is the resistivity of powder in (Ωm) 
the generation rate is primarily determined by work done
Dissipation controlled by powder resistivity: τ=ϵ_0 ϵ_R ρ
'''
def charge_dissipation(epsilon0, epsionR, rho):
    tau = epsilon0 * epsionR * rho
    return tau


# discharge type source energy ignities
Incenditives = {
    'Lighting': ['', 1000, 'Everything'],
    'Spark': ['Conductors (i.e. People)', '1000 mj or higher', 'All Gas/Vapour/Dusts'],
    'Propagating Brush': ['Insulators with metal backing', '1000 or higher', 'All Gas/Vapour/Dusts'],
    'Cone': ['Bulk Powders', 'Max 10 - 100 mj', 'All Gas/Vapour and some Dusts'],
    'Brush': ['Insulators', 'less then or equal to 3 mj', 'All Gas/Vapour few Dusts'],
    'Corona': ['Sharp Points', 'less then 0.1mj', 'Only unusually sensitive atmospheres']
}

#pressure explosion ratio is typically 7-8 as such the temperature explosion ratio as well
#(P_ex/P_0 )≈(T_ex/T_0 )
#where knowing that T_0≈300K we can deduce that its T_ex≈1500-3000K if the ratio is between 5-10
#for a constant pressure case:
#(V_ex/V_0 )≈(T_ex/T_0 ) 

#Flame speed in chemicals
# usually 7-8
# and is approximately identical to the temperature explosion ratio
def pressure_explosion_calculation(P0, ratio=7):
    P_explosion = P0*ratio
    return P_explosion

def flame_speed_velocity(volume_mixture_consumed_per_second, flame_area):
    flame_speed = volume_mixture_consumed_per_second/flame_area
    return flame_speed

#S_t is laminar burning velocity in m/s and MESG in mm
Published_values_of_S_t_and_MESG = {
    'Ammonia': (np.nan, 3.18),
    'Methane': (0.36, 1.14),
    'Acetone': (0.43, 1.04),
    'Chloromethane': (np.nan, 1.0),
    'Vinyl Chloride': (np.nan, 0.99),
    'Cyclohexane': (0.44, 0.94),
    'Methanol': (0.5, 0.92),
    'Propane': (0.37, 0.92),
    'Ethane': (0.37, 0.91),
    'Ethanol': (np.nan, 0.89),
    'Diethyl Ether': (0.48, 0.87),
    'Ethylene': (0.76, 0.65),
    'Acetylene': (1.5, 0.37),
    'Carobn Disulphide': (0.59, 0.34),
    'Hydrogen': (3.0, 0.29)
}

#the data is stored as to have b0 as the first value of the touple and b1 as the second 
# dataset taken from https://www.sciencedirect.com/topics/chemistry/flash-point
# p_25 represents the vapour pressure of the liquid at 25 degrees C 
# Vapor pressure of liquids data can also be accessed from engineered toolbox website 
# https://www.engineeringtoolbox.com/vapor-pressure-d_312.html#:~:text=Liquids%20-%20Vapor%20Pressure%20%20%20%20Fluid,%20%2030%20%2051%20more%20rows%20
def calculate_flashpoint(compound, P_25):
    bi = {
        'Acetates' : (2.976, 0.380),
        'Acids' : (2.777, 0.491),
        'Alcohols' : (2.953, 0.323),    
        'Phenols' : (2.953, 0.323),
        'Aldehydes' : (2.924, 0.443),
        'Alkanes' : (3.142, 0.319),
        'Alkanes*' : (2.948, 0.470),
        'Aromatics' : (3.142, 0.319),
        'Aromatics*' :  (2.948, 0.470), 
        'Alkenes' : (3.097, 0.424),
        'Amines' :  (3.077, 0.322),
        'Esters' : (2.948,  0.385),
        'Ethers' : (3.056, 0.357),
        'Ketones' : (3.033, 0.381)
    }
    k = bi[compound][1]*math.log(P_25, 10) + bi[compound][0]
    flashpoint = 1000/k - 273
    return flashpoint

# in kpa
liquid_vapour_pressure = {
    'Acetaldehyde': 120,
    'Acetic acid':  2.1,
    'Acetic acid anhydride':    0.68,
    'Acetone':  30,
    'Allyl alcohol':    2.3,
    'Allyl chloride':   40,
    'Aluminum nitrate, 10 wt prcnt in water':  2.4,
    'Aluminum sulphate, 10 wt prcnt in water': 2.4,
    'Amyl acetate': 0.47,
    'Aniline':  0.09,
    'Beer': 2.4,
    'Benzene':  14,
    'Benzyl alcohol':   0.013,
    'Bromine':  28,
    'Butyl acetate':    1.5,
    'Butyl alcohol, 1-butanol': 0.93,
    'Butyric acid n':   48,
    'Calcium chloride, 25 wt prcnt in water':  2.4,
    'Calcium chloride, 5 wt prcnt in water':   2.4,
    'Carbon disulphide':    48,
    'Carbon tetrachloride': 15.3,
    'Chloroform':   26,
    'Cyclohexanol': 0.9,
    'Cyclohexanone':    0.67,
    'Ethyl acetate':    14,
    'Ethyl alcohol':    12.4,
    'Ethyl glycol': 0.7,
    'Ethylene glycol':  0.007,
    'Formic acid':  5.7,
    'Furfurol, 2-Furaldehyde':  0.3,
    'Heptane':  6,
    'Hexane':   17.6,
    'Isopropyl alcohol (rubbing alcohol)':  4.4,
    'Kerosene': 0.7,
    'Methyl acetate':   28.8,
    'Methyl alcohol, methanol': 16.9,
    'Methylene chloride, dichloromethane':  58,
    'Milk': 2.4,
    'Nitrobenzene': 0.03,
    'Nonane':   0.6,
    'Octane':   1.9,
    'Pentane':  58,
    'Phenol':   0.05,
    'Propanol': 2.8,
    'Propionic acid':   0.47,
    'Sea water':    2.4,
    'Sodium chloride, 25 wt prcnt in water':   2.4,
    'Sodium hydroxide, 20 wt prcnt in water':  2.4,
    'Sodium hydroxide, 30 wt prcnt in water':  2.4,
    'Styrene':  0.85,
    'Tetrachloroethane':    0.7,
    'Tetrachloroethylene':  2.5,
    'Toluene':  3.8,
    'Trichloroethylene':    9.2,
    'Water':    2.4
}

Hot_surface_test = ['layer ignition test', 'cloud ignition test']
Electrostatic_spark = 'Minimum ignition energy'
dust_explosion_tests = ['vertical tube test', 'particle size analysis']
fire_spreading_across_a_layer_of_dust = 'train fire test'
avoid_dust_clouds_capable_of_exploding = 'minimum explosible concentrate'
explosion_severity_tests = ['20 litre sphere', 'K_st', 'P_max']
testing_how_air_impacts_explosion_risk = 'limiting oxygen concentration'

# K_st = dp/dt_max for a 1 m^3 vessel Kst is in bar.m/s
def K_st_calculation(dpdt_max, volume):
    K_st = dpdt_max*(volume**(1/3))
    return K_st

'''
Brode’s Equation
    Bursting vessel explosion hazards 
    W_e=(P-P_E )V/(γ-1)
    Where We is the energy of explosion, P is absolute gas pressure, PE is the absolute ambient pressure, 
    V is vapour volume, and  is the ratio of specific heats
    this can be converted from heat of explosion (j/g) to calculate how much in kg of a particular substance is required to generate the calculated We.
'''

def energy_of_explosion_calculations(P_abs,P_ambient,vapourVolume,gamma):
    W_e = ((P_abs - P_ambient)*vapourVolume)/(gamma - 1)
    return W_e
#this can be converted from heat of explosion (j/g) to calculate how much in kg of a particular substance is required to generate the calculated We. 

'''
Minimum Ignition Energy 
    the smallest amount of energy in a single discrete spark, at which the most ignitable dust air mixture will ignite 

    Minimum Ignition Temperature (MIT)
    this is the lowest temperature at which the most ignitable dust air mixture will spontaneously ignite
    Use of MIT Data can be to identify safe drying conditions (typically a 50k safety factor is used)
    Used for specifying the maximum surface temperature of electrical equipment which should be less than 2/3 of the MIT.

    Layer Ignition Temperature
    Lowest temperature that hot surface will ignite a powder when settled as a dust layer. 
    •	Usually 5 mm thick layer of dust. 
    •	Usually lower than MIT.
'''
Minimum_ignition_energy = {
    'Coffee' : 85,
    'Grain dust': 55,
    'Sugar': 35,
    'Wheat flour': 50,
    'Coal': 55,
    'Wood flouir': 40,
    'Nylon': 20,
    'Polyethylene': 10,
    'Polystyrene': 15, 
    'Aluminium': 15, 
    'Magnesium': 40 
}

#typical value for LEL for powders is 40g/m^3
LEL = 40
def lower_explosible_limit_calculations(volume, LEL):
    Kilograms_of_powder_required = LEL*volume
    return Kilograms_of_powder_required

# MIE in mj
def give_Ignition_energy_related_Precautions(MIE):
    if MIE > 100:
        precautions = 'perform general earthing and prevent propagating brush'
    elif MIE > 10 and MIE < 100:
        precautions = 'cone discharge need consideration and personnel are potential ignition hazards'
    elif MIE < 30:
        precautions = 'Ground people'
    elif MIE < 10:
        precautions = 'Cone and brush discharges possible and static hazard may be unavoidable'
    elif MIE < 1:
        precautions = 'Seek Expert Advice and non sparking tools'
    else:
        precautions = None
        print('MIE value is not classifiable')
    return precautions


#----------------------------------------------------------------------------------------------------
# RESULTS AND CLASSIFICATIONS

'''
regulations are relevant where flammable dusts may occur. These are:
    •	The Fire Precautions (Workplace) Regulations 19974
    •	The Provision and Use of Work Equipment Regulations 19985
    •	The Workplace (Health, Safety and Welfare) Regulations 19926
    •	The Control of Substances Hazardous to Health Regulations 19997
    •	The Equipment and Protective Systems for Use in Potentially Explosive Atmospheres Regulations 19968
    according to the law it is important to classify hazardous areas this is calso known as zoning:
'''
hazardous_area_classification = {
    'Zone 0': 'explosive gas-air mixtures are present continuously or present for long periods. Specify intrisically safe equipment',
    'Zone1': 'explosive gas-air mixtures are likely to occcur in normal operation. Specify: insitrically safe equipment, or flame-proof enclosures with pressurizing and purging.',
    'Zone 3': '''explosive gas-air mixtures not likely to occur during normal operation, but could occur for short periods. 
    Specify: intrinsically safe equipment, or total enclosure, or non-sparking apparatus.'''
}

    #National Fire Protection Association
flashpoint_boilingpoint_NFPA_Class = {
    'Propane' : [105, 42, 'IA'],
    'Pentane' : [49, 36, 'IA'],
    'Ethyl ether' : [45, 35, 'IA'],
    'Acetaldehyde': [39,21,'IA'],
    'Dimethyl sulfide' : [38,37,'IA'],
    'Carbon disulfide' : [30,46,'IB'],
    'Ethylene oxide' : [29,13,'IA'],
    'n-Hexane' : [22,69,'IB'],
    'Acetone' : [20,133,'IA'],
    'Cyclohexane' : [20,81,'IB'],
    'Tetrahydrofuran': [14,67,'IB'],
    'Benzene' : [11,80,'IB'],
    'Triethylamine': [7,89,'IB'],
    'Methyl ethyl ketone (MEK)': [4,80,'IB'],
    'Toluene': [4,111,'IB'],
    'Methyl alcohol' : [11,65,'IB'],
    'Isopropyl alcohol (IPA)' : [12,82,'IB'],
    'Ethyl alcohol':[13,78,'IB'],
    'Pyridine':[20,116,'IB'],
    '2-Nitropropane':   [24,120,'IC'],
    'Tert butyl isocyanate' :[27,86,'IC'],
    'Chlorobenzene':    [28,132,'IC'],
    'Epichlorohydrin':  [31,116,'IC'],
    'Xylene 27–32': [138,144,'IC'],
    'Morpholine'    :[38,128,'II'],
    'Acetic acid, glacial': [39,48,'II'],
    'Bromobenzene': [48,155,'II'],
    'Formic acid'   :[50,101,'II'],
    'Methyl lactate':   [57,144,'II'],
    'Stoddard solvent': [49,155,'II'],
    'Iso-propyl lactate':   [60,157,'II'],
    'Ethyl lactate' :[61,153,'IIIA'],
    'Benzaldehyde'  :[63,178,'IIIA'],
    'Cyclohexanol'  :[68,161,'IIIA'],
    'Tetrahydronaphthalene': [71,208,'IIIA'],
    'Iso-butyl lactate':    [76,182,'IIIB'],
    'Methacrylic acid': [77,    158,    'IIIA'],
    'Butyl lactate' :[79,   187,    'IIIB'],
    'Nitrobenzene'  :[88,   211,    'IIIA'],
    'n-Methyl pyrrolidone': [93,    202,    'IIIA'],
    'Benzyl alcohol':   [101,   205,    'IIIB'],
    'Caproic acid'  :[102,  204,    'IIIB'],
    'Ethylene glycol':  [111,   198,    'IIIB'],
    '3-Ethyllhexyl lactate':    [113,   246,    'IIIB'],
    'Phenyl ether': [115,   258,    'IIIB'],
    'Stearic acid': [196,   386,    'IIIB'],
}

    #Flashpoint classification:
def check_flashpoint_classification(flash_point, boiling_point):
    flashpoint_classification = ['Class IA', 'Class IB', 'Class IC']
    if flash_point < 22.8 and boiling_point < 37.8 : #degrees
        print(f'liquid is {flashpoint_classification[0]}')
    elif flash_point > 22.8 and boiling_point > 37.8 :
        print(f'liquid is {flashpoint_classification[1]}')
    elif flash_point > 22.8 and boiling_point < 37.8 :
        print(f'liquid is {flashpoint_classification[2]}')
    else:
        print('liquid is not classfiable by flashpoint')

    #classification of maximum surface temperature for electrical equipment 

# temperatures in degrees         
def check_maximum_surface_temperature_for_electrical_equipment(max_surface_temperature):
    if max_surface_temperature > 300 and max_surface_temperature < 450:
        classification = 'T1'
    elif max_surface_temperature > 200 and max_surface_temperature < 300:
        classification = 'T2'
    elif max_surface_temperature > 135 and max_surface_temperature < 200:
        classification = 'T3'
    elif max_surface_temperature > 100 and max_surface_temperature < 135:
        classification = 'T4'
    elif max_surface_temperature > 85 and max_surface_temperature < 100:
        classification = 'T5'
    elif max_surface_temperature < 85:
        classification = 'T6'
    else:
        classification = None
        print(' equipment cannot be classified')
    return classification

# ST classification of Dusts:
def ST_powder_classification(K_st):
    if K_st == 0:
        st_classification = 'ST 0'
        Characteristics = 'no explosion'
    elif K_st < 200:
        st_classification = 'ST 1'
        Characteristics = 'weak/moderate explosion'
    elif K_st > 200 and K_st < 300:
        st_classification = 'ST 2'
        Characteristics = 'Strong explosion'
    elif K_st > 300:
        st_classification = 'ST 3'
        Characteristics = 'Very Strong explosion'
    else:
        st_classification = None
        Characteristics = None
    return st_classification, Characteristics

#Layer Burning Behaviour of dust or powders
Layer_Burning_Behaviour_Classification = {
    1 : 'No ignition',
    2 : 'Brief ignition, rapid extintion',
    3 : 'Localised, minimal Spreading',
    4 : 'No flame, slow spread',
    5 : 'Propagating flames or sparks',
    6 : 'Very rapid combustion/ decomposition, with/without flame'
}
#-------------------------------------------------------------------------------------
#Powder Flammability
def check_powder_flammability_classification(variable):
    powder_flammability_classification = ['Group A', 'Group B']
    if variable == 'A':
        flammability_classification = powder_flammability_classification[0]
    elif variable == 'B':
        flammability_classification = powder_flammability_classification[1]
    else:
        print('Group can only be either A or B')

    if flammability_classification == 'Group B':
        print('''
        •   for T > 110 °C furnace test needed before a Group B can be confirmed 
        •   Group B powders may burn or be thermally unstable 
            '''
            )
    else:
        print(
            'powder is not flammable'
        )
#for dusts minimum explosive concentrations are usually 3 Lower explosion limit (LEL) for dusts usually 30 - 100 gm^-3

# returns maximum flow velocity in metres per second
def check_maximum_flow_velocity_restrictions(single_phase, liquid_resistivity):
    if liquid_resistivity < 2*10**10:
        maximumm_flow_velocity = np.nan
    elif liquid_resistivity > 2*10**10 and single_phase:
        maximumm_flow_velocity = 7
    elif liquid_resistivity > 2*10**10 and single_phase == False:
        maximumm_flow_velocity = 1
    else:
        maximumm_flow_velocity = np.nan
    return maximumm_flow_velocity
 

#-------------------------------------------------------------------------------------------------------------------
# CHEMICAL ENIGNEERING DESIGN

#this data comes from https://powderprocess.net/Safety/Dust_Minimum_Ignition_Energy_MIE.html 
# the stored key_value pairs represent - Material : MIE (mJ)

class Powders(object):

    def __init__(self,ST_Classification, Explosion_Characteristics, Minimum_Oxygen_for_Combustion, Electrical_Resistivity, Flammability, Minimum_Ignition_Energy, Minimum_Ignition_Temperature, Thermal_Stability, Burning_Properties):
        self.Flammability = Flammability
        self.Minimum_Ignition_Energy = Minimum_Ignition_Energy
        self.Thermal_Stability = Thermal_Stability
        self.Minimum_Ignition_Temperature = Minimum_Ignition_Temperature
        self.Burning_Properties = Burning_Properties
        self.Electrical_Resistivity = Electrical_Resistivity
        self.Minimum_Oxygen_for_Combustion = Minimum_Oxygen_for_Combustion
        self.Explosion_Characteristics = Explosion_Characteristics
        self.ST_Classification = ST_Classification

# look for data for MIE MIT{CLOSUD AND LAYER} LOC, MEC in g/m^3, Volume resistivity in ohms.m 
# self heating onset temperature (0C)

# flammability ranges in %by volume from Chemical Engineering Design 5th EDITION page 483
# lower_limit - upper_limit
Flammability_ranges = {
    'Hydrogen': (4.1, 74.2),
    'Ammonia': (15.0, 28.0),
    'Hydrocyanic acid': (5.6, 40.0),
    'Hydrogen sulphide': (4.3, 45.0),
    'Carbon disulphide': (1.3, 44.0),
    'Carbon monoxide': (12.5, 74.2),
    'Methane': (5.3, 14.0),
    'Ethane': (3.0, 12.5),
    'Propane': (2.3, 9.5),
    'Butane': (1.9, 8.5),
    'Isobutane': (1.8, 8.4),
    'Ethylene': (3.1, 32.0),
    'Propylene': (2.4, 10.3),
   ' n-Butene': (1.6, 9.3),
    'Isobutene': (1.8, 9.7),
    'Butadiene': (2.0, 11.5),
    'Benzene': (1.4, 7.1),
    'Toluene': (1.4, 6.7),
    'Cyclohexane': (1.3, 8.0),
    'Methanol': (7.3, 36.0),
    'Ethanol': (4.3, 19.0),
    'Isopropanol': (2.2, 12.0),
    'Form aldehyde': (7.0, 73.0),
    'Acetaldehyde': (4.1, 57.0),
    'Aetone': (3.0, 12.8),
    'Methylethyl ketone': (1.8, 10.0),
    'Dimethylamine (DEA)': (2.8, 184),
    'Trimethylamine (TEA)': (2.0, 11.6),
    'Petrol (gasoline)': (1.3, 7.0),
    'Paraffin (kerosene)': (0.7, 5.6),
    'Gas oil (diesel)': (6.0, 13.5)
}

Vent_piping_design_considerations = '''
    When designing relief venting systems it is important to ensure that flammable or toxic
    gases are vented to a safe location. This will normally mean venting at a sufficient
    height to ensure that the gases are dispersed without creating a hazard. For highly toxic
    materials it may be necessary to provide a scrubber to absorb and “kill” the material
'''

'''
Fire and Explosion Hazard Assessment Process
    Identify & characterise (record) flammable materials and atmosphere 
    •	Identify & quantify ignition sources 
'''

def F_and_EI_index_calculations(F1,F2,Material_Factor,C1,C2,C3):
    F_3 = F1*F2 # unit hazard factor
    F_and_EI_Index = Material_Factor*F_3
    Credit_Factor = C1*C2*C3

# MF, Flash point°C ,Heat of combustion MJ/kg
Material_Factor_data = {
    'Acetaldehyde': [24, 39, 24.4],
    'Acetone': [16, 20, 28.6],
    'Acetylene': [40, np.nan, 48.2],
    'Ammonia': [4, np.nan, 18.6],
    'Benzene': [16, 11, 40.2],
    'Butane': [21 ,np.nan ,45.8],
    'Chlorine': [1, np.nan, 0.0],
    'Cyclohexane': [16, 20, 43.5],
    'Ethyl alcohol': [16, 13, 26.8],
    'Hydrogen': [21, np.nan ,120.0],
    'Nitroglycerine': [40, np.nan, 18.2],
    'Sulphur': [4, np.nan, 9.3],
    'Toluene': [16, 40, 31.3],
    'Vinyl Chloride': [21, np.nan, 18.6]
}

Control_Credit_Factors_Variables = {
    'emergency_power' : (0.98, np.nan),
    'cooling' : (0.97, 0.99),
    'explosion_control' : (0.84, 0.98),
    'emergency_shutdown' : (0.96, 0.99),
    'computer_control' : (0.93, 0.99),
    'inert_gas' : (0.94, 0.96),
    'operating_instructions' : (0.91, 0.99),
    'reactive_chemical_review' : (0.91, 0.98),
    'other_hazards' : (0.91, 0.98),
    'remote_control_valves' : (0.96, 0.98),
    'dump_blowdown' : (0.96, 0.98),
    'drainage': (0.91, 0.97),
    'interlock' : (0.98, np.nan),
    'leak_detection' : (0.94, 0.98),
    'structural_steel' : (0.95, 0.98),
    'fire_water_supply' : (0.94, 0.97),
    'special_systems' : (0.91, np.nan),
    'sprinkler_systems' : (0.74, 0.97),
    'water_curtains' : (0.97, 0.98),
    'foam' : (0.92, 0.97),
    'hand_extinguishers' : (0.93, 0.98),
    'cable_protection' : (0.94, 0.98)
}
Loss_Control_Credit_Factors = {
    'Process Control Credit Factor (C1)': ['emergency_power', 'cooling', 'explosion_control', 'emergency_shutdown', 'computer_control', 'inert_gas', 'operating_instructions', 'reactive_chemical_review', 'other_hazards'],
    'Material Isolation Credit Factor (C2)': ['remote_control_valves', 'dump_blowdown', 'drainage', 'interlock'],
    'Fire Protection Credit Factor (C3)': ['leak_detection', 'structural_steel', 'fire_water_supply', 'special_systems', 'sprinkler_systems', 'water_curtains', 'foam', 'hand_extinguishers', 'cable_protection']
}

#where the f_np is inhgerent frequency in number of events per year
# is the impact of the hazrd ( impact per loss event)
def Inherent_risk_calculations(F_np, C):
    R_np = F_np * C
    return R_np

def tolerable_risk_calculation(F_t, C): 
    R_t = F_t * C
    return R_t

#the risk reduction factor of the protective system can be calculated as the ratio between f_np and f_t    
# that is basically calculating how much of the inherent risk F_np has been normalised by the F_t
#PFD is the probablility that the system will fail in operation
def PFD(F_np,F_t):
    delta_R = F_np/F_t
    PFD_average = 1/delta_R
    return PFD_average

# SIL UPPER AND LOWER BOUND OF PROBABILITY
Safety_Integrity_Level = {
    4 : (1/100000, 1/10000),
    3 : (1/10000, 1/1000),
    2 : (1/1000, 1/100),
    1 : (1/100, 1/10)
}

# the failure rate lambda is the number of time per year that a protetcitve system is faulty
# the time interval between tests of the devices is tau (how many times is tested per year)
#probability protective system is inactive when required is fractional dead time
def fractioncal_Dead_time_calculation(tau, Lambda):
    fractional_dead_time = tau * Lambda/2
    return fractional_dead_time

# f is the number of occasions per year that the protective device is actuated and sigma is the demand rate
def annual_hazard_rate_calculation(sigma, fractional_dead_time):
    F_hazard_rate = sigma*fractional_dead_time
    return F_hazard_rate

def lethal_dose50_claassification(lethal_dose50):
    if lethal_dose50 < 25 or lethal_dose50 == 25:
        classification = 'very toxic'
    elif lethal_dose50 > 25 and lethal_dose50 < 200:
        classification = 'toxic'
    elif lethal_dose50 == 200 and lethal_dose50 < 2000:
        classification = 'harmful'
    else:
        print('unclassifiable')
    return classification

# PEL first value and LD_50 
lethal_dose50_PEL_data = {
    'Carbon monoxide': (50, 1807),
    'Carbon disulfide': (20, 3188),
    'Chlorine': (1, 239),
    'Chlorine dioxide': (0.1, 292),
    'Chloroform': (50, 1188),
    'Cyclohexane': (300, np.nan),
    'Dioxane': (100, 4200),
    'Ethylbenzene': (100, 3500),
    'Formic acid': (5, 1100),
    'Furfural': (5, 260),
    'Hydrogen chloride': (5, 4701),
    'Hydrogen cyanide': (10 ,3.7),
    'Isopropyl alcohol': (400, 5045),
    'Toluene': (100, 5000),
    'Xylene': (100, 4300)
}

#Rating SEV OCC DET
Suggested_rating_scale_for_FMEA = {
    1: ['Effect is insignificant', 'Failure is very unlikely,' 'Current safeguards will always prevent failure mode'],
    4: ['Minor disruption, possible loss of production', 'Occasional failure possible', 'High probability that current safeguard will detect or prevent'],
    7: ['Major disruption, possible damage to local equipment,' 'Infrequent failure is likely', 'Low probability that current safeguard will detect or prevent'],
    10: ['Severe disruption, major damage to plant, possible injury to personnel' 'Failure is very likely or frequent', 'No current method of detection']
}

Design_Safety_Checklist = '''
    Materials
    a. flashpoint
    b. flammability range
    c. autoignition temperature
    d. composition
    e. stability (shock sensitive?)
    f. toxicity, TLV
    g. corrosion
    h. physical properties (unusual?)
    i. heat of combustion/reaction
    Process
    1. Reactors
    a. exothermic—heat of reaction
    b. temperature control—emergency systems
    c. side reactions—dangerous?
    d. effect of contamination
    e. effect of unusual concentrations (including catalyst)
    f. corrosion
    2. Pressure systems
    a. need?
    b. design to current codes
    c. materials of construction—adequate?
    d. pressure relief—adequate?
    e. safe venting systems
    f. flame arresters
    Control systems
    a. fail safe
    b. backup power supplies
    c. high/low alarms and trips on critical variables
    i. temperature
    ii. pressure
    iii. flow
    iv. level
    v. composition
    d. backup/duplicate systems on critical variables
    e. remote operation of valves
    f. block valves on critical lines
    g. excess-flow valves
    h. interlock systems to prevent misoperation
    i. automatic shutdown systems
    Storages
    a. limit quantity
    b. inert purging/blanketing
    c. floating roof tanks
    d. dykeing
    e. loading/unloading facilities—safety
    f. earthing
    g. ignition sources—vehicles
    General
    a. inert purging systems needed
    b. compliance with electrical codes
    c. adequate lighting
    d. lightning protection
    e. sewers and drains adequate, flame traps
    f. dust-explosion hazards
    g. buildup of dangerous impurities—purges
    h. plant layout
    i. separation of units
    ii. access
    iii. siting of control rooms and offices
    iv. services
    i. safety showers, eye baths
    Fire protection
    a. emergency water supplies
    b. fire mains and hydrants
    c. foam systems
    d. sprinklers and deluge systems
    e. insulation and protection of structures
    f. access to buildings
    g. firefighting equipment
'''

for_extra_readings = {
    'powde handlings handbook' : 'https://www.powderprocess.net/index.html',
    'Combustible Dust in Industry' : 'https://www.osha.gov/sites/default/files/publications/shib073105.pdf'
}

