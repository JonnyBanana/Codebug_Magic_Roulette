var lucky_number;
var count;

codebug_direction('U');
codebug_sleepafter(3);
io_configure(0, IO_DIGITAL_INPUT);
io_configure(1, IO_DIGITAL_INPUT);
io_configure(2, IO_DIGITAL_INPUT);
io_configure(3, IO_DIGITAL_INPUT);
io_configure(4, IO_DIGITAL_INPUT);
io_configure(5, IO_DIGITAL_INPUT);
io_configure(6, IO_DIGITAL_INPUT);
io_configure(7, IO_DIGITAL_INPUT);
io_configure_pullup(0, 0);
io_configure_pullup(2, 0);
io_configure_pullup(3, 0);
io_configure_pullup(4, 0);
io_configure_pullup(5, 0);
codebug_colourtail_init(EXT_CS);


for (count = 0; count < 1; count++) {
  fivebyfivedisplay.sprite_scroll((new StringSprite('Welcome to Magic Roulette...  GOOD LUCK!!!', 'R')), 100, 'L');
}
while (true) {
  if (io_get_input('A') == 1) {
    lucky_number = random_range(0, 36);
    fivebyfivedisplay.sprite_scroll((new StringSprite('The Lucky Number is...', 'R')), 100, 'L');
    sleep(1000);
    fivebyfivedisplay.sprite_scroll((new StringSprite(lucky_number, 'R')), 500, 'L');
  }
}
