# Create a program that logs your pet's daily activities! (If you don't have a pet, imagine one!)
# Your task: Fill in the blanks

import logging
logging.basicConfig(level=logging.DEBUG) # Choose a level!

# Log these events:
# - Your pet waking up (debug)
logging.debug('Spot is not feeling well')
# - Your pet eating (info)
logging.info('Spot is hungry')
# - Your pet making mess (warning)
logging.warning('Spot is making a mess')
# - Your pet breaking something (error)
logging.error('Spot broke a vase!\n')