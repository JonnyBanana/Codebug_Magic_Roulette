import codebug_tether
from codebug_tether import (IO_DIGITAL_OUTPUT,
                            IO_DIGITAL_INPUT,
                            IO_PWM_OUTPUT,
                            IO_ANALOG_INPUT)
import codebug_tether.colourtail
from codebug_tether.sprites import StringSprite
import random
import time

lucky_number = None

codebug = codebug_tether.CodeBug()
codebug.set_leg_io(0, IO_DIGITAL_INPUT);
codebug.set_leg_io(1, IO_DIGITAL_INPUT);
codebug.set_leg_io(2, IO_DIGITAL_INPUT);
codebug.set_leg_io(3, IO_DIGITAL_INPUT);
codebug.set_leg_io(4, IO_DIGITAL_INPUT);
codebug.set_leg_io(5, IO_DIGITAL_INPUT);
codebug.set_leg_io(6, IO_DIGITAL_INPUT);
codebug.set_leg_io(7, IO_DIGITAL_INPUT);

colourtail = codebug_tether.colourtail.CodeBugColourTail(codebug)
colourtail.init();


for count in range(1):
  codebug.scroll_sprite(StringSprite('Welcome to Magic Roulette...  GOOD LUCK!!!', 'R'), 100/1000, 'L')
while True:
  if codebug.get_input('A') == 1:
    lucky_number = random.randint(0, 36)
    codebug.scroll_sprite(StringSprite('The Lucky Number is...', 'R'), 100/1000, 'L')
    time.sleep(1000/1000);
    codebug.scroll_sprite(StringSprite(lucky_number, 'R'), 500/1000, 'L')
